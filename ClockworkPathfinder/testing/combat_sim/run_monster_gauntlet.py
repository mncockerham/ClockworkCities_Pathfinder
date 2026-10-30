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

MONSTERS = [
    ("creature_bear_lv5.json", "Bear (Brute)"),
    ("creature_wolf_lv5.json", "Wolf (Stalker)"),
    ("creature_scorpion_lv5.json", "Scorpion (Venom)")
]

ENVIRONMENTS = ["Civil", "High", "Low", "Neither"]

def run_monster_gauntlet(level=5, iters=1000):
    tmpl_dir = Path(__file__).parent / "templates"
    creat_dir = Path(__file__).parent / "creatures"

    # Total fights: 17 classes * 3 monsters * 4 environments * iters
    total_fights = len(CLASSES) * len(MONSTERS) * len(ENVIRONMENTS) * iters

    print("=" * 80)
    print(f"MONSTER GAUNTLET: ALL 17 CLASSES (LV{level}) VS 3 1v1 MONSTERS")
    print(f"Monsters: Bear (Brute), Wolf (Stalker), Scorpion (Venomous)")
    print(f"Total Fights: {total_fights:,} ({iters:,} per environment/matchup)")
    print("Metrics: Pure PC Win % (Alive at end) / PC Loss % across all environments")
    print("=" * 80)

    # Store results per class per monster:
    # data[class][monster] = {"wins": int, "losses": int, "total": int}
    matrix = {c: {m_label: {"wins": 0, "losses": 0, "total": 0} for _, m_label in MONSTERS} for c in CLASSES}
    class_totals = {c: {"wins": 0, "losses": 0, "total": 0} for c in CLASSES}

    for c in CLASSES:
        c_file = tmpl_dir / f"{c}_lv{level}.json"
        dist = 60 if c in ["scout", "clockworkrifleman"] else 40

        for m_file_name, m_label in MONSTERS:
            m_file = creat_dir / m_file_name
            sim = Simulator(str(c_file), str(m_file), initial_distance=dist)
            suite = sim.run_environment_suite(iterations=iters)

            for env in ENVIRONMENTS:
                r = suite["results"][env]
                # Win = PC alive at end (Clear Win + Mod Win + Close Win)
                w_pct = r["Clear Win"] + r["Mod Win"] + r["Close Win"]
                # Loss = Monster alive at end (Minor Def + Major Def + Clear Def)
                l_pct = r["Minor Def"] + r["Major Def"] + r["Clear Def"]
                # In case of draws / too close, remainder is accounted for
                w_count = round((w_pct / 100) * iters)
                l_count = round((l_pct / 100) * iters)

                matrix[c][m_label]["wins"] += w_count
                matrix[c][m_label]["losses"] += l_count
                matrix[c][m_label]["total"] += iters

                class_totals[c]["wins"] += w_count
                class_totals[c]["losses"] += l_count
                class_totals[c]["total"] += iters

    # Print Clean Formatted Table
    print(f"{'Class Archetype':<20} | {'Bear (Win/Loss)':^17} | {'Wolf (Win/Loss)':^17} | {'Scorpion (Win/Loss)':^19} | {'TOTAL (Win / Loss)':^20}")
    print("-" * 20 + "-+-" + "-" * 17 + "-+-" + "-" * 17 + "-+-" + "-" * 19 + "-+-" + "-" * 20)

    # Sort classes by overall win %
    sorted_classes = sorted(CLASSES, key=lambda c: class_totals[c]["wins"] / class_totals[c]["total"], reverse=True)

    for c in sorted_classes:
        name = c.capitalize()
        if c == "clockworkengineer": name = "Engineer"
        if c == "clockworkrifleman": name = "Rifleman"
        if c == "blackmarketeer": name = "BlackMarketeer"
        if c == "madbomber": name = "MadBomber"
        if c == "skycaptain": name = "SkyCaptain"

        # Bear
        b_w = round((matrix[c]["Bear (Brute)"]["wins"] / matrix[c]["Bear (Brute)"]["total"]) * 100, 1)
        b_l = round((matrix[c]["Bear (Brute)"]["losses"] / matrix[c]["Bear (Brute)"]["total"]) * 100, 1)
        b_str = f"{b_w:>4.1f}% / {b_l:>4.1f}%"

        # Wolf
        w_w = round((matrix[c]["Wolf (Stalker)"]["wins"] / matrix[c]["Wolf (Stalker)"]["total"]) * 100, 1)
        w_l = round((matrix[c]["Wolf (Stalker)"]["losses"] / matrix[c]["Wolf (Stalker)"]["total"]) * 100, 1)
        w_str = f"{w_w:>4.1f}% / {w_l:>4.1f}%"

        # Scorpion
        s_w = round((matrix[c]["Scorpion (Venom)"]["wins"] / matrix[c]["Scorpion (Venom)"]["total"]) * 100, 1)
        s_l = round((matrix[c]["Scorpion (Venom)"]["losses"] / matrix[c]["Scorpion (Venom)"]["total"]) * 100, 1)
        s_str = f"{s_w:>4.1f}% / {s_l:>4.1f}%"

        # Overall Total
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
    print(f"OVERALL COMBINED OUTCOME ACROSS ALL 204,000 FIGHTS:")
    print(f"  - Player Won (Alive): {grand_wins:,} fights ({pct_win:.1f}%)")
    print(f"  - Player Lost (Died):  {grand_losses:,} fights ({pct_loss:.1f}%)")
    print("=" * 80)

if __name__ == "__main__":
    run_monster_gauntlet(level=5, iters=1000)

