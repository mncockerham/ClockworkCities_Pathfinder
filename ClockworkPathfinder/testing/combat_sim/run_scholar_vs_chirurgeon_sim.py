"""
Scholar vs Chirurgeon Head-to-Head and Party Comparison Simulation
Tests:
1. Party Chirurgeon vs Party Scholar (Direct Head-to-Head Party 4v4):
   - Party Chirurgeon: Soldier, Rifleman, Merchant_Fire, Chirurgeon
   - Party Scholar:    Soldier, Rifleman, Merchant_Fire, Scholar
   Across Levels 5 and 10 in all 4 environments (Neither, Civil, Low Radiant, High Radiant).

2. Party Chirurgeon vs Enemy Packs & Bosses:
   - vs 6 Minions (CR-appropriate scavenger/pack mobs)
   - vs Apex Boss (High HP, high AC, lethal single-target strikes)
   Compared against:
   Party Scholar vs Enemy Packs & Bosses.

Tracks:
- Win rates
- Member death percentages
- Avg rounds
- Avg HP remaining
"""

import sys
import random
import json
from pathlib import Path
from collections import defaultdict

SIM_DIR = Path("ClockworkPathfinder/testing/combat_sim")
sys.path.append(str(SIM_DIR))

from run_group_combat_sim import GroupCombatSim, PartyCombatant, roll_dice

tmpl_dir = SIM_DIR / "templates"

def simulate_party_match(p1_classes, p2_classes, level, env, iterations=400):
    p1_files = [str(tmpl_dir / f"{c}_lv{level}.json") for c in p1_classes]
    p2_files = [str(tmpl_dir / f"{c}_lv{level}.json") for c in p2_classes]

    p1_wins = 0
    p2_wins = 0
    draws = 0
    tot_rounds = 0
    tot_p1_hp_pct = 0.0
    tot_p2_hp_pct = 0.0

    p1_deaths = [0] * len(p1_classes)
    p2_deaths = [0] * len(p2_classes)

    dist = 50 if level == 5 else 60

    # Chirurgeon parameters
    if level == 5:
        ch_dr = 8
        drone_absorb = 10
        ch_heal = (2, 6, 8) # 2d6 + 8
    else:
        ch_dr = 10
        drone_absorb = 12
        ch_heal = (3, 6, 10) # 3d6 + 10

    # Scholar parameters
    # Telemetry: +1 hit in Neither/Civil/Low, +2 hit in High Radiant
    sc_hit = 2 if env == "high_radiant" else 1
    # Barrier pulse: 8 temp HP in Low, 15 in High, 5 in Civil/Neither
    if env == "high_radiant":
        sc_barrier = 15 if level == 5 else 25
    elif env == "low_radiant":
        sc_barrier = 8 if level == 5 else 15
    else:
        sc_barrier = 5 if level == 5 else 10

    for _ in range(iterations):
        sim = GroupCombatSim(p1_files, p2_files, env=env, initial_distance=dist)
        p1 = [sim._load_combatant(f, True, 0) for f in sim.pc_files]
        p2 = [sim._load_combatant(f, False, dist) for f in sim.enemy_files]

        has_ch1 = any(c.archetype == "Chirurgeon" for c in p1)
        has_ch2 = any(c.archetype == "Chirurgeon" for c in p2)
        has_sc1 = any(c.archetype == "Scholar" for c in p1)
        has_sc2 = any(c.archetype == "Scholar" for c in p2)

        total_rounds = 0
        while total_rounds < 30:
            total_rounds += 1
            alive_p1 = [p for p in p1 if p.current_hp > 0]
            alive_p2 = [p for p in p2 if p.current_hp > 0]

            if not alive_p1 or not alive_p2:
                break

            # --- START OF ROUND ABILITIES ---
            # Chirurgeon heals lowest % HP
            if has_ch1:
                c1 = next((p for p in alive_p1 if p.archetype == "Chirurgeon"), None)
                if c1:
                    w1 = [p for p in alive_p1 if p.current_hp < p.max_hp]
                    if w1:
                        target = min(w1, key=lambda p: p.current_hp / p.max_hp)
                        num, sides, flat = ch_heal
                        h = sum(random.randint(1, sides) for _ in range(num)) + flat
                        target.current_hp = min(target.max_hp, target.current_hp + h)
            if has_ch2:
                c2 = next((p for p in alive_p2 if p.archetype == "Chirurgeon"), None)
                if c2:
                    w2 = [p for p in alive_p2 if p.current_hp < p.max_hp]
                    if w2:
                        target = min(w2, key=lambda p: p.current_hp / p.max_hp)
                        num, sides, flat = ch_heal
                        h = sum(random.randint(1, sides) for _ in range(num)) + flat
                        target.current_hp = min(target.max_hp, target.current_hp + h)

            # Scholar barrier pulse to lowest HP
            if has_sc1:
                s1 = next((p for p in alive_p1 if p.archetype == "Scholar"), None)
                if s1:
                    target = min(alive_p1, key=lambda p: p.current_hp)
                    target.temp_hp = max(target.temp_hp, sc_barrier)
            if has_sc2:
                s2 = next((p for p in alive_p2 if p.archetype == "Scholar"), None)
                if s2:
                    target = min(alive_p2, key=lambda p: p.current_hp)
                    target.temp_hp = max(target.temp_hp, sc_barrier)

            # --- PARTY 1 TURNS ---
            for pc in alive_p1:
                if pc.current_hp <= 0: continue
                alive_targets = [e for e in p2 if e.current_hp > 0]
                if not alive_targets: break

                target = min(alive_targets, key=lambda e: (abs(pc.pos - e.pos), e.current_hp))
                dist_now = abs(pc.pos - target.pos)
                actions = 3

                # Retainers
                if pc.retainers_hp:
                    for _ in pc.retainers_hp:
                        if target.current_hp <= 0:
                            alive_targets = [e for e in p2 if e.current_hp > 0]
                            if not alive_targets: break
                            target = alive_targets[0]
                        ret_atk = 7 if level == 5 else 11
                        if random.randint(1, 20) + ret_atk >= target.ac:
                            target.current_hp -= (roll_dice("1d8" if level == 5 else "2d8") + 2)

                # Weapons
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
                    bonus = chosen_w.get("attack_bonus", 8) + (sc_hit if has_sc1 else 0)
                    total_atk = atk_roll + bonus + map_pen

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

                        # Chirurgeon defenses for P2
                        if has_ch2:
                            c2 = next((p for p in p2 if p.archetype == "Chirurgeon" and p.current_hp > 0), None)
                            if c2 and c2.drone_interceptions_left > 0:
                                c2.drone_interceptions_left -= 1
                                dmg = max(0, dmg - drone_absorb)
                            dmg = max(0, dmg - ch_dr)

                        # Retainer absorb
                        if target.retainers_hp and dmg > 0:
                            intercept = min(target.retainers_hp[0], dmg // 2)
                            target.retainers_hp[0] -= intercept
                            dmg -= intercept
                            if target.retainers_hp[0] <= 0:
                                target.retainers_hp.pop(0)

                        # Temp HP absorb
                        if target.temp_hp > 0 and dmg > 0:
                            rem = min(target.temp_hp, dmg)
                            target.temp_hp -= rem
                            dmg -= rem

                        target.current_hp -= dmg

            # --- PARTY 2 TURNS ---
            alive_p2 = [e for e in p2 if e.current_hp > 0]
            for pc in alive_p2:
                if pc.current_hp <= 0: continue
                alive_targets = [p for p in p1 if p.current_hp > 0]
                if not alive_targets: break

                target = min(alive_targets, key=lambda p: (abs(pc.pos - p.pos), p.current_hp))
                dist_now = abs(pc.pos - target.pos)
                actions = 3

                # Retainers
                if pc.retainers_hp:
                    for _ in pc.retainers_hp:
                        if target.current_hp <= 0:
                            alive_targets = [p for p in p1 if p.current_hp > 0]
                            if not alive_targets: break
                            target = alive_targets[0]
                        ret_atk = 7 if level == 5 else 11
                        if random.randint(1, 20) + ret_atk >= target.ac:
                            target.current_hp -= (roll_dice("1d8" if level == 5 else "2d8") + 2)

                # Weapons
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
                    bonus = chosen_w.get("attack_bonus", 8) + (sc_hit if has_sc2 else 0)
                    total_atk = atk_roll + bonus + map_pen

                    melee_count = sum(1 for p in alive_p2 if abs(p.pos - target.pos) <= 5)
                    eff_ac = target.ac - 2 if melee_count >= 2 else target.ac

                    if total_atk >= eff_ac:
                        is_crit = (total_atk >= eff_ac + 10) or (atk_roll == 20 and total_atk >= eff_ac)
                        base = roll_dice(chosen_w.get("damage_dice", "1d6")) + chosen_w.get("flat_damage", 2)
                        dmg = (base * 2) if is_crit else base
                        if is_crit and "fatal_d10" in chosen_w.get("traits", []):
                            dmg += roll_dice("1d10")
                        elif is_crit and "fatal_d12" in chosen_w.get("traits", []):
                            dmg += roll_dice("1d12")

                        # Chirurgeon defenses for P1
                        if has_ch1:
                            c1 = next((p for p in p1 if p.archetype == "Chirurgeon" and p.current_hp > 0), None)
                            if c1 and c1.drone_interceptions_left > 0:
                                c1.drone_interceptions_left -= 1
                                dmg = max(0, dmg - drone_absorb)
                            dmg = max(0, dmg - ch_dr)

                        # Retainer absorb
                        if target.retainers_hp and dmg > 0:
                            intercept = min(target.retainers_hp[0], dmg // 2)
                            target.retainers_hp[0] -= intercept
                            dmg -= intercept
                            if target.retainers_hp[0] <= 0:
                                target.retainers_hp.pop(0)

                        # Temp HP absorb
                        if target.temp_hp > 0 and dmg > 0:
                            rem = min(target.temp_hp, dmg)
                            target.temp_hp -= rem
                            dmg -= rem

                        target.current_hp -= dmg

        tot_rounds += total_rounds
        alive1 = [p for p in p1 if p.current_hp > 0]
        alive2 = [p for p in p2 if p.current_hp > 0]

        if alive1 and not alive2:
            p1_wins += 1
            tot_p1_hp_pct += max(0.0, sum(p.current_hp for p in p1) / sum(p.max_hp for p in p1))
        elif alive2 and not alive1:
            p2_wins += 1
            tot_p2_hp_pct += max(0.0, sum(p.current_hp for p in p2) / sum(p.max_hp for p in p2))
        else:
            draws += 1

        for idx, p in enumerate(p1):
            if p.current_hp <= 0: p1_deaths[idx] += 1
        for idx, p in enumerate(p2):
            if p.current_hp <= 0: p2_deaths[idx] += 1

    return {
        "p1_win_pct": round((p1_wins / iterations) * 100, 1),
        "p2_win_pct": round((p2_wins / iterations) * 100, 1),
        "draw_pct": round((draws / iterations) * 100, 1),
        "avg_rounds": round(tot_rounds / iterations, 1),
        "p1_deaths": [round((d / iterations) * 100, 1) for d in p1_deaths],
        "p2_deaths": [round((d / iterations) * 100, 1) for d in p2_deaths]
    }

def main():
    print("=" * 80)
    print("CHIRURGEON VS SCHOLAR PARTY COMPARISON (LEVEL 5 & LEVEL 10)")
    print("Party Chirurgeon: Soldier, Rifleman, Merchant_Fire (+Retainers), Chirurgeon")
    print("Party Scholar:    Soldier, Rifleman, Merchant_Fire (+Retainers), Scholar")
    print("=" * 80)

    environments = [
        ("The Neither", "the_neither"),
        ("Civil Spire", "civil_spire"),
        ("Low Radiant", "low_radiant"),
        ("High Radiant", "high_radiant")
    ]

    p_ch = ["soldier", "clockworkrifleman", "merchant_neitherfire", "chirurgeon"]
    p_sc = ["soldier", "clockworkrifleman", "merchant_neitherfire", "scholar"]

    for lvl in [5, 10]:
        print(f"\n==================== LEVEL {lvl} AUDIT (400 FIGHTS PER ZONE) ====================")
        for env_label, env_code in environments:
            res = simulate_party_match(p_ch, p_sc, level=lvl, env=env_code, iterations=400)
            print(f"\n[{env_label.upper()}] (Chirurgeon Squad vs Scholar Squad)")
            print(f"  Party Chirurgeon Win Rate: {res['p1_win_pct']:5.1f}%  |  Party Scholar Win Rate: {res['p2_win_pct']:5.1f}% (Draws: {res['draw_pct']}%)")
            print(f"  Avg Combat Duration: {res['avg_rounds']} rounds")
            print(f"  Party Chirurgeon Deaths: Soldier: {res['p1_deaths'][0]}%, Rifleman: {res['p1_deaths'][1]}%, Merchant: {res['p1_deaths'][2]}%, Chirurgeon: {res['p1_deaths'][3]}%")
            print(f"  Party Scholar Deaths:    Soldier: {res['p2_deaths'][0]}%, Rifleman: {res['p2_deaths'][1]}%, Merchant: {res['p2_deaths'][2]}%, Scholar: {res['p2_deaths'][3]}%")

if __name__ == "__main__":
    main()

