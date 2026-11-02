"""
Clockwork Cities Pathfinder — Simplified Class vs. Class Problem/Pairing Analyzer
Runs 1v1 PvP combat simulations across all core classes plus the 4 Merchant specializations,
or analyzes existing matrix results.

Highlights:
1. Hard Counters / Severe Mismatches: Win rate >= 90% or <= 10% (one class dominates completely).
2. Moderate Imbalances: Win rate 75-89% or 11-25%.
3. Environmental Extremes: Matchups where environment completely flips the outcome (>50% swing between Civil and Neither/High).
4. Merchant Specialization Comparison: Side-by-side performance of Reflex, Fortitude, Will, and Neither Fire against each opposing class.
"""

import sys
import os
import json
import itertools
from pathlib import Path
from collections import defaultdict

# Add combat_sim to path
sys.path.append(str(Path(__file__).parent))
from combat_sim import Simulator

CLASSES_TO_TEST = [
    "artisan", "chirurgeon", "clockworkengineer", "clockworkrifleman",
    "dandy", "greymarketeer", "inspector", "madbomber", "noble", "officer",
    "pugilist", "scholar", "scout", "skycaptain", "soldier", "survivor",
    "merchant_reflex", "merchant_fortitude", "merchant_will", "merchant_neitherfire"
]

ENVIRONMENTS = ["Civil", "High", "Low", "Neither"]

def run_matchups(level=5, iterations=40):
    tmpl_dir = Path(__file__).parent / "templates"
    pairs = list(itertools.combinations(CLASSES_TO_TEST, 2))
    print(f"Running simulation for {len(pairs)} matchups at Level {level} ({iterations} iters/env)...")
    
    results = []
    for idx, (c1, c2) in enumerate(pairs):
        f1 = tmpl_dir / f"{c1}_lv{level}.json"
        f2 = tmpl_dir / f"{c2}_lv{level}.json"
        if not f1.exists() or not f2.exists():
            continue
            
        sim = Simulator(str(f1), str(f2))
        record = {"char_a": c1, "char_b": c2, "env_results": {}}
        
        env_suite = sim.run_environment_suite(iterations=iterations)
        
        for env in ENVIRONMENTS:
            res_dict = env_suite["results"][env]
            round_dict = env_suite.get("round_stats", {}).get(env, {})
            wins_a = res_dict.get("Clear Win", 0) + res_dict.get("Mod Win", 0) + res_dict.get("Close Win", 0)
            wins_b = res_dict.get("Clear Def", 0) + res_dict.get("Major Def", 0) + res_dict.get("Minor Def", 0)
            draws = res_dict.get("Too Close", 0)
            total = wins_a + wins_b + draws
            pct_a = round((wins_a / total) * 100, 1) if total else 0.0
            pct_b = round((wins_b / total) * 100, 1) if total else 0.0
            record["env_results"][env] = {
                "win_a": pct_a,
                "win_b": pct_b,
                "draw": round((draws / total) * 100, 1) if total else 0.0,
                "avg_rounds": round_dict.get("avg", 0.0)
            }
        results.append(record)
        if (idx + 1) % 30 == 0 or (idx + 1) == len(pairs):
            print(f"  Completed {idx+1}/{len(pairs)} matchups...")
    return results

def analyze_records(records):
    # 1. Overall win rates
    overall_wins = defaultdict(lambda: {e: [] for e in ENVIRONMENTS})
    for r in records:
        a = r["char_a"]
        b = r["char_b"]
        for env, data in r["env_results"].items():
            overall_wins[a][env].append(data["win_a"])
            overall_wins[b][env].append(data["win_b"])
            
    avg_by_class = {}
    for cls, env_dict in overall_wins.items():
        avg_by_class[cls] = {}
        all_env_vals = []
        for env, vals in env_dict.items():
            avg_env = round(sum(vals) / len(vals), 1) if vals else 0.0
            avg_by_class[cls][env] = avg_env
            all_env_vals.extend(vals)
        avg_by_class[cls]["Overall"] = round(sum(all_env_vals) / len(all_env_vals), 1) if all_env_vals else 0.0

    # 2. Hard Counters / Severe Mismatches (Win >= 85% overall or in multiple environments)
    severe_matchups = []
    for r in records:
        a = r["char_a"]
        b = r["char_b"]
        a_wins_all = [r["env_results"][e]["win_a"] for e in ENVIRONMENTS]
        avg_a = round(sum(a_wins_all) / len(a_wins_all), 1)
        
        if avg_a >= 85.0 or avg_a <= 15.0:
            winner = a if avg_a >= 85.0 else b
            loser = b if avg_a >= 85.0 else a
            win_pct = avg_a if avg_a >= 85.0 else round(100.0 - avg_a, 1)
            severe_matchups.append({
                "winner": winner,
                "loser": loser,
                "avg_win": win_pct,
                "env_detail": {e: r["env_results"][e]["win_a"] if winner == a else r["env_results"][e]["win_b"] for e in ENVIRONMENTS}
            })
            
    severe_matchups.sort(key=lambda x: x["avg_win"], reverse=True)

    # 3. Environmental Polarizations (> 50% swing between Civil and Wild/Neither)
    polarized_matchups = []
    for r in records:
        a = r["char_a"]
        b = r["char_b"]
        civil_win_a = r["env_results"]["Civil"]["win_a"]
        neither_win_a = r["env_results"]["Neither"]["win_a"]
        high_win_a = r["env_results"]["High"]["win_a"]
        
        swing_civil_neither = abs(civil_win_a - neither_win_a)
        swing_civil_high = abs(civil_win_a - high_win_a)
        max_swing = max(swing_civil_neither, swing_civil_high)
        if max_swing >= 50.0:
            polarized_matchups.append({
                "char_a": a,
                "char_b": b,
                "civil_win_a": civil_win_a,
                "high_win_a": high_win_a,
                "neither_win_a": neither_win_a,
                "max_swing": max_swing
            })
    polarized_matchups.sort(key=lambda x: x["max_swing"], reverse=True)

    # 4. Merchant Specialization Comparison
    merchant_types = ["merchant_reflex", "merchant_fortitude", "merchant_will", "merchant_neitherfire"]
    core_classes = [c for c in CLASSES_TO_TEST if not c.startswith("merchant_")]
    merchant_vs_core = defaultdict(dict)
    
    for r in records:
        a = r["char_a"]
        b = r["char_b"]
        m_cls = None
        opp_cls = None
        if a in merchant_types and b in core_classes:
            m_cls = a
            opp_cls = b
            m_wins = [r["env_results"][e]["win_a"] for e in ENVIRONMENTS]
        elif b in merchant_types and a in core_classes:
            m_cls = b
            opp_cls = a
            m_wins = [r["env_results"][e]["win_b"] for e in ENVIRONMENTS]
            
        if m_cls and opp_cls:
            avg_m = round(sum(m_wins) / len(m_wins), 1)
            merchant_vs_core[opp_cls][m_cls] = {
                "avg": avg_m,
                "civil": r["env_results"]["Civil"]["win_a" if m_cls == a else "win_b"],
                "neither": r["env_results"]["Neither"]["win_a" if m_cls == a else "win_b"]
            }

    return {
        "avg_by_class": avg_by_class,
        "severe_matchups": severe_matchups,
        "polarized_matchups": polarized_matchups,
        "merchant_vs_core": merchant_vs_core
    }

if __name__ == "__main__":
    records = run_matchups(level=5, iterations=40)
    analysis = analyze_records(records)
    
    out_dir = Path(__file__).parent / "matrix_results"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "simplified_pvp_analysis.json"
    with open(out_path, "w") as f:
        json.dump(analysis, f, indent=2)
    print(f"Analysis saved to {out_path}")
