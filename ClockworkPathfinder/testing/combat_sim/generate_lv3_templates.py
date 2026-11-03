"""
Generate Level 3 Templates for all 13 Core Classes + Merchant Variants:
Level 3 in PF2e Remaster:
- Level 3 vs Level 4:
  * HP: 8 + 3 * per_lvl
  * AC: 1 lower than Lv 4 (or 2 lower than Lv 5)
  * Saves: 1 lower than Lv 4 (or 2 lower than Lv 5)
  * Attack bonus: 1 lower than Lv 4 (or 3 lower than Lv 5)
  * Flat damage: same as Lv 4 or -1
- Retainers: 1 retainer (12 HP) or 2 (12 HP)
- Combat backpack: 6 temp HP, +9 to hit, 1d8+2
"""

import json
from pathlib import Path

tmpl_dir = Path("ClockworkPathfinder/testing/combat_sim/templates")

CLASSES_TO_GENERATE = [
    "soldier",
    "survivor",
    "rake",
    "pugilist",
    "scout",
    "clockworkrifleman",
    "officer",
    "chirurgeon",
    "scholar",
    "greymarketeer",
    "noble",
    "clockworkengineer",
    "merchant_neitherfire",
    "merchant_reflex",
    "merchant_fortitude",
    "merchant_will"
]

def generate_lv3_template(class_name: str):
    f4 = tmpl_dir / f"{class_name}_lv4.json"
    with open(f4, "r", encoding="utf-8") as f:
        d4 = json.load(f)

    d3 = dict(d4)
    d3["name"] = d4["name"].replace("Lv4", "Lv3")
    d3["level"] = 3

    # Calculate Level 3 HP
    # From Lv 4: hp = 8 + 4 * per_lvl => per_lvl = (hp - 8) / 4
    per_lvl = round((d4["hp"] - 8) / 4)
    d3["hp"] = 8 + 3 * per_lvl

    # AC: 1 lower than Lv 4
    d3["ac"] = d4["ac"] - 1
    if "outland_ac" in d3:
        d3["outland_ac"] = d4["outland_ac"] - 1

    # Saves: 1 lower than Lv 4
    d3["fort"] = d4["fort"] - 1
    d3["ref"] = d4["ref"] - 1
    d3["will"] = d4["will"] - 1

    # Unarmed
    d3["unarmed_bonus"] = max(1, d4.get("unarmed_bonus", 6) - 1)

    # Weapons: attack bonus -1 relative to Lv 4
    weapons3 = []
    for w in d4.get("weapons", []):
        w3 = dict(w)
        w3["attack_bonus"] = max(1, w.get("attack_bonus", 6) - 1)
        weapons3.append(w3)
    d3["weapons"] = weapons3

    if "outland_weapons" in d4:
        out_w3 = []
        for w in d4["outland_weapons"]:
            w3 = dict(w)
            w3["attack_bonus"] = max(1, w.get("attack_bonus", 6) - 1)
            out_w3.append(w3)
        d3["outland_weapons"] = out_w3

    # Abilities scaling for Lv 3
    ab3 = dict(d4.get("abilities", {}))
    if ab3.get("combat_backpack", False):
        ab3["backpack_temp_hp"] = 6 # 2 * Level
        ab3["backpack_turret_bonus"] = max(1, ab3.get("backpack_turret_bonus", 10) - 1)
        ab3["backpack_turret_dice"] = "1d8"
        ab3["backpack_turret_flat"] = 2
    if ab3.get("armed_retainers", False):
        ab3["retainer_count"] = 2
        ab3["retainer_hp"] = 12
    d3["abilities"] = ab3

    f3 = tmpl_dir / f"{class_name}_lv3.json"
    with open(f3, "w", encoding="utf-8") as f:
        json.dump(d3, f, indent=2)

    print(f"Generated {f3.name}: HP={d3['hp']} (was {d4['hp']}), AC={d3['ac']}, Weapons={len(d3['weapons'])}")

def main():
    print("Generating Level 3 templates...")
    for c in CLASSES_TO_GENERATE:
        generate_lv3_template(c)

if __name__ == "__main__":
    main()

