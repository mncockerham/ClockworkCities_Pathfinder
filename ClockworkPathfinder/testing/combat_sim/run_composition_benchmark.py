"""
Benchmark Script: Compare Total Rounds Fought and Wave Endurance across 4 Party Compositions:
1. Neither (No Chirurgeon, No Scholar)
2. Chirurgeon Only (With Chirurgeon, No Scholar)
3. Scholar Only (With Scholar, No Chirurgeon)
4. Both (With both Chirurgeon and Scholar)

Runs in both THE_NEITHER and HIGH_RADIANT across Lv 3 and Lv 4 enemy waves at 50% healing (and 0% healing).
Uses the 7/9/10-13 weighted targeting model.
"""

import sys
import random
import json
from pathlib import Path
from collections import defaultdict

SIM_DIR = Path("ClockworkPathfinder/testing/combat_sim")
sys.path.append(str(SIM_DIR))

import run_weighted_targeting_grind as rwg

tmpl_dir = SIM_DIR / "templates"
OTHER_CLASSES = [c for c in rwg.CORE_13_CLASSES if c not in ["chirurgeon", "scholar"]]

def run_composition_experiment(composition_type, env="the_neither", enemy_level=3, heal_pct=0.5, num_trials=300):
    total_waves_cleared = []
    total_rounds_fought = []
    
    for _ in range(num_trials):
        # Build party according to composition_type
        if composition_type == "neither":
            pc_classes = random.sample(OTHER_CLASSES, 4)
        elif composition_type == "chirurgeon_only":
            pc_classes = ["chirurgeon"] + random.sample(OTHER_CLASSES, 3)
        elif composition_type == "scholar_only":
            pc_classes = ["scholar"] + random.sample(OTHER_CLASSES, 3)
        elif composition_type == "both":
            pc_classes = ["chirurgeon", "scholar"] + random.sample(OTHER_CLASSES, 2)
        else:
            raise ValueError(f"Unknown composition {composition_type}")
            
        random.shuffle(pc_classes)
        sim = rwg.GroupCombatSim([str(tmpl_dir / f"{c}_lv5.json") for c in pc_classes], [], env=env)
        pcs = [sim._load_combatant(f, True, 0) for f in sim.pc_files]
        
        waves_won = 0
        cumulative_rounds = 0
        
        while waves_won < 20:
            alive_pcs = [p for p in pcs if p.current_hp > 0]
            if not alive_pcs:
                break
                
            enemy_classes = random.choices(rwg.CORE_13_CLASSES, k=4)
            victory, rounds = rwg.simulate_wave_weighted(pcs, enemy_classes, enemy_level=enemy_level, env=env, dist=50)
            cumulative_rounds += rounds
            
            if victory:
                waves_won += 1
                if heal_pct > 0:
                    for p in pcs:
                        if p.current_hp > 0:
                            p.current_hp = min(p.max_hp, int(p.current_hp + (p.max_hp * heal_pct)))
            else:
                break
                
        total_waves_cleared.append(waves_won)
        total_rounds_fought.append(cumulative_rounds)
        
    avg_waves = sum(total_waves_cleared) / len(total_waves_cleared)
    avg_rounds = sum(total_rounds_fought) / len(total_rounds_fought)
    avg_rounds_per_fight = (avg_rounds / (avg_waves + 1)) if (avg_waves + 1) > 0 else 0
    
    return {
        "avg_waves": avg_waves,
        "avg_rounds": avg_rounds,
        "rounds_per_fight": avg_rounds_per_fight
    }

def main():
    configs = [
        ("THE_NEITHER", 3, 0.5),
        ("THE_NEITHER", 4, 0.5),
        ("HIGH_RADIANT", 3, 0.5),
        ("HIGH_RADIANT", 4, 0.5),
    ]
    
    compositions = ["neither", "chirurgeon_only", "scholar_only", "both"]
    
    print("=" * 105)
    print("SUPPORT COMPOSITION COMBAT ENDURANCE COMPARISON")
    print("Neither vs Chirurgeon Only vs Scholar Only vs Both (300 Trials Per Setup)")
    print("=" * 105)
    
    for zone, lvl, heal in configs:
        print(f"\n>>> ENVIRONMENT: {zone} | ENEMIES: Level {lvl} | HEAL: {int(heal*100)}% <<<")
        print("-" * 105)
        print(f"{'Composition':<22} | {'Avg Waves Cleared':<18} | {'Total Rounds Fought':<22} | {'Rounds / Fight':<16}")
        print("-" * 105)
        
        for comp in compositions:
            res = run_composition_experiment(comp, env=zone.lower(), enemy_level=lvl, heal_pct=heal, num_trials=300)
            comp_label = {
                "neither": "Without Both",
                "chirurgeon_only": "With Chirurgeon Only",
                "scholar_only": "With Scholar Only",
                "both": "With Both (Chir+Sch)"
            }[comp]
            print(f"{comp_label:<22} | {res['avg_waves']:<18.2f} | {res['avg_rounds']:<22.1f} | {res['rounds_per_fight']:<16.2f}")

if __name__ == "__main__":
    main()
