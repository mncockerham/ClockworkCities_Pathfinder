import json
import subprocess
import sys
from pathlib import Path

# Run Soldier (Lv5) against all other 16 classes (Lv5)
# 1000 iterations per environment = 4,000 matches per matchup x 16 matchups = 64,000 battles!

CLASSES = [
    "artisan",
    "blackmarketeer",
    "chirurgeon",
    "clockworkengineer",
    "clockworkrifleman",
    "dandy",
    "inspector",
    "madbomber",
    "merchant",
    "noble",
    "officer",
    "pugilist",
    "scholar",
    "scout",
    "skycaptain",
    "survivor"
]

def run_soldier_gauntlet(level=5, iters=1000):
    tmpl_dir = Path("ClockworkPathfinder/testing/combat_sim/templates")
    sim_script = Path("ClockworkPathfinder/testing/combat_sim/combat_sim.py")
    
    soldier_file = tmpl_dir / f"soldier_lv{level}.json"

    print("=" * 80)
    print(f"SOLDIER GAUNTLET: SOLDIER (LV{level}) VS ALL OTHER 16 CLASSES")
    print(f"Iterations: {iters:,} per environment (Total: {iters*4:,} battles per class)")
    print("All metrics report SOLDIER'S WIN RATE % & PERFORMANCE TIER")
    print("=" * 80)

    results = []

    # Print table header
    hdr = f"{'Opponent Class':<20} | {'Civil Win %':>11} | {'High Win %':>10} | {'Low Win %':>9} | {'Neither Win %':>13} | {'Overall Tiers (Civ/Hi/Lo/Nei)':<30}"
    print(hdr)
    print("-" * 20 + "-+-" + "-" * 11 + "-+-" + "-" * 10 + "-+-" + "-" * 9 + "-+-" + "-" * 13 + "-+-" + "-" * 30)

    # Import simulator directly in python for maximum speed (no subprocess overhead for 64,000 runs)
    sys.path.append(str(sim_script.parent))
    from combat_sim import Simulator

    for opp in CLASSES:
        opp_file = tmpl_dir / f"{opp}_lv{level}.json"
        sim = Simulator(str(soldier_file), str(opp_file), initial_distance=40)
        suite = sim.run_environment_suite(iterations=iters)
        
        # Calculate Soldier's win % in each environment
        civ_w = suite['results']['Civil']['Clear Win'] + suite['results']['Civil']['Mod Win'] + suite['results']['Civil']['Close Win']
        high_w = suite['results']['High']['Clear Win'] + suite['results']['High']['Mod Win'] + suite['results']['High']['Close Win']
        low_w = suite['results']['Low']['Clear Win'] + suite['results']['Low']['Mod Win'] + suite['results']['Low']['Close Win']
        nei_w = suite['results']['Neither']['Clear Win'] + suite['results']['Neither']['Mod Win'] + suite['results']['Neither']['Close Win']

        tier_summary = f"{suite['tiers']['Civil'][0]} / {suite['tiers']['High'][0]} / {suite['tiers']['Low'][0]} / {suite['tiers']['Neither'][0]}"
        opp_name = opp.capitalize()
        if opp == "clockworkengineer": opp_name = "Engineer"
        if opp == "clockworkrifleman": opp_name = "Rifleman"
        if opp == "blackmarketeer": opp_name = "BlackMarketeer"
        if opp == "madbomber": opp_name = "MadBomber"
        if opp == "skycaptain": opp_name = "SkyCaptain"

        row = f"{opp_name:<20} | {civ_w:>10}% | {high_w:>9}% | {low_w:>8}% | {nei_w:>12}% | {tier_summary:<30}"
        print(row)
        results.append({
            "opp": opp_name,
            "civil": civ_w,
            "high": high_w,
            "low": low_w,
            "neither": nei_w,
            "tiers": tier_summary
        })

    print("=" * 80)
    print("\nSUMMARY OF SOLDIER COMBAT IDENTITY ACROSS 64,000 BATTLES:")
    avg_civ = sum(r["civil"] for r in results) / len(results)
    avg_high = sum(r["high"] for r in results) / len(results)
    avg_low = sum(r["low"] for r in results) / len(results)
    avg_nei = sum(r["neither"] for r in results) / len(results)

    print(f"  - Civil Spire Average Win Rate:  {avg_civ:.1f}%")
    print(f"  - High Radiant Average Win Rate: {avg_high:.1f}%")
    print(f"  - Low Radiant Average Win Rate:  {avg_low:.1f}%")
    print(f"  - The Neither Average Win Rate:  {avg_nei:.1f}%")
    print("=" * 80)

if __name__ == "__main__":
    run_soldier_gauntlet(level=5, iters=1000)
