import sys
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

BEASTS = ["bear", "wolf", "scorpion"]
ENVIRONMENTS = ["Civil", "High", "Low", "Neither"]

def test_tier_matrix(player_level, beast_levels, iters=200):
    tmpl_dir = Path(__file__).parent / "templates"
    creat_dir = Path(__file__).parent / "creatures"

    print("=" * 100)
    print(f"CALIBRATION AUDIT: LEVEL {player_level} CHARACTERS VS MONSTERS (LEVELS {beast_levels})")
    print(f"Monte Carlo Iterations: {iters} per environment/matchup across all 4 environments")
    print("=" * 100)

    for beast_lvl in beast_levels:
        ratio = (beast_lvl / player_level) * 100
        print(f"\n>>> TEST: Monster Level {beast_lvl} ({ratio:.0f}% of Player Level {player_level}) <<<")
        
        for mode in ["Berserk", "Flee"]:
            class_wins = {}
            total_wins = 0
            total_losses = 0
            total_fights = 0

            for c in CLASSES:
                c_file = tmpl_dir / f"{c}_lv{player_level}.json"
                dist = 60 if c in ["scout", "clockworkrifleman"] else 40
                c_w = 0
                c_l = 0
                c_tot = 0

                for b in BEASTS:
                    suffix = f"_flee_lv{beast_lvl}.json" if mode == "Flee" else f"_lv{beast_lvl}.json"
                    b_file = creat_dir / f"creature_{b}{suffix}"
                    sim = Simulator(str(c_file), str(b_file), initial_distance=dist)
                    suite = sim.run_environment_suite(iterations=iters)

                    for env in ENVIRONMENTS:
                        r = suite["results"][env]
                        w_pct = r["Clear Win"] + r["Mod Win"] + r["Close Win"]
                        l_pct = r["Minor Def"] + r["Major Def"] + r["Clear Def"]

                        w_count = round((w_pct / 100) * iters)
                        l_count = round((l_pct / 100) * iters)

                        c_w += w_count
                        c_l += l_count
                        c_tot += iters

                class_wins[c] = (c_w / c_tot) * 100
                total_wins += c_w
                total_losses += c_l
                total_fights += c_tot

            overall_win = (total_wins / total_fights) * 100
            overall_loss = (total_losses / total_fights) * 100

            print(f"--- Mode: {mode.upper()} (Beast Lv{beast_lvl} vs PC Lv{player_level}) | Overall Win: {overall_win:.1f}% | Loss: {overall_loss:.1f}% ---")
            sorted_classes = sorted(class_wins.items(), key=lambda x: x[1], reverse=True)
            row_str = " | ".join([f"{k[:8]}: {v:.0f}%" for k, v in sorted_classes[:9]])
            print(f"    Top: {row_str}")
            row_str2 = " | ".join([f"{k[:8]}: {v:.0f}%" for k, v in sorted_classes[9:]])
            print(f"    Bot: {row_str2}")

if __name__ == "__main__":
    # Test Level 5 PCs against Lv1 (20%), Lv3 (60%), Lv5 (100%), Lv7 (140%)
    print("\n" + "#" * 100)
    print("LEVEL 5 PLAYER BENCHMARKS")
    print("#" * 100)
    test_tier_matrix(player_level=5, beast_levels=[1, 3, 5, 7], iters=100)

    # Test Level 10 PCs against Lv1 (10%), Lv3 (30%), Lv5 (50%), Lv7 (70%), Lv10 (100%)
    print("\n" + "#" * 100)
    print("LEVEL 10 PLAYER BENCHMARKS")
    print("#" * 100)
    test_tier_matrix(player_level=10, beast_levels=[1, 3, 5, 7, 10], iters=100)

