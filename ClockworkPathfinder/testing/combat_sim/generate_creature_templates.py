import json
from pathlib import Path

# Baseline Bear (PF2e Grizzly Bear chassis adapted):
# Base: Level 3, 50 HP, AC 19, Fort +12, Ref +7, Will +8, Speed 35, Jaws 1d10+5, Claws 1d8+5 (Agile)
# Brute progression scales it up to Level 5 (+2 Brute), Level 10 (+7 Brute), Level 15 (+12 Brute)

BEAR_BRUTE = {
    5: {
        "name": "Corrupted Grizzly Bear (Brute Lv5)",
        "archetype": "BruteBear",
        "level": 5,
        "hp": 95,
        "ac": 21,
        "fort": 15,
        "ref": 9,
        "will": 10,
        "speed": 45,
        "max_ap": 0,
        "status": 0,
        "civil_spire_legal": False,
        "civil_ac_penalty": 0,
        "unarmed_damage_dice": "2d8",
        "unarmed_bonus": 14,
        "unarmed_flat_dmg": 7,
        "unarmed_traits": ["agile"],
        "weapons": [
            {
                "name": "Frenzied Jaws",
                "attack_bonus": 14,
                "damage_dice": "2d10",
                "flat_damage": 8,
                "damage_type": "P",
                "range": 0,
                "ap_cost": 0,
                "traits": ["deadly_d10"],
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]
            },
            {
                "name": "Crushing Claws",
                "attack_bonus": 14,
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
            "damage_resistance_physical": 3,
            "feral_adrenaline_surge": True,
            "surge_temp_hp": 20
        }
    },
    10: {
        "name": "Apex Neither Bear (Brute Lv10)",
        "archetype": "BruteBear",
        "level": 10,
        "hp": 210,
        "ac": 29,
        "fort": 22,
        "ref": 16,
        "will": 17,
        "speed": 55,
        "max_ap": 0,
        "status": 0,
        "civil_spire_legal": False,
        "civil_ac_penalty": 0,
        "unarmed_damage_dice": "3d8",
        "unarmed_bonus": 22,
        "unarmed_flat_dmg": 11,
        "unarmed_traits": ["agile"],
        "weapons": [
            {
                "name": "Titan Jaws",
                "attack_bonus": 22,
                "damage_dice": "3d10",
                "flat_damage": 12,
                "damage_type": "P",
                "range": 0,
                "ap_cost": 0,
                "traits": ["deadly_d10"],
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]
            },
            {
                "name": "Titan Claws",
                "attack_bonus": 22,
                "damage_dice": "3d8",
                "flat_damage": 11,
                "damage_type": "S",
                "range": 0,
                "ap_cost": 0,
                "traits": ["agile"],
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]
            }
        ],
        "abilities": {
            "damage_resistance_physical": 6,
            "feral_adrenaline_surge": True,
            "surge_temp_hp": 30
        }
    },
    15: {
        "name": "Storm Titan Bear (Brute Lv15)",
        "archetype": "BruteBear",
        "level": 15,
        "hp": 350,
        "ac": 37,
        "fort": 30,
        "ref": 23,
        "will": 24,
        "speed": 65,
        "max_ap": 0,
        "status": 0,
        "civil_spire_legal": False,
        "civil_ac_penalty": 0,
        "unarmed_damage_dice": "4d8",
        "unarmed_bonus": 30,
        "unarmed_flat_dmg": 16,
        "unarmed_traits": ["agile"],
        "weapons": [
            {
                "name": "Abyssal Jaws",
                "attack_bonus": 30,
                "damage_dice": "4d12",
                "flat_damage": 18,
                "damage_type": "P",
                "range": 0,
                "ap_cost": 0,
                "traits": ["deadly_d12"],
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]
            },
            {
                "name": "Abyssal Claws",
                "attack_bonus": 30,
                "damage_dice": "4d8",
                "flat_damage": 16,
                "damage_type": "S",
                "range": 0,
                "ap_cost": 0,
                "traits": ["agile"],
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]
            }
        ],
        "abilities": {
            "damage_resistance_physical": 10,
            "feral_adrenaline_surge": True,
            "surge_temp_hp": 45
        }
    }
}

# Baseline Wolf (PF2e Wolf chassis adapted):
# Base: Level 1, 24 HP, AC 15, Fort +7, Ref +7, Will +4, Speed 35, Jaws 1d6+2 (Trip)
# Stalker scales speed, precision bleed, stealth reflex, nimble reactions

WOLF_STALKER = {
    5: {
        "name": "Shadow Stalker Wolf (Lv5)",
        "archetype": "StalkerWolf",
        "level": 5,
        "hp": 75,
        "ac": 23,
        "fort": 11,
        "ref": 15,
        "will": 10,
        "speed": 60,
        "max_ap": 0,
        "status": 0,
        "civil_spire_legal": False,
        "civil_ac_penalty": 0,
        "unarmed_damage_dice": "2d6",
        "unarmed_bonus": 14,
        "unarmed_flat_dmg": 6,
        "unarmed_traits": ["agile", "finesse"],
        "weapons": [
            {
                "name": "Serrated Throat Bite",
                "attack_bonus": 14,
                "damage_dice": "2d8",
                "flat_damage": 7,  # Includes precision damage
                "damage_type": "P",
                "range": 0,
                "ap_cost": 0,
                "traits": ["deadly_d8", "finesse"],
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]
            },
            {
                "name": "Flensing Claws",
                "attack_bonus": 14,
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
    10: {
        "name": "Apex Mist Wolf (Stalker Lv10)",
        "archetype": "StalkerWolf",
        "level": 10,
        "hp": 165,
        "ac": 31,
        "fort": 18,
        "ref": 23,
        "will": 17,
        "speed": 80,
        "max_ap": 0,
        "status": 0,
        "civil_spire_legal": False,
        "civil_ac_penalty": 0,
        "unarmed_damage_dice": "3d6",
        "unarmed_bonus": 22,
        "unarmed_flat_dmg": 10,
        "unarmed_traits": ["agile", "finesse"],
        "weapons": [
            {
                "name": "Apex Flensing Jaws",
                "attack_bonus": 23,
                "damage_dice": "3d8",
                "flat_damage": 12,
                "damage_type": "P",
                "range": 0,
                "ap_cost": 0,
                "traits": ["deadly_d10", "finesse"],
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]
            },
            {
                "name": "Hamstring Rake Claws",
                "attack_bonus": 23,
                "damage_dice": "3d6",
                "flat_damage": 9,
                "damage_type": "S",
                "range": 0,
                "ap_cost": 0,
                "traits": ["agile", "finesse"],
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]
            }
        ],
        "abilities": {}
    },
    15: {
        "name": "Deep Stalker Alpha (Stalker Lv15)",
        "archetype": "StalkerWolf",
        "level": 15,
        "hp": 275,
        "ac": 39,
        "fort": 25,
        "ref": 31,
        "will": 24,
        "speed": 95,
        "max_ap": 0,
        "status": 0,
        "civil_spire_legal": False,
        "civil_ac_penalty": 0,
        "unarmed_damage_dice": "4d6",
        "unarmed_bonus": 30,
        "unarmed_flat_dmg": 15,
        "unarmed_traits": ["agile", "finesse"],
        "weapons": [
            {
                "name": "Severing Abyssal Bite",
                "attack_bonus": 31,
                "damage_dice": "4d10",
                "flat_damage": 16,
                "damage_type": "P",
                "range": 0,
                "ap_cost": 0,
                "traits": ["deadly_d12", "finesse"],
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]
            },
            {
                "name": "Tendon Flensing Claws",
                "attack_bonus": 31,
                "damage_dice": "4d6",
                "flat_damage": 13,
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

def generate_creature_templates():
    out_dir = Path("ClockworkPathfinder/testing/combat_sim/creatures")
    out_dir.mkdir(parents=True, exist_ok=True)
    
    for lvl, data in BEAR_BRUTE.items():
        filename = f"bear_brute_lv{lvl}.json"
        with open(out_dir / filename, 'w') as f:
            json.dump(data, f, indent=2)
            
    for lvl, data in WOLF_STALKER.items():
        filename = f"wolf_stalker_lv{lvl}.json"
        with open(out_dir / filename, 'w') as f:
            json.dump(data, f, indent=2)

    print(f"Generated 6 creature templates (Bear Brute Lv5/10/15, Wolf Stalker Lv5/10/15) in {out_dir}")

if __name__ == "__main__":
    generate_creature_templates()

