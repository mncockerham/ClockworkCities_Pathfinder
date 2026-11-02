"""
Monster Encounters Comparison:
3 Parties Compared:
1. Party Chirurgeon: Soldier, Rifleman, Merchant_Fire (+2 Retainers), Chirurgeon
2. Party Scholar:    Soldier, Rifleman, Merchant_Fire (+2 Retainers), Scholar
3. Party 2-Soldier:  Soldier, Soldier, Rifleman, Merchant_Fire (+2 Retainers)

Tested against:
- Minion Horde: 8 Level 3 Wolves (Stalkers)
- Equal Squad:  4 Level 5 Brute Bears
- Apex Boss:    1 Level 10 Apex Monster (high AC, huge HP, lethal crits)

At Level 5 (Core Tier) across 400 runs each.
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

parties = {
    "Chirurgeon Party": ["soldier", "clockworkrifleman", "merchant_neitherfire", "chirurgeon"],
    "Scholar Party":    ["soldier", "clockworkrifleman", "merchant_neitherfire", "scholar"],
    "2-Soldier Party":  ["soldier", "soldier", "clockworkrifleman", "merchant_neitherfire"]
}

def run_monster_test(party_name, pc_classes, monster_file, monster_count, env="the_neither", level=5, iterations=400):
    pc_files = [str(tmpl_dir / f"{c}_lv{level}.json") for c in pc_classes]
    m_files = [str(monster_file) for _ in range(monster_count)]

    wins = 0
    tot_rounds = 0
    tot_hp_pct = 0.0
    member_deaths = [0] * len(pc_classes)

    # Dist: 40 ft for mobs, 50 ft for boss
    dist = 50 if monster_count == 1 else 40

    ch_dr = 8 if level == 5 else 10
    drone_absorb = 10 if level == 5 else 12
    ch_heal = (2, 6, 8) if level == 5 else (3, 6, 10)

    sc_hit = 2 if env == "high_radiant" else 1
    sc_barrier = 15 if env == "high_radiant" else (8 if env == "low_radiant" else 5)

    has_ch = "chirurgeon" in pc_classes
    has_sc = "scholar" in pc_classes

    for _ in range(iterations):
        sim = GroupCombatSim(pc_files, m_files, env=env, initial_distance=dist)
        pcs = [sim._load_combatant(f, True, 0) for f in sim.pc_files]
        enemies = [sim._load_combatant(f, False, dist) for f in sim.enemy_files]

        total_rounds = 0
        while total_rounds < 30:
            total_rounds += 1
            alive_pcs = [p for p in pcs if p.current_hp > 0]
            alive_enemies = [e for e in enemies if e.current_hp > 0]
            if not alive_pcs or not alive_enemies:
                break

            # Start of round support
            if has_ch:
                c = next((p for p in alive_pcs if p.archetype == "Chirurgeon"), None)
                if c:
                    wounded = [p for p in alive_pcs if p.current_hp < p.max_hp]
                    if wounded:
                        target = min(wounded, key=lambda p: p.current_hp / p.max_hp)
                        num, sides, flat = ch_heal
                        target.current_hp = min(target.max_hp, target.current_hp + sum(random.randint(1, sides) for _ in range(num)) + flat)
            if has_sc:
                s = next((p for p in alive_pcs if p.archetype == "Scholar"), None)
                if s:
                    target = min(alive_pcs, key=lambda p: p.current_hp)
                    target.temp_hp = max(target.temp_hp, sc_barrier)

            # PC turns
            for pc in alive_pcs:
                if pc.current_hp <= 0: continue
                alive_e = [e for e in enemies if e.current_hp > 0]
                if not alive_e: break

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
                    bonus = chosen_w.get("attack_bonus", 8) + (sc_hit if has_sc else 0)
                    total_atk = atk_roll + bonus + map_pen

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

            # Enemy turns
            alive_e = [e for e in enemies if e.current_hp > 0]
            for en in alive_e:
                if en.current_hp <= 0: continue
                alive_p = [p for p in pcs if p.current_hp > 0]
                if not alive_p: break

                target = min(alive_p, key=lambda p: abs(en.pos - p.pos))
                dist_now = abs(en.pos - target.pos)
                actions = 3

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

                        if has_ch:
                            c = next((p for p in pcs if p.archetype == "Chirurgeon" and p.current_hp > 0), None)
                            if c and c.drone_interceptions_left > 0:
                                c.drone_interceptions_left -= 1
                                dmg = max(0, dmg - drone_absorb)
                            dmg = max(0, dmg - ch_dr)

                        if target.retainers_hp and dmg > 0:
                            intercept = min(target.retainers_hp[0], dmg // 2)
                            target.retainers_hp[0] -= intercept
                            dmg -= intercept
                            if target.retainers_hp[0] <= 0:
                                target.retainers_hp.pop(0)

                        if target.temp_hp > 0 and dmg > 0:
                            rem = min(target.temp_hp, dmg)
                            target.temp_hp -= rem
                            dmg -= rem

                        target.current_hp -= dmg

        tot_rounds += total_rounds
        alive = [p for p in pcs if p.current_hp > 0]
        if alive:
            wins += 1
            tot_hp_pct += sum(p.current_hp for p in pcs) / sum(p.max_hp for p in pcs)
        for idx, p in enumerate(pcs):
            if p.current_hp <= 0:
                member_deaths[idx] += 1

    return {
        "party": party_name,
        "win_pct": round((wins / iterations) * 100, 1),
        "avg_rounds": round(tot_rounds / iterations, 1),
        "avg_hp_pct": round((tot_hp_pct / iterations) * 100, 1),
        "deaths": [round((d / iterations) * 100, 1) for d in member_deaths]
    }

def main():
    print("=" * 100)
    print("MONSTER ENCOUNTER BENCHMARK: CHIRURGEON vs SCHOLAR vs 2-SOLDIER PARTY")
    print("Tested over 400 battles each in The Neither at Level 5")
    print("=" * 100)

    scenarios = [
        ("Minion Horde: 8 Lv 3 Wolves", creat_dir / "creature_wolf_lv3.json", 8),
        ("Equal Squad: 4 Lv 5 Bears", creat_dir / "creature_bear_lv5.json", 4),
        ("Apex Boss: 1 Lv 10 Apex Bear", creat_dir / "bear_brute_lv10.json", 1)
    ]

    for sc_name, m_file, count in scenarios:
        print(f"\n>>> SCENARIO: {sc_name}")
        print(f"{'Party Composition':<22} | {'Win Rate':<10} | {'Avg HP Left':<12} | {'Avg Rounds':<11} | {'Member Death Breakdown'}")
        print("-" * 100)
        for p_name, p_classes in parties.items():
            res = run_monster_test(p_name, p_classes, m_file, count, env="the_neither", level=5, iterations=400)
            deaths_str = ", ".join(f"{p_classes[i]}: {res['deaths'][i]}%" for i in range(len(p_classes)))
            print(f"{res['party']:<22} | {res['win_pct']:5.1f}%    | {res['avg_hp_pct']:5.1f}%       | {res['avg_rounds']:4.1f}        | {deaths_str}")

if __name__ == "__main__":
    main()
