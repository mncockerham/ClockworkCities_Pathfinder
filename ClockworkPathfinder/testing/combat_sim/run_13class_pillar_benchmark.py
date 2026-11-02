"""
Comprehensive 13-Class 4-Environment Squad Benchmark & Pillar Impact Audit:
- Exactly 13 Playable Classes:
  1. Chirurgeon
  2. Clockwork Engineer
  3. Clockwork Rifleman
  4. Grey Marketeer
  5. Merchant
  6. Noble
  7. Officer
  8. Pugilist
  9. Rake
  10. Scholar
  11. Scout
  12. Soldier
  13. Survivor

- 800 Random 4v4 Squad Battles PER ENVIRONMENT (3,200 Total Battles) at Level 5.
- Reports each environment separately, ranking classes 1 to 13.
- Includes:
  1. Win Rate %
  2. Survival Rate %
  3. Social Tier Rating (1-10 scale based on canon Spire status/retainers/influence)
  4. Knowledge / Research Rating (1-10 scale based on Spire university/conduit/investigation canon)
  5. Overall Total Game Impact (Combat Avg + Social + Knowledge)
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
    "merchant_neitherfire" # Representative canon Merchant with Retainers & Ordnance
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

# Canon Setting Pillar Ratings (Scale 1 to 10)
# Social Tier: Status, legal privileges, retinues, economic credit, political standing
# Knowledge / Research: University access, blueprint theory, Neither alchemy, archaeology, diagnosis
PILLAR_SCORES = {
    "Noble":              {"social": 10.0, "knowledge": 5.0, "notes": "Status 5-6 Peerage, Retainers, High Court legal immunity"},
    "Officer":            {"social": 8.0,  "knowledge": 6.0, "notes": "Status 4-5 Commission, Military intelligence, Crown rank"},
    "Merchant":           {"social": 8.5,  "knowledge": 6.0, "notes": "Status 4-5 Merchant Guilds, Retainers, financial leverage"},
    "Rake":               {"social": 7.5,  "knowledge": 4.0, "notes": "Status 3-4 Gentry / Salon networks, dueling circles"},
    "Scholar":            {"social": 6.5,  "knowledge": 10.0, "notes": "Status 4 University Chair, Radiant dynamos, pure theory"},
    "Chirurgeon":         {"social": 5.0,  "knowledge": 8.5, "notes": "Status 2-4 Guild Clinic, Neither bio-chemistry, toxicology"},
    "Clockwork Engineer": {"social": 4.5,  "knowledge": 9.0, "notes": "Status 2-3 Craft Guild, Automaton architecture, dynamos"},
    "Grey Marketeer":     {"social": 6.0,  "knowledge": 6.5, "notes": "Underworld / Warrens syndicate, black market logistics"},
    "Soldier":            {"social": 4.0,  "knowledge": 3.0, "notes": "Status 1-2 Common Guard, tactical field drills"},
    "Clockwork Rifleman": {"social": 3.5,  "knowledge": 4.0, "notes": "Status 1-2 Marksman corps, ballistics maintenance"},
    "Pugilist":           {"social": 3.0,  "knowledge": 2.0, "notes": "Status 0-1 Warrens brawler, illegal fight rings"},
    "Scout":              {"social": 2.5,  "knowledge": 5.5, "notes": "Status 1 Outland guide, wilderness navigation, tracking"},
    "Survivor":           {"social": 1.5,  "knowledge": 3.5, "notes": "Status 0 Sump scavenger, raw instinct, scrap survival"}
}

ENVIRONMENTS = [
    ("The Neither", "the_neither"),
    ("Civil Spire", "civil_spire"),
    ("Low Radiant", "low_radiant"),
    ("High Radiant", "high_radiant")
]

def run_full_pillar_benchmark(num_fights=800, level=5):
    env_results = {}
    dist = 50

    for env_label, env_code in ENVIRONMENTS:
        class_appearances = defaultdict(int)
        class_team_wins = defaultdict(int)
        class_deaths = defaultdict(int)

        for _ in range(num_fights):
            team_a = random.sample(CORE_13_CLASSES, 4)
            team_b = random.sample(CORE_13_CLASSES, 4)

            p1_files = [str(tmpl_dir / f"{c}_lv{level}.json") for c in team_a]
            p2_files = [str(tmpl_dir / f"{c}_lv{level}.json") for c in team_b]

            sim = GroupCombatSim(p1_files, p2_files, env=env_code, initial_distance=dist)
            p1 = [sim._load_combatant(f, True, 0) for f in sim.pc_files]
            p2 = [sim._load_combatant(f, False, dist) for f in sim.enemy_files]

            for c in team_a: class_appearances[c] += 1
            for c in team_b: class_appearances[c] += 1

            has_ch1 = any(p.archetype == "Chirurgeon" for p in p1)
            has_ch2 = any(p.archetype == "Chirurgeon" for p in p2)
            has_sc1 = any(p.archetype == "Scholar" for p in p1)
            has_sc2 = any(p.archetype == "Scholar" for p in p2)

            ch1_heals = 3
            ch2_heals = 3
            ch1_drone_ints = 6
            ch2_drone_ints = 6

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
                if not alive1 or not alive2: break

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
                for c in team_a: class_team_wins[c] += 1
            elif len(alive2_end) > 0 and len(alive1_end) == 0:
                for c in team_b: class_team_wins[c] += 1

            for idx, p in enumerate(p1):
                if p.current_hp <= 0: class_deaths[team_a[idx]] += 1
            for idx, p in enumerate(p2):
                if p.current_hp <= 0: class_deaths[team_b[idx]] += 1

        env_stats = []
        for c in CORE_13_CLASSES:
            app = class_appearances[c]
            w_pct = round((class_team_wins[c] / app) * 100, 1) if app > 0 else 0.0
            surv_pct = round((1.0 - (class_deaths[c] / app)) * 100, 1) if app > 0 else 0.0
            disp = DISPLAY_NAMES[c]
            soc = PILLAR_SCORES[disp]["social"]
            knw = PILLAR_SCORES[disp]["knowledge"]
            # Combat score on 1-10 scale = win_pct / 10
            com_score = round(w_pct / 10.0, 1)
            # Total Impact = average of Combat, Social, Knowledge
            total_impact = round((com_score + soc + knw) / 3.0, 1)
            env_stats.append({
                "class_code": c,
                "name": disp,
                "appearances": app,
                "win_pct": w_pct,
                "survival_pct": surv_pct,
                "combat_score": com_score,
                "social_score": soc,
                "knowledge_score": knw,
                "total_impact": total_impact
            })

        # Rank 1 to 13 by Win Rate
        env_stats.sort(key=lambda x: x["win_pct"], reverse=True)
        for rank, item in enumerate(env_stats, 1):
            item["rank"] = rank

        env_results[env_code] = env_stats

    # Print clean formatted markdown reports for each environment
    for env_label, env_code in ENVIRONMENTS:
        stats = env_results[env_code]
        print(f"\n### Environment: {env_label} (800 Fights | Level 5 Squad Combat)")
        print(f"| Rank | Class | Win Rate % | Survival % | Combat (1-10) | Social Tier (1-10) | Knowledge / Research (1-10) | Overall Impact |")
        print(f"|:---:|:---|:---:|:---:|:---:|:---:|:---:|:---:|")
        for item in stats:
            print(f"| **#{item['rank']}** | **{item['name']}** | {item['win_pct']:5.1f}% | {item['survival_pct']:5.1f}% | {item['combat_score']} | {item['social_score']} | {item['knowledge_score']} | **{item['total_impact']}** |")

    # Aggregate cross-environment summary table
    print("\n" + "=" * 110)
    print("### CROSS-ENVIRONMENT SUMMARY: OVERALL GAME IMPACT ACROSS ALL 4 ENVIRONMENTS (3,200 BATTLES)")
    print("=" * 110)
    print(f"| Class | Neither Win% | Civil Spire Win% | Low Rad Win% | High Rad Win% | Avg Combat (1-10) | Social (1-10) | Knowledge (1-10) | **Final Game Impact** |")
    print(f"|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|")

    final_rankings = []
    for c in CORE_13_CLASSES:
        disp = DISPLAY_NAMES[c]
        w_neither = next(x["win_pct"] for x in env_results["the_neither"] if x["name"] == disp)
        w_civil   = next(x["win_pct"] for x in env_results["civil_spire"] if x["name"] == disp)
        w_low     = next(x["win_pct"] for x in env_results["low_radiant"] if x["name"] == disp)
        w_high    = next(x["win_pct"] for x in env_results["high_radiant"] if x["name"] == disp)

        avg_combat = round((w_neither + w_civil + w_low + w_high) / 40.0, 1)
        soc = PILLAR_SCORES[disp]["social"]
        knw = PILLAR_SCORES[disp]["knowledge"]
        final_impact = round((avg_combat + soc + knw) / 3.0, 1)

        final_rankings.append({
            "name": disp,
            "w_neither": w_neither,
            "w_civil": w_civil,
            "w_low": w_low,
            "w_high": w_high,
            "avg_combat": avg_combat,
            "social": soc,
            "knowledge": knw,
            "final_impact": final_impact
        })

    final_rankings.sort(key=lambda x: x["final_impact"], reverse=True)
    for r in final_rankings:
        print(f"| **{r['name']}** | {r['w_neither']:5.1f}% | {r['w_civil']:5.1f}% | {r['w_low']:5.1f}% | {r['w_high']:5.1f}% | {r['avg_combat']} | {r['social']} | {r['knowledge']} | **{r['final_impact']}** |")

if __name__ == "__main__":
    run_full_pillar_benchmark(num_fights=800, level=5)
