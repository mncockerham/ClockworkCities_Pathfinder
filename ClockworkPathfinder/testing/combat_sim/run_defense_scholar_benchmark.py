"""
Benchmark: Scholar on Pure Defense Party Share vs Offensive Scholar vs No Scholar
Rule Tested:
- Scholar on Pure Defense:
  * Personal: Only 1 activation of personal AC defense (+2 AC to self)
  * Party Share Safe: Broadcasts defensive trajectory warnings to all allies (+1 AC to all party members in Neither; +2 AC in High Radiant)
  * Instead of offensive buffs (sc_pc_hit = 0), party receives defensive AC boost and predictive temp HP buffers (Actuarial Risk Assessment).
Compare 300 trials across:
1. No Scholar (Control)
2. Scholar (Offense focus: +1/+2 Attack bonus & Temp HP)
3. Scholar (Pure Defense focus: +1/+2 AC to all allies + personal AC + Temp HP)
"""

import sys
import random
from pathlib import Path

SIM_DIR = Path("ClockworkPathfinder/testing/combat_sim")
sys.path.append(str(SIM_DIR))

import run_weighted_targeting_grind as rwg
from run_group_combat_sim import roll_dice

tmpl_dir = SIM_DIR / "templates"
OTHER_CLASSES = [c for c in rwg.CORE_13_CLASSES if c not in ["scholar"]]

def simulate_wave_defense_scholar(pcs, enemy_classes, enemy_level=4, env="the_neither", dist=50, scholar_mode="defense"):
    sim = rwg.GroupCombatSim([], [str(tmpl_dir / f"{c}_lv{enemy_level}.json") for c in enemy_classes], env=env, initial_distance=dist)
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
    
    # Scholar Configuration
    sc_pc_hit = 0
    sc_pc_party_ac = 0
    sc_pc_self_ac = 0
    
    if has_sc_pc:
        if scholar_mode == "offense":
            sc_pc_hit = 2 if env == "high_radiant" else 1
            if alive_pcs:
                alive_pcs[0].temp_hp += (15 if env == "high_radiant" else 8)
        elif scholar_mode == "defense":
            # Pure Defense: Party share safe, 1 personal AC activation
            # Actuarial Risk Assessment / Defensive trajectory: +1 circumstance AC to all allies (+2 in High Radiant)
            sc_pc_party_ac = 2 if env == "high_radiant" else 1
            sc_pc_self_ac = 2  # 1 activation of personal AC defense
            # Distribute defensive buffer across frontliners
            for p in alive_pcs:
                p.temp_hp += (6 if env == "high_radiant" else 4)

    # Enemy Scholar (standard)
    sc_en_hit = 2 if (has_sc_en and env == "high_radiant") else (1 if has_sc_en else 0)

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

            if pc.archetype == "ClockworkEngineer":
                t = rwg.pick_weighted_target(alive_e_now)
                if abs(pc.pos - t.pos) <= 60:
                    if random.randint(1, 20) + 12 >= t.ac:
                        t.current_hp -= (roll_dice("2d8") + 3)

            if pc.archetype == "Chirurgeon" and ch_pc_heals > 0:
                wounded = [p for p in alive_p if p.current_hp < p.max_hp]
                if wounded:
                    ch_pc_heals -= 1
                    t = min(wounded, key=lambda x: x.current_hp / x.max_hp)
                    t.current_hp = min(t.max_hp, t.current_hp + roll_dice("2d6") + 4)
                    actions -= 2

            if pc.retainers_hp:
                for _ in pc.retainers_hp:
                    if not alive_e_now: break
                    t = alive_e_now[0]
                    if random.randint(1, 20) + 7 >= t.ac:
                        t.current_hp -= (roll_dice("1d8") + 2)
                    alive_e_now = [e for e in enemies if e.current_hp > 0]

            if not alive_e_now: break
            target = rwg.pick_weighted_target(alive_e_now)
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
                t = rwg.pick_weighted_target(alive_p_now)
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
            target = rwg.pick_weighted_target(alive_p_now)
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
                
                # Effective PC AC with Scholar Defense Mode:
                pc_ac = target.ac + sc_pc_party_ac
                if target.archetype == "Scholar":
                    pc_ac += sc_pc_self_ac
                eff_ac = pc_ac - 2 if sum(1 for e in alive_e if abs(e.pos - target.pos) <= 5) >= 2 else pc_ac

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

def run_experiment(mode, env="the_neither", enemy_level=3, heal_pct=0.5, num_trials=300):
    total_waves = []
    total_rounds = []
    
    for _ in range(num_trials):
        if mode == "no_scholar":
            pc_classes = random.sample(OTHER_CLASSES, 4)
            scholar_mode = "none"
        elif mode == "scholar_offense":
            pc_classes = ["scholar"] + random.sample(OTHER_CLASSES, 3)
            scholar_mode = "offense"
        elif mode == "scholar_defense":
            pc_classes = ["scholar"] + random.sample(OTHER_CLASSES, 3)
            scholar_mode = "defense"
        else:
            raise ValueError()

        random.shuffle(pc_classes)
        sim = rwg.GroupCombatSim([str(tmpl_dir / f"{c}_lv5.json") for c in pc_classes], [], env=env)
        pcs = [sim._load_combatant(f, True, 0) for f in sim.pc_files]
        
        waves_won = 0
        cum_rounds = 0
        
        while waves_won < 20:
            if not any(p.current_hp > 0 for p in pcs): break
            enemy_classes = random.choices(rwg.CORE_13_CLASSES, k=4)
            vic, r = simulate_wave_defense_scholar(pcs, enemy_classes, enemy_level=enemy_level, env=env, dist=50, scholar_mode=scholar_mode)
            cum_rounds += r
            if vic:
                waves_won += 1
                if heal_pct > 0:
                    for p in pcs:
                        if p.current_hp > 0:
                            p.current_hp = min(p.max_hp, int(p.current_hp + (p.max_hp * heal_pct)))
            else:
                break
        total_waves.append(waves_won)
        total_rounds.append(cum_rounds)
        
    return sum(total_waves)/len(total_waves), sum(total_rounds)/len(total_rounds)

def main():
    print("=" * 105)
    print("SCHOLAR PURE DEFENSE vs OFFENSIVE SCHOLAR vs NO SCHOLAR (300 Trials per configuration)")
    print("Pure Defense: +1/+2 AC to whole party + 1 personal AC activation (+2) + temp HP buffer")
    print("=" * 105)
    
    cases = [
        ("THE_NEITHER", 3, 0.5),
        ("THE_NEITHER", 4, 0.5),
        ("HIGH_RADIANT", 3, 0.5),
        ("HIGH_RADIANT", 4, 0.5),
    ]
    
    for zone, lvl, heal in cases:
        print(f"\n>>> ZONE: {zone} | ENEMIES: Level {lvl} | HEAL: {int(heal*100)}% <<<")
        print(f"{'Scholar Strategy':<25} | {'Avg Waves Cleared':<20} | {'Total Rounds Fought':<20} | {'Rounds / Fight':<15}")
        print("-" * 85)
        for mode in ["no_scholar", "scholar_offense", "scholar_defense"]:
            w, r = run_experiment(mode, env=zone.lower(), enemy_level=lvl, heal_pct=heal, num_trials=300)
            label = {
                "no_scholar": "No Scholar (Control)",
                "scholar_offense": "Scholar: Offensive Focus",
                "scholar_defense": "Scholar: Pure Defense Focus"
            }[mode]
            r_per_f = r / (w + 1)
            print(f"{label:<25} | {w:<20.2f} | {r:<20.1f} | {r_per_f:<15.2f}")

if __name__ == "__main__":
    main()

