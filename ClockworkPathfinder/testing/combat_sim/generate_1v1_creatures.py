import json
from pathlib import Path

# ==============================================================================
# 1v1 CALIBRATED CREATURE TEMPLATES (Player Level = Target Level)
# Goal: Provide a close, challenging fight where a prepared player character 
# wins slightly more often than they lose (~55% to 65% PC win rate).
# ==============================================================================

OUT_DIR = Path("ClockworkPathfinder/testing/combat_sim/creatures")
OUT_DIR.mkdir(parents=True, exist_ok=True)

# ------------------------------------------------------------------------------
# 1. CALIBRATED BEARS (Brute Template tuned for 1v1)
# High HP, moderate AC, heavy physical hits, damage resistance
# ------------------------------------------------------------------------------
CALIBRATED_BEARS = {
    1: {
        "name": "Fringe Black Bear (1v1 Lv1)",
        "archetype": "BruteBear",
        "level": 1,
        "hp": 22,
        "ac": 15,
        "fort": 8,
        "ref": 5,
        "will": 5,
        "speed": 35,
        "max_ap": 0,
        "status": 0,
        "civil_spire_legal": False,
        "civil_ac_penalty": 0,
        "unarmed_damage_dice": "1d6",
        "unarmed_bonus": 7,
        "unarmed_flat_dmg": 3,
        "unarmed_traits": ["agile"],
        "weapons": [
            {
                "name": "Feral Jaws",
                "attack_bonus": 7,
                "damage_dice": "1d8",
                "flat_damage": 3,
                "damage_type": "P",
                "range": 0,
                "ap_cost": 0,
                "traits": [],
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]
            },
            {
                "name": "Heavy Claws",
                "attack_bonus": 7,
                "damage_dice": "1d6",
                "flat_damage": 3,
                "damage_type": "S",
                "range": 0,
                "ap_cost": 0,
                "traits": ["agile"],
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]
            }
        ],
        "abilities": {
            "damage_resistance_physical": 1
        }
    },
    5: {
        "name": "Sump Brown Bear (1v1 Lv5)",
        "archetype": "BruteBear",
        "level": 5,
        "hp": 65,
        "ac": 21,
        "fort": 13,
        "ref": 9,
        "will": 10,
        "speed": 40,
        "max_ap": 0,
        "status": 0,
        "civil_spire_legal": False,
        "civil_ac_penalty": 0,
        "unarmed_damage_dice": "2d6",
        "unarmed_bonus": 13,
        "unarmed_flat_dmg": 5,
        "unarmed_traits": ["agile"],
        "weapons": [
            {
                "name": "Crushing Jaws",
                "attack_bonus": 13,
                "damage_dice": "2d8",
                "flat_damage": 6,
                "damage_type": "P",
                "range": 0,
                "ap_cost": 0,
                "traits": ["deadly_d8"],
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]
            },
            {
                "name": "Mauling Claws",
                "attack_bonus": 13,
                "damage_dice": "2d6",
                "flat_damage": 5,
                "damage_type": "S",
                "range": 0,
                "ap_cost": 0,
                "traits": ["agile"],
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]
            }
        ],
        "abilities": {
            "damage_resistance_physical": 2
        }
    },
    10: {
        "name": "Neither Grizzly (1v1 Lv10)",
        "archetype": "BruteBear",
        "level": 10,
        "hp": 135,
        "ac": 29,
        "fort": 20,
        "ref": 16,
        "will": 17,
        "speed": 45,
        "max_ap": 0,
        "status": 0,
        "civil_spire_legal": False,
        "civil_ac_penalty": 0,
        "unarmed_damage_dice": "3d6",
        "unarmed_bonus": 20,
        "unarmed_flat_dmg": 8,
        "unarmed_traits": ["agile"],
        "weapons": [
            {
                "name": "Grizzly Jaws",
                "attack_bonus": 20,
                "damage_dice": "3d8",
                "flat_damage": 9,
                "damage_type": "P",
                "range": 0,
                "ap_cost": 0,
                "traits": ["deadly_d10"],
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]
            },
            {
                "name": "Grizzly Claws",
                "attack_bonus": 20,
                "damage_dice": "3d6",
                "flat_damage": 8,
                "damage_type": "S",
                "range": 0,
                "ap_cost": 0,
                "traits": ["agile"],
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]
            }
        ],
        "abilities": {
            "damage_resistance_physical": 4
        }
    }
}

# ------------------------------------------------------------------------------
# 2. CALIBRATED WOLVES (Stalker Template tuned for 1v1)
# Fast sprint, high Reflex/AC, precision throat bite, low HP
# ------------------------------------------------------------------------------
CALIBRATED_WOLVES = {
    1: {
        "name": "Feral Wolf (1v1 Lv1)",
        "archetype": "StalkerWolf",
        "level": 1,
        "hp": 16,
        "ac": 16,
        "fort": 6,
        "ref": 8,
        "will": 5,
        "speed": 45,
        "max_ap": 0,
        "status": 0,
        "civil_spire_legal": False,
        "civil_ac_penalty": 0,
        "unarmed_damage_dice": "1d4",
        "unarmed_bonus": 8,
        "unarmed_flat_dmg": 2,
        "unarmed_traits": ["agile", "finesse"],
        "weapons": [
            {
                "name": "Serrated Bite",
                "attack_bonus": 8,
                "damage_dice": "1d6",
                "flat_damage": 3,
                "damage_type": "P",
                "range": 0,
                "ap_cost": 0,
                "traits": ["deadly_d8", "finesse"],
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]
            },
            {
                "name": "Quick Claws",
                "attack_bonus": 8,
                "damage_dice": "1d4",
                "flat_damage": 2,
                "damage_type": "S",
                "range": 0,
                "ap_cost": 0,
                "traits": ["agile", "finesse"],
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]
            }
        ],
        "abilities": {}
    },
    5: {
        "name": "Dusk Stalker Wolf (1v1 Lv5)",
        "archetype": "StalkerWolf",
        "level": 5,
        "hp": 52,
        "ac": 23,
        "fort": 10,
        "ref": 14,
        "will": 10,
        "speed": 55,
        "max_ap": 0,
        "status": 0,
        "civil_spire_legal": False,
        "civil_ac_penalty": 0,
        "unarmed_damage_dice": "2d4",
        "unarmed_bonus": 14,
        "unarmed_flat_dmg": 4,
        "unarmed_traits": ["agile", "finesse"],
        "weapons": [
            {
                "name": "Throat-Ripper Bite",
                "attack_bonus": 14,
                "damage_dice": "2d6",
                "flat_damage": 5,
                "damage_type": "P",
                "range": 0,
                "ap_cost": 0,
                "traits": ["deadly_d8", "finesse"],
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]
            },
            {
                "name": "Flensing Claws",
                "attack_bonus": 14,
                "damage_dice": "2d4",
                "flat_damage": 4,
                "damage_type": "S",
                "range": 0,
                "ap_cost": 0,
                "traits": ["agile", "finesse"],
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]
            }
        ],
        "abilities": {}
    },
    10: {
        "name": "Shadow Alpha Wolf (1v1 Lv10)",
        "archetype": "StalkerWolf",
        "level": 10,
        "hp": 115,
        "ac": 31,
        "fort": 17,
        "ref": 22,
        "will": 17,
        "speed": 65,
        "max_ap": 0,
        "status": 0,
        "civil_spire_legal": False,
        "civil_ac_penalty": 0,
        "unarmed_damage_dice": "3d4",
        "unarmed_bonus": 22,
        "unarmed_flat_dmg": 7,
        "unarmed_traits": ["agile", "finesse"],
        "weapons": [
            {
                "name": "Apex Throat-Tearer",
                "attack_bonus": 22,
                "damage_dice": "3d6",
                "flat_damage": 9,
                "damage_type": "P",
                "range": 0,
                "ap_cost": 0,
                "traits": ["deadly_d10", "finesse"],
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]
            },
            {
                "name": "Tendon Rake Claws",
                "attack_bonus": 22,
                "damage_dice": "3d4",
                "flat_damage": 7,
                "damage_type": "S",
                "range": 0,
                "ap_cost": 0,
                "traits": ["agile", "finesse"],
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]
            }
        ],
        "abilities": {}
    }
}

# ------------------------------------------------------------------------------
# 3. CALIBRATED SCORPIONS (Venomous Template tuned for 1v1)
# Armored chitin (+Hardness/AC), pincer grapples, barbed venomous stinger
# ------------------------------------------------------------------------------
CALIBRATED_SCORPIONS = {
    1: {
        "name": "Trench Scorpion (1v1 Lv1)",
        "archetype": "VenomousScorpion",
        "level": 1,
        "hp": 18,
        "ac": 16,
        "fort": 7,
        "ref": 6,
        "will": 4,
        "speed": 30,
        "max_ap": 0,
        "status": 0,
        "civil_spire_legal": False,
        "civil_ac_penalty": 0,
        "unarmed_damage_dice": "1d4",
        "unarmed_bonus": 6,
        "unarmed_flat_dmg": 2,
        "unarmed_traits": ["agile"],
        "weapons": [
            {
                "name": "Envenomed Stinger",
                "attack_bonus": 7,
                "damage_dice": "1d6",
                "flat_damage": 3,  # Piercing + Stage 1 poison
                "damage_type": "P",
                "range": 0,
                "ap_cost": 0,
                "traits": ["deadly_d8"],
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]
            },
            {
                "name": "Chitinous Pincer",
                "attack_bonus": 6,
                "damage_dice": "1d6",
                "flat_damage": 2,
                "damage_type": "B",
                "range": 0,
                "ap_cost": 0,
                "traits": ["agile"],
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]
            }
        ],
        "abilities": {
            "damage_resistance_physical": 1
        }
    },
    5: {
        "name": "Spore-Barbed Scorpion (1v1 Lv5)",
        "archetype": "VenomousScorpion",
        "level": 5,
        "hp": 55,
        "ac": 23,
        "fort": 12,
        "ref": 11,
        "will": 9,
        "speed": 35,
        "max_ap": 0,
        "status": 0,
        "civil_spire_legal": False,
        "civil_ac_penalty": 0,
        "unarmed_damage_dice": "2d4",
        "unarmed_bonus": 13,
        "unarmed_flat_dmg": 4,
        "unarmed_traits": ["agile"],
        "weapons": [
            {
                "name": "Virulent Neurotoxin Stinger",
                "attack_bonus": 14,
                "damage_dice": "2d6",
                "flat_damage": 6,  # Piercing + Stage 2 neurotoxin
                "damage_type": "P",
                "range": 0,
                "ap_cost": 0,
                "traits": ["deadly_d10"],
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]
            },
            {
                "name": "Vise Pincers",
                "attack_bonus": 13,
                "damage_dice": "2d6",
                "flat_damage": 4,
                "damage_type": "B",
                "range": 0,
                "ap_cost": 0,
                "traits": ["agile"],
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]
            }
        ],
        "abilities": {
            "damage_resistance_physical": 2
        }
    },
    10: {
        "name": "Titan Neither Scorpion (1v1 Lv10)",
        "archetype": "VenomousScorpion",
        "level": 10,
        "hp": 125,
        "ac": 31,
        "fort": 19,
        "ref": 18,
        "will": 16,
        "speed": 40,
        "max_ap": 0,
        "status": 0,
        "civil_spire_legal": False,
        "civil_ac_penalty": 0,
        "unarmed_damage_dice": "3d4",
        "unarmed_bonus": 21,
        "unarmed_flat_dmg": 7,
        "unarmed_traits": ["agile"],
        "weapons": [
            {
                "name": "Apex Necrotic Stinger",
                "attack_bonus": 22,
                "damage_dice": "3d6",
                "flat_damage": 10,  # Piercing + Stage 3 necrotic poison
                "damage_type": "P",
                "range": 0,
                "ap_cost": 0,
                "traits": ["deadly_d12"],
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]
            },
            {
                "name": "Crushing Titan Pincers",
                "attack_bonus": 21,
                "damage_dice": "3d6",
                "flat_damage": 7,
                "damage_type": "B",
                "range": 0,
                "ap_cost": 0,
                "traits": ["agile"],
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]
            }
        ],
        "abilities": {
            "damage_resistance_physical": 4
        }
    }
}

def generate_1v1_creatures():
    for lvl, data in CALIBRATED_BEARS.items():
        fn = f"creature_bear_lv{lvl}.json"
        with open(OUT_DIR / fn, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    for lvl, data in CALIBRATED_WOLVES.items():
        fn = f"creature_wolf_lv{lvl}.json"
        with open(OUT_DIR / fn, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    for lvl, data in CALIBRATED_SCORPIONS.items():
        fn = f"creature_scorpion_lv{lvl}.json"
        with open(OUT_DIR / fn, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    print(f"Generated 9 Calibrated 1v1 Creature Templates (Bear, Wolf, Scorpion at Lv1, Lv5, Lv10) in {OUT_DIR}")

if __name__ == "__main__":
    generate_1v1_creatures()

