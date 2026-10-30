import sys
from pathlib import Path

# Add simulator to path
sys.path.append(str(Path(__file__).parent))
from combat_sim import Simulator

CLASSES = [
    ("soldier", "Soldier"),
    ("pugilist", "Pugilist"),
    ("officer", "Officer"),
    ("blackmarketeer", "BlackMarketeer"),
    ("noble", "Noble"),
    ("scout", "Scout"),
    ("merchant", "Merchant"),
    ("skycaptain", "SkyCaptain"),
    ("dandy", "Dandy"),
    ("clockworkrifleman", "Rifleman"),
    ("inspector", "Inspector"),
    ("survivor", "Survivor"),
    ("clockworkengineer", "Engineer"),
    ("madbomber", "MadBomber"),
    ("artisan", "Artisan"),
    ("chirurgeon", "Chirurgeon"),
    ("scholar", "Scholar")
]

BEASTS = [
    ("bear", "Bear"),
    ("wolf", "Wolf"),
    ("scorpion", "Scorpion")
]

ENVIRONMENTS = ["Civil", "High", "Low", "Neither"]

def run_reduction_audit(pc_level, beast_level, iters=500):
    tmpl_dir = Path(__file__).parent / "templates"
    creat_dir = Path(__file__).parent / "creatures"

    print("=" * 105)
    print(f"REDUCTION AUDIT: LEVEL {pc_level} PCS VS LEVEL {beast_level} BEASTS (-{pc_level - beast_level} LEVELS / ~{(beast_level/pc_level)*100:.0f}% RATIO)")
    print(f"Total Matchups: {len(CLASSES)} Classes x {len(BEASTS)} Beasts x {len(ENVIRONMENTS)} Envs x {iters} Iters = {len(CLASSES)*len(BEASTS)*len(ENVIRONMENTS)*iters:,} Fights per Mode")
    print("=" * 105)

    for mode in ["Berserk", "Flee"]:
        print(f"\n--- MODE: {mode.upper()} (Beasts have {'100% HP' if mode == 'Berserk' else '50% HP Flee Threshold'}) ---")
        print(f"{'Class Archetype':<18} | {'Bear Lv' + str(beast_level):<18} | {'Wolf Lv' + str(beast_level):<18} | {'Scorpion Lv' + str(beast_level):<18} | {'TOTAL Win / Loss':<20}")
        print("-" * 105)

        total_all_wins = 0
        total_all_losses = 0
        total_all_fights = 0

        for c_key, c_label in CLASSES:
            c_file = tmpl_dir / f"{c_key}_lv{pc_level}.json"
            dist = 60 if c_key in ["scout", "clockworkrifleman"] else 40
            
            c_wins_total = 0
            c_losses_total = 0
            c_fights_total = 0
            beast_col_strs = []

            for b_key, b_label in BEASTS:
                suffix = f"_flee_lv{beast_level}.json" if mode == "Flee" else f"_lv{beast_level}.json"
                b_file = creat_dir / f"creature_{b_key}{suffix}"
                sim = Simulator(str(c_file), str(b_file), initial_distance=dist)
                suite = sim.run_environment_suite(iterations=iters)

                b_w = 0
                b_l = 0
                b_tot = 0

                for env in ENVIRONMENTS:
                    r = suite["results"][env]
                    w_pct = r["Clear Win"] + r["Mod Win"] + r["Close Win"]
                    l_pct = r["Minor Def"] + r["Major Def"] + r["Clear Def"]

                    w_count = round((w_pct / 100) * iters)
                    l_count = round((l_pct / 100) * iters)

                    b_w += w_count
                    b_l += l_count
                    b_tot += iters

                w_rate = (b_w / b_tot) * 100
                l_rate = (b_l / b_tot) * 100
                beast_col_strs.append(f"{w_rate:5.1f}% / {l_rate:4.1f}%")

                c_wins_total += b_w
                c_losses_total += b_l
                c_fights_total += b_tot

            class_w_rate = (c_wins_total / c_fights_total) * 100
            class_l_rate = (c_losses_total / c_fights_total) * 100
            total_all_wins += c_wins_total
            total_all_losses += c_losses_total
            total_all_fights += c_fights_total

            print(f"{c_label:<18} | {beast_col_strs[0]:<18} | {beast_col_strs[1]:<18} | {beast_col_strs[2]:<18} | {class_w_rate:5.1f}% / {class_l_rate:4.1f}%")

        overall_win_rate = (total_all_wins / total_all_fights) * 100
        overall_loss_rate = (total_all_losses / total_all_fights) * 100
        print("-" * 105)
        print(f"OVERALL COMBINED: {total_all_wins:,} Wins ({overall_win_rate:.1f}%) | {total_all_losses:,} Losses ({overall_loss_rate:.1f}%) across {total_all_fights:,} battles\n")

if __name__ == "__main__":
    # 1. Level 5 PCs vs Level 3 Beasts (-2 Levels, ~30% reduction)
    run_reduction_audit(pc_level=5, beast_level=3, iters=500)

    # 2. Level 10 PCs vs Level 7 Beasts (-3 Levels, ~30% reduction)
    run_reduction_audit(pc_level=10, beast_level=7, iters=500)

