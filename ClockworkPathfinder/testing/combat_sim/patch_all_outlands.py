import os, sys, json
sys.path.insert(0, 'ClockworkPathfinder/testing/combat_sim')
from combat_sim import Simulator

# Let's inspect the current CLASS_SPECS in generate_all_templates.py
with open('ClockworkPathfinder/testing/combat_sim/generate_all_templates.py', 'r', encoding='utf-8') as f:
    text = f.read()

# We want to add outland_ac, outland_weapons, outland_abilities across all classes:

# 1. ClockworkRifleman:
rifle_old = """    "ClockworkRifleman": {
        "archetype": "ClockworkRifleman",
        "hp_per_lvl": 10,
        "con_mod": [1, 2, 2],
        "ac": [16, 22, 29],
        "speed": 25,
        "max_ap": [3, 5, 7],
        "status": 3,
        "civil_legal": False,
        "civil_ac_pen": -4,
        "saves": {
            "fort": [7, 12, 17],
            "ref": [9, 15, 22],
            "will": [4, 9, 16]
        },
        "unarmed": {
            1: {"dice": "1d4", "bonus": 5, "flat": 0},
            5: {"dice": "1d4", "bonus": 10, "flat": 0},
            10: {"dice": "1d4", "bonus": 15, "flat": 1}
        },
        "weapons": lambda lvl: [
            {
                "name": "Heavy Military Rifle",
                "attack_bonus": 9 if lvl==1 else (16 if lvl==5 else 23),
                "damage_dice": "1d10" if lvl==1 else ("2d10" if lvl==5 else "3d10"),
                "flat_damage": 2 if lvl==1 else (3 if lvl==5 else 4),
                "damage_type": "P",
                "range": 120,
                "ap_cost": 0,
                "traits": ["cartridge", "fatal_d12"],
                "ammo_capacity": 5,
                "reload_actions": 1,
                "allowed_environments": ["high_radiant", "low_radiant", "the_neither"]
            },
            {
                "name": "Combat Bayonet",
                "attack_bonus": 6 if lvl==1 else (11 if lvl==5 else 17),
                "damage_dice": "1d6" if lvl==1 else ("2d6" if lvl==5 else "3d6"),
                "flat_damage": 1 if lvl==1 else (2 if lvl==5 else 3),
                "damage_type": "P",
                "range": 0,
                "ap_cost": 0,
                "traits": ["agile", "finesse"],
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]
            }
        ],
        "abilities": lambda lvl: {}
    },"""

rifle_new = """    "ClockworkRifleman": {
        "archetype": "ClockworkRifleman",
        "hp_per_lvl": 10,
        "con_mod": [1, 2, 2],
        "ac": [16, 22, 29],
        "speed": 25,
        "max_ap": [3, 5, 7],
        "status": 3,
        "civil_legal": False,
        "civil_ac_pen": -4,
        "outland_ac": [17, 24, 31],
        "saves": {
            "fort": [7, 12, 17],
            "ref": [9, 15, 22],
            "will": [4, 9, 16]
        },
        "unarmed": {
            1: {"dice": "1d4", "bonus": 5, "flat": 0},
            5: {"dice": "1d4", "bonus": 10, "flat": 0},
            10: {"dice": "1d4", "bonus": 15, "flat": 1}
        },
        "weapons": lambda lvl: [
            {
                "name": "Heavy Military Rifle",
                "attack_bonus": 9 if lvl==1 else (16 if lvl==5 else 23),
                "damage_dice": "1d10" if lvl==1 else ("2d10" if lvl==5 else "3d10"),
                "flat_damage": 2 if lvl==1 else (3 if lvl==5 else 4),
                "damage_type": "P",
                "range": 120,
                "ap_cost": 0,
                "traits": ["cartridge", "fatal_d12"],
                "ammo_capacity": 6,
                "reload_actions": 1,
                "allowed_environments": ["high_radiant", "low_radiant", "the_neither", "wilderness"]
            },
            {
                "name": "Combat Bayonet",
                "attack_bonus": 6 if lvl==1 else (12 if lvl==5 else 18),
                "damage_dice": "1d6" if lvl==1 else ("2d6" if lvl==5 else "3d6"),
                "flat_damage": 1 if lvl==1 else (2 if lvl==5 else 3),
                "damage_type": "P",
                "range": 0,
                "ap_cost": 0,
                "traits": ["agile", "finesse"],
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither", "wilderness"]
            }
        ],
        "outland_weapons": lambda lvl: [
            {
                "name": "Heavy Military Rifle (Outland)",
                "attack_bonus": 10 if lvl==1 else (17 if lvl==5 else 24),
                "damage_dice": "1d10" if lvl==1 else ("2d10" if lvl==5 else "3d10"),
                "flat_damage": 3 if lvl==1 else (5 if lvl==5 else 8),
                "damage_type": "P",
                "range": 120,
                "ap_cost": 0,
                "traits": ["cartridge", "fatal_d12"],
                "ammo_capacity": 6,
                "reload_actions": 1,
                "allowed_environments": ["high_radiant", "low_radiant", "the_neither", "wilderness"]
            },
            {
                "name": "Reinforced Bayonet",
                "attack_bonus": 8 if lvl==1 else (14 if lvl==5 else 20),
                "damage_dice": "1d6" if lvl==1 else ("2d6" if lvl==5 else "3d6"),
                "flat_damage": 3 if lvl==1 else (5 if lvl==5 else 7),
                "damage_type": "P",
                "range": 0,
                "ap_cost": 0,
                "traits": ["agile", "finesse"],
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither", "wilderness"]
            }
        ],
        "abilities": lambda lvl: {}
    },"""

assert rifle_old in text, 'rifle_old not found'
text = text.replace(rifle_old, rifle_new, 1)

# 2. Survivor:
survivor_old = """    "Survivor": {
        "archetype": "Survivor",
        "hp_per_lvl": 8,
        "con_mod": [1, 1, 2],
        "ac": [16, 21, 28],
        "speed": 25,
        "max_ap": [3, 5, 7],
        "status": 2,
        "civil_legal": True,
        "civil_ac_pen": 0,
        "saves": {
            "fort": [5, 10, 16],
            "ref": [8, 14, 21],
            "will": [6, 11, 18]
        },
        "unarmed": {
            1: {"dice": "1d4", "bonus": 5, "flat": 0},
            5: {"dice": "1d4", "bonus": 9, "flat": 0},
            10: {"dice": "1d4", "bonus": 14, "flat": 1}
        },
        "weapons": lambda lvl: [
            {
                "name": "Mundane Steel Utility Dagger",
                "attack_bonus": 7 if lvl==1 else (13 if lvl==5 else 19),
                "damage_dice": "1d4" if lvl==1 else ("2d4" if lvl==5 else "3d4"),
                "flat_damage": 1 if lvl==1 else (2 if lvl==5 else 3),
                "damage_type": "P/S",
                "range": 0,
                "ap_cost": 0,
                "traits": ["agile", "finesse", "deadly_d8"],
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]
            }
        ],
        "abilities": lambda lvl: {}
    },"""

survivor_new = """    "Survivor": {
        "archetype": "Survivor",
        "hp_per_lvl": 8,
        "con_mod": [1, 1, 2],
        "ac": [16, 21, 28],
        "outland_ac": [17, 23, 30],
        "speed": 25,
        "max_ap": [3, 5, 7],
        "status": 2,
        "civil_legal": True,
        "civil_ac_pen": 0,
        "saves": {
            "fort": [5, 10, 16],
            "ref": [8, 14, 21],
            "will": [6, 11, 18]
        },
        "unarmed": {
            1: {"dice": "1d4", "bonus": 5, "flat": 0},
            5: {"dice": "1d4", "bonus": 9, "flat": 0},
            10: {"dice": "1d4", "bonus": 14, "flat": 1}
        },
        "weapons": lambda lvl: [
            {
                "name": "Mundane Steel Utility Dagger",
                "attack_bonus": 7 if lvl==1 else (13 if lvl==5 else 19),
                "damage_dice": "1d4" if lvl==1 else ("2d4" if lvl==5 else "3d4"),
                "flat_damage": 1 if lvl==1 else (2 if lvl==5 else 3),
                "damage_type": "P/S",
                "range": 0,
                "ap_cost": 0,
                "traits": ["agile", "finesse", "deadly_d8"],
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither", "wilderness"]
            }
        ],
        "outland_weapons": lambda lvl: [
            {
                "name": "Niracrest Trench Blade (+1 Striking)",
                "attack_bonus": 8 if lvl==1 else (15 if lvl==5 else 22),
                "damage_dice": "1d6" if lvl==1 else ("2d6" if lvl==5 else "3d6"),
                "flat_damage": 3 if lvl==1 else (6 if lvl==5 else 9),
                "damage_type": "S",
                "range": 0,
                "ap_cost": 0,
                "traits": ["agile", "finesse", "deadly_d8"],
                "allowed_environments": ["high_radiant", "low_radiant", "the_neither", "wilderness"]
            },
            {
                "name": "Outland Hunting Hand-Crossbow",
                "attack_bonus": 7 if lvl==1 else (14 if lvl==5 else 21),
                "damage_dice": "1d6" if lvl==1 else ("2d6" if lvl==5 else "3d6"),
                "flat_damage": 2 if lvl==1 else (4 if lvl==5 else 6),
                "damage_type": "P",
                "range": 60,
                "ap_cost": 0,
                "traits": [],
                "allowed_environments": ["high_radiant", "low_radiant", "the_neither", "wilderness"]
            }
        ],
        "abilities": lambda lvl: {}
    },"""

assert survivor_old in text, 'survivor_old not found'
text = text.replace(survivor_old, survivor_new, 1)

# 3. ClockworkEngineer:
engineer_old = """    "ClockworkEngineer": {
        "archetype": "ClockworkEngineer",
        "hp_per_lvl": 8,
        "con_mod": [1, 2, 2],
        "ac": [15, 21, 28],
        "speed": 25,
        "max_ap": [3, 5, 7],
        "status": 3,
        "civil_legal": False,
        "civil_ac_pen": -4,
        "saves": {
            "fort": [7, 12, 17],
            "ref": [5, 10, 16],
            "will": [6, 11, 18]
        },
        "unarmed": {
            1: {"dice": "1d4", "bonus": 5, "flat": 0},
            5: {"dice": "1d4", "bonus": 10, "flat": 0},
            10: {"dice": "1d4", "bonus": 15, "flat": 1}
        },
        "weapons": lambda lvl: [
            {
                "name": "Heavy Neither Carbine",
                "attack_bonus": 7 if lvl==1 else (13 if lvl==5 else 19),
                "damage_dice": "1d8" if lvl==1 else ("2d8" if lvl==5 else "3d8"),
                "flat_damage": 2 if lvl==1 else (3 if lvl==5 else 4),
                "damage_type": "P",
                "range": 60,
                "ap_cost": 0,
                "traits": ["cartridge", "fatal_d10"],
                "ammo_capacity": 6,
                "reload_actions": 1,
                "allowed_environments": ["high_radiant", "low_radiant", "the_neither"]
            },
            {
                "name": "Tuned Heavy Induction Halberd",
                "attack_bonus": 7 if lvl==1 else (13 if lvl==5 else 19),
                "damage_dice": "1d10" if lvl==1 else ("2d10" if lvl==5 else "3d10"),
                "flat_damage": 3 if lvl==1 else (4 if lvl==5 else 6),
                "damage_type": "P/S",
                "range": 0,
                "ap_cost": 3,
                "traits": ["reach", "radiant"],
                "allowed_environments": ["high_radiant", "low_radiant"]
            }
        ],
        "abilities": lambda lvl: {
            "arc_deflection_screen": True,
            "deflection_ap_cost": 2,
            "deflection_ac_bonus": 3
        }
    },"""

engineer_new = """    "ClockworkEngineer": {
        "archetype": "ClockworkEngineer",
        "hp_per_lvl": 8,
        "con_mod": [1, 2, 2],
        "ac": [15, 21, 28],
        "outland_ac": [18, 25, 32],
        "speed": 25,
        "max_ap": [3, 5, 7],
        "status": 3,
        "civil_legal": False,
        "civil_ac_pen": -4,
        "saves": {
            "fort": [7, 12, 17],
            "ref": [5, 10, 16],
            "will": [6, 11, 18]
        },
        "unarmed": {
            1: {"dice": "1d4", "bonus": 5, "flat": 0},
            5: {"dice": "1d4", "bonus": 10, "flat": 0},
            10: {"dice": "1d4", "bonus": 15, "flat": 1}
        },
        "weapons": lambda lvl: [
            {
                "name": "Heavy Neither Carbine",
                "attack_bonus": 7 if lvl==1 else (13 if lvl==5 else 19),
                "damage_dice": "1d8" if lvl==1 else ("2d8" if lvl==5 else "3d8"),
                "flat_damage": 2 if lvl==1 else (3 if lvl==5 else 4),
                "damage_type": "P",
                "range": 60,
                "ap_cost": 0,
                "traits": ["cartridge", "fatal_d10"],
                "ammo_capacity": 6,
                "reload_actions": 1,
                "allowed_environments": ["high_radiant", "low_radiant", "the_neither", "wilderness"]
            },
            {
                "name": "Tuned Heavy Induction Halberd",
                "attack_bonus": 7 if lvl==1 else (13 if lvl==5 else 19),
                "damage_dice": "1d10" if lvl==1 else ("2d10" if lvl==5 else "3d10"),
                "flat_damage": 3 if lvl==1 else (4 if lvl==5 else 6),
                "damage_type": "P/S",
                "range": 0,
                "ap_cost": 3,
                "traits": ["reach", "radiant"],
                "allowed_environments": ["high_radiant", "low_radiant"]
            }
        ],
        "outland_weapons": lambda lvl: [
            {
                "name": "Reinforced Outland Carbine (Heavy)",
                "attack_bonus": 8 if lvl==1 else (15 if lvl==5 else 22),
                "damage_dice": "1d8" if lvl==1 else ("2d8" if lvl==5 else "3d8"),
                "flat_damage": 3 if lvl==1 else (6 if lvl==5 else 9),
                "damage_type": "P",
                "range": 60,
                "ap_cost": 0,
                "traits": ["cartridge", "fatal_d10"],
                "ammo_capacity": 6,
                "reload_actions": 1,
                "allowed_environments": ["high_radiant", "low_radiant", "the_neither", "wilderness"]
            },
            {
                "name": "Tuned Heavy Induction Halberd",
                "attack_bonus": 8 if lvl==1 else (15 if lvl==5 else 22),
                "damage_dice": "1d10" if lvl==1 else ("2d10" if lvl==5 else "3d10"),
                "flat_damage": 4 if lvl==1 else (7 if lvl==5 else 10),
                "damage_type": "P/S",
                "range": 0,
                "ap_cost": 3,
                "traits": ["reach", "radiant"],
                "allowed_environments": ["high_radiant", "low_radiant"]
            }
        ],
        "outland_abilities": lambda lvl: {
            "arc_deflection_screen": True,
            "deflection_ap_cost": 2,
            "deflection_ac_bonus": 3,
            "shield_block": True,
            "shield_hp": 20 if lvl==1 else (35 if lvl==5 else 50),
            "shield_hardness": 5 if lvl==1 else (8 if lvl==5 else 12)
        },
        "abilities": lambda lvl: {
            "arc_deflection_screen": True,
            "deflection_ap_cost": 2,
            "deflection_ac_bonus": 3
        }
    },"""

assert engineer_old in text, 'engineer_old not found'
text = text.replace(engineer_old, engineer_new, 1)

# 4. Scout:
scout_old = """    "Scout": {
        "archetype": "Scout",
        "hp_per_lvl": 10,
        "con_mod": [1, 2, 2],
        "ac": [16, 22, 29],
        "speed": 30,
        "max_ap": [3, 5, 7],
        "status": 2,
        "civil_legal": True,
        "civil_ac_pen": 0,
        "saves": {
            "fort": [7, 12, 17],
            "ref": [8, 14, 21],
            "will": [5, 10, 16]
        },
        "unarmed": {
            1: {"dice": "1d4", "bonus": 5, "flat": 0},
            5: {"dice": "1d4", "bonus": 10, "flat": 0},
            10: {"dice": "1d4", "bonus": 15, "flat": 1}
        },
        "weapons": lambda lvl: [
            {
                "name": "Heavy Outland Crossbow",
                "attack_bonus": 8 if lvl==1 else (14 if lvl==5 else 20),
                "damage_dice": "1d10" if lvl==1 else ("2d10" if lvl==5 else "3d10"),
                "flat_damage": 2 if lvl==1 else (3 if lvl==5 else 4),
                "damage_type": "P",
                "range": 120,
                "ap_cost": 0,
                "traits": [],
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]
            },
            {
                "name": "Prospecting Pick / Hatchet",
                "attack_bonus": 6 if lvl==1 else (11 if lvl==5 else 17),
                "damage_dice": "1d6" if lvl==1 else ("2d6" if lvl==5 else "3d6"),
                "flat_damage": 2 if lvl==1 else (3 if lvl==5 else 5),
                "damage_type": "P/S",
                "range": 0,
                "ap_cost": 0,
                "traits": ["fatal_d10"],
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]
            }
        ],
        "abilities": lambda lvl: {}
    },"""

scout_new = """    "Scout": {
        "archetype": "Scout",
        "hp_per_lvl": 10,
        "con_mod": [1, 2, 2],
        "ac": [16, 22, 29],
        "outland_ac": [17, 24, 31],
        "speed": 30,
        "max_ap": [3, 5, 7],
        "status": 2,
        "civil_legal": True,
        "civil_ac_pen": 0,
        "saves": {
            "fort": [7, 12, 17],
            "ref": [8, 14, 21],
            "will": [5, 10, 16]
        },
        "unarmed": {
            1: {"dice": "1d4", "bonus": 5, "flat": 0},
            5: {"dice": "1d4", "bonus": 10, "flat": 0},
            10: {"dice": "1d4", "bonus": 15, "flat": 1}
        },
        "weapons": lambda lvl: [
            {
                "name": "Heavy Outland Crossbow",
                "attack_bonus": 8 if lvl==1 else (14 if lvl==5 else 20),
                "damage_dice": "1d10" if lvl==1 else ("2d10" if lvl==5 else "3d10"),
                "flat_damage": 2 if lvl==1 else (3 if lvl==5 else 4),
                "damage_type": "P",
                "range": 120,
                "ap_cost": 0,
                "traits": [],
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither", "wilderness"]
            },
            {
                "name": "Prospecting Pick / Hatchet",
                "attack_bonus": 6 if lvl==1 else (11 if lvl==5 else 17),
                "damage_dice": "1d6" if lvl==1 else ("2d6" if lvl==5 else "3d6"),
                "flat_damage": 2 if lvl==1 else (3 if lvl==5 else 5),
                "damage_type": "P/S",
                "range": 0,
                "ap_cost": 0,
                "traits": ["fatal_d10"],
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither", "wilderness"]
            }
        ],
        "outland_weapons": lambda lvl: [
            {
                "name": "Composite Outland Longbow (+1 Striking)",
                "attack_bonus": 9 if lvl==1 else (16 if lvl==5 else 23),
                "damage_dice": "1d8" if lvl==1 else ("2d8" if lvl==5 else "3d8"),
                "flat_damage": 3 if lvl==1 else (6 if lvl==5 else 9),
                "damage_type": "P",
                "range": 100,
                "ap_cost": 0,
                "traits": ["deadly_d10"],
                "allowed_environments": ["high_radiant", "low_radiant", "the_neither", "wilderness"]
            },
            {
                "name": "Master Sapper Pick",
                "attack_bonus": 8 if lvl==1 else (14 if lvl==5 else 21),
                "damage_dice": "1d6" if lvl==1 else ("2d6" if lvl==5 else "3d6"),
                "flat_damage": 4 if lvl==1 else (7 if lvl==5 else 10),
                "damage_type": "P",
                "range": 0,
                "ap_cost": 0,
                "traits": ["fatal_d10"],
                "allowed_environments": ["high_radiant", "low_radiant", "the_neither", "wilderness"]
            }
        ],
        "outland_abilities": lambda lvl: {
            "shield_block": True,
            "shield_hp": 15 if lvl==1 else (25 if lvl==5 else 40),
            "shield_hardness": 4 if lvl==1 else (6 if lvl==5 else 10)
        },
        "abilities": lambda lvl: {}
    },"""

assert scout_old in text, 'scout_old not found'
text = text.replace(scout_old, scout_new, 1)

# 5. Chirurgeon:
chirurgeon_old = """    "Chirurgeon": {
        "archetype": "Chirurgeon",
        "hp_per_lvl": 8,
        "con_mod": [1, 1, 2],
        "ac": [15, 21, 28],
        "speed": 25,
        "max_ap": [3, 5, 7],
        "status": 3,
        "civil_legal": True,
        "civil_ac_pen": 0,
        "saves": {
            "fort": [7, 13, 19],
            "ref": [5, 11, 17],
            "will": [6, 11, 18]
        },
        "unarmed": {
            1: {"dice": "1d4", "bonus": 4, "flat": 0},
            5: {"dice": "1d4", "bonus": 8, "flat": 1},
            10: {"dice": "1d4", "bonus": 13, "flat": 1}
        },
        "weapons": lambda lvl: [
            {
                "name": "Surgical Scalpel / Lancet",
                "attack_bonus": 6 if lvl==1 else (12 if lvl==5 else 18),
                "damage_dice": "1d4" if lvl==1 else ("2d4" if lvl==5 else "3d4"),
                "flat_damage": 1 if lvl==1 else (3 if lvl==5 else 4),
                "damage_type": "P/S",
                "range": 0,
                "ap_cost": 0,
                "traits": ["agile", "finesse", "deadly_d8"],
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]
            },
            {
                "name": "Corrosive Acid Phial",
                "attack_bonus": 5 if lvl==1 else (11 if lvl==5 else 17),
                "damage_dice": "1d6" if lvl==1 else ("2d6" if lvl==5 else "3d6"),
                "flat_damage": 2 if lvl==1 else (4 if lvl==5 else 5),
                "damage_type": "Acid",
                "range": 30,
                "ap_cost": 0,
                "traits": ["bomb"],
                "allowed_environments": ["high_radiant", "low_radiant", "the_neither"]
            }
        ],
        "abilities": lambda lvl: {}
    },"""

chirurgeon_new = """    "Chirurgeon": {
        "archetype": "Chirurgeon",
        "hp_per_lvl": 8,
        "con_mod": [1, 1, 2],
        "ac": [15, 21, 28],
        "speed": 25,
        "max_ap": [3, 5, 7],
        "status": 3,
        "civil_legal": True,
        "civil_ac_pen": 0,
        "saves": {
            "fort": [7, 13, 19],
            "ref": [5, 11, 17],
            "will": [6, 11, 18]
        },
        "unarmed": {
            1: {"dice": "1d4", "bonus": 4, "flat": 0},
            5: {"dice": "1d4", "bonus": 8, "flat": 1},
            10: {"dice": "1d4", "bonus": 13, "flat": 1}
        },
        "weapons": lambda lvl: [
            {
                "name": "Surgical Scalpel / Lancet",
                "attack_bonus": 6 if lvl==1 else (12 if lvl==5 else 18),
                "damage_dice": "1d4" if lvl==1 else ("2d4" if lvl==5 else "3d4"),
                "flat_damage": 1 if lvl==1 else (3 if lvl==5 else 4),
                "damage_type": "P/S",
                "range": 0,
                "ap_cost": 0,
                "traits": ["agile", "finesse", "deadly_d8"],
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither", "wilderness"]
            },
            {
                "name": "Corrosive Acid Phial",
                "attack_bonus": 5 if lvl==1 else (11 if lvl==5 else 17),
                "damage_dice": "1d6" if lvl==1 else ("2d6" if lvl==5 else "3d6"),
                "flat_damage": 2 if lvl==1 else (4 if lvl==5 else 5),
                "damage_type": "Acid",
                "range": 30,
                "ap_cost": 0,
                "traits": ["bomb"],
                "allowed_environments": ["high_radiant", "low_radiant", "the_neither", "wilderness"]
            }
        ],
        "outland_abilities": lambda lvl: {
            "temp_hp": 8 if lvl==1 else (20 if lvl==5 else 50),
            "damage_resistance_physical": 4 if lvl==1 else (8 if lvl==5 else 10)
        },
        "abilities": lambda lvl: {}
    },"""

assert chirurgeon_old in text, 'chirurgeon_old not found'
text = text.replace(chirurgeon_old, chirurgeon_new, 1)

with open('ClockworkPathfinder/testing/combat_sim/generate_all_templates.py', 'w', encoding='utf-8') as f:
    f.write(text)
print('Successfully updated generate_all_templates.py with Outland Loadouts across all classes!')
