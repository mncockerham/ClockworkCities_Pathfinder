import json
import os
from pathlib import Path

# Base definitions for the 15 Clockwork Cities player classes
# Keys:
#   hp_base: class HP per level (excl ancestry 8)
#   con_mod: base CON mod by level [lv1, lv5, lv10]
#   ac_base: base AC progression [lv1, lv5, lv10]
#   speed: base movement speed
#   max_ap: AP progression [lv1, lv5, lv10]
#   status: default status tier
#   civil_legal: whether class weapon/armor style is Spire legal
#   civil_ac_pen: AC penalty in Spire if wearing illegal combat armor
#   saves: dict of [lv1, lv5, lv10] for fort, ref, will
#   weapons: function(lvl) returning list of weapons
#   abilities: function(lvl) returning dict of abilities

CLASS_SPECS = {
    "Pugilist": {
        "archetype": "Pugilist",
        "hp_per_lvl": 10,
        "con_mod": [3, 3, 4],
        "ac": [16, 22, 29],
        "speed": 35,
        "max_ap": [5, 8, 12],
        "status": 0,
        "civil_legal": True,
        "civil_ac_pen": 0,
        "saves": {
            "fort": [8, 13, 20],
            "ref": [8, 13, 20],
            "will": [5, 10, 17]
        },
        "unarmed": {
            1: {"dice": "1d6", "bonus": 7, "flat": 3},
            5: {"dice": "2d6", "bonus": 13, "flat": 4},
            10: {"dice": "3d6", "bonus": 20, "flat": 6}
        },
        "weapons": lambda lvl: [
            {
                "name": f"+{1 if lvl<5 else (1 if lvl<10 else 2)} Striking Brass Knuckles" if lvl>=5 else "Brass Knuckles",
                "attack_bonus": 7 if lvl==1 else (13 if lvl==5 else 20),
                "damage_dice": "1d6" if lvl==1 else ("2d6" if lvl==5 else "3d6"),
                "flat_damage": 3 if lvl==1 else (4 if lvl==5 else 6),
                "damage_type": "B",
                "range": 0,
                "ap_cost": 0,
                "traits": ["agile", "finesse"],
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]
            }
        ],
        "abilities": lambda lvl: {
            "flurry_of_blows": True,
            "damage_resistance_physical": 1 if lvl==1 else (2 if lvl==5 else 4)
        }
    },
    "Soldier": {
        "archetype": "Soldier",
        "hp_per_lvl": 10,
        "con_mod": [3, 3, 4],
        "ac": [18, 24, 31],
        "speed": 20,
        "max_ap": [4, 6, 8],
        "status": 2,
        "civil_legal": False,
        "civil_ac_pen": -5,
        "saves": {
            "fort": [8, 13, 20],
            "ref": [5, 10, 17],
            "will": [5, 10, 17]
        },
        "unarmed": {
            1: {"dice": "1d4", "bonus": 6, "flat": 3},
            5: {"dice": "1d4", "bonus": 11, "flat": 4},
            10: {"dice": "2d4", "bonus": 18, "flat": 5}
        },
        "weapons": lambda lvl: [
            {
                "name": "Master Broadsword",
                "attack_bonus": 9 if lvl==1 else (15 if lvl==5 else 22),
                "damage_dice": "1d8" if lvl==1 else ("2d8" if lvl==5 else "3d8"),
                "flat_damage": 3 if lvl==1 else (4 if lvl==5 else 6),
                "damage_type": "S",
                "range": 0,
                "ap_cost": 0,
                "traits": ["versatile_p"],
                "allowed_environments": ["high_radiant", "low_radiant", "the_neither"]
            },
            {
                "name": "Heavy Wrench / Club (Civil)",
                "attack_bonus": 7 if lvl==1 else (13 if lvl==5 else 20),
                "damage_dice": "1d6" if lvl==1 else ("2d6" if lvl==5 else "3d6"),
                "flat_damage": 3 if lvl==1 else (4 if lvl==5 else 6),
                "damage_type": "B",
                "range": 0,
                "ap_cost": 0,
                "traits": [],
                "allowed_environments": ["civil_spire"]
            }
        ],
        "abilities": lambda lvl: {
            "shield_block": True,
            "shield_hardness": 5 if lvl==1 else (7 if lvl==5 else 10),
            "shield_hp": 20 if lvl==1 else (30 if lvl==5 else 45),
            "shield_raised_ac_bonus": 2
        }
    },
    "ClockworkEngineer": {
        "archetype": "ClockworkEngineer",
        "hp_per_lvl": 8,
        "con_mod": [2, 2, 3],
        "ac": [15, 21, 28],
        "speed": 25,
        "max_ap": [5, 9, 14],
        "status": 2,
        "civil_legal": False,
        "civil_ac_pen": -3,
        "saves": {
            "fort": [5, 10, 17],
            "ref": [6, 11, 18],
            "will": [7, 12, 19]
        },
        "unarmed": {
            1: {"dice": "1d4", "bonus": 4, "flat": 0},
            5: {"dice": "1d4", "bonus": 7, "flat": 0},
            10: {"dice": "1d4", "bonus": 12, "flat": 0}
        },
        "weapons": lambda lvl: [
            {
                "name": "Inductive Arc Projector (High)",
                "attack_bonus": 7 if lvl==1 else (12 if lvl==5 else 19),
                "damage_dice": "1d12" if lvl==1 else ("2d12" if lvl==5 else "3d12"),
                "flat_damage": 2 if lvl==1 else (4 if lvl==5 else 6),
                "damage_type": "Electricity",
                "range": 60,
                "ap_cost": 2,
                "traits": ["radiant", "deadly_d10"],
                "allowed_environments": ["high_radiant"]
            },
            {
                "name": "Inductive Arc Projector (Low)",
                "attack_bonus": 7 if lvl==1 else (12 if lvl==5 else 19),
                "damage_dice": "1d8" if lvl==1 else ("2d8" if lvl==5 else "3d8"),
                "flat_damage": 1 if lvl==1 else (3 if lvl==5 else 5),
                "damage_type": "Electricity",
                "range": 40,
                "ap_cost": 2,
                "traits": ["radiant"],
                "allowed_environments": ["low_radiant"]
            },
            {
                "name": "Heavy Neither Carbine (Cartridge)",
                "attack_bonus": 7 if lvl==1 else (12 if lvl==5 else 19),
                "damage_dice": "1d8" if lvl==1 else ("2d8" if lvl==5 else "3d8"),
                "flat_damage": 1 if lvl==1 else (3 if lvl==5 else 5),
                "damage_type": "P",
                "range": 60,
                "ap_cost": 0,
                "traits": ["cartridge", "fatal_d10"],
                "ammo_capacity": 6,
                "reload_actions": 1,
                "allowed_environments": ["low_radiant", "the_neither"]
            },
            {
                "name": "Cartridge Arc Pistol",
                "attack_bonus": 6 if lvl==1 else (11 if lvl==5 else 18),
                "damage_dice": "1d6" if lvl==1 else ("2d6" if lvl==5 else "3d6"),
                "flat_damage": 1 if lvl==1 else (2 if lvl==5 else 4),
                "damage_type": "P/Electricity",
                "range": 30,
                "ap_cost": 0,
                "traits": ["cartridge", "fatal_d10"],
                "ammo_capacity": 6,
                "reload_actions": 1,
                "allowed_environments": ["low_radiant", "the_neither"]
            },
            {
                "name": "Heavy Wrench",
                "attack_bonus": 5 if lvl==1 else (9 if lvl==5 else 15),
                "damage_dice": "1d6" if lvl==1 else ("1d6" if lvl==5 else "2d6"),
                "flat_damage": 1 if lvl==1 else (1 if lvl==5 else 2),
                "damage_type": "B",
                "range": 0,
                "ap_cost": 0,
                "traits": ["shove"],
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]
            }
        ],
        "abilities": lambda lvl: {
            "radiant_barrier": True,
            "barrier_temp_hp_high": 8 if lvl==1 else (15 if lvl==5 else 25),
            "barrier_temp_hp_low": 4 if lvl==1 else (8 if lvl==5 else 14)
        }
    },
    "ClockworkRifleman": {
        "archetype": "ClockworkRifleman",
        "hp_per_lvl": 8,
        "con_mod": [2, 2, 3],
        "ac": [16, 23, 30],
        "speed": 25,
        "max_ap": [3, 6, 9],
        "status": 2,
        "civil_legal": False,
        "civil_ac_pen": -3,
        "saves": {
            "fort": [6, 11, 18],
            "ref": [8, 14, 21],
            "will": [5, 10, 17]
        },
        "unarmed": {
            1: {"dice": "1d4", "bonus": 5, "flat": 1},
            5: {"dice": "1d4", "bonus": 10, "flat": 1},
            10: {"dice": "1d4", "bonus": 16, "flat": 2}
        },
        "weapons": lambda lvl: [
            {
                "name": "Service Rifle (Radiant High)",
                "attack_bonus": 9 if lvl==1 else (14 if lvl==5 else 21),
                "damage_dice": "1d10" if lvl==1 else ("2d10" if lvl==5 else "3d10"),
                "flat_damage": 1 if lvl==1 else (3 if lvl==5 else 5),
                "damage_type": "P/Electricity",
                "range": 120,
                "ap_cost": 1,
                "traits": ["radiant", "fatal_d12"],
                "allowed_environments": ["high_radiant"]
            },
            {
                "name": "Service Rifle (Radiant Low)",
                "attack_bonus": 9 if lvl==1 else (14 if lvl==5 else 21),
                "damage_dice": "1d8" if lvl==1 else ("2d8" if lvl==5 else "3d8"),
                "flat_damage": 1 if lvl==1 else (2 if lvl==5 else 4),
                "damage_type": "P/Electricity",
                "range": 90,
                "ap_cost": 1,
                "traits": ["radiant", "fatal_d12"],
                "allowed_environments": ["low_radiant"]
            },
            {
                "name": "Service Rifle (Cartridge Neither)",
                "attack_bonus": 9 if lvl==1 else (14 if lvl==5 else 21),
                "damage_dice": "1d8" if lvl==1 else ("2d8" if lvl==5 else "3d8"),
                "flat_damage": 1 if lvl==1 else (2 if lvl==5 else 4),
                "damage_type": "P",
                "range": 90,
                "ap_cost": 0,
                "traits": ["cartridge", "fatal_d12"],
                "ammo_capacity": 5,
                "reload_actions": 1,
                "allowed_environments": ["the_neither"]
            },
            {
                "name": "Bayonet / Trench Knife",
                "attack_bonus": 7 if lvl==1 else (12 if lvl==5 else 18),
                "damage_dice": "1d6" if lvl==1 else ("1d6" if lvl==5 else "2d6"),
                "flat_damage": 1 if lvl==1 else (2 if lvl==5 else 3),
                "damage_type": "P",
                "range": 0,
                "ap_cost": 0,
                "traits": ["agile", "finesse"],
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]
            }
        ],
        "abilities": lambda lvl: {}
    },
    "Merchant": {
        "archetype": "Merchant",
        "hp_per_lvl": 8,
        "con_mod": [1, 1, 2],
        "ac": [15, 21, 27],
        "speed": 25,
        "max_ap": [4, 6, 8],
        "status": 6,
        "civil_legal": True,
        "civil_ac_pen": 0,
        "saves": {
            "fort": [5, 10, 16],
            "ref": [6, 11, 18],
            "will": [7, 13, 20]
        },
        "unarmed": {
            1: {"dice": "1d4", "bonus": 4, "flat": 0},
            5: {"dice": "1d4", "bonus": 8, "flat": 0},
            10: {"dice": "1d4", "bonus": 13, "flat": 1}
        },
        "weapons": lambda lvl: [
            {
                "name": "Fair Steel Spire Dueling Rapier",
                "attack_bonus": 7 if lvl==1 else (13 if lvl==5 else 19),
                "damage_dice": "1d6" if lvl==1 else ("2d6" if lvl==5 else "3d6"),
                "flat_damage": 2 if lvl==1 else (3 if lvl==5 else 5),
                "damage_type": "P",
                "range": 0,
                "ap_cost": 0,
                "traits": ["deadly_d8", "disarm", "finesse"],
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]
            },
            {
                "name": "Pistol Cane",
                "attack_bonus": 5 if lvl==1 else (10 if lvl==5 else 16),
                "damage_dice": "1d8" if lvl==1 else ("1d8" if lvl==5 else "2d8"),
                "flat_damage": 0 if lvl==1 else (1 if lvl==5 else 2),
                "damage_type": "P",
                "range": 30,
                "ap_cost": 0,
                "traits": ["cartridge", "fatal_d10", "concealed"],
                "ammo_capacity": 1,
                "reload_actions": 1,
                "allowed_environments": ["high_radiant", "low_radiant", "the_neither"]
            }
        ],
        "abilities": lambda lvl: {
            "armed_retainers": True,
            # Number: 1 at Lv1, 2 at Lv5, 3 at Lv10
            "retainer_count": 1 if lvl==1 else (2 if lvl==5 else 3),
            # Level: ceil(lvl / 2) -> Lv1: Retainer Lv1 (12 HP, +4, 1d6+1)
            #                         Lv5: Retainer Lv3 (20 HP, +7, 1d6+2)
            #                         Lv10: Retainer Lv5 (32 HP, +11, 2d6+3)
            "retainer_hp": 12 if lvl==1 else (20 if lvl==5 else 32),
            "retainer_attack": 4 if lvl==1 else (7 if lvl==5 else 11),
            "retainer_damage_dice": "1d6" if lvl<10 else "2d6",
            "retainer_flat_damage": 1 if lvl==1 else (2 if lvl==5 else 3),
            "social_authority_bonus": 4
        }
    },
    "Scout": {
        "archetype": "Scout",
        "hp_per_lvl": 10,
        "con_mod": [2, 2, 3],
        "ac": [17, 22, 29],
        "speed": 30,
        "max_ap": [3, 5, 8],
        "status": 1,
        "civil_legal": False,
        "civil_ac_pen": -4,
        "saves": {
            "fort": [7, 12, 19],
            "ref": [7, 13, 20],
            "will": [6, 11, 18]
        },
        "unarmed": {
            1: {"dice": "1d4", "bonus": 6, "flat": 2},
            5: {"dice": "1d4", "bonus": 11, "flat": 3},
            10: {"dice": "1d4", "bonus": 17, "flat": 4}
        },
        "weapons": lambda lvl: [
            {
                "name": "Composite Longbow",
                "attack_bonus": 8 if lvl==1 else (14 if lvl==5 else 21),
                "damage_dice": "1d8" if lvl==1 else ("2d8" if lvl==5 else "3d8"),
                "flat_damage": 2 if lvl==1 else (3 if lvl==5 else 4),
                "damage_type": "P",
                "range": 100,
                "ap_cost": 0,
                "traits": ["deadly_d10", "propulsive"],
                "allowed_environments": ["high_radiant", "low_radiant", "the_neither"]
            },
            {
                "name": "Hunting Shortsword",
                "attack_bonus": 7 if lvl==1 else (13 if lvl==5 else 19),
                "damage_dice": "1d6" if lvl==1 else ("2d6" if lvl==5 else "3d6"),
                "flat_damage": 2 if lvl==1 else (3 if lvl==5 else 4),
                "damage_type": "P/S",
                "range": 0,
                "ap_cost": 0,
                "traits": ["agile", "finesse"],
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]
            }
        ],
        "abilities": lambda lvl: {
            "damage_resistance_physical": 1 if lvl>=5 else 0
        }
    },
    "Dandy": {
        "archetype": "Dandy",
        "hp_per_lvl": 10,
        "con_mod": [1, 1, 2],
        "ac": [16, 22, 29],
        "speed": 30,
        "max_ap": [3, 5, 7],
        "status": 5,
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
                "name": "Fair Steel Salon Rapier",
                "attack_bonus": 8 if lvl==1 else (14 if lvl==5 else 21),
                "damage_dice": "1d6" if lvl==1 else ("2d6" if lvl==5 else "3d6"),
                "flat_damage": 3 if lvl==1 else (5 if lvl==5 else 8),
                "damage_type": "P",
                "range": 0,
                "ap_cost": 0,
                "traits": ["deadly_d8", "disarm", "finesse"],
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]
            },
            {
                "name": "Dueling Pistol",
                "attack_bonus": 6 if lvl==1 else (11 if lvl==5 else 17),
                "damage_dice": "1d8" if lvl==1 else ("2d8" if lvl==5 else "3d8"),
                "flat_damage": 1 if lvl==1 else (2 if lvl==5 else 3),
                "damage_type": "P",
                "range": 40,
                "ap_cost": 0,
                "traits": ["cartridge", "fatal_d10", "concealed"],
                "ammo_capacity": 1,
                "reload_actions": 1,
                "allowed_environments": ["high_radiant", "low_radiant", "the_neither"]
            }
        ],
        "abilities": lambda lvl: {}
    },
    "Survivor": {
        "archetype": "Survivor",
        "hp_per_lvl": 8,
        "con_mod": [2, 2, 3],
        "ac": [16, 22, 29],
        "speed": 25,
        "max_ap": [3, 5, 7],
        "status": 0,
        "civil_legal": True,
        "civil_ac_pen": 0,
        "saves": {
            "fort": [5, 10, 16],
            "ref": [8, 14, 21],
            "will": [6, 12, 19]
        },
        "unarmed": {
            1: {"dice": "1d4", "bonus": 6, "flat": 1},
            5: {"dice": "1d4", "bonus": 11, "flat": 1},
            10: {"dice": "1d4", "bonus": 17, "flat": 2}
        },
        "weapons": lambda lvl: [
            {
                "name": "Utility Dagger / Shiv",
                "attack_bonus": 7 if lvl==1 else (13 if lvl==5 else 20),
                "damage_dice": "1d4" if lvl==1 else ("2d4" if lvl==5 else "3d4"),
                "flat_damage": 3 if lvl==1 else (6 if lvl==5 else 9), # Includes sneak attack average
                "damage_type": "P/S",
                "range": 0,
                "ap_cost": 0,
                "traits": ["agile", "finesse", "versatile_s"],
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]
            },
            {
                "name": "Concealed Hand Crossbow",
                "attack_bonus": 6 if lvl==1 else (12 if lvl==5 else 18),
                "damage_dice": "1d6" if lvl==1 else ("2d6" if lvl==5 else "3d6"),
                "flat_damage": 1 if lvl==1 else (3 if lvl==5 else 6),
                "damage_type": "P",
                "range": 50,
                "ap_cost": 0,
                "traits": ["concealed"],
                "allowed_environments": ["high_radiant", "low_radiant", "the_neither"]
            }
        ],
        "abilities": lambda lvl: {}
    },
    "Inspector": {
        "archetype": "Inspector",
        "hp_per_lvl": 8,
        "con_mod": [1, 1, 2],
        "ac": [15, 21, 28],
        "speed": 25,
        "max_ap": [4, 6, 9],
        "status": 3,
        "civil_legal": True,
        "civil_ac_pen": 0,
        "saves": {
            "fort": [5, 10, 16],
            "ref": [7, 12, 19],
            "will": [8, 14, 21]
        },
        "unarmed": {
            1: {"dice": "1d4", "bonus": 5, "flat": 0},
            5: {"dice": "1d4", "bonus": 9, "flat": 0},
            10: {"dice": "1d4", "bonus": 14, "flat": 1}
        },
        "weapons": lambda lvl: [
            {
                "name": "Constable Truncheon / Cane",
                "attack_bonus": 7 if lvl==1 else (13 if lvl==5 else 20),
                "damage_dice": "1d6" if lvl==1 else ("2d6" if lvl==5 else "3d6"),
                "flat_damage": 3 if lvl==1 else (6 if lvl==5 else 9), # Devise stratagem precision
                "damage_type": "B",
                "range": 0,
                "ap_cost": 0,
                "traits": ["agile", "finesse", "nonlethal"],
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]
            },
            {
                "name": "Service Revolver",
                "attack_bonus": 6 if lvl==1 else (12 if lvl==5 else 18),
                "damage_dice": "1d8" if lvl==1 else ("2d8" if lvl==5 else "3d8"),
                "flat_damage": 2 if lvl==1 else (4 if lvl==5 else 7),
                "damage_type": "P",
                "range": 40,
                "ap_cost": 0,
                "traits": ["cartridge", "fatal_d10"],
                "ammo_capacity": 6,
                "reload_actions": 1,
                "allowed_environments": ["high_radiant", "low_radiant", "the_neither"]
            }
        ],
        "abilities": lambda lvl: {}
    },
    "Scholar": {
        "archetype": "Scholar",
        "hp_per_lvl": 6,
        "con_mod": [1, 1, 2],
        "ac": [14, 20, 26],
        "speed": 25,
        "max_ap": [6, 10, 16],
        "status": 4,
        "civil_legal": True,
        "civil_ac_pen": 0,
        "saves": {
            "fort": [4, 9, 15],
            "ref": [5, 10, 16],
            "will": [8, 14, 21]
        },
        "unarmed": {
            1: {"dice": "1d4", "bonus": 3, "flat": 0},
            5: {"dice": "1d4", "bonus": 7, "flat": 0},
            10: {"dice": "1d4", "bonus": 12, "flat": 0}
        },
        "weapons": lambda lvl: [
            {
                "name": "High Radiant Arc Resonator",
                "attack_bonus": 7 if lvl==1 else (12 if lvl==5 else 19),
                "damage_dice": "1d12" if lvl==1 else ("2d12" if lvl==5 else "3d12"),
                "flat_damage": 3 if lvl==1 else (5 if lvl==5 else 8),
                "damage_type": "Electricity",
                "range": 80,
                "ap_cost": 3,
                "traits": ["radiant", "deadly_d10"],
                "allowed_environments": ["high_radiant"]
            },
            {
                "name": "Technical Cartridge Sidearm",
                "attack_bonus": 6 if lvl==1 else (11 if lvl==5 else 18),
                "damage_dice": "1d8" if lvl==1 else ("2d8" if lvl==5 else "3d8"),
                "flat_damage": 1 if lvl==1 else (2 if lvl==5 else 4),
                "damage_type": "P",
                "range": 40,
                "ap_cost": 0,
                "traits": ["cartridge", "fatal_d10"],
                "ammo_capacity": 6,
                "reload_actions": 1,
                "allowed_environments": ["low_radiant", "the_neither"]
            },
            {
                "name": "Scholastic Stave / Cane",
                "attack_bonus": 5 if lvl==1 else (9 if lvl==5 else 14),
                "damage_dice": "1d6" if lvl==1 else ("1d6" if lvl==5 else "2d6"),
                "flat_damage": 0 if lvl==1 else (1 if lvl==5 else 2),
                "damage_type": "B",
                "range": 0,
                "ap_cost": 0,
                "traits": ["finesse"],
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]
            }
        ],
        "abilities": lambda lvl: {
            "radiant_barrier": True,
            "barrier_temp_hp_high": 10 if lvl==1 else (20 if lvl==5 else 30),
            "barrier_temp_hp_low": 4 if lvl==1 else (8 if lvl==5 else 12)
        }
    },
    "Artisan": {
        "archetype": "Artisan",
        "hp_per_lvl": 8,
        "con_mod": [2, 2, 3],
        "ac": [15, 21, 28],
        "speed": 25,
        "max_ap": [5, 8, 12],
        "status": 2,
        "civil_legal": True,
        "civil_ac_pen": 0,
        "saves": {
            "fort": [7, 12, 19],
            "ref": [5, 10, 16],
            "will": [6, 11, 18]
        },
        "unarmed": {
            1: {"dice": "1d4", "bonus": 5, "flat": 1},
            5: {"dice": "1d4", "bonus": 9, "flat": 2},
            10: {"dice": "1d4", "bonus": 15, "flat": 3}
        },
        "weapons": lambda lvl: [
            {
                "name": "Forge Sledge / Maul",
                "attack_bonus": 6 if lvl==1 else (12 if lvl==5 else 18),
                "damage_dice": "1d8" if lvl==1 else ("2d8" if lvl==5 else "3d8"),
                "flat_damage": 2 if lvl==1 else (3 if lvl==5 else 5),
                "damage_type": "B",
                "range": 0,
                "ap_cost": 0,
                "traits": ["shove"],
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]
            },
            {
                "name": "Pneumatic Rivet Driver",
                "attack_bonus": 6 if lvl==1 else (11 if lvl==5 else 17),
                "damage_dice": "1d8" if lvl==1 else ("2d8" if lvl==5 else "3d8"),
                "flat_damage": 1 if lvl==1 else (2 if lvl==5 else 4),
                "damage_type": "P",
                "range": 30,
                "ap_cost": 1,
                "traits": ["cartridge"],
                "ammo_capacity": 4,
                "reload_actions": 1,
                "allowed_environments": ["high_radiant", "low_radiant", "the_neither"]
            }
        ],
        "abilities": lambda lvl: {
            "damage_resistance_physical": 1 if lvl>=5 else 0
        }
    },
    "Chirurgeon": {
        "archetype": "Chirurgeon",
        "hp_per_lvl": 8,
        "con_mod": [1, 2, 2],
        "ac": [15, 21, 27],
        "speed": 25,
        "max_ap": [3, 5, 8],
        "status": 3,
        "civil_legal": True,
        "civil_ac_pen": 0,
        "saves": {
            "fort": [7, 13, 20],
            "ref": [6, 11, 18],
            "will": [6, 11, 18]
        },
        "unarmed": {
            1: {"dice": "1d4", "bonus": 4, "flat": 0},
            5: {"dice": "1d4", "bonus": 8, "flat": 1},
            10: {"dice": "1d4", "bonus": 14, "flat": 1}
        },
        "weapons": lambda lvl: [
            {
                "name": "Surgical Scalpel / Lancet",
                "attack_bonus": 6 if lvl==1 else (12 if lvl==5 else 18),
                "damage_dice": "1d4" if lvl==1 else ("2d4" if lvl==5 else "3d4"),
                "flat_damage": 2 if lvl==1 else (3 if lvl==5 else 4),
                "damage_type": "P/S",
                "range": 0,
                "ap_cost": 0,
                "traits": ["agile", "finesse", "deadly_d8"],
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]
            },
            {
                "name": "Corrosive Acid Phial",
                "attack_bonus": 6 if lvl==1 else (11 if lvl==5 else 17),
                "damage_dice": "1d6" if lvl==1 else ("2d6" if lvl==5 else "3d6"),
                "flat_damage": 2 if lvl==1 else (4 if lvl==5 else 6),
                "damage_type": "Acid",
                "range": 30,
                "ap_cost": 0,
                "traits": ["bomb"],
                "allowed_environments": ["high_radiant", "low_radiant", "the_neither"]
            }
        ],
        "abilities": lambda lvl: {}
    },
    "MadBomber": {
        "archetype": "MadBomber",
        "hp_per_lvl": 8,
        "con_mod": [1, 2, 2],
        "ac": [15, 21, 28],
        "speed": 25,
        "max_ap": [3, 5, 8],
        "status": 1,
        "civil_legal": False,
        "civil_ac_pen": -3,
        "saves": {
            "fort": [7, 13, 20],
            "ref": [7, 12, 19],
            "will": [5, 10, 16]
        },
        "unarmed": {
            1: {"dice": "1d4", "bonus": 4, "flat": 0},
            5: {"dice": "1d4", "bonus": 8, "flat": 1},
            10: {"dice": "1d4", "bonus": 14, "flat": 1}
        },
        "weapons": lambda lvl: [
            {
                "name": "Volatile Nitro Bomb",
                "attack_bonus": 7 if lvl==1 else (13 if lvl==5 else 20),
                "damage_dice": "1d8" if lvl==1 else ("2d8" if lvl==5 else "3d8"),
                "flat_damage": 3 if lvl==1 else (5 if lvl==5 else 8),
                "damage_type": "Fire",
                "range": 40,
                "ap_cost": 0,
                "traits": ["bomb", "splash"],
                "allowed_environments": ["high_radiant", "low_radiant", "the_neither"]
            },
            {
                "name": "Trench Dagger",
                "attack_bonus": 5 if lvl==1 else (9 if lvl==5 else 15),
                "damage_dice": "1d4" if lvl==1 else ("1d4" if lvl==5 else "2d4"),
                "flat_damage": 1 if lvl==1 else (1 if lvl==5 else 2),
                "damage_type": "P",
                "range": 0,
                "ap_cost": 0,
                "traits": ["agile", "finesse"],
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]
            }
        ],
        "abilities": lambda lvl: {}
    },
    "SkyCaptain": {
        "archetype": "SkyCaptain",
        "hp_per_lvl": 10,
        "con_mod": [1, 2, 2],
        "ac": [16, 22, 29],
        "speed": 30,
        "max_ap": [4, 6, 9],
        "status": 3,
        "civil_legal": True,
        "civil_ac_pen": 0,
        "saves": {
            "fort": [6, 11, 18],
            "ref": [8, 14, 21],
            "will": [6, 11, 18]
        },
        "unarmed": {
            1: {"dice": "1d4", "bonus": 5, "flat": 1},
            5: {"dice": "1d4", "bonus": 10, "flat": 1},
            10: {"dice": "1d4", "bonus": 16, "flat": 2}
        },
        "weapons": lambda lvl: [
            {
                "name": "Boarding Cutlass",
                "attack_bonus": 8 if lvl==1 else (14 if lvl==5 else 21),
                "damage_dice": "1d6" if lvl==1 else ("2d6" if lvl==5 else "3d6"),
                "flat_damage": 3 if lvl==1 else (4 if lvl==5 else 6),
                "damage_type": "S",
                "range": 0,
                "ap_cost": 0,
                "traits": ["finesse", "sweep"],
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]
            },
            {
                "name": "Sky-Fleet Deck Pistol",
                "attack_bonus": 7 if lvl==1 else (12 if lvl==5 else 19),
                "damage_dice": "1d8" if lvl==1 else ("2d8" if lvl==5 else "3d8"),
                "flat_damage": 1 if lvl==1 else (2 if lvl==5 else 3),
                "damage_type": "P",
                "range": 40,
                "ap_cost": 0,
                "traits": ["cartridge", "fatal_d10"],
                "ammo_capacity": 1,
                "reload_actions": 1,
                "allowed_environments": ["high_radiant", "low_radiant", "the_neither"]
            }
        ],
        "abilities": lambda lvl: {}
    },
    "Officer": {
        "archetype": "Officer",
        "hp_per_lvl": 8,
        "con_mod": [2, 2, 3],
        "ac": [16, 22, 29],
        "speed": 25,
        "max_ap": [4, 6, 8],
        "status": 3,
        "civil_legal": True,
        "civil_ac_pen": 0,
        "saves": {
            "fort": [7, 12, 19],
            "ref": [5, 10, 16],
            "will": [7, 13, 20]
        },
        "unarmed": {
            1: {"dice": "1d4", "bonus": 5, "flat": 1},
            5: {"dice": "1d4", "bonus": 9, "flat": 1},
            10: {"dice": "1d4", "bonus": 15, "flat": 2}
        },
        "weapons": lambda lvl: [
            {
                "name": "Officer's Sabre",
                "attack_bonus": 7 if lvl==1 else (13 if lvl==5 else 19),
                "damage_dice": "1d6" if lvl==1 else ("2d6" if lvl==5 else "3d6"),
                "flat_damage": 2 if lvl==1 else (3 if lvl==5 else 5),
                "damage_type": "S",
                "range": 0,
                "ap_cost": 0,
                "traits": ["finesse"],
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]
            },
            {
                "name": "Service Pistol",
                "attack_bonus": 6 if lvl==1 else (11 if lvl==5 else 17),
                "damage_dice": "1d8" if lvl==1 else ("2d8" if lvl==5 else "3d8"),
                "flat_damage": 1 if lvl==1 else (2 if lvl==5 else 3),
                "damage_type": "P",
                "range": 40,
                "ap_cost": 0,
                "traits": ["cartridge", "fatal_d10"],
                "ammo_capacity": 6,
                "reload_actions": 1,
                "allowed_environments": ["high_radiant", "low_radiant", "the_neither"]
            }
        ],
        "abilities": lambda lvl: {
            "armed_retainers": True,
            "retainer_count": 1 if lvl==1 else (2 if lvl==5 else 3),
            "retainer_hp": 12 if lvl==1 else (20 if lvl==5 else 32),
            "retainer_attack": 4 if lvl==1 else (7 if lvl==5 else 11),
            "retainer_damage_dice": "1d8" if lvl<10 else "2d8",
            "retainer_flat_damage": 1 if lvl==1 else (2 if lvl==5 else 3)
        }
    },
    "Noble": {
        "archetype": "Noble",
        "hp_per_lvl": 8,
        "con_mod": [0, 1, 2],
        "ac": [15, 21, 28],
        "speed": 25,
        "max_ap": [4, 6, 8],
        "status": 6,
        "civil_legal": True,
        "civil_ac_pen": 0,
        "saves": {
            "fort": [4, 9, 15],
            "ref": [6, 11, 18],
            "will": [8, 14, 21]
        },
        "unarmed": {
            1: {"dice": "1d4", "bonus": 4, "flat": 0},
            5: {"dice": "1d4", "bonus": 8, "flat": 0},
            10: {"dice": "1d4", "bonus": 13, "flat": 1}
        },
        "weapons": lambda lvl: [
            {
                "name": "Ancestral Fair Steel Rapier",
                "attack_bonus": 7 if lvl==1 else (13 if lvl==5 else 20),
                "damage_dice": "1d6" if lvl==1 else ("2d6" if lvl==5 else "3d6"),
                "flat_damage": 2 if lvl==1 else (3 if lvl==5 else 5),
                "damage_type": "P",
                "range": 0,
                "ap_cost": 0,
                "traits": ["deadly_d8", "disarm", "finesse"],
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]
            },
            {
                "name": "Elven Dueling Pistol",
                "attack_bonus": 6 if lvl==1 else (11 if lvl==5 else 17),
                "damage_dice": "1d8" if lvl==1 else ("2d8" if lvl==5 else "3d8"),
                "flat_damage": 1 if lvl==1 else (2 if lvl==5 else 3),
                "damage_type": "P",
                "range": 40,
                "ap_cost": 0,
                "traits": ["cartridge", "fatal_d10"],
                "ammo_capacity": 1,
                "reload_actions": 1,
                "allowed_environments": ["high_radiant", "low_radiant", "the_neither"]
            }
        ],
        "abilities": lambda lvl: {
            "armed_retainers": True,
            "retainer_count": 1 if lvl==1 else (2 if lvl==5 else 3),
            "retainer_hp": 12 if lvl==1 else (20 if lvl==5 else 35),
            "retainer_attack": 4 if lvl==1 else (7 if lvl==5 else 12),
            "retainer_damage_dice": "1d8" if lvl<10 else "2d8",
            "retainer_flat_damage": 1 if lvl==1 else (2 if lvl==5 else 3),
            "social_authority_bonus": 5
        }
    },
    "BlackMarketeer": {
        "archetype": "BlackMarketeer",
        "hp_per_lvl": 8,
        "con_mod": [1, 2, 2],
        "ac": [15, 21, 28],
        "speed": 25,
        "max_ap": [4, 6, 9],
        "status": 3,
        "civil_legal": True,
        "civil_ac_pen": 0,
        "saves": {
            "fort": [5, 10, 16],
            "ref": [8, 14, 21],
            "will": [7, 12, 19]
        },
        "unarmed": {
            1: {"dice": "1d4", "bonus": 5, "flat": 1},
            5: {"dice": "1d4", "bonus": 10, "flat": 1},
            10: {"dice": "1d4", "bonus": 16, "flat": 2}
        },
        "weapons": lambda lvl: [
            {
                "name": "Black-Market Stiletto",
                "attack_bonus": 7 if lvl==1 else (13 if lvl==5 else 19),
                "damage_dice": "1d4" if lvl==1 else ("2d4" if lvl==5 else "3d4"),
                "flat_damage": 3 if lvl==1 else (5 if lvl==5 else 8),
                "damage_type": "P",
                "range": 0,
                "ap_cost": 0,
                "traits": ["agile", "finesse", "deadly_d8"],
                "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]
            },
            {
                "name": "Bootleg Snub Cartridge Gun",
                "attack_bonus": 6 if lvl==1 else (12 if lvl==5 else 18),
                "damage_dice": "1d8" if lvl==1 else ("2d8" if lvl==5 else "3d8"),
                "flat_damage": 2 if lvl==1 else (3 if lvl==5 else 5),
                "damage_type": "P",
                "range": 30,
                "ap_cost": 0,
                "traits": ["cartridge", "fatal_d10", "concealed"],
                "ammo_capacity": 4,
                "reload_actions": 1,
                "allowed_environments": ["high_radiant", "low_radiant", "the_neither"]
            }
        ],
        "abilities": lambda lvl: {
            "armed_retainers": True,
            "retainer_count": 1 if lvl==1 else (2 if lvl==5 else 3),
            "retainer_hp": 12 if lvl==1 else (20 if lvl==5 else 32),
            "retainer_attack": 4 if lvl==1 else (7 if lvl==5 else 11),
            "retainer_damage_dice": "1d6" if lvl<10 else "2d6",
            "retainer_flat_damage": 1 if lvl==1 else (2 if lvl==5 else 3)
        }
    }
}

def generate_templates():
    out_dir = Path("ClockworkPathfinder/testing/combat_sim/templates")
    out_dir.mkdir(parents=True, exist_ok=True)
    
    levels = [1, 5, 10]
    lvl_idx_map = {1: 0, 5: 1, 10: 2}

    count = 0
    for class_name, spec in CLASS_SPECS.items():
        for lvl in levels:
            idx = lvl_idx_map[lvl]
            hp = 8 + (spec["hp_per_lvl"] * lvl) + (spec["con_mod"][idx] * lvl)
            ac = spec["ac"][idx]
            max_ap = spec["max_ap"][idx]
            
            unarmed_info = spec["unarmed"][lvl]
            
            data = {
                "name": f"{class_name} (Lv{lvl})",
                "archetype": class_name,
                "level": lvl,
                "hp": hp,
                "ac": ac,
                "fort": spec["saves"]["fort"][idx],
                "ref": spec["saves"]["ref"][idx],
                "will": spec["saves"]["will"][idx],
                "speed": spec["speed"],
                "max_ap": max_ap,
                "status": spec["status"],
                "civil_spire_legal": spec["civil_legal"],
                "civil_ac_penalty": spec["civil_ac_pen"],
                "unarmed_damage_dice": unarmed_info["dice"],
                "unarmed_bonus": unarmed_info["bonus"],
                "unarmed_flat_dmg": unarmed_info["flat"],
                "unarmed_traits": ["agile", "nonlethal"],
                "weapons": spec["weapons"](lvl),
                "abilities": spec["abilities"](lvl)
            }
            
            filename = f"{class_name.lower()}_lv{lvl}.json"
            filepath = out_dir / filename
            with open(filepath, 'w') as f:
                json.dump(data, f, indent=2)
            count += 1

    print(f"Generated {count} character templates in {out_dir}")

if __name__ == "__main__":
    generate_templates()

