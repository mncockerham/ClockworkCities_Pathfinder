import json
from pathlib import Path

OUT_DIR = Path("ClockworkPathfinder/testing/combat_sim/creatures")
OUT_DIR.mkdir(parents=True, exist_ok=True)

# ==============================================================================
# LEVEL 7 NON-BERSERK (50% HP FLEE) CREATURES
# Calibrated for testing against Level 5 Player Characters (+2 Level Boss / Apex)
# Base Level 7 Stats (PF2e GM Core / Remaster Monster Building Baseline):
#   - Normal Full HP: 95 - 110 HP -> 50% Flee HP: 48 - 55 HP
#   - AC: 24 - 26
#   - Attack Bonus: +16 to +17
#   - Strike Damage: 2d10+7 or 2d8+7 (Deadly traits)
#   - Physical Resistance: 3
# ==============================================================================

LV7_FLEE_CREATURES = {
    # 1. Bear (Brute Template Lv7)
    # Full HP was ~105 HP -> 50% Flee HP = 52 HP
    "bear": {
        "name": "Apex Trench Bear (Lv7 - Flee 50%)",
        "archetype": "BruteBear",
        "level": 7,
        "hp": 52,
        "ac": 24,
        "fort": 16,
        "ref": 12,
        "will": 13,
        "speed": 40,
        "max_ap": 0,
        "status": 0,
        "civil_spire_legal": False,
        "civil_ac_penalty": 0,
        "unarmed_damage_dice": "2d8",
        "unarmed_bonus": 16,
        "unarmed_flat_dmg": 7,
        "unarmed_traits": ["agile"],
        "weapons": [
            {
                "name": "Crushing Jaws",
                "attack_bonus": 16,
                "damage_dice": "2d10",
                "flat_damage": 8,
                "damage_type": "P",
                "range": 0,
                "ap_cost": 0,
                "traits": ["deadly_d10"],
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]
            },
            {
                "name": "Mauling Claws",
                "attack_bonus": 16,
                "damage_dice": "2d8",
                "flat_damage": 7,
                "damage_type": "S",
                "range": 0,
                "ap_cost": 0,
                "traits": ["agile"],
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]
            }
        ],
        "abilities": {
            "damage_resistance_physical": 3
        }
    },

    # 2. Wolf (Stalker Template Lv7)
    # Full HP was ~85 HP -> 50% Flee HP = 42 HP
    "wolf": {
        "name": "Dire Mist Wolf (Lv7 - Flee 50%)",
        "archetype": "StalkerWolf",
        "level": 7,
        "hp": 42,
        "ac": 26,
        "fort": 13,
        "ref": 17,
        "will": 13,
        "speed": 60,
        "max_ap": 0,
        "status": 0,
        "civil_spire_legal": False,
        "civil_ac_penalty": 0,
        "unarmed_damage_dice": "2d6",
        "unarmed_bonus": 17,
        "unarmed_flat_dmg": 6,
        "unarmed_traits": ["agile", "finesse"],
        "weapons": [
            {
                "name": "Serrated Throat Tear",
                "attack_bonus": 17,
                "damage_dice": "2d8",
                "flat_damage": 7,
                "damage_type": "P",
                "range": 0,
                "ap_cost": 0,
                "traits": ["deadly_d10", "finesse"],
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]
            },
            {
                "name": "Flensing Claws",
                "attack_bonus": 17,
                "damage_dice": "2d6",
                "flat_damage": 5,
                "damage_type": "S",
                "range": 0,
                "ap_cost": 0,
                "traits": ["agile", "finesse"],
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]
            }
        ],
        "abilities": {}
    },

    # 3. Scorpion (Venomous Template Lv7)
    # Full HP was ~90 HP -> 50% Flee HP = 45 HP
    "scorpion": {
        "name": "Carapace Dread Scorpion (Lv7 - Flee 50%)",
        "archetype": "VenomousScorpion",
        "level": 7,
        "hp": 45,
        "ac": 26,
        "fort": 15,
        "ref": 14,
        "will": 12,
        "speed": 35,
        "max_ap": 0,
        "status": 0,
        "civil_spire_legal": False,
        "civil_ac_penalty": 0,
        "unarmed_damage_dice": "2d6",
        "unarmed_bonus": 16,
        "unarmed_flat_dmg": 6,
        "unarmed_traits": ["agile"],
        "weapons": [
            {
                "name": "Barbed Neurotoxin Stinger",
                "attack_bonus": 17,
                "damage_dice": "2d8",
                "flat_damage": 8,
                "damage_type": "P",
                "range": 0,
                "ap_cost": 0,
                "traits": ["deadly_d10"],
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]
            },
            {
                "name": "Heavy Vise Pincer",
                "attack_bonus": 16,
                "damage_dice": "2d6",
                "flat_damage": 6,
                "damage_type": "B",
                "range": 0,
                "ap_cost": 0,
                "traits": ["agile"],
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]
            }
        ],
        "abilities": {
            "damage_resistance_physical": 3
        }
    }
}

for key, data in LV7_FLEE_CREATURES.items():
    fn = f"creature_{key}_flee_lv7.json"
    with open(OUT_DIR / fn, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

print(f"Generated 3 Level 7 Non-Berserk Fleeing Creature Templates in {OUT_DIR}")

