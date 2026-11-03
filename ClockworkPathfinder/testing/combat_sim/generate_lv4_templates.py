"""
Generate Level 4 Templates for all 13 Core Classes + Merchant Variants:
Level 4 stats in PF2e Remaster:
- Level 4 is exactly 1 level below Level 5 (no stat boost tier; Level 5 gives +1 to attack from level, +1 weapon proficiency at Expert, +1 from attribute boosts).
- Attack bonuses: typically -2 relative to Lv 5 (+1 from level, +1 from Expert weapon proficiency or stat boost).
- AC: -1 or -2 relative to Lv 5.
- Saves: -1 relative to Lv 5.
- HP: HP = 8 (ancestry) + (hp_per_lvl + con_mod) * 4.
  * 10 HP classes with +3 CON: 8 + 13*4 = 60 HP (vs 73 at Lv 5).
  * 8 HP classes with +2 CON: 8 + 10*4 = 48 HP (vs 58 at Lv 5).
  * 6 HP classes with +1 CON: 8 + 7*4 = 36 HP (vs 53 at Lv 5).
- Weapons damage dice: striking runes typically occur at level 4 in PF2e (so weapons keep striking 2-dice or 1-dice based on class baseline).
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

def generate_lv4_template(class_name: str):
    f5 = tmpl_dir / f"{class_name}_lv5.json"
    with open(f5, "r", encoding="utf-8") as f:
        d5 = json.load(f)

    # Derive Lv 4
    d4 = dict(d5)
    d4["name"] = d5["name"].replace("Lv5", "Lv4")
    d4["level"] = 4

    # Calculate Level 4 HP
    # Determine hp_per_lvl + con
    # At Lv 5: hp = 8 + 5 * per_lvl => per_lvl = (hp - 8) / 5
    per_lvl = round((d5["hp"] - 8) / 5)
    d4["hp"] = 8 + 4 * per_lvl

    # AC: 1 lower than Lv 5 (since level is 1 lower, same armor proficiency)
    d4["ac"] = d5["ac"] - 1
    if "outland_ac" in d4:
        d4["outland_ac"] = d5["outland_ac"] - 1

    # Saves: 1 lower than Lv 5
    d4["fort"] = d5["fort"] - 1
    d4["ref"] = d5["ref"] - 1
    d4["will"] = d5["will"] - 1

    # Unarmed
    d4["unarmed_bonus"] = max(1, d5.get("unarmed_bonus", 8) - 2)

    # Weapons: attack bonus -2, flat damage -1
    weapons4 = []
    for w in d5.get("weapons", []):
        w4 = dict(w)
        w4["attack_bonus"] = max(1, w.get("attack_bonus", 8) - 2)
        w4["flat_damage"] = max(0, w.get("flat_damage", 2) - 1)
        weapons4.append(w4)
    d4["weapons"] = weapons4

    if "outland_weapons" in d5:
        out_w4 = []
        for w in d5["outland_weapons"]:
            w4 = dict(w)
            w4["attack_bonus"] = max(1, w.get("attack_bonus", 8) - 2)
            w4["flat_damage"] = max(0, w.get("flat_damage", 2) - 1)
            out_w4.append(w4)
        d4["outland_weapons"] = out_w4

    # Abilities scaling for Lv 4
    ab4 = dict(d5.get("abilities", {}))
    if ab4.get("combat_backpack", False):
        ab4["backpack_temp_hp"] = 8 # 2 * Level
        ab4["backpack_turret_bonus"] = max(1, ab4.get("backpack_turret_bonus", 12) - 2)
        ab4["backpack_turret_dice"] = "1d8"
        ab4["backpack_turret_flat"] = 3
    if "damage_resistance_physical" in ab4:
        ab4["damage_resistance_physical"] = max(1, ab4["damage_resistance_physical"] - 1)
    if ab4.get("armed_retainers", False):
        ab4["retainer_count"] = 2
        ab4["retainer_hp"] = 16 # slightly lower at Lv 4
    d4["abilities"] = ab4

    f4 = tmpl_dir / f"{class_name}_lv4.json"
    with open(f4, "w", encoding="utf-8") as f:
        json.dump(d4, f, indent=2)

    print(f"Generated {f4.name}: HP={d4['hp']} (was {d5['hp']}), AC={d4['ac']}, Weapons={len(d4['weapons'])}")

def main():
    print("Generating Level 4 templates...")
    for c in CLASSES_TO_GENERATE:
        generate_lv4_template(c)

if __name__ == "__main__":
    main()

