"""
The Grind: Group Maintenance Combat Endurance Simulation (Test 3)
Parameters:
- 4 PC Party at Level 5 (randomly drafted from 13 core classes).
- Faces sequential waves of 4 Level 4 NPCs (randomly drafted from 13 core classes at Lv 4).
- Up to 20 consecutive fights per trial, running until all 4 original PCs are dead.
- Tested under Healing % between fights:
  * Test 3.A: 0% Healing between fights (Pure attrition / raw meatgrinder).
  * (Can also test 25%, 50%, or Chirurgeon convalescence / Treat Wounds recovery).
- Tracks for EACH PC in the party:
  * Class / Archetype
  * Fight Number in which they died (Survival Depth: 1 to 20+)
  * Total damage taken
  * Total rounds fought
- Tracks for the SQUAD:
  * How many consecutive fights won before total party wipe (TPW)
  * Average rounds per fight
  * Total rounds survived across the gauntlet
  * First PC to die vs Last PC standing
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

def simulate_single_wave(pcs, enemy_classes, env="the_neither", dist=50):
    # Load 4 fresh enemies at Lv 4
    sim = GroupCombatSim([], [str(tmpl_dir / f"{c}_lv4.json") for c in enemy_classes], env=env, initial_distance=dist)
    enemies = [sim._load_combatant(f, False, dist) for f in sim.enemy_files]

    # Reposition living PCs at pos 0, restore temp HP/AP
    for p in pcs:
        p.pos = 0
        p.temp_hp = 0

    has_ch_pc = any(p.archetype == "Chirurgeon" and p.current_hp > 0 for p in pcs)
    has_ch_en = any(e.archetype == "Chirurgeon" and e.current_hp > 0 for e in enemies)
    has_sc_pc = any(p.archetype == "Scholar" and p.current_hp > 0 for p in pcs)
    has_sc_en = any(e.archetype == "Scholar" and e.current_hp > 0 for e in enemies)

    # In-combat charges
    ch_pc_heals = 3 if has_ch_pc else 0
    ch_en_heals = 3 if has_ch_en else 0
    ch_pc_drone_ints = 6 if has_ch_pc else 0
    ch_en_drone_ints = 6 if has_ch_en else 0

    # Scholar barrier
    alive_pcs = [p for p in pcs if p.current_hp > 0]
    if has_sc_pc and alive_pcs:
        alive_pcs[0].temp_hp += (15 if env == "high_radiant" else 8)
    if has_sc_en and enemies:
        enemies[0].temp_hp += (15 if env == "high_radiant" else 8)

    sc_pc_hit = 2 if (has_sc_pc and env == "high_radiant") else (1 if has_sc_pc else 0)
    sc_en_hit = 2 if (has_sc_en and env == "high_radiant") else (1 if has_sc_en else 0)

    # Engineer Combat Backpack at start of fight
    for p in pcs:
        if p.archetype == "ClockworkEngineer" and p.current_hp > 0:
            p.temp_hp += 8
    for e in enemies:
        if e.archetype == "ClockworkEngineer" and e.current_hp > 0:
            e.temp_hp += 8

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

            # Engineer Backpack autonomous shot
            if pc.archetype == "ClockworkEngineer":
                t = min(alive_e_now, key=lambda e: (abs(pc.pos - e.pos), e.current_hp))
                if abs(pc.pos - t.pos) <= 60:
                    if random.randint(1, 20) + 12 >= t.ac:
                        t.current_hp -= (roll_dice("2d8") + 3)

            # Chirurgeon heal
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
                    if random.randint(1, 20) + 10 >= t.ac:
                        t.current_hp -= (roll_dice("1d8") + 3)

            if en.archetype == "Chirurgeon" and ch_en_heals > 0:
                w = [e for e in alive_e if e.current_hp < e.max_hp]
                if w:
                    ch_en_heals -= 1
                    t = min(w, key=lambda x: x.current_hp / x.max_hp)
                    t.current_hp = min(t.max_hp, t.current_hp + roll_dice("2d6") + 4)
                    actions -= 2

            if en.retainers_hp:
                for _ in en.retainers_hp:
                    if not alive_p_now: break
                    t = alive_p_now[0]
                    if random.randint(1, 20) + 6 >= t.ac:
                        t.current_hp -= (roll_dice("1d8") + 2)
                    alive_p_now = [p for p in pcs if p.current_hp > 0]

            if not alive_p_now: break
            target = min(alive_p_now, key=lambda p: (abs(en.pos - p.pos), p.current_hp))
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
                tot_atk = random.randint(1, 20) + chosen_w.get("attack_bonus", 8) + sc_en_hit + pen
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

def run_grind_gauntlet(num_runs=300, max_waves=20, heal_pct=0.0, env="the_neither"):
    print("=" * 105)
    print(f"THE GRIND: COMBAT ENDURANCE GAUNTLET (4 PCs Lv 5 vs Waves of 4 NPCs Lv 4)")
    print(f"Environment: {env.upper()} | Between-Fight Healing: {heal_pct*100:.0f}% | Trials: {num_runs} Squads | Max Waves: {max_waves}")
    print("=" * 105)

    # Metrics per class
    class_runs = defaultdict(int)
    class_death_fight = defaultdict(list)
    class_rounds_fought = defaultdict(list)
    class_survived_wave1 = defaultdict(int)

    squad_waves_won = []
    squad_total_rounds = []

    for trial in range(num_runs):
        # 1. Draft 4 random unique Level 5 PCs
        pc_classes = random.sample(CORE_13_CLASSES, 4)
        sim = GroupCombatSim([str(tmpl_dir / f"{c}_lv5.json") for c in pc_classes], [], env=env)
        pcs = [sim._load_combatant(f, True, 0) for f in sim.pc_files]

        for c in pc_classes:
            class_runs[c] += 1

        # Death tracker for this squad: index -> fight number of death (or max_waves+1 if survived)
        death_fight_num = {idx: None for idx in range(4)}
        rounds_participated = {idx: 0 for idx in range(4)}

        waves_won = 0
        total_squad_rounds = 0

        for wave in range(1, max_waves + 1):
            # Check living PCs
            living_indices = [idx for idx, p in enumerate(pcs) if p.current_hp > 0]
            if not living_indices:
                break

            # Draft 4 random unique Level 4 enemies
            enemy_classes = random.sample(CORE_13_CLASSES, 4)

            # Fight the wave
            pc_won, fight_rounds = simulate_single_wave(pcs, enemy_classes, env=env)
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

                # Apply Between-Fight Healing (if any)
                if heal_pct > 0.0:
                    for p in pcs:
                        if p.current_hp > 0:
                            missing = p.max_hp - p.current_hp
                            p.current_hp = min(p.max_hp, p.current_hp + int(missing * heal_pct))
            else:
                # Party wiped or defeated in this wave
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

    # Aggregate & Report
    avg_squad_waves = sum(squad_waves_won) / len(squad_waves_won)
    avg_squad_rounds = sum(squad_total_rounds) / len(squad_total_rounds)

    print(f"\nSQUAD PERFORMANCE ACROSS {num_runs} EXPEDITIONS:")
    print(f"  • Average Consecutive Waves Cleared: {avg_squad_waves:.2f} fights (without healing)")
    print(f"  • Average Total Rounds Survived:      {avg_squad_rounds:.1f} rounds before TPW")
    print(f"  • Maximum Waves Cleared by Best Squad: {max(squad_waves_won)} consecutive fights")
    print("-" * 105)

    print(f"{'Class / Archetype':<24} | {'Drafted':<8} | {'Avg Death Fight #':<18} | {'Survive Wave 1 %':<18} | {'Avg Rounds Fought':<18} | {'Attrition Role'}")
    print("-" * 105)

    rankings = []
    for c in CORE_13_CLASSES:
        runs = class_runs[c]
        if runs == 0: continue
        avg_df = sum(class_death_fight[c]) / runs
        surv_w1 = (class_survived_wave1[c] / runs) * 100
        avg_rf = sum(class_rounds_fought[c]) / runs
        disp = DISPLAY_NAMES[c]
        rankings.append((disp, runs, avg_df, surv_w1, avg_rf))

    # Sort by Avg Death Fight Number descending
    rankings.sort(key=lambda x: x[2], reverse=True)

    for disp, runs, avg_df, surv_w1, avg_rf in rankings:
        if avg_df >= 2.5:
            role = "Ironclad Anchor (Survives multiple fights)"
        elif avg_df >= 2.0:
            role = "Durable Frontline / Skirmisher"
        elif avg_df >= 1.6:
            role = "Midline Asset (Moderate attrition)"
        else:
            role = "Fragile / High Attrition Priority"
        print(f"{disp:<24} | {runs:<8} | Fight #{avg_df:4.2f}          | {surv_w1:5.1f}%             | {avg_rf:4.1f} rounds        | {role}")

    print("=" * 105)
    return rankings

if __name__ == "__main__":
    run_grind_gauntlet(num_runs=400, max_waves=20, heal_pct=0.0, env="the_neither")
