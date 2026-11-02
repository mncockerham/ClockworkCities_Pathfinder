"""
Full Class vs Class Matchup Analyzer with:
1. Noble Soldier (holds lawful 1d6 Fair Steel Noble Dueling Blade in Spire)
2. Four Merchant Specializations by Damage/Save Type:
   - Merchant (Reflex - Fire Bombs)
   - Merchant (Fortitude - Acid/Poison Gas)
   - Merchant (Will - Flashbang / Disorientation)
   - Merchant (Neither Fire - Inductive Alchemical Fire)
3. Standard 13 core classes (including Soldier with closing crossbow, Pugilist with Solar Plexus Shot, Rake, etc.)
"""

import sys
from pathlib import Path
import itertools
from collections import defaultdict

sys.path.append(str(Path(__file__).parent))
from combat_sim import Simulator

CLASSES = [
    ("soldier", "Soldier"),
    ("noble_soldier", "Nob_Soldier"),
    ("clockworkrifleman", "Rifleman"),
    ("pugilist", "Pugilist"),
    ("survivor", "Survivor"),
    ("scout", "Scout"),
    ("officer", "Officer"),
    ("rake", "Rake"),
    ("scholar", "Scholar"),
    ("clockworkengineer", "Engineer"),
    ("noble", "Noble"),
    ("merchant_reflex", "Merch_Ref"),
    ("merchant_fortitude", "Merch_Fort"),
    ("merchant_will", "Merch_Will"),
    ("merchant_neitherfire", "Merch_Fire"),
    ("greymarketeer", "GreyMarket"),
    ("chirurgeon", "Chirurgeon")
]

def run_all_matrices(level=5, iterations=100):
    tmpl_dir = Path(__file__).parent / "templates"
    
    envs = ["civil_spire", "high_radiant", "low_radiant", "the_neither"]
    env_labels = {
        "civil_spire": "CIVIL SPIRE (Disarmament: Fists, Utility Daggers, 1d6 Noble/Merchant/Rake Blades)",
        "high_radiant": "HIGH RADIANT (Dynamos, Battlements & Saturated Wireless Induction)",
        "low_radiant": "LOW RADIANT (Perimeters, Airships & 4-Mile Buffer)",
        "the_neither": "THE NEITHER (Zero Induction, Cartridge Attrition & Raw Physical Combat)"
    }
    
    matrix = {e: defaultdict(dict) for e in envs}
    stats = {e: defaultdict(lambda: {"wins": 0, "losses": 0, "total": 0}) for e in envs}

    pairs = list(itertools.combinations(CLASSES, 2))

    for (k1, name1), (k2, name2) in pairs:
        f1 = tmpl_dir / f"{k1}_lv{level}.json"
        f2 = tmpl_dir / f"{k2}_lv{level}.json"

        if not f1.exists() or not f2.exists():
            continue

        for env in envs:
            if env == "civil_spire":
                dist = 20
            else:
                dist = 60 if ("rifleman" in k1 or "scout" in k1 or "rifleman" in k2 or "scout" in k2) else 40

            sim = Simulator(str(f1), str(f2), initial_distance=dist)
            env_key_map = {
                "civil_spire": "Civil",
                "high_radiant": "High",
                "low_radiant": "Low",
                "the_neither": "Neither"
            }
            sim_env = env_key_map[env]
            suite = sim.run_environment_suite(iterations=iterations)
            r = suite["results"][sim_env]

            w_pct = r["Clear Win"] + r["Mod Win"] + r["Close Win"]
            l_pct = r["Minor Def"] + r["Major Def"] + r["Clear Def"]

            matrix[env][name1][name2] = w_pct
            matrix[env][name2][name1] = l_pct

            w_cnt = round((w_pct / 100) * iterations)
            l_cnt = round((l_pct / 100) * iterations)

            stats[env][name1]["wins"] += w_cnt
            stats[env][name1]["losses"] += l_cnt
            stats[env][name1]["total"] += iterations

            stats[env][name2]["wins"] += l_cnt
            stats[env][name2]["losses"] += w_cnt
            stats[env][name2]["total"] += iterations

    short_headers = [name[:5] for _, name in CLASSES]
    col_w = 6
    header_str = f"{'Attacker (Row)':<13} | " + " | ".join([f"{sh:>{col_w}}" for sh in short_headers])

    for env in envs:
        print("\n" + "=" * 125)
        print(f"GRID: {env_labels[env]}")
        print("Cell Value = Win % of ROW class against COLUMN class (Top)")
        print("=" * 125)
        print(header_str)
        print("-" * 125)

        for _, r_name in CLASSES:
            cells = []
            for _, c_name in CLASSES:
                if r_name == c_name:
                    cells.append(f"{'--':>{col_w}}")
                else:
                    win_rate = matrix[env][r_name].get(c_name, 0.0)
                    cells.append(f"{win_rate:>{col_w-1}.0f}%")
            print(f"{r_name:<13} | " + " | ".join(cells))

        # Also print rank summary
        print("-" * 125)
        print(f"RANKINGS SUMMARY ({env.upper()}):")
        sorted_ranks = sorted(
            CLASSES, 
            key=lambda c: stats[env][c[1]]["wins"] / max(1, stats[env][c[1]]["total"]),
            reverse=True
        )
        rank_line = []
        for rk, (_, nm) in enumerate(sorted_ranks, 1):
            pct = (stats[env][nm]["wins"] / max(1, stats[env][nm]["total"])) * 100
            rank_line.append(f"{rk}. {nm} ({pct:.1f}%)")
        print(" | ".join(rank_line[:9]))
        print(" | ".join(rank_line[9:]))

if __name__ == "__main__":
    run_all_matrices(level=5, iterations=100)

