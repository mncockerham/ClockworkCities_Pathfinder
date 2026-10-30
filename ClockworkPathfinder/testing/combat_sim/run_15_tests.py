import subprocess
import sys
from pathlib import Path

# 15 Diverse Character vs Character Test Matchups
TEST_MATCHUPS = [
    # Matchup 1: Level 1 Parlor Duel (Civil Master vs High Status Noble)
    ("dandy_lv1.json", "noble_lv1.json", 30, "M01: Lv1 Dandy vs Noble (Civil Parlor Fencing)"),
    
    # Matchup 2: Level 1 Urban Back-Alley (Underworld Survivor vs Civil Pugilist)
    ("survivor_lv1.json", "pugilist_lv1.json", 30, "M02: Lv1 Survivor vs Pugilist (Alley Ambush)"),
    
    # Matchup 3: Level 1 Martial Line (Soldier vs Outland Scout)
    ("soldier_lv1.json", "scout_lv1.json", 40, "M03: Lv1 Soldier vs Scout (Vanguard vs Outrider)"),

    # Matchup 4: Level 5 High Radiant Duel (Scholar vs Clockwork Engineer)
    ("scholar_lv5.json", "clockworkengineer_lv5.json", 50, "M04: Lv5 Scholar vs Engineer (Inductive Arc Siege)"),

    # Matchup 5: Level 5 Airship Skirmish (Sky Captain vs Clockwork Rifleman)
    ("skycaptain_lv5.json", "clockworkrifleman_lv5.json", 60, "M05: Lv5 Sky Captain vs Rifleman (Airship Deck Skirmish)"),

    # Matchup 6: Level 5 Influence Clash (Merchant vs Officer)
    ("merchant_lv5.json", "officer_lv5.json", 40, "M06: Lv5 Merchant vs Officer (Wall Retainers vs Military Retinue)"),

    # Matchup 7: Level 5 Street Investigation (Inspector vs Black Marketeer)
    ("inspector_lv5.json", "blackmarketeer_lv5.json", 30, "M07: Lv5 Inspector vs Black Marketeer (Raid & Shakedown)"),

    # Matchup 8: Level 5 Outland Delve (Artisan vs Chirurgeon)
    ("artisan_lv5.json", "chirurgeon_lv5.json", 40, "M08: Lv5 Artisan vs Chirurgeon (Forge Sledge vs Surgical Acids)"),

    # Matchup 9: Level 5 Demolition & Chaos (Mad Bomber vs Soldier)
    ("madbomber_lv5.json", "soldier_lv5.json", 50, "M09: Lv5 Mad Bomber vs Soldier (Chemical Ordnance vs Heavy Shield)"),

    # Matchup 10: Level 5 Outland Supremacy (Scout vs Pugilist)
    ("scout_lv5.json", "pugilist_lv5.json", 60, "M10: Lv5 Scout vs Pugilist (Ranged Kiting vs Bare-Knuckle Rush)"),

    # Matchup 11: Level 10 Apex Martian Clash (Soldier vs Pugilist)
    ("soldier_lv10.json", "pugilist_lv10.json", 40, "M11: Lv10 Soldier vs Pugilist (Apex Vanguard vs Master Pit Fighter)"),

    # Matchup 12: Level 10 High-Tech vs Sniper (Clockwork Engineer vs Clockwork Rifleman)
    ("clockworkengineer_lv10.json", "clockworkrifleman_lv10.json", 80, "M12: Lv10 Engineer vs Rifleman (Long-Range Grid Siege)"),

    # Matchup 13: Level 10 High Aristocracy vs High Underworld (Noble vs Black Marketeer)
    ("noble_lv10.json", "blackmarketeer_lv10.json", 40, "M13: Lv10 Noble vs Black Marketeer (4 Retainers vs Syndicate Squad)"),

    # Matchup 14: Level 10 Academic Siege vs Outland Hunter (Scholar vs Scout)
    ("scholar_lv10.json", "scout_lv10.json", 80, "M14: Lv10 Scholar vs Scout (Arc Resonator vs Composite Longbow)"),

    # Matchup 15: Level 10 Aerial Duel (Sky Captain vs Officer)
    ("skycaptain_lv10.json", "officer_lv10.json", 50, "M15: Lv10 Sky Captain vs Officer (Swashbuckler Cutlass vs Military Command)")
]

def run_suite():
    tmpl_dir = Path("ClockworkPathfinder/testing/combat_sim/templates")
    sim_script = Path("ClockworkPathfinder/testing/combat_sim/combat_sim.py")

    print("====================================================================")
    print("RUNNING 15 COMPREHENSIVE CHARACTER VS CHARACTER BENCHMARK TESTS")
    print("====================================================================")

    for i, (a_file, b_file, dist, title) in enumerate(TEST_MATCHUPS, 1):
        path_a = tmpl_dir / a_file
        path_b = tmpl_dir / b_file
        
        print(f"\n>>> TEST {i}/15: {title}")
        cmd = [
            sys.executable,
            str(sim_script),
            "--char_a", str(path_a),
            "--char_b", str(path_b),
            "--dist", str(dist),
            "--iters", "100"
        ]
        res = subprocess.run(cmd, capture_output=True, text=True)
        print(res.stdout)

if __name__ == "__main__":
    run_suite()

