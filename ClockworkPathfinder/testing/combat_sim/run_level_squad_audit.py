"""
Multi-Level 4v4 Squad Combat Simulation:
Compares Party 1 (Team B with Chirurgeon) vs Party 2 (Team A with Double Soldier)
Across Levels 1, 5, and 10 separately over 400 iterations each in The Neither.

Party 1 (The Support Squad):
- Member 1: Soldier
- Member 2: Clockwork Rifleman
- Member 3: Merchant (Neither Fire) [+ Retainers]
- Member 4: Chirurgeon

Party 2 (The Double-Soldier Squad):
- Member 1: Soldier
- Member 2: Soldier
- Member 3: Clockwork Rifleman
- Member 4: Merchant (Neither Fire) [+ Retainers]

Outputs:
- Win Rate of Party 1
- Win Rate of Party 2
- Death % of EACH member of Party 1 across 400 battles
- Average Rounds per battle
- Party 1 Average HP remaining %
"""

import sys
import random
from pathlib import Path
from collections import defaultdict

sys.path.append(str(Path(__file__).parent))
from run_group_combat_sim import GroupCombatSim, roll_dice

tmpl_dir = Path("ClockworkPathfinder/testing/combat_sim/templates")

LEVELS = [1, 5, 10]

def run_level_squad_audit(level: int, iterations: int = 400, env: str = "the_neither"):
    p1_files = [
        str(tmpl_dir / f"soldier_lv{level}.json"),
        str(tmpl_dir / f"clockworkrifleman_lv{level}.json"),
        str(tmpl_dir / f"merchant_neitherfire_lv{level}.json"),
        str(tmpl_dir / f"chirurgeon_lv{level}.json")
    ]
    p1_member_names = ["Soldier", "Rifleman", "Merchant_Fire", "Chirurgeon"]

    p2_files = [
        str(tmpl_dir / f"soldier_lv{level}.json"),
        str(tmpl_dir / f"soldier_lv{level}.json"),
        str(tmpl_dir / f"clockworkrifleman_lv{level}.json"),
        str(tmpl_dir / f"merchant_neitherfire_lv{level}.json")
    ]

    p1_wins = 0
    p2_wins = 0
    tot_rounds = 0
    tot_p1_hp_pct = 0.0

    # Death counts for each individual member of Party 1
    # index 0: Soldier, 1: Rifleman, 2: Merchant, 3: Chirurgeon
    p1_deaths = [0, 0, 0, 0]

    for _ in range(iterations):
        # Initial distance: 40 ft for Lv 1, 50 ft for Lv 5, 60 ft for Lv 10
        dist = 40 if level == 1 else (50 if level == 5 else 60)
        sim = GroupCombatSim(p1_files, p2_files, env=env, initial_distance=dist)

        # Execute battle directly to track individual member deaths
        pcs = [sim._load_combatant(f, True, 0) for f in sim.pc_files]
        enemies = [sim._load_combatant(f, False, dist) for f in sim.enemy_files]

        # Party 1 Chirurgeon Scaling by Level:
        # Lv 1: DR = 1 * WIS = 4 DR, Drone absorb = 2 * INT = 8, Heal = 1d6 + 4
        # Lv 5: DR = 2 * WIS = 8 DR, Drone absorb = 2 * INT = 10, Heal = 2d6 + 8
        # Lv 10: DR = 2 * WIS = 10 DR, Drone absorb = 2 * INT = 12, Heal = 3d6 + 10
        if level == 1:
            party_dr = 4
            drone_absorb = 8
            heal_formula = "1d6+4"
        elif level == 5:
            party_dr = 8
            drone_absorb = 10
            heal_formula = "2d6+8"
        else:
            party_dr = 10
            drone_absorb = 12
            heal_formula = "3d6+10"

        total_rounds = 0
        while total_rounds < 30:
            total_rounds += 1
            alive_pcs = [p for p in pcs if p.current_hp > 0]
            alive_enemies = [e for e in enemies if e.current_hp > 0]
            if not alive_pcs or not alive_enemies:
                break

            # Chirurgeon Heal
            c = next((p for p in alive_pcs if p.archetype == "Chirurgeon"), None)
            if c:
                wounded = [p for p in alive_pcs if p.current_hp < p.max_hp]
                if wounded:
                    target = min(wounded, key=lambda p: p.current_hp / p.max_hp)
                    parts = heal_formula.split('+')
                    heal_amt = roll_dice(parts[0]) + int(parts[1])
                    target.current_hp = min(target.max_hp, target.current_hp + heal_amt)

            # Party 1 Turns
            for pc in alive_pcs:
                if pc.current_hp <= 0: continue
                alive_e = [e for e in enemies if e.current_hp > 0]
                if not alive_e: break

                # Target closest or lowest HP
                target = min(alive_e, key=lambda e: (abs(pc.pos - e.pos), e.current_hp))
                dist_now = abs(pc.pos - target.pos)
                actions = 3

                # Retainers
                if pc.retainers_hp:
                    for _ in pc.retainers_hp:
                        if target.current_hp <= 0:
                            alive_e = [e for e in enemies if e.current_hp > 0]
                            if not alive_e: break
                            target = alive_e[0]
                        if random.randint(1, 20) + (5 if level==1 else (7 if level==5 else 11)) >= target.ac:
                            target.current_hp -= (roll_dice("1d8" if level<10 else "2d8") + 2)

                # Pick weapon
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
                    melee_count = sum(1 for p in alive_pcs if abs(p.pos - target.pos) <= 5)
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

            # Party 2 Turns (Enemies)
            alive_e = [e for e in enemies if e.current_hp > 0]
            for en in alive_e:
                if en.current_hp <= 0: continue
                alive_p = [p for p in pcs if p.current_hp > 0]
                if not alive_p: break

                target = min(alive_p, key=lambda p: abs(en.pos - p.pos))
                dist_now = abs(en.pos - target.pos)
                actions = 3

                # Retainers
                if en.retainers_hp:
                    for _ in en.retainers_hp:
                        if target.current_hp <= 0:
                            alive_p = [p for p in pcs if p.current_hp > 0]
                            if not alive_p: break
                            target = alive_p[0]
                        if random.randint(1, 20) + (5 if level==1 else (7 if level==5 else 11)) >= target.ac:
                            target.current_hp -= (roll_dice("1d8" if level<10 else "2d8") + 2)

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

                        # Drone Intercept
                        if c and c.drone_interceptions_left > 0:
                            c.drone_interceptions_left -= 1
                            dmg = max(0, dmg - drone_absorb)

                        # Party-wide Prophylactic DR
                        dmg = max(0, dmg - party_dr)

                        # Retainer Intercept
                        if target.retainers_hp and dmg > 0:
                            intercept = min(target.retainers_hp[0], dmg // 2)
                            target.retainers_hp[0] -= intercept
                            dmg -= intercept
                            if target.retainers_hp[0] <= 0:
                                target.retainers_hp.pop(0)

                        target.current_hp -= dmg

        # Record Battle End State
        tot_rounds += total_rounds
        alive_at_end = [p for p in pcs if p.current_hp > 0]
        if len(alive_at_end) > 0:
            p1_wins += 1
            tot_p1_hp_pct += max(0.0, sum(p.current_hp for p in pcs) / sum(p.max_hp for p in pcs))
        else:
            p2_wins += 1

        # Check death of each member of Party 1
        for idx, pc in enumerate(pcs):
            if pc.current_hp <= 0:
                p1_deaths[idx] += 1

    p1_win_rate = (p1_wins / iterations) * 100
    p2_win_rate = (p2_wins / iterations) * 100
    avg_rounds = tot_rounds / iterations
    avg_hp_left = (tot_p1_hp_pct / iterations) * 100

    print("=" * 95)
    print(f"AUDIT REPORT: LEVEL {level} SQUAD COMBAT (400 BATTLES IN THE NEITHER)")
    print(f"Party 1 (Support): Soldier, Rifleman, Merchant_Fire (+Retainers), Chirurgeon")
    print(f"Party 2 (Power):   Soldier, Soldier, Rifleman, Merchant_Fire (+Retainers)")
    print("=" * 95)
    print(f"PARTY 1 WIN RATE: {p1_win_rate:5.1f}%  |  PARTY 2 WIN RATE: {p2_win_rate:5.1f}%")
    print(f"Average Battle Duration: {avg_rounds:.1f} Rounds  |  Party 1 Avg HP Remaining: {avg_hp_left:4.1f}%")
    print("-" * 95)
    print(f"{'Party 1 Member':<20} | {'Deaths':<8} | {'Death %':<10} | {'Survival Rate':<14} | {'Role & Target Profile':<30}")
    print("-" * 95)
    profiles = [
        "Primary Frontline Tank (Takes brunt of initial charge)",
        "Ranged Sniper (Backline overwatch)",
        "Mid-Range Bomb / Retainer Master",
        "Dedicated Triage / Swarm Commander"
    ]
    for idx, name in enumerate(p1_member_names):
        d_count = p1_deaths[idx]
        d_pct = (d_count / iterations) * 100
        surv_pct = 100.0 - d_pct
        print(f"{name:<20} | {d_count:<8} | {d_pct:5.1f}%   | {surv_pct:5.1f}%        | {profiles[idx]:<30}")
    print("=" * 95 + "\n")

if __name__ == "__main__":
    for lvl in LEVELS:
        run_level_squad_audit(level=lvl, iterations=400, env="the_neither")

