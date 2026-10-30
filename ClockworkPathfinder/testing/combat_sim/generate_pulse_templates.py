import json
from pathlib import Path

# Template directory
TMPL_DIR = Path("ClockworkPathfinder/testing/combat_sim/templates")

# ==============================================================================
# NEITHER-TECH PULSE DEFENSE ITEMS
# Replaces shield as 3rd item slot; non-military (civilian legal); costs AP
# Free activation on turn if character has unspent AP.
#
# Variants tested:
# 1. Harmonic Mind-Anchor (Will +3, AC +1, AP 1) -> Counter to Disorientors
# 2. Galvanic Aegis Pulse (AC +2, Ref +2, Fort +1, AP 1) -> General balanced pulse
# 3. Bulwark Resonance Core (AC +3, Fort +2, AP 1) -> Heavy kinetic/acid defense
# ==============================================================================

VARIANTS = {
    # Soldier with Harmonic Mind-Anchor
    "soldier_mind_anchor": {
        "base": "soldier_lv5.json",
        "name": "Soldier (Lv5 - Mind Anchor Pulse)",
        "remove_shield": True,
        "pulse_defense": {
            "name": "Harmonic Mind-Anchor",
            "ap_cost": 1,
            "ac_bonus": 1,
            "fort_bonus": 0,
            "ref_bonus": 0,
            "will_bonus": 3
        }
    },
    # Soldier with Galvanic Aegis (Balanced)
    "soldier_galvanic_pulse": {
        "base": "soldier_lv5.json",
        "name": "Soldier (Lv5 - Galvanic Pulse)",
        "remove_shield": True,
        "pulse_defense": {
            "name": "Galvanic Aegis Pulse",
            "ap_cost": 1,
            "ac_bonus": 2,
            "fort_bonus": 1,
            "ref_bonus": 2,
            "will_bonus": 1
        }
    },
    # Scholar with Resonant Mind-Anchor (Will +4, AC +1, AP 1)
    "scholar_mind_anchor": {
        "base": "scholar_lv5.json",
        "name": "Scholar (Lv5 - Mind Anchor Pulse)",
        "remove_shield": False,
        "pulse_defense": {
            "name": "Resonant Mind-Anchor",
            "ap_cost": 1,
            "ac_bonus": 1,
            "fort_bonus": 0,
            "ref_bonus": 0,
            "will_bonus": 4
        }
    },
    # Pugilist with Galvanic Pulse (AC +2, Ref +2, Fort +1, Will +1, AP 1)
    "pugilist_galvanic_pulse": {
        "base": "pugilist_lv5.json",
        "name": "Pugilist (Lv5 - Galvanic Pulse)",
        "remove_shield": False,
        "pulse_defense": {
            "name": "Galvanic Aegis Pulse",
            "ap_cost": 1,
            "ac_bonus": 2,
            "fort_bonus": 1,
            "ref_bonus": 2,
            "will_bonus": 1
        }
    }
}

def generate_pulse_test_templates():
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

    print(f"Generated {len(created)} Pulse Defense test templates in {TMPL_DIR}:")
    for c in created:
        print(f"  - {c}")

if __name__ == "__main__":
    generate_pulse_test_templates()

