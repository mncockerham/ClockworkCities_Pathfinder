"""
Party vs Encounter Combat Simulator (Clockwork Cities Pathfinder)
Simulates:
- 4 PCs (customizable party composition, e.g., Soldier, Survivor, Chirurgeon, Scholar)
- Retainers (from Nobles / Merchants)
- Versus 3 to 10 NPCs / Monsters (Minion mobs, elite patrols, or Solo Boss Creatures)
- Full Modeling of:
  * Chirurgeon Healing & Support:
    - 0-AP Autonomous Micro-Drone healing triage (heals lowest-HP ally per turn: 2d6 + 2*WIS)
    - Prophylactic DR (party-wide damage reduction: 2*WIS = 8-10 DR)
    - Drone Interceptions (absorbs 2*INT damage on ally physical hits)
    - Hemostatic spray (stops bleed)
    - Mycological Solvents (strips enemy Hardness/DR by 2*INT)
  * Scholar Party Boost & Telemetry:
    - Tactical Telemetry (+1 to +2 circumstance bonus to all allies' attack rolls & saves)
    - Inductive Kinetic/Mind Barrier (temp HP or reactive AC pulse to allies in High/Low radiant)
    - Target Focus Telemetry (reduces enemy AC / off-guard coordinate broadcasting)
  * Party Flanking Dynamics (automatically enabled for melee allies like Survivor / Pugilist)
  * Retainer Meat-Shield Interceptions & Attack Flooding
"""

import sys
import json
import random
from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional

def roll_dice(dice_str: str) -> int:
    if not dice_str or dice_str == "0d0":
        return 0
    parts = dice_str.split('d')
    num = int(parts[0])
    sides = int(parts[1])
    return sum(random.randint(1, sides) for _ in range(num))

@dataclass
class PartyCombatant:
    name: str
    archetype: str
    level: int
    current_hp: int
    max_hp: int
    temp_hp: int
    ac: int
    fort: int
    ref: int
    will: int
    speed: int
    current_ap: int
    max_ap: int
    pos: int
    is_pc: bool
    data: Dict[str, Any]
    weapons: List[Dict[str, Any]]
    abilities: Dict[str, Any]
    retainers_hp: List[int] = field(default_factory=list)
    drone_interceptions_left: int = 0
    solvents_left: int = 0

class GroupCombatSim:
    def __init__(self, pc_templates: List[str], enemy_templates: List[str], env: str = "the_neither", initial_distance: int = 50):
        self.env = env
        self.initial_dist = initial_distance
        self.pc_files = pc_templates
        self.enemy_files = enemy_templates

    def _load_combatant(self, path: str, is_pc: bool, pos: int) -> PartyCombatant:
        with open(path, 'r', encoding='utf-8') as f:
            d = json.load(f)

        ac = d.get("outland_ac", d["ac"]) if self.env != "civil_spire" else d["ac"]
        if self.env == "civil_spire" and not d.get("civil_spire_legal", False):
            ac += d.get("civil_ac_penalty", -4)

        abilities = dict(d.get("abilities", {}))
        if self.env != "civil_spire" and "outland_abilities" in d:
            abilities.update(d["outland_abilities"])

        if self.env != "civil_spire" and "outland_weapons" in d:
            weapons = d["outland_weapons"]
        else:
            weapons = d.get("weapons", [])

        # Filter usable weapons for environment
        usable_weapons = []
        for w in weapons:
            allowed = w.get("allowed_environments", [])
            if self.env in allowed:
                usable_weapons.append(w)
        if not usable_weapons:
            usable_weapons.append({
                "name": "Unarmed Strike",
                "attack_bonus": d.get("unarmed_bonus", 8),
                "damage_dice": d.get("unarmed_damage_dice", "1d4"),
                "flat_damage": d.get("unarmed_flat_dmg", 1),
                "range": 0,
                "traits": ["agile"]
            })

        # Retainers
        ret_hp = []
        if abilities.get("armed_retainers", False):
            count = abilities.get("retainer_count", 2)
            rhp = abilities.get("retainer_hp", 20)
            ret_hp = [rhp for _ in range(count)]

        lvl = d.get("level", 5)
        drone_ints = (2 * lvl) if d.get("archetype") == "Chirurgeon" else 0
        solvents = 4 if d.get("archetype") == "Chirurgeon" else 0

        return PartyCombatant(
            name=d["name"],
            archetype=d.get("archetype", "Unknown"),
            level=lvl,
            current_hp=d["hp"],
            max_hp=d["hp"],
            temp_hp=abilities.get("temp_hp", 0),
            ac=ac,
            fort=d.get("fort", 10),
            ref=d.get("ref", 10),
            will=d.get("will", 10),
            speed=d.get("speed", 25),
            current_ap=d.get("max_ap", 6),
            max_ap=d.get("max_ap", 6),
            pos=pos,
            is_pc=is_pc,
            data=d,
            weapons=usable_weapons,
            abilities=abilities,
            retainers_hp=ret_hp,
            drone_interceptions_left=drone_ints,
            solvents_left=solvents
        )

    def run_battle(self) -> Dict[str, Any]:
        # Position: PCs at 0, Enemies at initial_dist
        pcs = [self._load_combatant(f, True, 0) for f in self.pc_files]
        enemies = [self._load_combatant(f, False, self.initial_dist) for f in self.enemy_files]

        # Check for party support presence
        has_chirurgeon = any(c.archetype == "Chirurgeon" for c in pcs)
        has_scholar = any(c.archetype == "Scholar" for c in pcs)
        has_officer = any(c.archetype == "Officer" for c in pcs)

        # Party-wide Prophylactic DR from Chirurgeon: 2 * WIS = 8 DR physical/elemental
        party_dr = 8 if has_chirurgeon else 0
        # Scholar Telemetry Boost: +1 to hit for all allies, +2 in High Radiant
        telemetry_hit_bonus = 2 if (has_scholar and self.env == "high_radiant") else (1 if has_scholar else 0)
        # Officer Tactician Aura: +1 circumstance bonus to damage or hit
        officer_buff = 1 if has_officer else 0

        total_rounds = 0
        max_rounds = 30

        while total_rounds < max_rounds:
            total_rounds += 1
            alive_pcs = [p for p in pcs if p.current_hp > 0]
            alive_enemies = [e for e in enemies if e.current_hp > 0]

            if not alive_pcs or not alive_enemies:
                break

            # 1. Chirurgeon Start-of-Round Support:
            if has_chirurgeon:
                chirurgeon = next((p for p in alive_pcs if p.archetype == "Chirurgeon"), None)
                if chirurgeon:
                    # Autonomous Drone Heal to most wounded ally
                    wounded_allies = [p for p in alive_pcs if p.current_hp < p.max_hp]
                    if wounded_allies:
                        target = min(wounded_allies, key=lambda p: p.current_hp / p.max_hp)
                        # Drone delivers 0-AP healing tonic: 2d6 + 8 (2*WIS)
                        heal_val = roll_dice("2d6") + 8
                        target.current_hp = min(target.max_hp, target.current_hp + heal_val)

                    # Solvent spray on strongest enemy (strip Hardness/DR)
                    if chirurgeon.solvents_left > 0 and alive_enemies:
                        strongest = max(alive_enemies, key=lambda e: e.current_hp)
                        chirurgeon.solvents_left -= 1
                        strongest.ac = max(10, strongest.ac - 2) # Stripping armor/DR translates to -2 effective AC

            # 2. Scholar Start-of-Round Telemetry / Mind Barrier:
            if has_scholar and self.env in ["high_radiant", "low_radiant"]:
                scholar = next((p for p in alive_pcs if p.archetype == "Scholar"), None)
                if scholar:
                    # Pulse Mind Barrier to lowest HP ally
                    target = min(alive_pcs, key=lambda p: p.current_hp)
                    target.temp_hp += (15 if self.env == "high_radiant" else 8)

            # --- PC TURNS ---
            for pc in alive_pcs:
                if pc.current_hp <= 0:
                    continue
                alive_enemies = [e for e in enemies if e.current_hp > 0]
                if not alive_enemies:
                    break

                # Target selection: prioritize closest, lowest HP, or boss
                target = min(alive_enemies, key=lambda e: (abs(pc.pos - e.pos), e.current_hp))
                dist = abs(pc.pos - target.pos)
                actions = 3

                # Retainers attack
                if pc.retainers_hp:
                    for _ in pc.retainers_hp:
                        if target.current_hp <= 0:
                            alive_enemies = [e for e in enemies if e.current_hp > 0]
                            if not alive_enemies: break
                            target = alive_enemies[0]
                        ret_roll = random.randint(1, 20) + 7
                        if ret_roll >= target.ac:
                            target.current_hp -= (roll_dice("1d8") + 2)

                # Pick best weapon
                melee_w = [w for w in pc.weapons if w.get("range", 0) == 0]
                ranged_w = [w for w in pc.weapons if w.get("range", 0) >= dist]

                chosen_w = None
                if ranged_w and dist > 5:
                    chosen_w = max(ranged_w, key=lambda w: w.get("attack_bonus", 0))
                elif melee_w:
                    chosen_w = max(melee_w, key=lambda w: w.get("attack_bonus", 0))
                else:
                    chosen_w = pc.weapons[0]

                # Move into range if melee
                if chosen_w.get("range", 0) == 0 and dist > 5:
                    while dist > 5 and actions >= 1:
                        dist = max(5, dist - pc.speed)
                        pc.pos = target.pos - dist if pc.pos < target.pos else target.pos + dist
                        actions -= 1

                # Execute Strikes
                map_count = 0
                while actions >= 1 and target.current_hp > 0:
                    actions -= 1
                    map_pen = 0 if map_count == 0 else (-4 if "agile" in chosen_w.get("traits", []) else -5)
                    map_count += 1

                    hit_mod = pc.abilities.get("attack_bonus", 0) + telemetry_hit_bonus + officer_buff
                    atk_roll = random.randint(1, 20)
                    total_atk = atk_roll + chosen_w.get("attack_bonus", 10) + hit_mod + map_pen

                    # Flanking check: if 2 or more PCs are in melee (dist <= 5), target is Off-Guard (-2 AC)
                    melee_pcs_on_target = sum(1 for p in alive_pcs if abs(p.pos - target.pos) <= 5)
                    eff_target_ac = target.ac - 2 if melee_pcs_on_target >= 2 else target.ac

                    if total_atk >= eff_target_ac:
                        is_crit = (total_atk >= eff_target_ac + 10) or (atk_roll == 20 and total_atk >= eff_target_ac)
                        dmg_dice = chosen_w.get("damage_dice", "1d6")
                        flat_dmg = chosen_w.get("flat_damage", 3) + officer_buff

                        # Survivor Sneak Attack bonus if target is off-guard
                        if pc.archetype == "Survivor" and melee_pcs_on_target >= 2:
                            flat_dmg += 7 # +2d6 sneak attack at Lv 5

                        base_dmg = roll_dice(dmg_dice) + flat_dmg
                        final_dmg = (base_dmg * 2) if is_crit else base_dmg

                        # Fatal trait handling for firearms
                        if is_crit and "fatal_d10" in chosen_w.get("traits", []):
                            final_dmg += roll_dice("1d10")
                        elif is_crit and "fatal_d12" in chosen_w.get("traits", []):
                            final_dmg += roll_dice("1d12")

                        target.current_hp -= final_dmg

            # --- ENEMY TURNS ---
            alive_enemies = [e for e in enemies if e.current_hp > 0]
            for enemy in alive_enemies:
                if enemy.current_hp <= 0:
                    continue
                alive_pcs = [p for p in pcs if p.current_hp > 0]
                if not alive_pcs:
                    break

                # AI: Target closest or frontline PC
                target = min(alive_pcs, key=lambda p: abs(enemy.pos - p.pos))
                dist = abs(enemy.pos - target.pos)
                actions = 3

                # Move into melee if needed
                melee_w = [w for w in enemy.weapons if w.get("range", 0) == 0]
                chosen_w = melee_w[0] if melee_w else enemy.weapons[0]

                if chosen_w.get("range", 0) == 0 and dist > 5:
                    while dist > 5 and actions >= 1:
                        dist = max(5, dist - enemy.speed)
                        enemy.pos = target.pos - dist if enemy.pos < target.pos else target.pos + dist
                        actions -= 1

                map_count = 0
                while actions >= 1 and target.current_hp > 0:
                    actions -= 1
                    map_pen = 0 if map_count == 0 else (-4 if "agile" in chosen_w.get("traits", []) else -5)
                    map_count += 1

                    atk_roll = random.randint(1, 20)
                    total_atk = atk_roll + chosen_w.get("attack_bonus", 12) + map_pen

                    eff_ac = target.ac
                    # Reactive AP Deflection / Shield Block
                    if target.abilities.get("shield_block") and target.abilities.get("shield_hp", 0) > 0:
                        eff_ac += target.abilities.get("shield_raised_ac_bonus", 2)
                    elif target.abilities.get("arc_deflection_screen") and target.current_ap >= 2:
                        eff_ac += 3

                    if total_atk >= eff_ac:
                        is_crit = (total_atk >= eff_ac + 10) or (atk_roll == 20 and total_atk >= eff_ac)
                        base_dmg = roll_dice(chosen_w.get("damage_dice", "2d6")) + chosen_w.get("flat_damage", 6)
                        final_dmg = (base_dmg * 2) if is_crit else base_dmg

                        # Chirurgeon Micro-Drone Interception Reaction:
                        if has_chirurgeon:
                            chirurgeon = next((p for p in alive_pcs if p.archetype == "Chirurgeon"), None)
                            if chirurgeon and chirurgeon.drone_interceptions_left > 0:
                                chirurgeon.drone_interceptions_left -= 1
                                absorb = 10 # 2 * INT
                                final_dmg = max(0, final_dmg - absorb)

                        # Party-wide Prophylactic DR:
                        final_dmg = max(0, final_dmg - party_dr)

                        # Retainer Intercept:
                        if target.retainers_hp and final_dmg > 0:
                            intercept = min(target.retainers_hp[0], final_dmg // 2)
                            target.retainers_hp[0] -= intercept
                            final_dmg -= intercept
                            if target.retainers_hp[0] <= 0:
                                target.retainers_hp.pop(0)

                        # Apply Temp HP first
                        if target.temp_hp > 0:
                            t_absorb = min(target.temp_hp, final_dmg)
                            target.temp_hp -= t_absorb
                            final_dmg -= t_absorb

                        target.current_hp -= final_dmg

        alive_pcs = [p for p in pcs if p.current_hp > 0]
        return {
            "victory": len(alive_pcs) > 0,
            "rounds": total_rounds,
            "surviving_pcs": len(alive_pcs),
            "pc_hp_pct": sum(p.current_hp for p in pcs) / sum(p.max_hp for p in pcs)
        }

def run_party_suite(pc_names: List[str], scenario_name: str, enemy_files: List[str], env: str = "the_neither", iterations: int = 100):
    tmpl_dir = Path("ClockworkPathfinder/testing/combat_sim/templates")
    pc_paths = [str(tmpl_dir / f"{name}_lv5.json") for name in pc_names]
    
    wins = 0
    tot_rounds = 0
    tot_hp_pct = 0.0

    for _ in range(iterations):
        sim = GroupCombatSim(pc_paths, enemy_files, env=env, initial_distance=50)
        res = sim.run_battle()
        if res["victory"]:
            wins += 1
        tot_rounds += res["rounds"]
        tot_hp_pct += max(0.0, res["pc_hp_pct"])

    win_rate = (wins / iterations) * 100
    avg_rounds = tot_rounds / iterations
    avg_hp = (tot_hp_pct / iterations) * 100

    print(f"Scenario: {scenario_name:<38} | Env: {env:<12} | Win Rate: {win_rate:5.1f}% | Avg Rounds: {avg_rounds:.1f} | Party HP Remaining: {avg_hp:4.1f}%")

if __name__ == "__main__":
    creat_dir = Path("ClockworkPathfinder/testing/combat_sim/creatures")
    
    print("=" * 115)
    print("CLOCKWORK CITIES: 4-PC PARTY COMBAT SIMULATOR (PARTY VS MOB / BOSS AUDIT)")
    print("Testing Balanced Team: Soldier (Tank), Survivor (Flanker), Rifleman (Overwatch), Chirurgeon (Medic)")
    print("=" * 115)

    balanced_party = ["soldier", "survivor", "clockworkrifleman", "chirurgeon"]
    scholar_party   = ["soldier", "survivor", "scholar", "chirurgeon"]
    noble_party     = ["noble_soldier", "noble", "clockworkrifleman", "chirurgeon"]

    # 1. 4 PCs vs Pack of 6 Wolves (Stalkers)
    wolves_6 = [str(creat_dir / "creature_wolf_lv3.json") for _ in range(6)]
    run_party_suite(balanced_party, "4 PCs vs 6 Level 3 Wolves (Stalkers)", wolves_6, "the_neither")

    # 2. 4 PCs vs Pack of 8 Wolves (Minion Horde)
    wolves_8 = [str(creat_dir / "creature_wolf_lv3.json") for _ in range(8)]
    run_party_suite(balanced_party, "4 PCs vs 8 Level 3 Wolves (Minion Horde)", wolves_8, "the_neither")

    # 3. 4 PCs vs 4 Level 5 Brutes (Equal-Level Squad)
    bears_4 = [str(creat_dir / "creature_bear_lv5.json") for _ in range(4)]
    run_party_suite(balanced_party, "4 PCs vs 4 Level 5 Brute Bears (Equal Squad)", bears_4, "the_neither")

    # 4. 4 PCs vs 1 Level 10 Apex Monster (SOLO BOSS FIGHT)
    boss_bear = [str(creat_dir / "bear_brute_lv10.json")]
    run_party_suite(balanced_party, "4 PCs vs 1 Level 10 Apex Bear (BOSS)", boss_bear, "the_neither")

    # 5. High Radiant Test with Scholar & Chirurgeon vs Boss
    print("\n--- HIGH RADIANT TESTING (Scholar Telemetry & Inductive Barriers) ---")
    run_party_suite(scholar_party, "Scholar Party vs 1 Lv 10 Apex Bear", boss_bear, "high_radiant")
    run_party_suite(scholar_party, "Scholar Party vs 4 Lv 5 Acid Spitters", [str(creat_dir / "creature_acid_spitter_lv5.json") for _ in range(4)], "high_radiant")

    # 6. Noble + Retainers Test (Armed Bodyguard Shield Wall)
    print("\n--- NOBLE RETAINER TESTING (Action Flooding & Meat Shields) ---")
    run_party_suite(noble_party, "Noble Party (+4 Retainers) vs 4 Lv 5 Bears", bears_4, "the_neither")
    run_party_suite(noble_party, "Noble Party (+4 Retainers) vs 8 Lv 3 Wolves", wolves_8, "the_neither")

