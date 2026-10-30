import json
from pathlib import Path

# Directories
OUT_DIR = Path("ClockworkPathfinder/testing/combat_sim/creatures")
OUT_DIR.mkdir(parents=True, exist_ok=True)

# ==============================================================================
# BASELINE MONSTER STAT PROGRESSIONS (Levels 1, 3, 5, 7, 10)
# PF2e Remaster Monster Building Rules [GM Core / Remaster]:
#
# Level 1:
#   Bear (Brute): HP 22, AC 15, Fort +8, Ref +5, Will +5, Spd 35, Atk +7 (1d8+3 / 1d6+3), Res 1
#   Wolf (Stalker): HP 16, AC 16, Fort +6, Ref +8, Will +5, Spd 45, Atk +8 (1d6+3 / 1d4+2)
#   Scorpion (Venom): HP 18, AC 16, Fort +7, Ref +6, Will +4, Spd 30, Atk +7 (1d6+3 / 1d6+2), Res 1
#
# Level 3:
#   Bear (Brute): HP 45, AC 18, Fort +11, Ref +7, Will +8, Spd 35, Atk +11 (2d8+4 / 2d6+4), Res 2
#   Wolf (Stalker): HP 34, AC 20, Fort +8, Ref +11, Will +8, Spd 50, Atk +11 (2d6+4 / 2d4+3)
#   Scorpion (Venom): HP 38, AC 19, Fort +10, Ref +9, Will +7, Spd 35, Atk +11 (2d6+4 / 2d6+3), Res 2
#
# Level 5:
#   Bear (Brute): HP 65, AC 21, Fort +13, Ref +9, Will +10, Spd 40, Atk +13 (2d8+6 / 2d6+5), Res 2
#   Wolf (Stalker): HP 52, AC 23, Fort +10, Ref +14, Will +10, Spd 55, Atk +14 (2d6+5 / 2d4+4)
#   Scorpion (Venom): HP 55, AC 23, Fort +12, Ref +11, Will +9, Spd 35, Atk +14 (2d6+6 / 2d6+4), Res 2
#
# Level 7:
#   Bear (Brute): HP 104, AC 24, Fort +16, Ref +12, Will +13, Spd 40, Atk +16 (2d10+8 / 2d8+7), Res 3
#   Wolf (Stalker): HP 84, AC 26, Fort +13, Ref +17, Will +13, Spd 60, Atk +17 (2d8+7 / 2d6+6)
#   Scorpion (Venom): HP 90, AC 26, Fort +15, Ref +14, Will +12, Spd 40, Atk +16 (2d8+8 / 2d6+6), Res 3
#
# Level 10:
#   Bear (Brute): HP 135, AC 29, Fort +20, Ref +16, Will +17, Spd 45, Atk +20 (3d8+9 / 3d6+8), Res 4
#   Wolf (Stalker): HP 115, AC 31, Fort +17, Ref +22, Will +17, Spd 65, Atk +22 (3d6+9 / 3d4+7)
#   Scorpion (Venom): HP 125, AC 31, Fort +19, Ref +18, Will +16, Spd 40, Atk +22 (3d6+10 / 3d6+7), Res 4
# ==============================================================================

CREATURE_SPECS = {
    "bear": {
        "archetype": "BruteBear",
        "name_prefix": "Bear",
        "levels": {
            1: {
                "name": "Black Bear",
                "hp": 22, "ac": 15, "fort": 8, "ref": 5, "will": 5, "speed": 35,
                "unarmed_dice": "1d6", "unarmed_bonus": 7, "unarmed_flat": 3,
                "weapons": [
                    {"name": "Feral Jaws", "attack_bonus": 7, "damage_dice": "1d8", "flat_damage": 3, "damage_type": "P", "range": 0, "ap_cost": 0, "traits": [], "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]},
                    {"name": "Heavy Claws", "attack_bonus": 7, "damage_dice": "1d6", "flat_damage": 3, "damage_type": "S", "range": 0, "ap_cost": 0, "traits": ["agile"], "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]}
                ],
                "resistance": 1
            },
            3: {
                "name": "Cave Bear",
                "hp": 45, "ac": 18, "fort": 11, "ref": 7, "will": 8, "speed": 35,
                "unarmed_dice": "2d6", "unarmed_bonus": 11, "unarmed_flat": 4,
                "weapons": [
                    {"name": "Crushing Jaws", "attack_bonus": 11, "damage_dice": "2d8", "flat_damage": 5, "damage_type": "P", "range": 0, "ap_cost": 0, "traits": ["deadly_d8"], "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]},
                    {"name": "Mauling Claws", "attack_bonus": 11, "damage_dice": "2d6", "flat_damage": 4, "damage_type": "S", "range": 0, "ap_cost": 0, "traits": ["agile"], "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]}
                ],
                "resistance": 2
            },
            5: {
                "name": "Sump Brown Bear",
                "hp": 65, "ac": 21, "fort": 13, "ref": 9, "will": 10, "speed": 40,
                "unarmed_dice": "2d6", "unarmed_bonus": 13, "unarmed_flat": 5,
                "weapons": [
                    {"name": "Crushing Jaws", "attack_bonus": 13, "damage_dice": "2d8", "flat_damage": 6, "damage_type": "P", "range": 0, "ap_cost": 0, "traits": ["deadly_d8"], "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]},
                    {"name": "Mauling Claws", "attack_bonus": 13, "damage_dice": "2d6", "flat_damage": 5, "damage_type": "S", "range": 0, "ap_cost": 0, "traits": ["agile"], "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]}
                ],
                "resistance": 2
            },
            7: {
                "name": "Apex Trench Bear",
                "hp": 104, "ac": 24, "fort": 16, "ref": 12, "will": 13, "speed": 40,
                "unarmed_dice": "2d8", "unarmed_bonus": 16, "unarmed_flat": 7,
                "weapons": [
                    {"name": "Crushing Jaws", "attack_bonus": 16, "damage_dice": "2d10", "flat_damage": 8, "damage_type": "P", "range": 0, "ap_cost": 0, "traits": ["deadly_d10"], "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]},
                    {"name": "Mauling Claws", "attack_bonus": 16, "damage_dice": "2d8", "flat_damage": 7, "damage_type": "S", "range": 0, "ap_cost": 0, "traits": ["agile"], "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]}
                ],
                "resistance": 3
            },
            10: {
                "name": "Neither Grizzly",
                "hp": 135, "ac": 29, "fort": 20, "ref": 16, "will": 17, "speed": 45,
                "unarmed_dice": "3d6", "unarmed_bonus": 20, "unarmed_flat": 8,
                "weapons": [
                    {"name": "Grizzly Jaws", "attack_bonus": 20, "damage_dice": "3d8", "flat_damage": 9, "damage_type": "P", "range": 0, "ap_cost": 0, "traits": ["deadly_d10"], "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]},
                    {"name": "Grizzly Claws", "attack_bonus": 20, "damage_dice": "3d6", "flat_damage": 8, "damage_type": "S", "range": 0, "ap_cost": 0, "traits": ["agile"], "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]}
                ],
                "resistance": 4
            }
        }
    },
    "wolf": {
        "archetype": "StalkerWolf",
        "name_prefix": "Wolf",
        "levels": {
            1: {
                "name": "Feral Wolf",
                "hp": 16, "ac": 16, "fort": 6, "ref": 8, "will": 5, "speed": 45,
                "unarmed_dice": "1d4", "unarmed_bonus": 8, "unarmed_flat": 2,
                "weapons": [
                    {"name": "Serrated Bite", "attack_bonus": 8, "damage_dice": "1d6", "flat_damage": 3, "damage_type": "P", "range": 0, "ap_cost": 0, "traits": ["deadly_d8", "finesse"], "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]},
                    {"name": "Quick Claws", "attack_bonus": 8, "damage_dice": "1d4", "flat_damage": 2, "damage_type": "S", "range": 0, "ap_cost": 0, "traits": ["agile", "finesse"], "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]}
                ],
                "resistance": 0
            },
            3: {
                "name": "Timber Wolf",
                "hp": 34, "ac": 20, "fort": 8, "ref": 11, "will": 8, "speed": 50,
                "unarmed_dice": "2d4", "unarmed_bonus": 11, "unarmed_flat": 3,
                "weapons": [
                    {"name": "Throat Bite", "attack_bonus": 11, "damage_dice": "2d6", "flat_damage": 4, "damage_type": "P", "range": 0, "ap_cost": 0, "traits": ["deadly_d8", "finesse"], "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]},
                    {"name": "Rake Claws", "attack_bonus": 11, "damage_dice": "2d4", "flat_damage": 3, "damage_type": "S", "range": 0, "ap_cost": 0, "traits": ["agile", "finesse"], "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]}
                ],
                "resistance": 0
            },
            5: {
                "name": "Dusk Stalker Wolf",
                "hp": 52, "ac": 23, "fort": 10, "ref": 14, "will": 10, "speed": 55,
                "unarmed_dice": "2d4", "unarmed_bonus": 14, "unarmed_flat": 4,
                "weapons": [
                    {"name": "Throat-Ripper Bite", "attack_bonus": 14, "damage_dice": "2d6", "flat_damage": 5, "damage_type": "P", "range": 0, "ap_cost": 0, "traits": ["deadly_d8", "finesse"], "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]},
                    {"name": "Flensing Claws", "attack_bonus": 14, "damage_dice": "2d4", "flat_damage": 4, "damage_type": "S", "range": 0, "ap_cost": 0, "traits": ["agile", "finesse"], "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]}
                ],
                "resistance": 0
            },
            7: {
                "name": "Dire Mist Wolf",
                "hp": 84, "ac": 26, "fort": 13, "ref": 17, "will": 13, "speed": 60,
                "unarmed_dice": "2d6", "unarmed_bonus": 17, "unarmed_flat": 6,
                "weapons": [
                    {"name": "Serrated Throat Tear", "attack_bonus": 17, "damage_dice": "2d8", "flat_damage": 7, "damage_type": "P", "range": 0, "ap_cost": 0, "traits": ["deadly_d10", "finesse"], "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]},
                    {"name": "Eviscerating Claws", "attack_bonus": 17, "damage_dice": "2d6", "flat_damage": 6, "damage_type": "S", "range": 0, "ap_cost": 0, "traits": ["agile", "finesse"], "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]}
                ],
                "resistance": 0
            },
            10: {
                "name": "Shadow Alpha Wolf",
                "hp": 115, "ac": 31, "fort": 17, "ref": 22, "will": 17, "speed": 65,
                "unarmed_dice": "3d4", "unarmed_bonus": 22, "unarmed_flat": 7,
                "weapons": [
                    {"name": "Apex Throat-Tearer", "attack_bonus": 22, "damage_dice": "3d6", "flat_damage": 9, "damage_type": "P", "range": 0, "ap_cost": 0, "traits": ["deadly_d10", "finesse"], "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]},
                    {"name": "Tendon Rake Claws", "attack_bonus": 22, "damage_dice": "3d4", "flat_damage": 7, "damage_type": "S", "range": 0, "ap_cost": 0, "traits": ["agile", "finesse"], "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]}
                ],
                "resistance": 0
            }
        }
    },
    "scorpion": {
        "archetype": "VenomousScorpion",
        "name_prefix": "Scorpion",
        "levels": {
            1: {
                "name": "Trench Scorpion",
                "hp": 18, "ac": 16, "fort": 7, "ref": 6, "will": 4, "speed": 30,
                "unarmed_dice": "1d4", "unarmed_bonus": 6, "unarmed_flat": 2,
                "weapons": [
                    {"name": "Envenomed Stinger", "attack_bonus": 7, "damage_dice": "1d6", "flat_damage": 3, "damage_type": "P", "range": 0, "ap_cost": 0, "traits": ["deadly_d8"], "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]},
                    {"name": "Chitinous Pincer", "attack_bonus": 6, "damage_dice": "1d6", "flat_damage": 2, "damage_type": "B", "range": 0, "ap_cost": 0, "traits": ["agile"], "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]}
                ],
                "resistance": 1
            },
            3: {
                "name": "Barbed Trench Scorpion",
                "hp": 38, "ac": 19, "fort": 10, "ref": 9, "will": 7, "speed": 35,
                "unarmed_dice": "2d4", "unarmed_bonus": 10, "unarmed_flat": 3,
                "weapons": [
                    {"name": "Venomous Stinger", "attack_bonus": 11, "damage_dice": "2d6", "flat_damage": 4, "damage_type": "P", "range": 0, "ap_cost": 0, "traits": ["deadly_d8"], "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]},
                    {"name": "Vise Pincers", "attack_bonus": 10, "damage_dice": "2d4", "flat_damage": 3, "damage_type": "B", "range": 0, "ap_cost": 0, "traits": ["agile"], "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]}
                ],
                "resistance": 2
            },
            5: {
                "name": "Spore-Barbed Scorpion",
                "hp": 55, "ac": 23, "fort": 12, "ref": 11, "will": 9, "speed": 35,
                "unarmed_dice": "2d4", "unarmed_bonus": 13, "unarmed_flat": 4,
                "weapons": [
                    {"name": "Virulent Neurotoxin Stinger", "attack_bonus": 14, "damage_dice": "2d6", "flat_damage": 6, "damage_type": "P", "range": 0, "ap_cost": 0, "traits": ["deadly_d10"], "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]},
                    {"name": "Vise Pincers", "attack_bonus": 13, "damage_dice": "2d6", "flat_damage": 4, "damage_type": "B", "range": 0, "ap_cost": 0, "traits": ["agile"], "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]}
                ],
                "resistance": 2
            },
            7: {
                "name": "Dread Spore Scorpion",
                "hp": 90, "ac": 26, "fort": 15, "ref": 14, "will": 12, "speed": 40,
                "unarmed_dice": "2d6", "unarmed_bonus": 16, "unarmed_flat": 6,
                "weapons": [
                    {"name": "Apex Neurotoxin Stinger", "attack_bonus": 16, "damage_dice": "2d8", "flat_damage": 8, "damage_type": "P", "range": 0, "ap_cost": 0, "traits": ["deadly_d10"], "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]},
                    {"name": "Crushing Pincers", "attack_bonus": 16, "damage_dice": "2d6", "flat_damage": 6, "damage_type": "B", "range": 0, "ap_cost": 0, "traits": ["agile"], "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]}
                ],
                "resistance": 3
            },
            10: {
                "name": "Titan Neither Scorpion",
                "hp": 125, "ac": 31, "fort": 19, "ref": 18, "will": 16, "speed": 40,
                "unarmed_dice": "3d4", "unarmed_bonus": 21, "unarmed_flat": 7,
                "weapons": [
                    {"name": "Apex Necrotic Stinger", "attack_bonus": 22, "damage_dice": "3d6", "flat_damage": 10, "damage_type": "P", "range": 0, "ap_cost": 0, "traits": ["deadly_d12"], "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]},
                    {"name": "Crushing Titan Pincers", "attack_bonus": 21, "damage_dice": "3d6", "flat_damage": 7, "damage_type": "B", "range": 0, "ap_cost": 0, "traits": ["agile"], "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]}
                ],
                "resistance": 4
            }
        }
    }
}

def build_templates():
    LEVELS = [1, 3, 5, 7, 10]
    created = []

    for beast_key, beast_info in CREATURE_SPECS.items():
        for lvl in LEVELS:
            stat = beast_info["levels"][lvl]
            abilities_berserk = {}
            if stat["resistance"] > 0:
                abilities_berserk["damage_resistance_physical"] = stat["resistance"]

            # 1. BERSERK (Full HP)
            berserk_data = {
                "name": f"{stat['name']} (Lv{lvl} - Berserk)",
                "archetype": beast_info["archetype"],
                "level": lvl,
                "hp": stat["hp"],
                "ac": stat["ac"],
                "fort": stat["fort"],
                "ref": stat["ref"],
                "will": stat["will"],
                "speed": stat["speed"],
                "max_ap": 0,
                "status": 0,
                "civil_spire_legal": False,
                "civil_ac_penalty": 0,
                "unarmed_damage_dice": stat["unarmed_dice"],
                "unarmed_bonus": stat["unarmed_bonus"],
                "unarmed_flat_dmg": stat["unarmed_flat"],
                "unarmed_traits": ["agile"],
                "weapons": stat["weapons"],
                "abilities": abilities_berserk
            }

            berserk_filename = f"creature_{beast_key}_lv{lvl}.json"
            with open(OUT_DIR / berserk_filename, "w", encoding="utf-8") as f:
                json.dump(berserk_data, f, indent=2)
            created.append(berserk_filename)

            # 2. FLEE (1/2 HP threshold)
            abilities_flee = dict(abilities_berserk)
            flee_hp = max(1, stat["hp"] // 2)

            flee_data = {
                "name": f"{stat['name']} (Lv{lvl} - Flee 50%)",
                "archetype": beast_info["archetype"],
                "level": lvl,
                "hp": flee_hp,
                "ac": stat["ac"],
                "fort": stat["fort"],
                "ref": stat["ref"],
                "will": stat["will"],
                "speed": stat["speed"],
                "max_ap": 0,
                "status": 0,
                "civil_spire_legal": False,
                "civil_ac_penalty": 0,
                "unarmed_damage_dice": stat["unarmed_dice"],
                "unarmed_bonus": stat["unarmed_bonus"],
                "unarmed_flat_dmg": stat["unarmed_flat"],
                "unarmed_traits": ["agile"],
                "weapons": stat["weapons"],
                "abilities": abilities_flee
            }

            flee_filename = f"creature_{beast_key}_flee_lv{lvl}.json"
            with open(OUT_DIR / flee_filename, "w", encoding="utf-8") as f:
                json.dump(flee_data, f, indent=2)
            created.append(flee_filename)

    print(f"Successfully generated {len(created)} creature templates across Levels 1, 3, 5, 7, 10 in {OUT_DIR}:")
    for f in created:
        print(f"  - {f}")

if __name__ == "__main__":
    build_templates()

