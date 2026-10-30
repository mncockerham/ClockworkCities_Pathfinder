import json
from pathlib import Path

OUT_DIR = Path("ClockworkPathfinder/testing/combat_sim/creatures")
OUT_DIR.mkdir(parents=True, exist_ok=True)

# ==============================================================================
# SPECIAL SAVE-BASED EXOTIC CREATURE TEMPLATES
#
# 1. Acid Spitter (Reflex / Dex save - Full/Half/None/Double Acid Damage)
#    - Archetype: AcidSpitter
#    - Save: Reflex / Dex DC
#    - Type: Acid
#
# 2. Spore Sprayer (Fortitude / Con save - Toxic Corrosive Spores)
#    - Archetype: SporeSprayer
#    - Save: Fortitude / Con DC
#    - Type: Poison / Acid
#
# 3. Disorientor (Will save - Psychic/Harmonic Concussive Non-Lethal Damage)
#    - Archetype: Disorientor
#    - Save: Will DC
#    - Type: NonLethal / Mental
# ==============================================================================

# Standard PF2e DC by Level:
# Lv 1: DC 15
# Lv 3: DC 19
# Lv 5: DC 20
# Lv 7: DC 23
# Lv 10: DC 27

SPECIAL_SPECS = {
    "acid_spitter": {
        "archetype": "AcidSpitter",
        "name_base": "Caustic Acid Spitter",
        "save_type": "ref",
        "damage_type": "Acid",
        "traits": ["acid", "area", "range_30"],
        "levels": {
            1: {"hp": 18, "ac": 16, "fort": 7, "ref": 8, "will": 4, "spd": 35, "dc": 15, "save_dice": "1d8", "save_flat": 2, "atk": 7, "bite_dice": "1d6", "bite_flat": 2},
            3: {"hp": 38, "ac": 19, "fort": 10, "ref": 11, "will": 7, "spd": 35, "dc": 19, "save_dice": "2d8", "save_flat": 3, "atk": 11, "bite_dice": "2d6", "bite_flat": 3},
            5: {"hp": 56, "ac": 22, "fort": 12, "ref": 14, "will": 9, "spd": 40, "dc": 20, "save_dice": "3d8", "save_flat": 4, "atk": 13, "bite_dice": "2d6", "bite_flat": 5},
            7: {"hp": 88, "ac": 25, "fort": 15, "ref": 17, "will": 12, "spd": 40, "dc": 23, "save_dice": "4d8", "save_flat": 6, "atk": 16, "bite_dice": "2d8", "bite_flat": 7},
            10: {"hp": 120, "ac": 30, "fort": 18, "ref": 22, "will": 16, "spd": 45, "dc": 27, "save_dice": "6d8", "save_flat": 8, "atk": 21, "bite_dice": "3d8", "bite_flat": 8}
        }
    },
    "spore_sprayer": {
        "archetype": "SporeSprayer",
        "name_base": "Fungal Spore Sprayer",
        "save_type": "fort",
        "damage_type": "Poison",
        "traits": ["poison", "spore", "range_30"],
        "levels": {
            1: {"hp": 20, "ac": 15, "fort": 8, "ref": 5, "will": 6, "spd": 30, "dc": 15, "save_dice": "1d6", "save_flat": 3, "atk": 6, "bite_dice": "1d6", "bite_flat": 2},
            3: {"hp": 42, "ac": 18, "fort": 11, "ref": 7, "will": 9, "spd": 30, "dc": 19, "save_dice": "2d6", "save_flat": 5, "atk": 10, "bite_dice": "2d6", "bite_flat": 3},
            5: {"hp": 62, "ac": 21, "fort": 14, "ref": 9, "will": 12, "spd": 35, "dc": 20, "save_dice": "3d6", "save_flat": 6, "atk": 13, "bite_dice": "2d6", "bite_flat": 4},
            7: {"hp": 96, "ac": 24, "fort": 17, "ref": 12, "will": 15, "spd": 35, "dc": 23, "save_dice": "4d6", "save_flat": 8, "atk": 16, "bite_dice": "2d8", "bite_flat": 6},
            10: {"hp": 130, "ac": 29, "fort": 21, "ref": 16, "will": 19, "spd": 40, "dc": 27, "save_dice": "6d6", "save_flat": 10, "atk": 20, "bite_dice": "3d6", "bite_flat": 8}
        }
    },
    "disorientor": {
        "archetype": "Disorientor",
        "name_base": "Resonator Disorientor",
        "save_type": "will",
        "damage_type": "NonLethal",
        "traits": ["mental", "sonic", "nonlethal", "range_30"],
        "levels": {
            1: {"hp": 22, "ac": 16, "fort": 5, "ref": 7, "will": 8, "spd": 35, "dc": 16, "save_dice": "1d8", "save_flat": 3, "atk": 7, "bite_dice": "1d4", "bite_flat": 2},
            3: {"hp": 50, "ac": 19, "fort": 8, "ref": 10, "will": 12, "spd": 35, "dc": 20, "save_dice": "2d8", "save_flat": 5, "atk": 11, "bite_dice": "2d4", "bite_flat": 3},
            5: {"hp": 74, "ac": 22, "fort": 10, "ref": 13, "will": 15, "spd": 40, "dc": 22, "save_dice": "3d8", "save_flat": 6, "atk": 14, "bite_dice": "2d4", "bite_flat": 4},
            7: {"hp": 110, "ac": 25, "fort": 13, "ref": 16, "will": 18, "spd": 40, "dc": 25, "save_dice": "4d8", "save_flat": 8, "atk": 17, "bite_dice": "2d6", "bite_flat": 6},
            10: {"hp": 145, "ac": 30, "fort": 16, "ref": 20, "will": 22, "spd": 45, "dc": 29, "save_dice": "6d8", "save_flat": 12, "atk": 22, "bite_dice": "3d4", "bite_flat": 7}
        }
    }
}

def generate_special_templates():
    created = []
    LEVELS = [1, 3, 5, 7, 10]

    for key, spec in SPECIAL_SPECS.items():
        for lvl in LEVELS:
            data = spec["levels"][lvl]
            name_base = spec["name_base"]
            save_type = spec["save_type"]
            dmg_type = spec["damage_type"]
            traits = spec["traits"]

            # Save Emitter Weapon
            ability_name = f"{name_base} Burst" if key != "acid_spitter" else "Caustic Acid Stream"
            if key == "spore_sprayer":
                ability_name = "Choking Spore Cloud"
            elif key == "disorientor":
                ability_name = "Disorienting Harmonic Pulse"

            save_weapon = {
                "name": ability_name,
                "attack_bonus": 0,
                "damage_dice": data["save_dice"],
                "flat_damage": data["save_flat"],
                "damage_type": dmg_type,
                "range": 30,
                "ap_cost": 0,
                "traits": traits,
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"],
                "save_type": save_type,
                "save_dc": data["dc"],
                "save_damage_dice": data["save_dice"],
                "save_flat_damage": data["save_flat"],
                "action_cost": 2,
                "cooldown_rounds": 0
            }

            melee_strike = {
                "name": "Barbed Tendril / Mandible",
                "attack_bonus": data["atk"],
                "damage_dice": data["bite_dice"],
                "flat_damage": data["bite_flat"],
                "damage_type": "P",
                "range": 0,
                "ap_cost": 0,
                "traits": ["agile"],
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]
            }

            weapons_list = [save_weapon, melee_strike]

            # 1. Berserk (Full HP)
            berserk_obj = {
                "name": f"{name_base} (Lv{lvl} - Berserk)",
                "archetype": spec["archetype"],
                "level": lvl,
                "hp": data["hp"],
                "ac": data["ac"],
                "fort": data["fort"],
                "ref": data["ref"],
                "will": data["will"],
                "speed": data["spd"],
                "max_ap": 0,
                "status": 0,
                "civil_spire_legal": False,
                "civil_ac_penalty": 0,
                "unarmed_damage_dice": data["bite_dice"],
                "unarmed_bonus": data["atk"],
                "unarmed_flat_dmg": data["bite_flat"],
                "unarmed_traits": ["agile"],
                "weapons": weapons_list,
                "abilities": {}
            }

            berserk_file = f"creature_{key}_lv{lvl}.json"
            with open(OUT_DIR / berserk_file, "w", encoding="utf-8") as f:
                json.dump(berserk_obj, f, indent=2)
            created.append(berserk_file)

            # 2. Flee (50% HP)
            flee_obj = {
                "name": f"{name_base} (Lv{lvl} - Flee 50%)",
                "archetype": spec["archetype"],
                "level": lvl,
                "hp": max(1, data["hp"] // 2),
                "ac": data["ac"],
                "fort": data["fort"],
                "ref": data["ref"],
                "will": data["will"],
                "speed": data["spd"],
                "max_ap": 0,
                "status": 0,
                "civil_spire_legal": False,
                "civil_ac_penalty": 0,
                "unarmed_damage_dice": data["bite_dice"],
                "unarmed_bonus": data["atk"],
                "unarmed_flat_dmg": data["bite_flat"],
                "unarmed_traits": ["agile"],
                "weapons": weapons_list,
                "abilities": {}
            }

            flee_file = f"creature_{key}_flee_lv{lvl}.json"
            with open(OUT_DIR / flee_file, "w", encoding="utf-8") as f:
                json.dump(flee_obj, f, indent=2)
            created.append(flee_file)

    print(f"Generated {len(created)} special save-based creature templates in {OUT_DIR}:")
    for f in created:
        print(f"  - {f}")

if __name__ == "__main__":
    generate_special_templates()

