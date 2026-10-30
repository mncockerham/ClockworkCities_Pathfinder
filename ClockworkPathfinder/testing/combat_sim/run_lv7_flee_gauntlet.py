import sys
from pathlib import Path

# Add simulator to path
sys.path.append(str(Path(__file__).parent))
from combat_sim import Simulator

CLASSES = [
    "artisan", "blackmarketeer", "chirurgeon", "clockworkengineer",
    "clockworkrifleman", "dandy", "inspector", "madbomber", "merchant",
    "noble", "officer", "pugilist", "scholar", "scout", "skycaptain",
    "soldier", "survivor"
]

MONSTERS_LV7 = [
    ("creature_bear_flee_lv7.json", "Bear Lv7 (Flee)"),
    ("creature_wolf_flee_lv7.json", "Wolf Lv7 (Flee)"),
    ("creature_scorpion_flee_lv7.json", "Scorpion Lv7 (Flee)")
]

ENVIRONMENTS = ["Civil", "High", "Low", "Neither"]

def run_lv7_flee_gauntlet(iters=1000):
    tmpl_dir = Path(__file__).parent / "templates"
    creat_dir = Path(__file__).parent / "creatures"

    total_fights = len(CLASSES) * len(MONSTERS_LV7) * len(ENVIRONMENTS) * iters

    print("=" * 80)
    print("NON-BERSERK (50% FLEE) GAUNTLET: ALL 17 LV5 PCS VS LEVEL 7 APEX BEASTS")
    print(f"Total Fights: {total_fights:,} ({iters:,} per environment/matchup)")
    print("Outcome Definition: Win = Level 7 Beast reduced to 50% HP (forced to flee)")
    print("=" * 80)

    matrix = {c: {m_label: {"wins": 0, "losses": 0, "total": 0} for _, m_label in MONSTERS_LV7} for c in CLASSES}
    class_totals = {c: {"wins": 0, "losses": 0, "total": 0} for c in CLASSES}

    for c in CLASSES:
        c_file = tmpl_dir / f"{c}_lv5.json"
        dist = 60 if c in ["scout", "clockworkrifleman"] else 40

        for m_file_name, m_label in MONSTERS_LV7:
            m_file = creat_dir / m_file_name
            sim = Simulator(str(c_file), str(m_file), initial_distance=dist)
            suite = sim.run_environment_suite(iterations=iters)

            for env in ENVIRONMENTS:
                r = suite["results"][env]
                w_pct = r["Clear Win"] + r["Mod Win"] + r["Close Win"]
                l_pct = r["Minor Def"] + r["Major Def"] + r["Clear Def"]

                w_count = round((w_pct / 100) * iters)
                l_count = round((l_pct / 100) * iters)

                matrix[c][m_label]["wins"] += w_count
                matrix[c][m_label]["losses"] += l_count
                matrix[c][m_label]["total"] += iters

                class_totals[c]["wins"] += w_count
                class_totals[c]["losses"] += l_count
                class_totals[c]["total"] += iters

    # Print Formatted Table
    m1_name = MONSTERS_LV7[0][1]
    m2_name = MONSTERS_LV7[1][1]
    m3_name = MONSTERS_LV7[2][1]

    print(f"{'Class Archetype':<20} | {m1_name:^17} | {m2_name:^17} | {m3_name:^19} | {'TOTAL (Win / Loss)':^20}")
    print("-" * 20 + "-+-" + "-" * 17 + "-+-" + "-" * 17 + "-+-" + "-" * 19 + "-+-" + "-" * 20)

    sorted_classes = sorted(CLASSES, key=lambda c: class_totals[c]["wins"] / class_totals[c]["total"], reverse=True)

    for c in sorted_classes:
        name = c.capitalize()
        if c == "clockworkengineer": name = "Engineer"
        if c == "clockworkrifleman": name = "Rifleman"
        if c == "blackmarketeer": name = "BlackMarketeer"
        if c == "madbomber": name = "MadBomber"
        if c == "skycaptain": name = "SkyCaptain"

        b_w = round((matrix[c][m1_name]["wins"] / matrix[c][m1_name]["total"]) * 100, 1)
        b_l = round((matrix[c][m1_name]["losses"] / matrix[c][m1_name]["total"]) * 100, 1)
        b_str = f"{b_w:>4.1f}% / {b_l:>4.1f}%"

        w_w = round((matrix[c][m2_name]["wins"] / matrix[c][m2_name]["total"]) * 100, 1)
        w_l = round((matrix[c][m2_name]["losses"] / matrix[c][m2_name]["total"]) * 100, 1)
        w_str = f"{w_w:>4.1f}% / {w_l:>4.1f}%"

        s_w = round((matrix[c][m3_name]["wins"] / matrix[c][m3_name]["total"]) * 100, 1)
        s_l = round((matrix[c][m3_name]["losses"] / matrix[c][m3_name]["total"]) * 100, 1)
        s_str = f"{s_w:>4.1f}% / {s_l:>4.1f}%"

        tot_w = round((class_totals[c]["wins"] / class_totals[c]["total"]) * 100, 1)
        tot_l = round((class_totals[c]["losses"] / class_totals[c]["total"]) * 100, 1)
        tot_str = f"{tot_w:>5.1f}% / {tot_l:>5.1f}%"

        print(f"{name:<20} | {b_str:^17} | {w_str:^17} | {s_str:^19} | {tot_str:^20}")

    print("=" * 80)
    grand_wins = sum(class_totals[c]["wins"] for c in CLASSES)
    grand_losses = sum(class_totals[c]["losses"] for c in CLASSES)
    grand_total = sum(class_totals[c]["total"] for c in CLASSES)
    pct_win = (grand_wins / grand_total) * 100
    pct_loss = (grand_losses / grand_total) * 100
    print(f"OVERALL COMBINED OUTCOME ACROSS ALL {total_fights:,} FIGHTS:")
    print(f"  - Player Successfully Drove Off Lv7 Beast (Win): {grand_wins:,} fights ({pct_win:.1f}%)")
    print(f"  - Player Slain by Lv7 Beast (Loss):              {grand_losses:,} fights ({pct_loss:.1f}%)")
    print("=" * 80 + "\n")

if __name__ == "__main__":
    run_lv7_flee_gauntlet(iters=1000)

