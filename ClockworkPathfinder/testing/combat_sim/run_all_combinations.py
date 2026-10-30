"""
Clockwork Cities Pathfinder — Master All-Combinations 1v1 Battle Matrix
Runs 1v1 combat simulations for EVERY unique class pair at:
  - Level 1  (136 unique matchups x 4 environments)
  - Level 5  (136 unique matchups x 4 environments)
  - Level 10 (136 unique matchups x 4 environments)

Outputs:
  - Overall Environmental Win Rate Summary Table for all 17 classes per level.
  - Generates comprehensive markdown report and saves raw JSON matrix.
"""

import itertools
import json
import os
import sys
import time
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

ENVIRONMENTS = ["Civil", "High", "Low", "Neither"]

def run_level_matrix(level: int, iters: int = 100):
    tmpl_dir = Path(__file__).parent / "templates"
    pairs = list(itertools.combinations(CLASSES, 2))
    total_matchups = len(pairs)
    total_battles = total_matchups * len(ENVIRONMENTS) * iters

    print("=" * 80)
    print(f"RUNNING MASTER MATRIX: LEVEL {level} (ALL COMBINATIONS)")
    print(f"Classes: {len(CLASSES)} | Unique Pair Matchups: {total_matchups}")
    print(f"Iterations per matchup/env: {iters:,} | Total Simulated Battles: {total_battles:,}")
    print("=" * 80)

    # Track wins, losses, draws per class per environment
    # stats[cls][env] = {"wins": 0, "losses": 0, "draws": 0, "total": 0}
    stats = {c: {e: {"wins": 0, "losses": 0, "draws": 0, "total": 0} for e in ENVIRONMENTS} for c in CLASSES}
    matchup_records = []

    start_time = time.time()
    
    for idx, (c1, c2) in enumerate(pairs, 1):
        f1 = tmpl_dir / f"{c1}_lv{level}.json"
        f2 = tmpl_dir / f"{c2}_lv{level}.json"

        # Determine reasonable starting distance based on ranged capabilities
        dist = 40
        if "scout" in (c1, c2) or "clockworkrifleman" in (c1, c2):
            dist = 60

        sim = Simulator(str(f1), str(f2), initial_distance=dist)
        suite = sim.run_environment_suite(iterations=iters)

        record = {
            "char_a": c1,
            "char_b": c2,
            "level": level,
            "dist": dist,
            "results": suite["results"],
            "tiers": suite["tiers"]
        }
        matchup_records.append(record)

        # Accumulate stats
        for env in ENVIRONMENTS:
            r = suite["results"][env]
            # Outcomes are relative to c1
            w1 = r["Clear Win"] + r["Mod Win"] + r["Close Win"]
            draw = r["Too Close"]
            w2 = r["Minor Def"] + r["Major Def"] + r["Clear Def"]

            # Scaled counts
            c1_wins = round((w1 / 100) * iters)
            c2_wins = round((w2 / 100) * iters)
            draw_cnt = round((draw / 100) * iters)

            stats[c1][env]["wins"] += c1_wins
            stats[c1][env]["losses"] += c2_wins
            stats[c1][env]["draws"] += draw_cnt
            stats[c1][env]["total"] += iters

            stats[c2][env]["wins"] += c2_wins
            stats[c2][env]["losses"] += c1_wins
            stats[c2][env]["draws"] += draw_cnt
            stats[c2][env]["total"] += iters

        if idx % 34 == 0 or idx == total_matchups:
            elapsed = time.time() - start_time
            print(f"  Processed {idx:>3}/{total_matchups} matchups ({idx/total_matchups*100:.1f}%) in {elapsed:.1f}s...")

    elapsed_total = time.time() - start_time
    print(f"\nLevel {level} completed in {elapsed_total:.2f} seconds ({total_battles / elapsed_total:,.0f} battles/sec)!")

    # Calculate final percentage summary table
    summary_table = []
    for c in CLASSES:
        row = {"class": c}
        for env in ENVIRONMENTS:
            tot = stats[c][env]["total"]
            w = stats[c][env]["wins"]
            win_pct = round((w / tot) * 100, 1) if tot > 0 else 0.0
            row[env] = win_pct
            
            # Overall Tier calculation
            if win_pct >= 75:
                tier = "S"
            elif win_pct >= 60:
                tier = "A"
            elif win_pct >= 40:
                tier = "B"
            elif win_pct >= 20:
                tier = "C"
            else:
                tier = "D"
            row[f"{env}_tier"] = tier

        # Overall average across all 4 envs
        avg_pct = round(sum(row[e] for e in ENVIRONMENTS) / len(ENVIRONMENTS), 1)
        row["Average"] = avg_pct
        summary_table.append(row)

    # Sort by overall average performance
    summary_table.sort(key=lambda x: x["Average"], reverse=True)

    # Print summary table
    print("\n" + "=" * 80)
    print(f"MASTER CLASS WIN RATE MATRIX — LEVEL {level}")
    print("=" * 80)
    hdr = f"{'Class Archetype':<20} | {'Civil Win %':>11} | {'High Win %':>10} | {'Low Win %':>9} | {'Neither Win %':>13} | {'Average Win %':>13}"
    print(hdr)
    print("-" * 20 + "-+-" + "-" * 11 + "-+-" + "-" * 10 + "-+-" + "-" * 9 + "-+-" + "-" * 13 + "-+-" + "-" * 13)

    for r in summary_table:
        name = r["class"].capitalize()
        if r["class"] == "clockworkengineer": name = "Engineer"
        if r["class"] == "clockworkrifleman": name = "Rifleman"
        if r["class"] == "blackmarketeer": name = "BlackMarketeer"
        if r["class"] == "madbomber": name = "MadBomber"
        if r["class"] == "skycaptain": name = "SkyCaptain"

        print(f"{name:<20} | {r['Civil']:>10}% | {r['High']:>9}% | {r['Low']:>8}% | {r['Neither']:>12}% | {r['Average']:>12}%")

    print("=" * 80)
    return summary_table, matchup_records

def run_all_levels(levels=[1, 5, 10], iters=100):
    out_dir = Path(__file__).parent / "matrix_results"
    out_dir.mkdir(parents=True, exist_ok=True)

    master_results = {}

    for lvl in levels:
        summary, records = run_level_matrix(level=lvl, iters=iters)
        master_results[f"level_{lvl}"] = {
            "summary": summary,
            "records": records
        }

    # Save full JSON dump
    json_path = out_dir / "master_matrix_results.json"
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(master_results, f, indent=2)

    # Generate Markdown Report
    md_path = out_dir / "MASTER_BALANCE_REPORT.md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("# Master Class 1v1 Combat Matrix — Clockwork Cities Pathfinder\n\n")
        f.write(f"- **Simulated Levels:** Levels 1, 5, and 10\n")
        f.write(f"- **Class Count:** 17 Classes (136 unique pairs per level)\n")
        f.write(f"- **Environments Tested:** Civil Spire, High Radiant, Low Radiant, The Neither\n")
        f.write(f"- **Total Simulated Battles:** {len(levels) * 136 * 4 * iters:,} matches\n\n")
        f.write("---\n\n")

        for lvl in levels:
            data = master_results[f"level_{lvl}"]["summary"]
            f.write(f"## Level {lvl} Class Environmental Win Rate Rankings\n\n")
            f.write("| Rank | Class | Civil Spire | High Radiant | Low Radiant | The Neither | Overall Average | Environmental Tier Profile |\n")
            f.write("|:---:|---|:---:|:---:|:---:|:---:|:---:|:---:|\n")
            for rank, row in enumerate(data, 1):
                name = row["class"].capitalize()
                if row["class"] == "clockworkengineer": name = "Clockwork Engineer"
                if row["class"] == "clockworkrifleman": name = "Clockwork Rifleman"
                if row["class"] == "blackmarketeer": name = "Black Marketeer"
                if row["class"] == "madbomber": name = "Mad Bomber"
                if row["class"] == "skycaptain": name = "Sky Captain"

                tiers = f"`{row['Civil_tier']}` / `{row['High_tier']}` / `{row['Low_tier']}` / `{row['Neither_tier']}`"
                f.write(f"| {rank} | **{name}** | {row['Civil']}% | {row['High']}% | {row['Low']}% | {row['Neither']}% | **{row['Average']}%** | {tiers} |\n")
            f.write("\n---\n\n")

    print(f"\nSaved full matrix records to: {json_path}")
    print(f"Generated Markdown report to: {md_path}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Master All-Combinations Combat Matrix")
    parser.add_argument("--iters", type=int, default=100, help="Iterations per matchup per environment (default: 100)")
    parser.add_argument("--levels", type=int, nargs="+", default=[1, 5, 10], help="Levels to test (default: 1 5 10)")
    args = parser.parse_args()

    run_all_levels(levels=args.levels, iters=args.iters)

