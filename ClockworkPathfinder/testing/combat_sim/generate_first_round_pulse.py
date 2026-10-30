import json
from pathlib import Path

TMPL_DIR = Path("ClockworkPathfinder/testing/combat_sim/templates")

# ==============================================================================
# PULSE GENERATOR FIRST-ROUND TEST SUITE (ARMOR-EQUIVALENT DEFENSES)
#
# Rules:
# 1. Base AP cost is boosted by +2 (e.g. Base 3 AP).
# 2. Designated Technical/Academic classes (Scholar, Engineer, Mad Bomber, Artisan)
#    have the matching Technical/Clandestine discipline tag giving a -2 AP discount,
#    meaning they activate it at 1 AP (3 - 2 = 1 AP).
# 3. Untagged physical martial classes (Soldier, Pugilist) must pay the full 3 AP.
# 4. Bonuses are roughly equivalent to armor (+3 to +4 AC, or +3 to +4 Saves).
# ==============================================================================

VARIANTS = {
    # 1. SCHOLAR (Tagged: 3 AP - 2 Tag Discount = 1 AP per trigger)
    # Armed with Tier 1 Kinetic Deflection Brooch (+3 AC)
    "scholar_pulse_kinetic": {
        "base": "scholar_lv5.json",
        "name": "Scholar (Lv5 - Kinetic Pulse +3 AC)",
        "remove_shield": False,
        "pulse_defense": {
            "name": "Kinetic Deflection Brooch",
            "base_ap_cost": 3,
            "has_discipline_tag": True,
            "ap_cost": 1,  # 3 - 2 = 1 AP
            "ac_bonus": 3,
            "fort_bonus": 0,
            "ref_bonus": 0,
            "will_bonus": 0
        }
    },
    # 2. SCHOLAR (Tagged: 1 AP per trigger)
    # Armed with Tier 1 Harmonic Mind-Anchor (+3 Will, +1 AC)
    "scholar_pulse_mind": {
        "base": "scholar_lv5.json",
        "name": "Scholar (Lv5 - Mind Anchor Pulse)",
        "remove_shield": False,
        "pulse_defense": {
            "name": "Harmonic Mind-Anchor",
            "base_ap_cost": 3,
            "has_discipline_tag": True,
            "ap_cost": 1,  # 3 - 2 = 1 AP
            "ac_bonus": 1,
            "fort_bonus": 0,
            "ref_bonus": 0,
            "will_bonus": 3
        }
    },
    # 3. CLOCKWORK ENGINEER (Tagged: 1 AP per trigger)
    # Armed with Tier 1 Balanced Ward (+2 AC, +1 Fort, +1 Ref, +1 Will)
    "engineer_pulse_balanced": {
        "base": "clockworkengineer_lv5.json",
        "name": "Engineer (Lv5 - Balanced Ward Pulse)",
        "remove_shield": False,
        "pulse_defense": {
            "name": "Balanced Ward Node",
            "base_ap_cost": 3,
            "has_discipline_tag": True,
            "ap_cost": 1,  # 3 - 2 = 1 AP
            "ac_bonus": 2,
            "fort_bonus": 1,
            "ref_bonus": 1,
            "will_bonus": 1
        }
    },
    # 4. SOLDIER (Untagged Physical Class: Pays full 3 AP per trigger!)
    # Tests power drain / attack attrition when an untagged class tries to use pulse
    "soldier_pulse_untagged": {
        "base": "soldier_lv5.json",
        "name": "Soldier (Lv5 - Untagged 3 AP Pulse)",
        "remove_shield": True,
        "pulse_defense": {
            "name": "Kinetic Deflection Brooch (Untagged)",
            "base_ap_cost": 3,
            "has_discipline_tag": False,
            "ap_cost": 3,  # Full 3 AP cost!
            "ac_bonus": 3,
            "fort_bonus": 0,
            "ref_bonus": 0,
            "will_bonus": 0
        }
    }
}

def generate_first_round_pulse_templates():
    created = []
    for k, spec in VARIANTS.items():
        base_path = TMPL_DIR / spec["base"]
        with open(base_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        data["name"] = spec["name"]
        if spec.get("remove_shield", False):
            data["abilities"]["shield_block"] = False
            data["abilities"]["shield_hp"] = 0
            data["abilities"]["shield_hardness"] = 0

        data["abilities"]["pulse_defense"] = spec["pulse_defense"]

        out_path = TMPL_DIR / f"{k}.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        created.append(f"{k}.json")

    print(f"Generated {len(created)} calibrated pulse testing templates in {TMPL_DIR}:")
    for c in created:
        print(f"  - {c}")

if __name__ == "__main__":
    generate_first_round_pulse_templates()

