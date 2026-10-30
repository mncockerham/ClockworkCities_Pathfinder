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

# Standard Wild Environments (EXCLUDING Civil Spire)
WILD_ENVIRONMENTS = ["High", "Low", "Neither"]

CREATURES = [
    ("bear", "Bear (Brute)"),
    ("wolf", "Wolf (Stalker)"),
    ("scorpion", "Scorpion (Venom)"),
    ("acid_spitter", "Acid Spitter (Dex Save)"),
    ("spore_sprayer", "Spore Sprayer (Con Save)"),
    ("disorientor", "Disorientor (Will Save)")
]

def run_wild_gauntlet(pc_level=5, monster_level=5, mode="Berserk", iters=200):
    tmpl_dir = Path(__file__).parent / "templates"
    creat_dir = Path(__file__).parent / "creatures"

    title_mode = f"LEVEL {pc_level} PCS VS LEVEL {monster_level} MONSTERS ({mode.upper()})"
    print("=" * 115)
    print(f"WILDERNESS COMBAT AUDIT (NO CIVIL SPIRE): {title_mode}")
    print("Environments: High Radiant, Low Radiant, The Neither (Full Military Weapons & Unrestricted Armor)")
    print(f"Iterations: {iters} per environment/matchup across 3 wild zones")
    print("=" * 115)

    suffix = f"_flee_lv{monster_level}.json" if mode.lower() == "flee" else f"_lv{monster_level}.json"

    # Header
    col_w = 14
    header_str = f"{'Class':<16} | " + " | ".join([f"{c_lbl[:col_w]:<{col_w}}" for _, c_lbl in CREATURES]) + f" | {'TOTAL Win/Loss':<16}"
    print(header_str)
    print("-" * 115)

    tot_wins = 0
    tot_losses = 0
    tot_fights = 0

    for c_key, c_lbl in CLASSES:
        c_file = tmpl_dir / f"{c_key}_lv{pc_level}.json"
        dist = 60 if c_key in ["scout", "clockworkrifleman"] else 40

        c_w = 0
        c_l = 0
        c_f = 0
        col_cells = []

        for b_key, _ in CREATURES:
            b_file = creat_dir / f"creature_{b_key}{suffix}"
            sim = Simulator(str(c_file), str(b_file), initial_distance=dist)
            suite = sim.run_environment_suite(iterations=iters)

            b_w = 0
            b_l = 0
            b_f = 0

            for env in WILD_ENVIRONMENTS:
                r = suite["results"][env]
                w_pct = r["Clear Win"] + r["Mod Win"] + r["Close Win"]
                l_pct = r["Minor Def"] + r["Major Def"] + r["Clear Def"]

                w_cnt = round((w_pct / 100) * iters)
                l_cnt = round((l_pct / 100) * iters)

                b_w += w_cnt
                b_l += l_cnt
                b_f += iters

            c_w += b_w
            c_l += b_l
            c_f += b_f

            w_pct_val = (b_w / b_f) * 100
            l_pct_val = (b_l / b_f) * 100
            col_cells.append(f"{w_pct_val:4.0f}%/{l_pct_val:2.0f}%")

        tot_wins += c_w
        tot_losses += c_l
        tot_fights += c_f

        c_tot_w = (c_w / c_f) * 100
        c_tot_l = (c_l / c_f) * 100
        row_str = f"{c_lbl:<16} | " + " | ".join([f"{cell:<{col_w}}" for cell in col_cells]) + f" | {c_tot_w:5.1f}% / {c_tot_l:4.1f}%"
        print(row_str)

    print("-" * 115)
    overall_w = (tot_wins / tot_fights) * 100
    overall_l = (tot_losses / tot_fights) * 100
    print(f"OVERALL COMBINED ({mode.upper()}): {tot_wins:,} Wins ({overall_w:.1f}%) | {tot_losses:,} Losses ({overall_l:.1f}%) across {tot_fights:,} wilderness battles\n")

if __name__ == "__main__":
    # 1. Level 5 PCs vs Level 5 Monsters (Berserk - Terrifying Wild Encounters)
    run_wild_gauntlet(pc_level=5, monster_level=5, mode="Berserk", iters=200)

    # 2. Level 5 PCs vs Level 5 Monsters (Flee 50% HP)
    run_wild_gauntlet(pc_level=5, monster_level=5, mode="Flee", iters=200)

