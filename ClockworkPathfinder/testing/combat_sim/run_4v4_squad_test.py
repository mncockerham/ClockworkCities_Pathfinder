"""
4v4 Team Combat Simulation:
Team A (Raw Firepower / Double Frontline):
- Soldier
- Soldier
- Rifleman
- Merchant (Neither Fire) [+ 2 Retainers]

VS

Team B (Sustained Support & Triage):
- Soldier
- Rifleman
- Merchant (Neither Fire) [+ 2 Retainers]
- Chirurgeon (0-AP Drone Triage, Prophylactic DR 8, 10 Drone Interceptions, Mycological Solvents)

Tested across:
1. Civil Spire
2. High Radiant
3. Low Radiant
4. The Neither
"""

import sys
from pathlib import Path
from collections import defaultdict

sys.path.append(str(Path(__file__).parent))
from run_group_combat_sim import GroupCombatSim

tmpl_dir = Path("ClockworkPathfinder/testing/combat_sim/templates")

team_a_files = [
    str(tmpl_dir / "soldier_lv5.json"),
    str(tmpl_dir / "soldier_lv5.json"),
    str(tmpl_dir / "clockworkrifleman_lv5.json"),
    str(tmpl_dir / "merchant_neitherfire_lv5.json")
]

team_b_files = [
    str(tmpl_dir / "soldier_lv5.json"),
    str(tmpl_dir / "clockworkrifleman_lv5.json"),
    str(tmpl_dir / "merchant_neitherfire_lv5.json"),
    str(tmpl_dir / "chirurgeon_lv5.json")
]

envs = [
    ("civil_spire", "CIVIL SPIRE"),
    ("high_radiant", "HIGH RADIANT"),
    ("low_radiant", "LOW RADIANT"),
    ("the_neither", "THE NEITHER")
]

def run_team_matchups(iterations=200):
    print("=" * 110)
    print("4v4 SQUAD BATTLE: TEAM A (DOUBLE SOLDIER) VS TEAM B (CHIRURGEON SUPPORT)")
    print("Team A: Soldier, Soldier, Rifleman, Merchant_Fire (+2 Retainers)")
    print("Team B: Soldier, Rifleman, Merchant_Fire (+2 Retainers), Chirurgeon")
    print(f"Iterations: {iterations} per environment")
    print("=" * 110)

    for env_code, env_name in envs:
        team_a_wins = 0
        team_b_wins = 0
        tot_rounds = 0
        tot_team_a_hp_pct = 0.0
        tot_team_b_hp_pct = 0.0

        for _ in range(iterations):
            # In our sim, pcs = Team B, enemies = Team A (or vice versa)
            # Let Team B be the PCs (with Chirurgeon support logic) and Team A be the opposing squad
            dist = 20 if env_code == "civil_spire" else 50
            sim = GroupCombatSim(team_b_files, team_a_files, env=env_code, initial_distance=dist)
            res = sim.run_battle()

            tot_rounds += res["rounds"]
            if res["victory"]:
                team_b_wins += 1
                tot_team_b_hp_pct += max(0.0, res["pc_hp_pct"])
            else:
                team_a_wins += 1
                # If enemies won, estimate enemy HP pct
                tot_team_a_hp_pct += 0.35 # Typical survival buffer on close squad wipe

        b_pct = (team_b_wins / iterations) * 100
        a_pct = (team_a_wins / iterations) * 100
        avg_r = tot_rounds / iterations

        winner = "Team B (Chirurgeon Support)" if b_pct > a_pct else "Team A (Double Soldier Firepower)"
        print(f"[{env_name:<13}] -> Team B Wins: {b_pct:5.1f}% | Team A Wins: {a_pct:5.1f}% | Avg Rounds: {avg_r:.1f} | Favored: {winner}")

if __name__ == "__main__":
    run_team_matchups(iterations=200)

