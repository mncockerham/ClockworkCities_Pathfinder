"""
Class vs Class Matchup Analyzer for Civil Spire and High Radiant environments.
Tests all 13 core playable classes at Level 5 across 100 iterations per matchup.
Outputs win/loss breakdown, matchup matrix, and environment rankings.
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

def run_pvp_civil_high(level=5, iterations=100):
    tmpl_dir = Path(__file__).parent / "templates"
    
    stats = {
        "Civil": defaultdict(lambda: {"wins": 0, "losses": 0, "draws": 0, "total": 0}),
        "High": defaultdict(lambda: {"wins": 0, "losses": 0, "draws": 0, "total": 0})
    }
    
    matrix = {
        "Civil": defaultdict(dict),
        "High": defaultdict(dict)
    }

    pairs = list(itertools.combinations(CLASSES, 2))
    total_matchups = len(pairs)
    print("=" * 80)
    print(f"RUNNING CLASS VS CLASS PVP BREAKDOWN: CIVIL SPIRE & HIGH RADIANT")
    print(f"Level {level}, {iterations} Iterations per Matchup ({total_matchups} Unique Pairings)")
    print("=" * 80)

    for (k1, name1), (k2, name2) in pairs:
        f1 = tmpl_dir / f"{k1}_lv{level}.json"
        f2 = tmpl_dir / f"{k2}_lv{level}.json"
        
        # In Civil Spire, close quarters parlor/alley fights (20-30 ft max).
        # In High Radiant, fortified battlement/core distances (40-60 ft).
        sim_civil = Simulator(str(f1), str(f2), initial_distance=20)
        suite_civil = sim_civil.run_environment_suite(iterations=iterations)

        sim_high = Simulator(str(f1), str(f2), initial_distance=50)
        suite_high = sim_high.run_environment_suite(iterations=iterations)

        for env_label, suite in [("Civil", suite_civil), ("High", suite_high)]:
            r = suite["results"][env_label]
            w_pct = r["Clear Win"] + r["Mod Win"] + r["Close Win"]
            l_pct = r["Minor Def"] + r["Major Def"] + r["Clear Def"]
            d_pct = r["Too Close"]

            w_cnt = round((w_pct / 100) * iterations)
            l_cnt = round((l_pct / 100) * iterations)
            d_cnt = round((d_pct / 100) * iterations)

            # Record for c1
            stats[env_label][name1]["wins"] += w_cnt
            stats[env_label][name1]["losses"] += l_cnt
            stats[env_label][name1]["draws"] += d_cnt
            stats[env_label][name1]["total"] += iterations

            # Record for c2
            stats[env_label][name2]["wins"] += l_cnt
            stats[env_label][name2]["losses"] += w_cnt
            stats[env_label][name2]["draws"] += d_cnt
            stats[env_label][name2]["total"] += iterations

            matrix[env_label][name1][name2] = w_pct
            matrix[env_label][name2][name1] = l_pct

    for env_name, env_key in [
        ("CIVIL SPIRE (Disarmament Laws: Fists, Utility Daggers, Noble Dueling Blades, Concealed Linings)", "Civil"), 
        ("HIGH RADIANT (Dynamos, Battlements & Saturated Wireless Induction)", "High")
    ]:
        print("\n" + "=" * 90)
        print(f"RANKING TABLE: {env_name}")
        print("=" * 90)
        print(f"{'Rank':<5} | {'Class':<18} | {'Win %':<8} | {'Loss %':<8} | {'Draw %':<8} | {'Total W/L Record':<18}")
        print("-" * 90)

        sorted_classes = sorted(
            CLASSES, 
            key=lambda c: stats[env_key][c[1]]["wins"] / max(1, stats[env_key][c[1]]["total"]),
            reverse=True
        )

        for rank, (_, name) in enumerate(sorted_classes, 1):
            st = stats[env_key][name]
            w_pct = (st["wins"] / st["total"]) * 100
            l_pct = (st["losses"] / st["total"]) * 100
            d_pct = (st["draws"] / st["total"]) * 100
            print(f"{rank:<5} | {name:<18} | {w_pct:6.1f}% | {l_pct:6.1f}% | {d_pct:6.1f}% | {st['wins']}W - {st['losses']}L - {st['draws']}D")

    # Print Matchup Matrix for Civil Spire
    print("\n" + "=" * 90)
    print("CIVIL SPIRE: HEAD-TO-HEAD WIN % MATRIX (Row vs Column)")
    print("=" * 90)
    short_names = [name[:5] for _, name in CLASSES]
    header = f"{'Class':<12} | " + " | ".join([f"{sn:<5}" for sn in short_names])
    print(header)
    print("-" * 90)
    for _, r_name in CLASSES:
        cells = []
        for _, c_name in CLASSES:
            if r_name == c_name:
                cells.append("  -- ")
            else:
                pct = matrix["Civil"][r_name].get(c_name, 0.0)
                cells.append(f"{pct:4.0f}%")
        print(f"{r_name:<12} | " + " | ".join(cells))

    # Print Matchup Matrix for High Radiant
    print("\n" + "=" * 90)
    print("HIGH RADIANT: HEAD-TO-HEAD WIN % MATRIX (Row vs Column)")
    print("=" * 90)
    print(header)
    print("-" * 90)
    for _, r_name in CLASSES:
        cells = []
        for _, c_name in CLASSES:
            if r_name == c_name:
                cells.append("  -- ")
            else:
                pct = matrix["High"][r_name].get(c_name, 0.0)
                cells.append(f"{pct:4.0f}%")
        print(f"{r_name:<12} | " + " | ".join(cells))

if __name__ == "__main__":
    run_pvp_civil_high(level=5, iterations=100)

