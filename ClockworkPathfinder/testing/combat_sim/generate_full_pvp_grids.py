"""
Generates Class vs Class Win Percentage Grids where:
- Columns (Top Header) = Opponents
- Rows (Side Header) = Acting Class
Cell value = Win % of the ROW class against the COLUMN class.
Outputs separate grids for:
1. Civil Spire
2. High Radiant
3. Low Radiant
4. The Neither
"""

import sys
from pathlib import Path
import itertools
from collections import defaultdict

sys.path.append(str(Path(__file__).parent))
from combat_sim import Simulator

CLASSES = [
    ("soldier", "Soldier"),
    ("clockworkrifleman", "Rifleman"),
    ("pugilist", "Pugilist"),
    ("survivor", "Survivor"),
    ("scout", "Scout"),
    ("officer", "Officer"),
    ("rake", "Rake"),
    ("scholar", "Scholar"),
    ("clockworkengineer", "Engineer"),
    ("noble", "Noble"),
    ("merchant", "Merchant"),
    ("greymarketeer", "GreyMarketeer"),
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
    
    # matrix[env][row_class][col_class] = win_pct
    matrix = {e: defaultdict(dict) for e in envs}

    pairs = list(itertools.combinations(CLASSES, 2))

    for (k1, name1), (k2, name2) in pairs:
        f1 = tmpl_dir / f"{k1}_lv{level}.json"
        f2 = tmpl_dir / f"{k2}_lv{level}.json"

        # Realistic engagement ranges
        # Spire: 20 ft
        # High/Low/Neither: 50 ft (or 60 ft if snipers/scouts)
        for env in envs:
            if env == "civil_spire":
                dist = 20
            else:
                dist = 60 if ("rifleman" in k1 or "scout" in k1 or "rifleman" in k2 or "scout" in k2) else 40

            sim = Simulator(str(f1), str(f2), initial_distance=dist)
            # Map env string to Simulator key
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

    # Print formatted grids
    short_headers = [name[:5] for _, name in CLASSES]
    header_str = f"{'Attacker (Row)':<15} | " + " | ".join([f"{sh:<5}" for sh in short_headers])

    for env in envs:
        print("\n" + "=" * 105)
        print(f"GRID: {env_labels[env]}")
        print("Cell Value = Win % of ROW class against COLUMN class (Top)")
        print("=" * 105)
        print(header_str)
        print("-" * 105)

        for _, r_name in CLASSES:
            cells = []
            for _, c_name in CLASSES:
                if r_name == c_name:
                    cells.append("  -- ")
                else:
                    win_rate = matrix[env][r_name].get(c_name, 0.0)
                    cells.append(f"{win_rate:4.0f}%")
            print(f"{r_name:<15} | " + " | ".join(cells))

if __name__ == "__main__":
    run_all_matrices(level=5, iterations=100)

