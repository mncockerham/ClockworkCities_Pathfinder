"""
4-Environment Standalone 4v4 Squad Benchmark:
Runs 800 random 4v4 squad battles PER ENVIRONMENT (The Neither, Civil Spire, Low Radiant, High Radiant)
Total battles: 3,200.
At 800 battles per zone with 17 classes, each class appears in ~375 squad battles per environment,
reducing the statistical margin of error to ~±2.5%.
"""

import sys
import random
import json
from pathlib import Path
from collections import defaultdict

SIM_DIR = Path("ClockworkPathfinder/testing/combat_sim")
sys.path.append(str(SIM_DIR))

from run_group_combat_sim import GroupCombatSim, roll_dice

tmpl_dir = SIM_DIR / "templates"

PLAYABLE_CLASSES = [
    "soldier",
    "noble_soldier",
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
    "merchant_neitherfire",
    "merchant_reflex",
    "merchant_fortitude",
    "merchant_will"
]

ENVIRONMENTS = [
    ("The Neither", "the_neither"),
    ("Civil Spire", "civil_spire"),
    ("Low Radiant", "low_radiant"),
    ("High Radiant", "high_radiant")
]

def run_environment_squad_suite(num_fights=800, level=5):
    all_results = {}
    dist = 50

    for env_label, env_code in ENVIRONMENTS:
        print(f"\n=========================================================================================")
        print(f"RUNNING {num_fights} SQUAD BATTLES IN [{env_label.upper()}] (LEVEL {level})")
        print(f"=========================================================================================")

        class_appearances = defaultdict(int)
        class_team_wins = defaultdict(int)
        class_deaths = defaultdict(int)

        for _ in range(num_fights):
            team_a_classes = random.sample(PLAYABLE_CLASSES, 4)
            team_b_classes = random.sample(PLAYABLE_CLASSES, 4)

            p1_files = [str(tmpl_dir / f"{c}_lv{level}.json") for c in team_a_classes]
            p2_files = [str(tmpl_dir / f"{c}_lv{level}.json") for c in team_b_classes]

            sim = GroupCombatSim(p1_files, p2_files, env=env_code, initial_distance=dist)
            p1 = [sim._load_combatant(f, True, 0) for f in sim.pc_files]
            p2 = [sim._load_combatant(f, False, dist) for f in sim.enemy_files]

            for c in team_a_classes: class_appearances[c] += 1
            for c in team_b_classes: class_appearances[c] += 1

            has_ch1 = any(p.archetype == "Chirurgeon" for p in p1)
            has_ch2 = any(p.archetype == "Chirurgeon" for p in p2)
            has_sc1 = any(p.archetype == "Scholar" for p in p1)
            has_sc2 = any(p.archetype == "Scholar" for p in p2)

            ch1_heals = 3
            ch2_heals = 3
            ch1_drone_ints = 6
            ch2_drone_ints = 6

            # Scholar radiant environmental buff
            if has_sc1:
                p1[0].temp_hp += (15 if env_code == "high_radiant" else (10 if env_code == "low_radiant" else 5))
            if has_sc2:
                p2[0].temp_hp += (15 if env_code == "high_radiant" else (10 if env_code == "low_radiant" else 5))

            sc1_hit = 2 if (has_sc1 and env_code == "high_radiant") else (1 if has_sc1 else 0)
            sc2_hit = 2 if (has_sc2 and env_code == "high_radiant") else (1 if has_sc2 else 0)

            total_rounds = 0
            while total_rounds < 30:
                total_rounds += 1
                alive1 = [p for p in p1 if p.current_hp > 0]
                alive2 = [p for p in p2 if p.current_hp > 0]
                if not alive1 or not alive2:
                    break

                p1_reaction_used = False
                p2_reaction_used = False

                # Team A
                for pc in alive1:
                    if pc.current_hp <= 0: continue
                    alive2_now = [e for e in p2 if e.current_hp > 0]
                    if not alive2_now: break
                    actions = 3

                    if pc.archetype == "Chirurgeon" and ch1_heals > 0:
                        wounded = [p for p in alive1 if p.current_hp < p.max_hp]
                        if wounded:
                            ch1_heals -= 1
                            t = min(wounded, key=lambda x: x.current_hp / x.max_hp)
                            t.current_hp = min(t.max_hp, t.current_hp + roll_dice("2d6") + 4)
                            actions -= 2

                    if pc.retainers_hp:
                        for _ in pc.retainers_hp:
                            if not alive2_now: break
                            t = alive2_now[0]
                            if random.randint(1, 20) + 7 >= t.ac:
                                t.current_hp -= (roll_dice("1d8") + 2)
                            alive2_now = [e for e in p2 if e.current_hp > 0]

                    if not alive2_now: break
                    target = min(alive2_now, key=lambda e: (abs(pc.pos - e.pos), e.current_hp))
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
                        map_pen = 0 if map_c == 0 else (-4 if "agile" in chosen_w.get("traits", []) else -5)
                        map_c += 1

                        tot_atk = random.randint(1, 20) + chosen_w.get("attack_bonus", 8) + sc1_hit + map_pen
                        melee_count = sum(1 for p in alive1 if abs(p.pos - target.pos) <= 5)
                        eff_ac = target.ac - 2 if melee_count >= 2 else target.ac

                        if tot_atk >= eff_ac:
                            is_crit = (tot_atk >= eff_ac + 10)
                            base = roll_dice(chosen_w.get("damage_dice", "1d6")) + chosen_w.get("flat_damage", 2)
                            dmg = (base * 2) if is_crit else base
                            if is_crit and "fatal_d10" in chosen_w.get("traits", []): dmg += roll_dice("1d10")
                            elif is_crit and "fatal_d12" in chosen_w.get("traits", []): dmg += roll_dice("1d12")

                            if has_ch2 and not p2_reaction_used and ch2_drone_ints > 0:
                                p2_reaction_used = True
                                ch2_drone_ints -= 1
                                dmg = max(0, dmg - 8)

                            if target.retainers_hp and dmg > 0:
                                intercept = min(target.retainers_hp[0], dmg // 2)
                                target.retainers_hp[0] -= intercept
                                dmg -= intercept
                                if target.retainers_hp[0] <= 0: target.retainers_hp.pop(0)

                            if target.temp_hp > 0 and dmg > 0:
                                rem = min(target.temp_hp, dmg)
                                target.temp_hp -= rem
                                dmg -= rem

                            target.current_hp -= dmg

                # Team B
                alive2 = [e for e in p2 if e.current_hp > 0]
                for pc in alive2:
                    if pc.current_hp <= 0: continue
                    alive1_now = [p for p in p1 if p.current_hp > 0]
                    if not alive1_now: break
                    actions = 3

                    if pc.archetype == "Chirurgeon" and ch2_heals > 0:
                        wounded = [p for p in alive2 if p.current_hp < p.max_hp]
                        if wounded:
                            ch2_heals -= 1
                            t = min(wounded, key=lambda x: x.current_hp / x.max_hp)
                            t.current_hp = min(t.max_hp, t.current_hp + roll_dice("2d6") + 4)
                            actions -= 2

                    if pc.retainers_hp:
                        for _ in pc.retainers_hp:
                            if not alive1_now: break
                            t = alive1_now[0]
                            if random.randint(1, 20) + 7 >= t.ac:
                                t.current_hp -= (roll_dice("1d8") + 2)
                            alive1_now = [p for p in p1 if p.current_hp > 0]

                    if not alive1_now: break
                    target = min(alive1_now, key=lambda p: (abs(pc.pos - p.pos), p.current_hp))
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
                        map_pen = 0 if map_c == 0 else (-4 if "agile" in chosen_w.get("traits", []) else -5)
                        map_c += 1

                        tot_atk = random.randint(1, 20) + chosen_w.get("attack_bonus", 8) + sc2_hit + map_pen
                        melee_count = sum(1 for p in alive2 if abs(p.pos - target.pos) <= 5)
                        eff_ac = target.ac - 2 if melee_count >= 2 else target.ac

                        if tot_atk >= eff_ac:
                            is_crit = (tot_atk >= eff_ac + 10)
                            base = roll_dice(chosen_w.get("damage_dice", "1d6")) + chosen_w.get("flat_damage", 2)
                            dmg = (base * 2) if is_crit else base
                            if is_crit and "fatal_d10" in chosen_w.get("traits", []): dmg += roll_dice("1d10")
                            elif is_crit and "fatal_d12" in chosen_w.get("traits", []): dmg += roll_dice("1d12")

                            if has_ch1 and not p1_reaction_used and ch1_drone_ints > 0:
                                p1_reaction_used = True
                                ch1_drone_ints -= 1
                                dmg = max(0, dmg - 8)

                            if target.retainers_hp and dmg > 0:
                                intercept = min(target.retainers_hp[0], dmg // 2)
                                target.retainers_hp[0] -= intercept
                                dmg -= intercept
                                if target.retainers_hp[0] <= 0: target.retainers_hp.pop(0)

                            if target.temp_hp > 0 and dmg > 0:
                                rem = min(target.temp_hp, dmg)
                                target.temp_hp -= rem
                                dmg -= rem

                            target.current_hp -= dmg

            alive1_end = [p for p in p1 if p.current_hp > 0]
            alive2_end = [p for p in p2 if p.current_hp > 0]

            if len(alive1_end) > 0 and len(alive2_end) == 0:
                for c in team_a_classes: class_team_wins[c] += 1
            elif len(alive2_end) > 0 and len(alive1_end) == 0:
                for c in team_b_classes: class_team_wins[c] += 1

            for idx, p in enumerate(p1):
                if p.current_hp <= 0: class_deaths[team_a_classes[idx]] += 1
            for idx, p in enumerate(p2):
                if p.current_hp <= 0: class_deaths[team_b_classes[idx]] += 1

        env_stats = []
        for c in PLAYABLE_CLASSES:
            app = class_appearances[c]
            w_pct = round((class_team_wins[c] / app) * 100, 1) if app > 0 else 0.0
            surv_pct = round((1.0 - (class_deaths[c] / app)) * 100, 1) if app > 0 else 0.0
            env_stats.append((c, app, w_pct, surv_pct))

        env_stats.sort(key=lambda x: x[2], reverse=True)
        all_results[env_code] = env_stats

        print(f"{'Class / Archetype':<24} | {'Appeared':<8} | {'Team Win %':<11} | {'Individual Survival %':<22}")
        print("-" * 75)
        for c, app, w_pct, surv_pct in env_stats:
            print(f"{c:<24} | {app:<8} | {w_pct:5.1f}%     | {surv_pct:5.1f}%")

    return all_results

if __name__ == "__main__":
    run_environment_squad_suite(num_fights=800, level=5)

