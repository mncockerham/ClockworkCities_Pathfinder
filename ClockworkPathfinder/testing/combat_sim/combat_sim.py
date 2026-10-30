"""
Clockwork Cities Pathfinder — Combat & Environmental Simulator
Runs N-iteration Monte Carlo combat simulations across all 4 combat environments:
  1. Civil   (civil_spire)
  2. High    (high_radiant)
  3. Low     (low_radiant)
  4. Neither (the_neither)

Outputs:
  - Concise environmental table with percentage outcomes relative to Character A.
  - Calculated Tier rating (S / A / B / C / D) per environment based on win rate.
"""

import json
import random
import sys
from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional

def roll_dice(dice_str: str) -> int:
    """Parses '2d6', '1d8', '3d10' etc. and returns sum."""
    if not dice_str or 'd' not in dice_str:
        return 0
    parts = dice_str.lower().split('d')
    num = int(parts[0]) if parts[0] else 1
    sides = int(parts[1])
    return sum(random.randint(1, sides) for _ in range(num))

@dataclass
class Weapon:
    name: str
    attack_bonus: int
    damage_dice: str
    flat_damage: int
    damage_type: str
    range_ft: int
    ap_cost: int
    traits: List[str]
    allowed_environments: List[str]
    ammo_capacity: int = 999
    reload_actions: int = 1
    save_type: Optional[str] = None  # 'ref', 'fort', 'will'
    save_dc: Optional[int] = None
    save_damage_dice: Optional[str] = None
    save_flat_damage: Optional[int] = None
    action_cost: int = 1
    cooldown_rounds: int = 0

@dataclass
class CombatantState:
    data: Dict[str, Any]
    current_hp: int
    max_hp: int
    temp_hp: int
    ac: int
    current_ap: int
    max_ap: int
    pos: int  # distance in feet
    retainers_hp: List[int] = field(default_factory=list)
    shield_hp: int = 0
    shield_raised: bool = False
    ammo_remaining: Dict[str, int] = field(default_factory=dict)
    save_ability_cooldowns: Dict[str, int] = field(default_factory=dict)
    active_weapon_is_two_handed: bool = False

class Simulator:
    def __init__(self, char_a_path: str, char_b_path: str, initial_distance: int = 40):
        with open(char_a_path, 'r') as f:
            self.raw_a = json.load(f)
        with open(char_b_path, 'r') as f:
            self.raw_b = json.load(f)
        self.initial_dist = initial_distance

    def _setup_combatant(self, raw: Dict[str, Any], env: str, start_pos: int) -> CombatantState:
        ac = raw["ac"]
        if env == "civil_spire":
            if not raw.get("civil_spire_legal", False):
                ac += raw.get("civil_ac_penalty", -4)

        max_hp = raw["hp"]
        temp_hp = 0
        abilities = raw.get("abilities", {})

        # Radiant Barrier
        if abilities.get("radiant_barrier", False):
            if env == "high_radiant":
                temp_hp += abilities.get("barrier_temp_hp_high", 15)
            elif env == "low_radiant":
                temp_hp += abilities.get("barrier_temp_hp_low", 8)

        retainers_hp = []
        if abilities.get("armed_retainers", False):
            count = abilities.get("retainer_count", 2)
            ret_hp = abilities.get("retainer_hp", 25)
            retainers_hp = [ret_hp for _ in range(count)]

        shield_hp = abilities.get("shield_hp", 0) if env != "civil_spire" else 0

        # Ammo tracking
        ammo = {}
        for w in raw.get("weapons", []):
            if "cartridge" in w.get("traits", []):
                ammo[w["name"]] = w.get("ammo_capacity", 6)

        return CombatantState(
            data=raw,
            current_hp=max_hp,
            max_hp=max_hp,
            temp_hp=temp_hp,
            ac=ac,
            current_ap=raw["max_ap"],
            max_ap=raw["max_ap"],
            pos=start_pos,
            retainers_hp=retainers_hp,
            shield_hp=shield_hp,
            shield_raised=False,
            ammo_remaining=ammo
        )

    def _get_usable_weapons(self, state: CombatantState, env: str) -> List[Weapon]:
        usable = []
        raw_weapons = state.data.get("weapons", [])
        for w in raw_weapons:
            allowed = w.get("allowed_environments", [])
            if env in allowed:
                if env == "civil_spire" and "cartridge" in w.get("traits", []):
                    continue
                if env == "the_neither" and "radiant" in w.get("traits", []):
                    continue
                if "cartridge" in w.get("traits", []):
                    if state.ammo_remaining.get(w["name"], 0) <= 0:
                        continue
                usable.append(Weapon(
                    name=w["name"],
                    attack_bonus=w.get("attack_bonus", 0),
                    damage_dice=w.get("damage_dice", "0d0"),
                    flat_damage=w.get("flat_damage", 0),
                    damage_type=w.get("damage_type", "B"),
                    range_ft=w.get("range", 0),
                    ap_cost=w.get("ap_cost", 0),
                    traits=w.get("traits", []),
                    allowed_environments=allowed,
                    ammo_capacity=w.get("ammo_capacity", 999),
                    reload_actions=w.get("reload_actions", 1),
                    save_type=w.get("save_type"),
                    save_dc=w.get("save_dc"),
                    save_damage_dice=w.get("save_damage_dice"),
                    save_flat_damage=w.get("save_flat_damage"),
                    action_cost=w.get("action_cost", 2 if w.get("save_type") else 1),
                    cooldown_rounds=w.get("cooldown_rounds", 0)
                ))
        return usable

    def _apply_damage(self, target: CombatantState, damage: int, is_physical: bool = True):
        phys_res = target.data.get("abilities", {}).get("damage_resistance_physical", 0)
        if is_physical and phys_res > 0:
            damage = max(0, damage - phys_res)

        if target.shield_raised and target.shield_hp > 0:
            hardness = target.data.get("abilities", {}).get("shield_hardness", 5)
            blocked = min(damage, hardness)
            excess = damage - blocked
            damage = excess
            target.shield_hp = max(0, target.shield_hp - excess)
            target.shield_raised = False

        if damage <= 0:
            return

        if target.temp_hp > 0:
            if target.temp_hp >= damage:
                target.temp_hp -= damage
                damage = 0
            else:
                damage -= target.temp_hp
                target.temp_hp = 0

        target.current_hp = max(0, target.current_hp - damage)

    def _execute_strike(self, attacker: CombatantState, defender: CombatantState, weapon: Weapon, map_penalty: int) -> int:
        d20 = random.randint(1, 20)
        attack_roll = d20 + weapon.attack_bonus + map_penalty

        # Physical Strike targeting AC.
        # Pulse devices are pure non-physical harmonic resonators protecting saving throws (Fort, Ref, Will).
        # They grant 0 AC bonus and do not trigger or drain AP on standard physical AC strikes.
        effective_ac = defender.ac + (2 if defender.shield_raised else 0)

        diff = attack_roll - effective_ac
        is_crit = False
        is_hit = False

        if diff >= 10 or d20 == 20:
            if d20 == 1:
                is_hit = True
            else:
                is_crit = True
                is_hit = True
        elif diff >= 0:
            if d20 == 1:
                is_hit = False
            else:
                is_hit = True
        else:
            if d20 == 20:
                is_hit = True
            else:
                is_hit = False

        if not is_hit:
            return 0

        base_dmg = roll_dice(weapon.damage_dice) + weapon.flat_damage
        if is_crit:
            total_dmg = base_dmg * 2
            for t in weapon.traits:
                if t.startswith("fatal_"):
                    fatal_die = t.replace("fatal_", "1")
                    total_dmg += roll_dice(fatal_die)
                elif t.startswith("deadly_"):
                    deadly_die = t.replace("deadly_", "1")
                    total_dmg += roll_dice(deadly_die)
        else:
            total_dmg = base_dmg

        if defender.retainers_hp:
            retainer_idx = 0
            intercept = min(defender.retainers_hp[retainer_idx], total_dmg // 2)
            defender.retainers_hp[retainer_idx] -= intercept
            total_dmg -= intercept
            if defender.retainers_hp[retainer_idx] <= 0:
                defender.retainers_hp.pop(0)

        is_phys = weapon.damage_type in ["B", "P", "S", "P/Electricity"]
        self._apply_damage(defender, total_dmg, is_phys)
        return total_dmg

    def _execute_save_ability(self, attacker: CombatantState, defender: CombatantState, weapon: Weapon) -> int:
        """Executes a saving throw ability (PF2e standard 4 degrees: Crit Success, Success, Failure, Crit Failure)."""
        save_type = (weapon.save_type or "ref").lower()

        # Reactive Pulse Defense activation on save
        # Must be activated for every incoming save check; costs AP (minimum 1) and requires unspent AP.
        # Characters cannot have both a shield and a pulse device.
        # Two-handed weapons / rifles prevent the activation of standard pulse devices.
        # Illegal / confiscated in Civil Spire.
        bonus = 0
        pulse_dr = 0
        pulse_cfg = defender.data.get("abilities", {}).get("pulse_defense")
        has_shield = defender.data.get("abilities", {}).get("shield_block", False) or defender.shield_hp > 0
        is_two_handed = defender.active_weapon_is_two_handed

        if pulse_cfg and isinstance(pulse_cfg, dict) and not has_shield and not is_two_handed:
            env = getattr(self, "_current_env", "")
            if env != "civil_spire" or pulse_cfg.get("civil_spire_legal", False):
                ap_cost = max(1, pulse_cfg.get("ap_cost", 1))
                if defender.current_ap >= ap_cost:
                    defender.current_ap -= ap_cost
                    if save_type in ["ref", "dex"]:
                        bonus = pulse_cfg.get("ref_bonus", 0)
                        pulse_dr = pulse_cfg.get("ref_dr", pulse_cfg.get("damage_reduction", 0) if pulse_cfg.get("ref_bonus", 0) > 0 else 0)
                    elif save_type in ["fort", "con"]:
                        bonus = pulse_cfg.get("fort_bonus", 0)
                        pulse_dr = pulse_cfg.get("fort_dr", pulse_cfg.get("damage_reduction", 0) if pulse_cfg.get("fort_bonus", 0) > 0 else 0)
                    elif save_type == "will":
                        bonus = pulse_cfg.get("will_bonus", 0)
                        pulse_dr = pulse_cfg.get("will_dr", pulse_cfg.get("damage_reduction", 0) if pulse_cfg.get("will_bonus", 0) > 0 else 0)

        if save_type in ["ref", "dex"]:
            save_mod = defender.data.get("ref", 10) + bonus
        elif save_type in ["fort", "con"]:
            save_mod = defender.data.get("fort", 10) + bonus
        elif save_type == "will":
            save_mod = defender.data.get("will", 10) + bonus
        else:
            save_mod = 10 + bonus

        dc = weapon.save_dc if weapon.save_dc is not None else (10 + attacker.data.get("level", 1) + 4)
        d20 = random.randint(1, 20)
        total_roll = d20 + save_mod
        diff = total_roll - dc

        # Degree of success determination
        # >= 10: Crit Success; >= 0: Success; < 0: Failure; <= -10: Crit Failure
        if diff >= 10:
            degree = 3  # Crit Success
        elif diff >= 0:
            degree = 2  # Success
        elif diff <= -10:
            degree = 0  # Crit Failure
        else:
            degree = 1  # Failure

        # Natural 20 increases degree by 1 step; Natural 1 decreases by 1 step
        if d20 == 20:
            degree = min(3, degree + 1)
        elif d20 == 1:
            degree = max(0, degree - 1)

        dice_str = weapon.save_damage_dice or weapon.damage_dice
        flat_val = weapon.save_flat_damage if weapon.save_flat_damage is not None else weapon.flat_damage
        base_dmg = roll_dice(dice_str) + flat_val

        # Pathfinder 2e Save Damage Logic:
        # Crit Success (3): No damage (0)
        # Success (2): Half damage (base_dmg // 2)
        # Failure (1): Full damage (base_dmg)
        # Crit Failure (0): Double damage (base_dmg * 2)
        if degree == 3:
            total_dmg = 0
        elif degree == 2:
            total_dmg = base_dmg // 2
        elif degree == 1:
            total_dmg = base_dmg
        else:
            total_dmg = base_dmg * 2

        # Apply targeted pulse damage reduction if active for this save type
        if pulse_dr > 0 and total_dmg > 0:
            total_dmg = max(0, total_dmg - pulse_dr)

        # Retainers intercept 50% of incoming damage
        if defender.retainers_hp and total_dmg > 0:
            retainer_idx = 0
            intercept = min(defender.retainers_hp[retainer_idx], total_dmg // 2)
            defender.retainers_hp[retainer_idx] -= intercept
            total_dmg -= intercept
            if defender.retainers_hp[retainer_idx] <= 0:
                defender.retainers_hp.pop(0)

        is_phys = weapon.damage_type in ["B", "P", "S"]
        self._apply_damage(defender, total_dmg, is_phys)
        return total_dmg

    def _combatant_turn(self, active: CombatantState, passive: CombatantState, env: str):
        actions = 3
        map_count = 0
        dist = abs(active.pos - passive.pos)
        speed = active.data.get("speed", 25)
        abilities = active.data.get("abilities", {})

        if env == "high_radiant":
            active.current_ap = active.max_ap
        elif env == "low_radiant":
            active.current_ap = min(active.max_ap, active.current_ap + 1)

        if active.retainers_hp:
            for _ in active.retainers_hp:
                ret_roll = random.randint(1, 20) + active.data["abilities"].get("retainer_attack", 9)
                if ret_roll >= passive.ac:
                    ret_dmg = roll_dice(active.data["abilities"].get("retainer_damage_dice", "1d8")) + active.data["abilities"].get("retainer_flat_damage", 3)
                    self._apply_damage(passive, ret_dmg, True)
                if passive.current_hp <= 0:
                    return

        # Decrement cooldowns at start of turn
        for k in list(active.save_ability_cooldowns.keys()):
            if active.save_ability_cooldowns[k] > 0:
                active.save_ability_cooldowns[k] -= 1

        weapons = self._get_usable_weapons(active, env)

        # 1. Check for Save-based special breath/emitter abilities (Acid Spitter, Spore Sprayer, Disorientor)
        save_weapons = [w for w in weapons if w.save_type and (w.range_ft == 0 or w.range_ft >= dist)]
        for sw in save_weapons:
            cost = sw.action_cost
            cd = active.save_ability_cooldowns.get(sw.name, 0)
            if actions >= cost and cd == 0:
                actions -= cost
                self._execute_save_ability(active, passive, sw)
                active.save_ability_cooldowns[sw.name] = sw.cooldown_rounds
                if passive.current_hp <= 0:
                    return

        if abilities.get("shield_block", False) and active.shield_hp > 0 and actions >= 1 and not active.shield_raised:
            if dist <= 30:
                active.shield_raised = True
                actions -= 1

        # Standard strike weapons (exclude save abilities for standard MAP strikes)
        strike_weapons = [w for w in weapons if not w.save_type]
        best_melee = [w for w in strike_weapons if w.range_ft == 0]
        best_ranged = [w for w in strike_weapons if w.range_ft >= dist]

        chosen_weapon = None
        if best_ranged:
            chosen_weapon = max(best_ranged, key=lambda w: w.attack_bonus)
        elif best_melee:
            chosen_weapon = max(best_melee, key=lambda w: w.attack_bonus)

        # Track whether active weapon is a two-handed weapon or rifle (which occupies both hands)
        if chosen_weapon:
            w_name_lower = chosen_weapon.name.lower()
            w_traits = [t.lower() for t in chosen_weapon.traits]
            is_2h = ("two-hand" in w_traits or "two_hand" in w_traits or
                     "greatsword" in w_name_lower or "rifle" in w_name_lower or
                     "longbow" in w_name_lower or "heavy crossbow" in w_name_lower)
            active.active_weapon_is_two_handed = is_2h
        else:
            active.active_weapon_is_two_handed = False

        while dist > 5 and chosen_weapon and chosen_weapon.range_ft == 0 and actions >= 1:
            dist = max(5, dist - speed)
            active.pos = dist
            actions -= 1

        if not chosen_weapon:
            chosen_weapon = Weapon(
                name="Fist",
                attack_bonus=active.data.get("unarmed_bonus", 10),
                damage_dice=active.data.get("unarmed_damage_dice", "1d4"),
                flat_damage=active.data.get("unarmed_flat_dmg", 0),
                damage_type="B",
                range_ft=0,
                ap_cost=0,
                traits=active.data.get("unarmed_traits", ["agile", "nonlethal"]),
                allowed_environments=["civil_spire", "high_radiant", "low_radiant", "the_neither"]
            )
            while dist > 5 and actions >= 1:
                dist = max(5, dist - speed)
                active.pos = dist
                actions -= 1

        if abilities.get("flurry_of_blows", False) and dist <= 5 and actions >= 1:
            actions -= 1
            self._execute_strike(active, passive, chosen_weapon, 0)
            if passive.current_hp <= 0:
                return
            map_penalty = -4 if "agile" in chosen_weapon.traits else -5
            self._execute_strike(active, passive, chosen_weapon, map_penalty)
            if passive.current_hp <= 0:
                return
            map_count += 2

        while actions >= 1 and passive.current_hp > 0:
            if chosen_weapon.range_ft > 0 and dist > chosen_weapon.range_ft:
                dist = max(chosen_weapon.range_ft, dist - speed)
                active.pos = dist
                actions -= 1
                continue

            if chosen_weapon.range_ft == 0 and dist > 5:
                dist = max(5, dist - speed)
                active.pos = dist
                actions -= 1
                continue

            if chosen_weapon.ap_cost > 0:
                if active.current_ap < chosen_weapon.ap_cost:
                    fallbacks = [w for w in weapons if w.ap_cost == 0]
                    if fallbacks:
                        chosen_weapon = fallbacks[0]
                    else:
                        break
                else:
                    active.current_ap -= chosen_weapon.ap_cost

            if "cartridge" in chosen_weapon.traits:
                if active.ammo_remaining.get(chosen_weapon.name, 0) <= 0:
                    if actions >= chosen_weapon.reload_actions:
                        actions -= chosen_weapon.reload_actions
                        active.ammo_remaining[chosen_weapon.name] = chosen_weapon.ammo_capacity
                        continue
                    else:
                        break
                active.ammo_remaining[chosen_weapon.name] -= 1

            if map_count == 0:
                penalty = 0
            elif map_count == 1:
                penalty = -4 if "agile" in chosen_weapon.traits else -5
            else:
                penalty = -8 if "agile" in chosen_weapon.traits else -10

            self._execute_strike(active, passive, chosen_weapon, penalty)
            map_count += 1
            actions -= 1

    def run_single_battle(self, env: str) -> str:
        self._current_env = env
        cA = self._setup_combatant(self.raw_a, env, 0)
        cB = self._setup_combatant(self.raw_b, env, self.initial_dist)

        init_a = random.randint(1, 20) + self.raw_a.get("perception", 10)
        init_b = random.randint(1, 20) + self.raw_b.get("perception", 10)

        turn = 0
        a_first = init_a >= init_b

        while cA.current_hp > 0 and cB.current_hp > 0 and turn < 30:
            turn += 1
            if a_first:
                self._combatant_turn(cA, cB, env)
                if cB.current_hp <= 0:
                    break
                self._combatant_turn(cB, cA, env)
            else:
                self._combatant_turn(cB, cA, env)
                if cA.current_hp <= 0:
                    break
                self._combatant_turn(cA, cB, env)

        hp_pct_a = cA.current_hp / cA.max_hp
        hp_pct_b = cB.current_hp / cB.max_hp

        if cA.current_hp > 0 and cB.current_hp <= 0:
            if hp_pct_a > 0.60:
                outcome = "Clear Win"
            elif hp_pct_a >= 0.35:
                outcome = "Mod Win"
            elif hp_pct_a >= 0.10:
                outcome = "Close Win"
            else:
                outcome = "Too Close"
        elif cB.current_hp > 0 and cA.current_hp <= 0:
            if hp_pct_b > 0.60:
                outcome = "Clear Def"
            elif hp_pct_b >= 0.35:
                outcome = "Major Def"
            elif hp_pct_b >= 0.10:
                outcome = "Minor Def"
            else:
                outcome = "Too Close"
        else:
            outcome = "Too Close"

        return outcome, turn

    def run_environment_suite(self, iterations: int = 100) -> Dict[str, Any]:
        envs = [
            ("Civil", "civil_spire"),
            ("High", "high_radiant"),
            ("Low", "low_radiant"),
            ("Neither", "the_neither")
        ]
        
        results = {}
        tiers = {}
        round_stats = {}

        for label, env_key in envs:
            counts = {
                "Clear Win": 0, "Mod Win": 0, "Close Win": 0,
                "Too Close": 0,
                "Minor Def": 0, "Major Def": 0, "Clear Def": 0
            }
            wins_a = 0
            rounds_list = []

            for _ in range(iterations):
                outcome, r_turns = self.run_single_battle(env_key)
                counts[outcome] += 1
                rounds_list.append(r_turns)
                if "Win" in outcome:
                    wins_a += 1

            # Convert to percentages
            pcts = {k: round((v / iterations) * 100) for k, v in counts.items()}
            results[label] = pcts

            # Calculate Round Statistics
            avg_rnd = round(sum(rounds_list) / len(rounds_list), 1) if rounds_list else 0.0
            min_rnd = min(rounds_list) if rounds_list else 0
            max_rnd = max(rounds_list) if rounds_list else 0
            round_stats[label] = {
                "avg": avg_rnd,
                "min": min_rnd,
                "max": max_rnd
            }

            # Calculate Tier Rating based on win rate & clear dominance
            win_pct = (wins_a / iterations) * 100
            clear_pct = pcts["Clear Win"]
            
            if win_pct >= 85 and clear_pct >= 50:
                tier_a = "S"
            elif win_pct >= 65:
                tier_a = "A"
            elif win_pct >= 40:
                tier_a = "B"
            elif win_pct >= 20:
                tier_a = "C"
            else:
                tier_a = "D"

            # Inverse for B
            win_pct_b = 100 - win_pct - (pcts["Too Close"])
            clear_pct_b = pcts["Clear Def"]
            if win_pct_b >= 85 and clear_pct_b >= 50:
                tier_b = "S"
            elif win_pct_b >= 65:
                tier_b = "A"
            elif win_pct_b >= 40:
                tier_b = "B"
            elif win_pct_b >= 20:
                tier_b = "C"
            else:
                tier_b = "D"

            tiers[label] = (tier_a, tier_b)

        return {
            "char_a": self.raw_a["name"],
            "char_b": self.raw_b["name"],
            "iterations": iterations,
            "results": results,
            "tiers": tiers,
            "round_stats": round_stats
        }

def print_clean_report(suite: Dict[str, Any]):
    char_a = suite["char_a"]
    char_b = suite["char_b"]
    iters = suite["iterations"]
    
    envs = [e for e in ["Civil", "High", "Low", "Neither"] if e in suite["results"]]
    
    print()
    print("=" * 68)
    print(f"COMBAT SUITE REPORT: {char_a.upper()} vs {char_b.upper()}")
    print(f"Iterations: {iters} per environment | Outcomes relative to {char_a}")
    print("=" * 68)
    
    # Environments on top header
    hdr = f"{'Outcome Category':<20} | " + " | ".join([f"{e:>9}" for e in envs])
    print(hdr)
    print("-" * 20 + "-+-" + "-+-".join(["-" * 9 for _ in envs]))
    
    rows = [
        ("Clear Win (>60%)", "Clear Win"),
        ("Mod Win (35-60%)", "Mod Win"),
        ("Close Win (10-35%)", "Close Win"),
        ("Too Close (<10%)", "Too Close"),
        ("Minor Def (10-35%)", "Minor Def"),
        ("Major Def (35-60%)", "Major Def"),
        ("Clear Def (>60%)", "Clear Def")
    ]
    
    for row_label, key in rows:
        row_vals = " | ".join([f"{suite['results'][e][key]:>8}%" for e in envs])
        print(f"{row_label:<20} | {row_vals}")
        
    print("-" * 20 + "-+-" + "-+-".join(["-" * 9 for _ in envs]))
    
    # Win rate summary row
    total_wins = []
    for e in envs:
        w_pct = suite['results'][e]['Clear Win'] + suite['results'][e]['Mod Win'] + suite['results'][e]['Close Win']
        total_wins.append(f"{w_pct:>8}%")
    print(f"{'TOTAL WIN RATE':<20} | " + " | ".join(total_wins))
    
    # Tier summary rows (capped for clean alignment)
    def format_tier_label(name: str) -> str:
        base = name.split()[0] if len(name) > 13 else name
        label = f"{base} Tier"
        return f"{label:<20}"

    tier_vals_a = " | ".join([f"{'Tier ' + suite['tiers'][e][0]:>9}" for e in envs])
    tier_vals_b = " | ".join([f"{'Tier ' + suite['tiers'][e][1]:>9}" for e in envs])

    print(f"{format_tier_label(char_a)} | {tier_vals_a}")
    print(f"{format_tier_label(char_b)} | {tier_vals_b}")

    # Round statistics rows
    if "round_stats" in suite:
        print("-" * 20 + "-+-" + "-+-".join(["-" * 9 for _ in envs]))
        avg_rnds = " | ".join([f"{suite['round_stats'][e]['avg']:>9}" for e in envs])
        min_rnds = " | ".join([f"{suite['round_stats'][e]['min']:>9}" for e in envs])
        max_rnds = " | ".join([f"{suite['round_stats'][e]['max']:>9}" for e in envs])
        print(f"{'Average Rounds':<20} | {avg_rnds}")
        print(f"{'Min Rounds':<20} | {min_rnds}")
        print(f"{'Max Rounds':<20} | {max_rnds}")

    print("=" * 68)
    print()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Clockwork Cities Full Environment Combat Simulator")
    parser.add_argument("--char_a", type=str, required=True, help="Path to Character A JSON")
    parser.add_argument("--char_b", type=str, required=True, help="Path to Character B JSON")
    parser.add_argument("--env", type=str, default="all", choices=["all", "civil_spire", "high_radiant", "low_radiant", "the_neither"], help="Environment to test (default: all)")
    parser.add_argument("--iters", type=int, default=100, help="Number of matches per environment")
    parser.add_argument("--dist", type=int, default=40, help="Initial distance in feet")
    args = parser.parse_args()

    sim = Simulator(args.char_a, args.char_b, args.dist)
    if args.env == "all":
        suite_data = sim.run_environment_suite(args.iters)
        print_clean_report(suite_data)
    else:
        # Run single environment and print focused table
        env_map = {
            "civil_spire": "Civil",
            "high_radiant": "High",
            "low_radiant": "Low",
            "the_neither": "Neither"
        }
        label = env_map[args.env]
        counts = {
            "Clear Win": 0, "Mod Win": 0, "Close Win": 0,
            "Too Close": 0,
            "Minor Def": 0, "Major Def": 0, "Clear Def": 0
        }
        wins_a = 0
        for _ in range(args.iters):
            outcome = sim.run_single_battle(args.env)
            counts[outcome] += 1
            if "Win" in outcome:
                wins_a += 1
        pcts = {k: round((v / args.iters) * 100) for k, v in counts.items()}
        win_pct = (wins_a / args.iters) * 100
        clear_pct = pcts["Clear Win"]
        if win_pct >= 85 and clear_pct >= 50:
            tier = "S"
        elif win_pct >= 65:
            tier = "A"
        elif win_pct >= 40:
            tier = "B"
        elif win_pct >= 20:
            tier = "C"
        else:
            tier = "D"
            
        suite_data = {
            "char_a": sim.raw_a["name"],
            "char_b": sim.raw_b["name"],
            "iterations": args.iters,
            "results": {label: pcts},
            "tiers": {label: tier}
        }
        print_clean_report(suite_data)
