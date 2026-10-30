# Clockwork Cities — Automated Combat Simulator

A lightweight Python Monte Carlo battle simulator for testing 1v1 combat balance across the four core environments in **Clockwork Cities Pathfinder**:
1. `civil_spire` (Disarmament laws active; unarmored/light clothing, legal dueling rapiers/fists/clubs only, firearms strictly banned, armed retainers active for Nobles/Wall Merchants).
2. `high_radiant` (Warrens & Dynamo Grids: 100% wireless induction saturation, high-damage arc weaponry, continuous force barriers, zero disarmament).
3. `low_radiant` (Airships & Walled Perimeters: Stepped-down radiant weapons, open firearm carry, martial competitive balance).
4. `the_neither` (Outland & Wilderness: Zero wireless power, cartridge scarcity, heavy martial and shield dominance).

---

## 1. Quick Start

Run a 100-match simulation between any two character JSON templates in any environment:

```powershell
python ClockworkPathfinder/testing/combat_sim/combat_sim.py --char_a ClockworkPathfinder/testing/combat_sim/pugilist_lv5.json --char_b ClockworkPathfinder/testing/combat_sim/soldier_lv5.json --env civil_spire --iters 100
```

### Command-Line Arguments
- `--char_a <path>`: Path to JSON template for Combatant A.
- `--char_b <path>`: Path to JSON template for Combatant B.
- `--env <env>`: One of `civil_spire`, `high_radiant`, `low_radiant`, `the_neither` (default: `low_radiant`).
- `--iters <int>`: Number of battle rounds to simulate (default: `100`).
- `--dist <int>`: Initial starting distance in feet (default: `40`).

---

## 2. Outcome Spectrum (Relative to Character A)

Every simulation generates a win/loss breakdown categorized by remaining HP margin:
- **Clear Win:** Char A wins with $> 60\%$ HP remaining.
- **Moderate Win:** Char A wins with $35\%\text{--}60\%$ HP remaining.
- **Close Win:** Char A wins with $10\%\text{--}35\%$ HP remaining.
- **Too Close to Call:** Either combatant wins with $< 10\%$ HP remaining, or a draw occurs.
- **Minor Defeat:** Char B wins with $10\%\text{--}35\%$ HP remaining.
- **Major Defeat:** Char B wins with $35\%\text{--}60\%$ HP remaining.
- **Clear Defeat:** Char B wins with $> 60\%$ HP remaining.

---

## 3. Character JSON Template Structure

Character files live in this directory. You can add or modify any character:

```json
{
  "name": "Corbin Hall",
  "archetype": "Soldier",
  "level": 5,
  "hp": 73,
  "ac": 24,
  "fort": 13,
  "ref": 10,
  "will": 10,
  "speed": 20,
  "max_ap": 6,
  "status": 2,
  "civil_spire_legal": false,
  "civil_ac_penalty": -5,
  "unarmed_damage_dice": "1d4",
  "unarmed_bonus": 11,
  "unarmed_flat_dmg": 4,
  "unarmed_traits": ["agile", "nonlethal"],
  "weapons": [
    {
      "name": "Master High-Tensile Broadsword",
      "attack_bonus": 15,
      "damage_dice": "2d8",
      "flat_damage": 4,
      "damage_type": "S",
      "range": 0,
      "ap_cost": 0,
      "traits": ["versatile_p"],
      "allowed_environments": ["high_radiant", "low_radiant", "the_neither"]
    }
  ],
  "abilities": {
    "shield_block": true,
    "shield_hardness": 7,
    "shield_hp": 30,
    "shield_raised_ac_bonus": 2,
    "pulse_defense": {
      "name": "Tier 1 Agile Shunt Node",
      "ap_cost": 1,
      "ref_bonus": 3,
      "ref_dr": 2,
      "civil_spire_legal": false
    }
  }
}
```

For in-depth testing methodology, exotic creature save mechanics, Neither-tech pulse defense rules, and benchmark survival baselines, see [TESTING_REFERENCE.md](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/testing/combat_sim/TESTING_REFERENCE.md).

