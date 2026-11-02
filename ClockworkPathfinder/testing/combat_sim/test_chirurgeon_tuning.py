"""
Tuning Chirurgeon to 60/40 or 65/35 target balance vs 2-Soldier and Scholar parties.
We test:
1. Baseline (Uncapped 8-10 DR passive on all hits + multiple drone intercepts per round) -> 100% win rate (Broken)
2. Variant A:
   - Drone Intercept: strictly 1 REACTION per round, absorbs 2*INT damage.
   - Prophylactic Salve: PF2e-aligned Resistance = WIS mod (4 at Lv 5, 5 at Lv 10) against 1 chosen damage type (e.g., Slashing or Fire), NOT all physical damage universally.
   - Drone Heals: Requires 1 Action (or if 0 AP, limited to 1 target per round for 1d8 + WIS).
3. Variant B:
   - Drone Intercept: 1 REACTION per round, absorbs 2*INT.
   - Prophylactic Salve: Temp HP buffer at start of combat = Level * WIS (20 temp HP at Lv 5), rather than infinite passive DR.
   - Drone Heals: 1d8 + WIS once per round.

Let's test these variants across 400 iterations at Level 5 in The Neither.
"""

import sys
import random
import json
from pathlib import Path

SIM_DIR = Path("ClockworkPathfinder/testing/combat_sim")
sys.path.append(str(SIM_DIR))

from run_group_combat_sim import GroupCombatSim, roll_dice

tmpl_dir = SIM_DIR / "templates"
creat_dir = SIM_DIR / "creatures"

p_ch = ["soldier", "clockworkrifleman", "merchant_neitherfire", "chirurgeon"]
p_2s = ["soldier", "soldier", "clockworkrifleman", "merchant_neitherfire"]
p_sc = ["soldier", "clockworkrifleman", "merchant_neitherfire", "scholar"]

def test_tuning(tuning_mode, p1_classes, p2_classes, level=5, iterations=400):
    p1_files = [str(tmpl_dir / f"{c}_lv{level}.json") for c in p1_classes]
    p2_files = [str(tmpl_dir / f"{c}_lv{level}.json") for c in p2_classes]
    dist = 50

    p1_wins = 0
    p2_wins = 0

    for _ in range(iterations):
        sim = GroupCombatSim(p1_files, p2_files, env="the_neither", initial_distance=dist)
        p1 = [sim._load_combatant(f, True, 0) for f in sim.pc_files]
        p2 = [sim._load_combatant(f, False, dist) for f in sim.enemy_files]

        # Tuning setup
        if tuning_mode == "baseline":
            party_dr = 8
            drone_absorb = 10
            heal_dice = "2d6+8"
            max_reactions_per_round = 999
            temp_buffer = 0
        elif tuning_mode == "variant_a": # Resistance = WIS (4), Reaction = 1/rnd
            party_dr = 4
            drone_absorb = 8
            heal_dice = "1d8+4"
            max_reactions_per_round = 1
            temp_buffer = 0
        elif tuning_mode == "variant_b": # Temp HP buffer (20), Reaction = 1/rnd, DR = 0
            party_dr = 0
            drone_absorb = 8
            heal_dice = "1d8+4"
            max_reactions_per_round = 1
            temp_buffer = 20
        elif tuning_mode == "variant_c": # Resistance = 2 (standard PF2e minor elixir), Reaction = 1/rnd
            party_dr = 2
            drone_absorb = 8
            heal_dice = "1d8+4"
            max_reactions_per_round = 1
            temp_buffer = 0

        if temp_buffer > 0:
            for p in p1:
                p.temp_hp += temp_buffer

        total_rounds = 0
        while total_rounds < 30:
            total_rounds += 1
            alive_p1 = [p for p in p1 if p.current_hp > 0]
            alive_p2 = [p for p in p2 if p.current_hp > 0]
            if not alive_p1 or not alive_p2:
                break

            # Chirurgeon resets reaction at start of their round
            reactions_used_this_round = 0

            # Heal 1 ally
            c = next((p for p in alive_p1 if p.archetype == "Chirurgeon"), None)
            if c:
                wounded = [p for p in alive_p1 if p.current_hp < p.max_hp]
                if wounded:
                    target = min(wounded, key=lambda p: p.current_hp / p.max_hp)
                    parts = heal_dice.split('+')
                    target.current_hp = min(target.max_hp, target.current_hp + roll_dice(parts[0]) + int(parts[1]))

            # Party 1 actions
            for pc in alive_p1:
                if pc.current_hp <= 0: continue
                alive_e = [e for e in p2 if e.current_hp > 0]
                if not alive_e: break
                target = min(alive_e, key=lambda e: (abs(pc.pos - e.pos), e.current_hp))
                dist_now = abs(pc.pos - target.pos)
                actions = 3

                # Retainers
                if pc.retainers_hp:
                    for _ in pc.retainers_hp:
                        if target.current_hp <= 0:
                            alive_e = [e for e in p2 if e.current_hp > 0]
                            if not alive_e: break
                            target = alive_e[0]
                        if random.randint(1, 20) + 7 >= target.ac:
                            target.current_hp -= (roll_dice("1d8") + 2)

                melee_w = [w for w in pc.weapons if w.get("range", 0) == 0]
                ranged_w = [w for w in pc.weapons if w.get("range", 0) >= dist_now]
                chosen_w = max(ranged_w, key=lambda w: w.get("attack_bonus", 0)) if (ranged_w and dist_now > 5) else (max(melee_w, key=lambda w: w.get("attack_bonus", 0)) if melee_w else pc.weapons[0])

                if chosen_w.get("range", 0) == 0 and dist_now > 5:
                    while dist_now > 5 and actions >= 1:
                        dist_now = max(5, dist_now - pc.speed)
                        pc.pos = target.pos - dist_now if pc.pos < target.pos else target.pos + dist_now
                        actions -= 1

                map_count = 0
                while actions >= 1 and target.current_hp > 0:
                    actions -= 1
                    map_pen = 0 if map_count == 0 else (-4 if "agile" in chosen_w.get("traits", []) else -5)
                    map_count += 1
                    atk_roll = random.randint(1, 20)
                    total_atk = atk_roll + chosen_w.get("attack_bonus", 8) + map_pen

                    melee_count = sum(1 for p in alive_p1 if abs(p.pos - target.pos) <= 5)
                    eff_ac = target.ac - 2 if melee_count >= 2 else target.ac

                    if total_atk >= eff_ac:
                        is_crit = (total_atk >= eff_ac + 10) or (atk_roll == 20 and total_atk >= eff_ac)
                        base = roll_dice(chosen_w.get("damage_dice", "1d6")) + chosen_w.get("flat_damage", 2)
                        dmg = (base * 2) if is_crit else base
                        if is_crit and "fatal_d10" in chosen_w.get("traits", []):
                            dmg += roll_dice("1d10")
                        elif is_crit and "fatal_d12" in chosen_w.get("traits", []):
                            dmg += roll_dice("1d12")
                        target.current_hp -= dmg

            # Party 2 actions
            alive_p2 = [e for e in p2 if e.current_hp > 0]
            for en in alive_p2:
                if en.current_hp <= 0: continue
                alive_p = [p for p in p1 if p.current_hp > 0]
                if not alive_p: break
                target = min(alive_p, key=lambda p: abs(en.pos - p.pos))
                dist_now = abs(en.pos - target.pos)
                actions = 3

                if en.retainers_hp:
                    for _ in en.retainers_hp:
                        if target.current_hp <= 0:
                            alive_p = [p for p in p1 if p.current_hp > 0]
                            if not alive_p: break
                            target = alive_p[0]
                        if random.randint(1, 20) + 7 >= target.ac:
                            target.current_hp -= (roll_dice("1d8") + 2)

                melee_w = [w for w in en.weapons if w.get("range", 0) == 0]
                ranged_w = [w for w in en.weapons if w.get("range", 0) >= dist_now]
                chosen_w = max(ranged_w, key=lambda w: w.get("attack_bonus", 0)) if (ranged_w and dist_now > 5) else (max(melee_w, key=lambda w: w.get("attack_bonus", 0)) if melee_w else en.weapons[0])

                if chosen_w.get("range", 0) == 0 and dist_now > 5:
                    while dist_now > 5 and actions >= 1:
                        dist_now = max(5, dist_now - en.speed)
                        en.pos = target.pos - dist_now if en.pos < target.pos else target.pos + dist_now
                        actions -= 1

                map_count = 0
                while actions >= 1 and target.current_hp > 0:
                    actions -= 1
                    map_pen = 0 if map_count == 0 else (-4 if "agile" in chosen_w.get("traits", []) else -5)
                    map_count += 1
                    atk_roll = random.randint(1, 20)
                    total_atk = atk_roll + chosen_w.get("attack_bonus", 8) + map_pen
                    eff_ac = target.ac

                    if total_atk >= eff_ac:
                        is_crit = (total_atk >= eff_ac + 10) or (atk_roll == 20 and total_atk >= eff_ac)
                        base = roll_dice(chosen_w.get("damage_dice", "1d6")) + chosen_w.get("flat_damage", 2)
                        dmg = (base * 2) if is_crit else base
                        if is_crit and "fatal_d10" in chosen_w.get("traits", []):
                            dmg += roll_dice("1d10")
                        elif is_crit and "fatal_d12" in chosen_w.get("traits", []):
                            dmg += roll_dice("1d12")

                        # Chirurgeon Drone Interception (STRICT 1 REACTION PER ROUND)
                        if c and reactions_used_this_round < max_reactions_per_round and c.drone_interceptions_left > 0:
                            reactions_used_this_round += 1
                            c.drone_interceptions_left -= 1
                            dmg = max(0, dmg - drone_absorb)

                        # Party-wide Resistance
                        dmg = max(0, dmg - party_dr)

                        # Retainer absorb
                        if target.retainers_hp and dmg > 0:
                            intercept = min(target.retainers_hp[0], dmg // 2)
                            target.retainers_hp[0] -= intercept
                            dmg -= intercept
                            if target.retainers_hp[0] <= 0:
                                target.retainers_hp.pop(0)

                        # Temp HP buffer
                        if target.temp_hp > 0 and dmg > 0:
                            rem = min(target.temp_hp, dmg)
                            target.temp_hp -= rem
                            dmg -= rem

                        target.current_hp -= dmg

        alive_end = [p for p in p1 if p.current_hp > 0]
        if alive_end:
            p1_wins += 1
        else:
            p2_wins += 1

    return round((p1_wins / iterations) * 100, 1)

print("=== TESTING TUNING VARIANTS AT LEVEL 5 (400 FIGHTS EACH) ===")
for mode in ["baseline", "variant_a", "variant_b", "variant_c"]:
    win_2s = test_tuning(mode, p_ch, p_2s, level=5, iterations=400)
    win_sc = test_tuning(mode, p_ch, p_sc, level=5, iterations=400)
    print(f"Mode: {mode:<10} | vs 2-Soldier Party Win%: {win_2s:5.1f}% | vs Scholar Party Win%: {win_sc:5.1f}%")

