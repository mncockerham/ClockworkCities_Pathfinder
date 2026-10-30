"""
Template Validator Script for Clockwork Cities Combat Simulator
Scans all JSON files in templates/ and creatures/ to ensure schema compliance,
valid dice strings, environment tagging, and attribute bounds.
"""

import json
import re
from pathlib import Path

DICE_REGEX = re.compile(r"^[0-9]+d[0-9]+$")
ALLOWED_ENVS = {"civil_spire", "high_radiant", "low_radiant", "the_neither"}
REQUIRED_FIELDS = [
    "name", "archetype", "level", "hp", "ac", "fort", "ref", "will",
    "speed", "max_ap", "status", "civil_spire_legal", "civil_ac_penalty",
    "unarmed_damage_dice", "unarmed_bonus", "unarmed_flat_dmg",
    "weapons", "abilities"
]

def validate_file(path: Path) -> list:
    errors = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        return [f"JSON Parse Error: {e}"]

    # Required top-level fields
    for field in REQUIRED_FIELDS:
        if field not in data:
            errors.append(f"Missing required field: '{field}'")

    # Value range checks
    if "level" in data and not (1 <= data["level"] <= 20):
        errors.append(f"Level must be 1-20, got {data['level']}")
    if "hp" in data and data["hp"] <= 0:
        errors.append(f"HP must be > 0, got {data['hp']}")
    if "ac" in data and data["ac"] < 10:
        errors.append(f"AC must be >= 10, got {data['ac']}")
    if "speed" in data and data["speed"] <= 0:
        errors.append(f"Speed must be > 0, got {data['speed']}")

    # Unarmed dice format
    if "unarmed_damage_dice" in data and not DICE_REGEX.match(data["unarmed_damage_dice"]):
        errors.append(f"Invalid unarmed dice format: '{data['unarmed_damage_dice']}'")

    # Weapons validation
    weapons = data.get("weapons", [])
    if not isinstance(weapons, list):
        errors.append("'weapons' must be a list")
    else:
        for idx, w in enumerate(weapons):
            w_name = w.get("name", f"Weapon #{idx}")
            if "damage_dice" in w and not DICE_REGEX.match(w["damage_dice"]):
                errors.append(f"{w_name}: Invalid damage dice '{w['damage_dice']}'")
            envs = w.get("allowed_environments", [])
            for env in envs:
                if env not in ALLOWED_ENVS:
                    errors.append(f"{w_name}: Unknown environment '{env}'")

    return errors

def main():
    root = Path("ClockworkPathfinder/testing/combat_sim")
    dirs = [root / "templates", root / "creatures"]
    
    total_files = 0
    passed = 0
    failed = 0

    print("=" * 65)
    print("VALIDATING COMBAT SIMULATOR TEMPLATES")
    print("=" * 65)

    for d in dirs:
        if not d.exists():
            continue
        for p in sorted(d.glob("*.json")):
            total_files += 1
            errs = validate_file(p)
            if errs:
                failed += 1
                print(f"[FAIL] {p.name}:")
                for err in errs:
                    print(f"       - {err}")
            else:
                passed += 1

    print("-" * 65)
    print(f"Total Scanned: {total_files} | Passed: {passed} | Failed: {failed}")
    if failed == 0:
        print("ALL TEMPLATES VALIDATED SUCCESSFULLY!")
    print("=" * 65)

if __name__ == "__main__":
    main()

