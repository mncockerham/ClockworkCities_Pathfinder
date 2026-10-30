import sys
from pathlib import Path

# Add simulator to path
sys.path.append("ClockworkPathfinder/testing/combat_sim")
from combat_sim import Simulator

CLASSES = [
    "artisan", "blackmarketeer", "chirurgeon", "clockworkengineer",
    "clockworkrifleman", "dandy", "inspector", "madbomber", "merchant",
    "noble", "officer", "pugilist", "scholar", "scout", "skycaptain",
    "soldier", "survivor"
]

CANDIDATES = [
    ("pugilist", "Pugilist (Is Civil Spire too broken? Can it hold up in Neither?)"),
    ("scout", "Scout (Does 100 ft Longbow kite everything too easily?)"),
    ("clockworkrifleman", "Clockwork Rifleman (Is Fatal d12 sniper burst too dominant at range?)"),
    ("noble", "Noble (Are armed retainers over-performing everywhere?)"),
    ("clockworkengineer", "Clockwork Engineer (Is it completely useless in Low/Neither?)"),
    ("scholar", "Scholar (Does it collapse outside High Radiant?)")
]

def run_problem_class_audit(level=5, iters=1000):
    tmpl_dir = Path("ClockworkPathfinder/testing/combat_sim/templates")

    print("=" * 84)
    print(f"POTENTIAL PROBLEM CLASS AUDIT: 6 CANDIDATES ACROSS ALL 16 OPPONENTS")
    print(f"Level {level} | Iterations: {iters:,} per environment (Total: {iters*4:,} battles per class)")
    print("=" * 84)

    for cand_key, desc in CANDIDATES:
        cand_file = tmpl_dir / f"{cand_key}_lv{level}.json"
        opponents = [c for c in CLASSES if c != cand_key]

        print(f"\n>>> AUDITING: {desc.upper()}")
        print(f"{'Opponent Class':<20} | {'Civil Win %':>11} | {'High Win %':>10} | {'Low Win %':>9} | {'Neither Win %':>13} | {'Tiers (Civ/Hi/Lo/Nei)':<22}")
        print("-" * 20 + "-+-" + "-" * 11 + "-+-" + "-" * 10 + "-+-" + "-" * 9 + "-+-" + "-" * 13 + "-+-" + "-" * 22)

        tot_civ, tot_high, tot_low, tot_nei = 0, 0, 0, 0

        for opp in opponents:
            opp_file = tmpl_dir / f"{opp}_lv{level}.json"
            # Distance: 40 ft default, but 60 ft for Scout/Rifleman to reflect ranged intent
            dist = 60 if cand_key in ["scout", "clockworkrifleman"] else 40
            
            sim = Simulator(str(cand_file), str(opp_file), initial_distance=dist)
            suite = sim.run_environment_suite(iterations=iters)

            civ_w = suite['results']['Civil']['Clear Win'] + suite['results']['Civil']['Mod Win'] + suite['results']['Civil']['Close Win']
            high_w = suite['results']['High']['Clear Win'] + suite['results']['High']['Mod Win'] + suite['results']['High']['Close Win']
            low_w = suite['results']['Low']['Clear Win'] + suite['results']['Low']['Mod Win'] + suite['results']['Low']['Close Win']
            nei_w = suite['results']['Neither']['Clear Win'] + suite['results']['Neither']['Mod Win'] + suite['results']['Neither']['Close Win']

            tot_civ += civ_w
            tot_high += high_w
            tot_low += low_w
            tot_nei += nei_w

            tier_str = f"{suite['tiers']['Civil'][0]}/{suite['tiers']['High'][0]}/{suite['tiers']['Low'][0]}/{suite['tiers']['Neither'][0]}"
            opp_name = opp.capitalize()
            if opp == "clockworkengineer": opp_name = "Engineer"
            if opp == "clockworkrifleman": opp_name = "Rifleman"
            if opp == "blackmarketeer": opp_name = "BlackMarketeer"
            if opp == "madbomber": opp_name = "MadBomber"
            if opp == "skycaptain": opp_name = "SkyCaptain"

            print(f"{opp_name:<20} | {civ_w:>10}% | {high_w:>9}% | {low_w:>8}% | {nei_w:>12}% | {tier_str:<22}")

        avg_c = tot_civ / len(opponents)
        avg_h = tot_high / len(opponents)
        avg_l = tot_low / len(opponents)
        avg_n = tot_nei / len(opponents)
        print("-" * 84)
        print(f"AVERAGE PROFILE: Civil: {avg_c:.1f}% | High: {avg_h:.1f}% | Low: {avg_l:.1f}% | Neither: {avg_n:.1f}%")
        print("=" * 84)

if __name__ == "__main__":
    run_problem_class_audit(level=5, iters=1000)

