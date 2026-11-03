"""
The Multi-Tier Grind: Combat Endurance Benchmark across Enemy Tiers (Lv 3 & Lv 4)
Tests:
- 4 PC Party at Level 5 (randomly drafted from 13 core classes).
- Facing sequential waves of:
  * Tier A: 4 Level 3 NPCs
  * Tier B: 4 Level 4 NPCs
- Across 3 Healing Conditions between fights:
  * 0% Healing (Raw Meatgrinder)
  * 10% Healing (Minor Quick Patch / Rest)
  * 50% Healing (Standard Treat Wounds / Field Concoction)
- 400 Trials per condition (Total: 2,400 gauntlets).
- Up to 20 waves per trial until Total Party Wipe (TPW).

Outputs:
- Average consecutive waves cleared before TPW
- Average total rounds fought
- For each class:
  * Lifespan Depth (Average fight number of death)
  * Survival % of Wave 1
  * Impact on squad victory / correlation
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

CORE_13_CLASSES = [
    "soldier",
    "survivor",
    "rake",
    "pugilist",
    "scout",
    "clockworkrifleman",
    "officer",
    "chirurgeon",
    "scholar",
    "greymarketeer",
    "noble",
    "clockworkengineer",
    "merchant_neitherfire"
]

DISPLAY_NAMES = {
    "soldier": "Soldier",
    "survivor": "Survivor",
    "rake": "Rake",
    "pugilist": "Pugilist",
    "scout": "Scout",
    "clockworkrifleman": "Clockwork Rifleman",
    "officer": "Officer",
    "chirurgeon": "Chirurgeon",
    "scholar": "Scholar",
    "greymarketeer": "Grey Marketeer",
    "noble": "Noble",
    "clockworkengineer": "Clockwork Engineer",
    "merchant_neitherfire": "Merchant"
}

def simulate_wave(pcs, enemy_classes, enemy_level=4, env="the_neither", dist=50):
    sim = GroupCombatSim([], [str(tmpl_dir / f"{c}_lv{enemy_level}.json") for c in enemy_classes], env=env, initial_distance=dist)
    enemies = [sim._load_combatant(f, False, dist) for f in sim.enemy_files]

    for p in pcs:
        p.pos = 0
        p.temp_hp = 0

    has_ch_pc = any(p.archetype == "Chirurgeon" and p.current_hp > 0 for p in pcs)
    has_ch_en = any(e.archetype == "Chirurgeon" and e.current_hp > 0 for e in enemies)
    has_sc_pc = any(p.archetype == "Scholar" and p.current_hp > 0 for p in pcs)
    has_sc_en = any(e.archetype == "Scholar" and e.current_hp > 0 for e in enemies)

    ch_pc_heals = 3 if has_ch_pc else 0
    ch_en_heals = 3 if has_ch_en else 0
    ch_pc_drone_ints = 6 if has_ch_pc else 0
    ch_en_drone_ints = 4 if enemy_level == 3 else 6

    alive_pcs = [p for p in pcs if p.current_hp > 0]
    if has_sc_pc and alive_pcs:
        alive_pcs[0].temp_hp += 8
    if has_sc_en and enemies:
        enemies[0].temp_hp += 6 if enemy_level == 3 else 8

    sc_pc_hit = 1 if has_sc_pc else 0
    sc_en_hit = 1 if has_sc_en else 0

    for p in pcs:
        if p.archetype == "ClockworkEngineer" and p.current_hp > 0:
            p.temp_hp += 8
    for e in enemies:
        if e.archetype == "ClockworkEngineer" and e.current_hp > 0:
            e.temp_hp += 6 if enemy_level == 3 else 8

    rounds = 0
    while rounds < 30:
        rounds += 1
        alive_p = [p for p in pcs if p.current_hp > 0]
        alive_e = [e for e in enemies if e.current_hp > 0]
        if not alive_p or not alive_e:
            break

        pc_reaction_used = False
        en_reaction_used = False

        # --- PC TURNS ---
        for pc in alive_p:
            if pc.current_hp <= 0: continue
            alive_e_now = [e for e in enemies if e.current_hp > 0]
            if not alive_e_now: break
            actions = 3

            # Engineer Backpack
            if pc.archetype == "ClockworkEngineer":
                t = min(alive_e_now, key=lambda e: (abs(pc.pos - e.pos), e.current_hp))
                if abs(pc.pos - t.pos) <= 60:
                    if random.randint(1, 20) + 12 >= t.ac:
                        t.current_hp -= (roll_dice("2d8") + 3)

            # Chirurgeon Heal
            if pc.archetype == "Chirurgeon" and ch_pc_heals > 0:
                wounded = [p for p in alive_p if p.current_hp < p.max_hp]
                if wounded:
                    ch_pc_heals -= 1
                    t = min(wounded, key=lambda x: x.current_hp / x.max_hp)
                    t.current_hp = min(t.max_hp, t.current_hp + roll_dice("2d6") + 4)
                    actions -= 2

            # Retainers
            if pc.retainers_hp:
                for _ in pc.retainers_hp:
                    if not alive_e_now: break
                    t = alive_e_now[0]
                    if random.randint(1, 20) + 7 >= t.ac:
                        t.current_hp -= (roll_dice("1d8") + 2)
                    alive_e_now = [e for e in enemies if e.current_hp > 0]

            if not alive_e_now: break
            target = min(alive_e_now, key=lambda e: (abs(pc.pos - e.pos), e.current_hp))
            if target.archetype in ["Scholar", "Chirurgeon"] and random.random() < 0.50:
                other_enemies = [e for e in alive_e_now if e.archetype not in ["Scholar", "Chirurgeon"]]
                if other_enemies:
                    target = max(other_enemies, key=lambda e: (e.ac, e.current_hp))
            dist_now = abs(pc.pos - target.pos)

            melee_w = [w for w in pc.weapons if w.get("range", 0) == 0]
            ranged_w = [w for w in pc.weapons if w.get("range", 0) >= dist_now]
            chosen_w = max(ranged_w, key=lambda x: x.get("attack_bonus", 0)) if (ranged_w and dist_now > 5) else (max(melee_w, key=lambda x: x.get("attack_bonus", 0)) if melee_w else pc.weapons[0])

            if chosen_w.get("range", 0) == 0 and dist_now > 5:
                while dist_now > 5 and actions >= 1:
                    dist_now = max(5, dist_now - pc.speed)
                    pc.pos = target.pos - dist_now if pc.pos < target.pos else target.pos + dist_now
                    actions -= 1

            map_c = 0
            while actions >= 1 and target.current_hp > 0:
                actions -= 1
                pen = 0 if map_c == 0 else (-4 if "agile" in chosen_w.get("traits", []) else -5)
                map_c += 1
                tot_atk = random.randint(1, 20) + chosen_w.get("attack_bonus", 8) + sc_pc_hit + pen
                eff_ac = target.ac - 2 if sum(1 for p in alive_p if abs(p.pos - target.pos) <= 5) >= 2 else target.ac

                if tot_atk >= eff_ac:
                    is_crit = (tot_atk >= eff_ac + 10)
                    base = roll_dice(chosen_w.get("damage_dice", "1d6")) + chosen_w.get("flat_damage", 2)
                    dmg = (base * 2) if is_crit else base
                    if is_crit and "fatal_d10" in chosen_w.get("traits", []): dmg += roll_dice("1d10")
                    elif is_crit and "fatal_d12" in chosen_w.get("traits", []): dmg += roll_dice("1d12")

                    if has_ch_en and not en_reaction_used and ch_en_drone_ints > 0:
                        en_reaction_used = True
                        ch_en_drone_ints -= 1
                        dmg = max(0, dmg - (6 if enemy_level == 3 else 8))

                    if target.retainers_hp and dmg > 0:
                        inc = min(target.retainers_hp[0], dmg // 2)
                        target.retainers_hp[0] -= inc
                        dmg -= inc
                        if target.retainers_hp[0] <= 0: target.retainers_hp.pop(0)

                    if target.temp_hp > 0 and dmg > 0:
                        rem = min(target.temp_hp, dmg)
                        target.temp_hp -= rem
                        dmg -= rem

                    target.current_hp -= dmg

        # --- ENEMY TURNS ---
        alive_e = [e for e in enemies if e.current_hp > 0]
        for en in alive_e:
            if en.current_hp <= 0: continue
            alive_p_now = [p for p in pcs if p.current_hp > 0]
            if not alive_p_now: break
            actions = 3

            if en.archetype == "ClockworkEngineer":
                t = min(alive_p_now, key=lambda p: (abs(en.pos - p.pos), p.current_hp))
                if abs(en.pos - t.pos) <= 60:
                    bonus = 9 if enemy_level == 3 else 10
                    if random.randint(1, 20) + bonus >= t.ac:
                        t.current_hp -= (roll_dice("1d8") + 2)

            if en.archetype == "Chirurgeon" and ch_en_heals > 0:
                w = [e for e in alive_e if e.current_hp < e.max_hp]
                if w:
                    ch_en_heals -= 1
                    t = min(w, key=lambda x: x.current_hp / x.max_hp)
                    t.current_hp = min(t.max_hp, t.current_hp + roll_dice("2d6") + (2 if enemy_level == 3 else 4))
                    actions -= 2

            if en.retainers_hp:
                for _ in en.retainers_hp:
                    if not alive_p_now: break
                    t = alive_p_now[0]
                    ret_atk = 5 if enemy_level == 3 else 6
                    if random.randint(1, 20) + ret_atk >= t.ac:
                        t.current_hp -= (roll_dice("1d8") + 1)
                    alive_p_now = [p for p in pcs if p.current_hp > 0]

            if not alive_p_now: break
            target = min(alive_p_now, key=lambda p: (abs(en.pos - p.pos), p.current_hp))
            # Party Bodyguard Redirection (Protecting Scholar & Chirurgeon Support):
            # If target is Scholar or Chirurgeon, 50% of attacks are intercepted/redirected to frontline/other allies
            if target.archetype in ["Scholar", "Chirurgeon"] and random.random() < 0.50:
                other_allies = [p for p in alive_p_now if p.archetype not in ["Scholar", "Chirurgeon"]]
                if other_allies:
                    # Priority bodyguard: highest HP or frontline tank (Soldier/Pugilist/Survivor)
                    target = max(other_allies, key=lambda p: (p.ac, p.current_hp))
            dist_now = abs(en.pos - target.pos)

            melee_w = [w for w in en.weapons if w.get("range", 0) == 0]
            ranged_w = [w for w in en.weapons if w.get("range", 0) >= dist_now]
            chosen_w = max(ranged_w, key=lambda x: x.get("attack_bonus", 0)) if (ranged_w and dist_now > 5) else (max(melee_w, key=lambda x: x.get("attack_bonus", 0)) if melee_w else en.weapons[0])

            if chosen_w.get("range", 0) == 0 and dist_now > 5:
                while dist_now > 5 and actions >= 1:
                    dist_now = max(5, dist_now - en.speed)
                    en.pos = target.pos - dist_now if en.pos < target.pos else target.pos + dist_now
                    actions -= 1

            map_c = 0
            while actions >= 1 and target.current_hp > 0:
                actions -= 1
                pen = 0 if map_c == 0 else (-4 if "agile" in chosen_w.get("traits", []) else -5)
                map_c += 1
                tot_atk = random.randint(1, 20) + chosen_w.get("attack_bonus", 7) + sc_en_hit + pen
                eff_ac = target.ac - 2 if sum(1 for e in alive_e if abs(e.pos - target.pos) <= 5) >= 2 else target.ac

                if tot_atk >= eff_ac:
                    is_crit = (tot_atk >= eff_ac + 10)
                    base = roll_dice(chosen_w.get("damage_dice", "1d6")) + chosen_w.get("flat_damage", 2)
                    dmg = (base * 2) if is_crit else base
                    if is_crit and "fatal_d10" in chosen_w.get("traits", []): dmg += roll_dice("1d10")
                    elif is_crit and "fatal_d12" in chosen_w.get("traits", []): dmg += roll_dice("1d12")

                    if has_ch_pc and not pc_reaction_used and ch_pc_drone_ints > 0:
                        pc_reaction_used = True
                        ch_pc_drone_ints -= 1
                        dmg = max(0, dmg - 8)

                    if target.retainers_hp and dmg > 0:
                        inc = min(target.retainers_hp[0], dmg // 2)
                        target.retainers_hp[0] -= inc
                        dmg -= inc
                        if target.retainers_hp[0] <= 0: target.retainers_hp.pop(0)

                    if target.temp_hp > 0 and dmg > 0:
                        rem = min(target.temp_hp, dmg)
                        target.temp_hp -= rem
                        dmg -= rem

                    target.current_hp -= dmg

    alive_pcs_end = [p for p in pcs if p.current_hp > 0]
    alive_en_end = [e for e in enemies if e.current_hp > 0]
    pc_victory = len(alive_pcs_end) > 0 and len(alive_en_end) == 0

    return pc_victory, rounds

def run_suite_tier(enemy_level, heal_pct, num_runs=400, max_waves=20, env="the_neither"):
    class_runs = defaultdict(int)
    class_death_fight = defaultdict(list)
    class_rounds_fought = defaultdict(list)
    class_survived_wave1 = defaultdict(int)

    squad_waves_won = []
    squad_total_rounds = []

    for trial in range(num_runs):
        pc_classes = random.sample(CORE_13_CLASSES, 4)
        sim = GroupCombatSim([str(tmpl_dir / f"{c}_lv5.json") for c in pc_classes], [], env=env)
        pcs = [sim._load_combatant(f, True, 0) for f in sim.pc_files]

        for c in pc_classes:
            class_runs[c] += 1

        death_fight_num = {idx: None for idx in range(4)}
        rounds_participated = {idx: 0 for idx in range(4)}

        waves_won = 0
        total_squad_rounds = 0

        for wave in range(1, max_waves + 1):
            living_indices = [idx for idx, p in enumerate(pcs) if p.current_hp > 0]
            if not living_indices:
                break

            enemy_classes = random.sample(CORE_13_CLASSES, 4)
            pc_won, fight_rounds = simulate_wave(pcs, enemy_classes, enemy_level=enemy_level, env=env)
            total_squad_rounds += fight_rounds

            for idx in living_indices:
                rounds_participated[idx] += fight_rounds
                if pcs[idx].current_hp <= 0 and death_fight_num[idx] is None:
                    death_fight_num[idx] = wave

            if pc_won:
                waves_won += 1
                if wave == 1:
                    for idx in range(4):
                        if death_fight_num[idx] is None or death_fight_num[idx] > 1:
                            class_survived_wave1[pc_classes[idx]] += 1

                if heal_pct > 0.0:
                    for p in pcs:
                        if p.current_hp > 0:
                            missing = p.max_hp - p.current_hp
                            p.current_hp = min(p.max_hp, p.current_hp + int(missing * heal_pct))
            else:
                for idx in range(4):
                    if death_fight_num[idx] is None:
                        death_fight_num[idx] = wave
                break

        squad_waves_won.append(waves_won)
        squad_total_rounds.append(total_squad_rounds)

        for idx, c in enumerate(pc_classes):
            df = death_fight_num[idx] if death_fight_num[idx] is not None else (max_waves + 1)
            class_death_fight[c].append(df)
            class_rounds_fought[c].append(rounds_participated[idx])

    avg_waves = sum(squad_waves_won) / len(squad_waves_won)
    avg_rounds = sum(squad_total_rounds) / len(squad_total_rounds)
    max_w = max(squad_waves_won)

    class_stats = []
    for c in CORE_13_CLASSES:
        runs = class_runs[c]
        avg_df = sum(class_death_fight[c]) / runs
        surv_w1 = (class_survived_wave1[c] / runs) * 100
        avg_rf = sum(class_rounds_fought[c]) / runs
        disp = DISPLAY_NAMES[c]
        class_stats.append((disp, avg_df, surv_w1, avg_rf))

    class_stats.sort(key=lambda x: x[1], reverse=True)

    return {
        "enemy_level": enemy_level,
        "heal_pct": heal_pct,
        "avg_waves": avg_waves,
        "avg_rounds": avg_rounds,
        "max_waves": max_w,
        "classes": class_stats
    }

def main():
    print("=" * 115)
    print("THE GRIND 3.0: 4 PCs (Lv 5) vs Consecutive Waves of Level 3 and Level 4 Enemies")
    print("Tested at 0%, 10%, and 50% Between-Fight Healing (400 Trials per condition = 2,400 Gauntlets)")
    print("=" * 115)

    suites = [
        (3, 0.0),
        (3, 0.10),
        (3, 0.50),
        (4, 0.0),
        (4, 0.10),
        (4, 0.50),
    ]

    results = []
    for elvl, heal in suites:
        print(f"\nRunning 400 Trials: Enemies Lv {elvl} | Healing {heal*100:.0f}%...")
        res = run_suite_tier(enemy_level=elvl, heal_pct=heal, num_runs=400)
        results.append(res)

    # Print summary tables
    for res in results:
        print("\n" + "=" * 115)
        print(f"ENEMIES: LEVEL {res['enemy_level']} | BETWEEN-FIGHT HEALING: {res['heal_pct']*100:.0f}%")
        print(f"Squad Performance: Avg Waves Won: {res['avg_waves']:.2f} | Avg Rounds: {res['avg_rounds']:.1f} | Max Waves Cleared: {res['max_waves']}")
        print("-" * 115)
        print(f"{'Rank':<5} | {'Class / Archetype':<22} | {'Lifespan (Avg Death Fight #)':<30} | {'Survive Wave 1 %':<18} | {'Avg Rounds Fought'}")
        print("-" * 115)
        for rank, (disp, avg_df, surv_w1, avg_rf) in enumerate(res['classes'], 1):
            print(f"#{rank:<4} | {disp:<22} | Fight #{avg_df:4.2f}                       | {surv_w1:5.1f}%             | {avg_rf:4.1f} rounds")

if __name__ == "__main__":
    main()

