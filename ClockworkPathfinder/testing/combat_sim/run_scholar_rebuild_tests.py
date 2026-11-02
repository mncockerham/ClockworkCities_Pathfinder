import sys
import os
import json
from pathlib import Path
from collections import defaultdict

SIM_DIR = Path("ClockworkPathfinder/testing/combat_sim")
sys.path.append(str(SIM_DIR))

import combat_sim

CLASSES_TO_TEST = [
    "artisan", "clockworkengineer", "clockworkrifleman", "chirurgeon",
    "dandy", "greymarketeer", "inspector", "madbomber", "noble", "officer",
    "pugilist", "scholar", "scout", "skycaptain", "soldier", "survivor",
    "merchant_reflex", "merchant_fortitude", "merchant_will", "merchant_neitherfire"
]

ENVIRONMENTS = ["High", "Low", "Neither", "Civil"]
ENV_MAP = {
    "High": "high_radiant",
    "Low": "low_radiant",
    "Neither": "the_neither",
    "Civil": "civil_spire"
}

def run_suite_for_level(level=5, iterations=40):
    tmpl_dir = SIM_DIR / "templates"
    print(f"\n=======================================================")
    print(f"RUNNING LEVEL {level} FULL CLASS PVP AUDIT ({iterations} iters/env)")
    print(f"=======================================================")

    win_counts = {env: defaultdict(int) for env in ENVIRONMENTS}
    total_matches = {env: defaultdict(int) for env in ENVIRONMENTS}

    n = len(CLASSES_TO_TEST)
    pair_count = 0

    for i in range(n):
        for j in range(i + 1, n):
            c1 = CLASSES_TO_TEST[i]
            c2 = CLASSES_TO_TEST[j]

            f1 = tmpl_dir / f"{c1}_lv{level}.json"
            f2 = tmpl_dir / f"{c2}_lv{level}.json"
            if not f1.exists() or not f2.exists():
                continue

            sim = combat_sim.Simulator(str(f1), str(f2))
            suite = sim.run_environment_suite(iterations=iterations)

            for env in ENVIRONMENTS:
                res = suite["results"][env]
                wins_1 = res.get("Clear Win", 0) + res.get("Mod Win", 0) + res.get("Close Win", 0)
                wins_2 = res.get("Clear Def", 0) + res.get("Major Def", 0) + res.get("Minor Def", 0)
                draws = res.get("Too Close", 0)
                tot = wins_1 + wins_2 + draws

                win_counts[env][c1] += wins_1
                win_counts[env][c2] += wins_2
                total_matches[env][c1] += tot
                total_matches[env][c2] += tot

            pair_count += 1
            if pair_count % 30 == 0:
                print(f"  Processed {pair_count} pairings...")

    # Calculate percentages
    summary = {}
    for env in ENVIRONMENTS:
        summary[env] = {}
        for c in CLASSES_TO_TEST:
            tot = total_matches[env][c]
            w = win_counts[env][c]
            summary[env][c] = round((w / tot) * 100, 1) if tot > 0 else 0.0

    return summary

if __name__ == "__main__":
    res_lv5 = run_suite_for_level(5, iterations=40)
    res_lv10 = run_suite_for_level(10, iterations=40)

    # Save to JSON
    out_file = SIM_DIR / "matrix_results" / "scholar_rebuild_lv5_lv10_comparison.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump({"level_5": res_lv5, "level_10": res_lv10}, f, indent=2)

    print("\n\n" + "="*80)
    print("SCHOLAR PERFORMANCE (PRE-REBUILD vs POST-REBUILD)")
    print("="*80)
    print(f"{'Environment':<12} | {'Scholar Lv5 Win Rate':<22} | {'Scholar Lv10 Win Rate':<22}")
    print("-" * 60)
    for env in ENVIRONMENTS:
        print(f"{env:<12} | {res_lv5[env]['scholar']:>20.1f}% | {res_lv10[env]['scholar']:>20.1f}%")

    print("\n" + "="*80)
    print("ALL CLASSES WIN RATE SUMMARY (LEVEL 5 vs LEVEL 10)")
    print("="*80)
    print(f"{'Class':<20} | {'Lv5 High':<8} {'Lv10 High':<9} | {'Lv5 Low':<8} {'Lv10 Low':<9} | {'Lv5 Neither':<11} {'Lv10 Neither':<12}")
    print("-" * 75)
    for c in sorted(CLASSES_TO_TEST):
        print(f"{c:<20} | {res_lv5['High'][c]:>7.1f}% {res_lv10['High'][c]:>8.1f}% | {res_lv5['Low'][c]:>7.1f}% {res_lv10['Low'][c]:>8.1f}% | {res_lv5['Neither'][c]:>10.1f}% {res_lv10['Neither'][c]:>11.1f}%")

