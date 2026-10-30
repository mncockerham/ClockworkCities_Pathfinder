import json
from pathlib import Path

OUT_DIR = Path("ClockworkPathfinder/testing/combat_sim/creatures")
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Generate Non-Berserk (50% HP threshold) creatures for Lv5 and Lv10
# When a creature has 50% HP in the sim, its effective fight duration 
# models fleeing as soon as it hits Bloodied threshold.

LEVELS = [5, 10]

for lvl in LEVELS:
    # 1. Bear (Original: Lv5=65 HP -> Flee=33 HP; Lv10=135 HP -> Flee=68 HP)
    bear_orig_path = OUT_DIR / f"creature_bear_lv{lvl}.json"
    with open(bear_orig_path, "r", encoding="utf-8") as f:
        bear_data = json.load(f)
    
    bear_data["name"] = f"Fleeing Bear (50% HP Lv{lvl})"
    bear_data["hp"] = max(1, bear_data["hp"] // 2)
    with open(OUT_DIR / f"creature_bear_flee_lv{lvl}.json", "w", encoding="utf-8") as f:
        json.dump(bear_data, f, indent=2)

    # 2. Wolf (Original: Lv5=52 HP -> Flee=26 HP; Lv10=115 HP -> Flee=58 HP)
    wolf_orig_path = OUT_DIR / f"creature_wolf_lv{lvl}.json"
    with open(wolf_orig_path, "r", encoding="utf-8") as f:
        wolf_data = json.load(f)
        
    wolf_data["name"] = f"Fleeing Wolf (50% HP Lv{lvl})"
    wolf_data["hp"] = max(1, wolf_data["hp"] // 2)
    with open(OUT_DIR / f"creature_wolf_flee_lv{lvl}.json", "w", encoding="utf-8") as f:
        json.dump(wolf_data, f, indent=2)

    # 3. Scorpion (Original: Lv5=55 HP -> Flee=28 HP; Lv10=125 HP -> Flee=63 HP)
    scorp_orig_path = OUT_DIR / f"creature_scorpion_lv{lvl}.json"
    with open(scorp_orig_path, "r", encoding="utf-8") as f:
        scorp_data = json.load(f)
        
    scorp_data["name"] = f"Fleeing Scorpion (50% HP Lv{lvl})"
    scorp_data["hp"] = max(1, scorp_data["hp"] // 2)
    with open(OUT_DIR / f"creature_scorpion_flee_lv{lvl}.json", "w", encoding="utf-8") as f:
        json.dump(scorp_data, f, indent=2)

print("Generated 6 Non-Berserk (50% HP Flee threshold) creature templates for Lv5 and Lv10.")

