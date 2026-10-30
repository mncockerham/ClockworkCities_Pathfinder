# Clockwork Cities — Combat Template Creation Guide

This guide details how to build, scale, and update character and creature JSON templates for the **Automated Combat & Environmental Simulator** (`combat_sim.py`).

---

## 1. File Naming & Directory Conventions

- **Player Classes:** Store in `ClockworkPathfinder/testing/combat_sim/templates/`
  - Pattern: `<classname_lowercase>_lv<level>.json`
  - Examples: `soldier_lv1.json`, `pugilist_lv5.json`, `clockworkengineer_lv10.json`
- **Creatures & Mutants:** Store in `ClockworkPathfinder/testing/combat_sim/creatures/`
  - Pattern: `<species>_<template>_lv<level>.json`
  - Examples: `bear_brute_lv5.json`, `wolf_stalker_lv10.json`

---

## 2. Core Template Structure & Math Guidelines

Every template must validate against [`template_schema.json`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/testing/combat_sim/template_schema.json).

### A. Health & Trauma Bands
$$\text{Hit Points} = \text{Ancestry Base (8)} + (\text{Class Base HP} \times \text{Level}) + (\text{Con Mod} \times \text{Level})$$
- **Level 1 HP Baseline:** Typically `15` (Scholar/Noble) to `21` (Soldier/Pugilist/Dwarf).
- **Level 5 HP Baseline:** Typically `45–55` (Influencers/Scholars) to `65–75` (Martials).
- **Level 10 HP Baseline:** Typically `95–115` (Influencers) to `140–160` (Martials).

### B. Defenses & Environmental Armors
- **Base Armor Class (Standard Environments):**
  - Light Armor / Agile Unarmored: AC $15\text{--}16$ (Lv1), $21\text{--}22$ (Lv5), $28\text{--}29$ (Lv10).
  - Heavy Armor (Soldier): AC $18$ (Lv1), $24$ (Lv5), $31$ (Lv10).
- **`civil_spire_legal` (Boolean):**
  - Set to `true` if character uses unarmored/light clothing, legal Fair Steel rapiers, fists, canes, or walking sticks.
  - Set to `false` if character relies on medium armor, heavy plate, longarms, visible clockwork rigs, or ordnance.
- **`civil_ac_penalty`:**
  - When a `civil_spire_legal: false` character enters `civil_spire`, municipal disarmament laws strip illegal armor down to civilian tunics:
    - Medium Armor stripped: `-3 AC`
    - Heavy Plate stripped: `-5 AC`

### C. Attacks & Weapon Scaling by Level

| Level | Weapon Tier | Attack Bonus (Trained/Expert/Master) | Melee Damage Dice | Ranged / Cartridge Dice |
|:---:|:---:|:---:|:---:|:---:|
| **Level 1** | Mundane / Standard | $+6 \text{ to } +9$ | `1d6` to `1d8` | `1d8` to `1d10` |
| **Level 5** | +1 Striking | $+11 \text{ to } +15$ | `2d6` to `2d8` | `2d8` to `2d10` |
| **Level 10** | +2 Greater Striking | $+18 \text{ to } +22$ | `3d6` to `3d8` | `3d8` to `3d10` |

### D. Weapon Environmental Activation

Weapons only function in their designated `allowed_environments`:
- `civil_spire`: Mundane steel rapiers, fists, brass knuckles, daggers, canes, shop hammers. **Firearms and radiant arc emitters are illegal and disabled.**
- `high_radiant`: Wireless saturated grid. Arc Projectors and Resonators deal maximum damage (`1d12` / `2d12` / `3d12` + `deadly_d10`). 
- `low_radiant`: Airships & perimeters. Stepped-down radiant weapons (`1d8` / `2d8` / `3d8`) and cartridge firearms operate freely.
- `the_neither`: Deep wilderness. **Radiant energy weapons do NOT function (zero power).** Cartridge weapons are active but consume ammunition (`ammo_capacity`). Bows, crossbows, and martial steel dominate.

---

## 3. Supported Ability Keys

Include any relevant abilities in the `"abilities"` block:

1. **`flurry_of_blows` (bool):** Allows 2 unarmed attacks for 1 action cost (Pugilist).
2. **`damage_resistance_physical` (int):** Flat damage reduction subtracted from all physical kinetic damage (e.g., `2` for Lv5 Pugilist, `6` for Lv10 Brute Bear).
3. **`shield_block` (bool), `shield_hardness` (int), `shield_hp` (int):**
   - Enables Raise Shield (+2 circumstance AC).
   - Reaction absorbs damage equal to `shield_hardness`; excess damages `shield_hp`.
4. **`radiant_barrier` (bool), `barrier_temp_hp_high` (int), `barrier_temp_hp_low` (int):**
   - Inductive energy shield granting regenerating Temp HP in High Radiant and Low Radiant environments.
5. **`armed_retainers` (bool), `retainer_count` (int), `retainer_hp` (int), `retainer_attack` (int), `retainer_damage_dice` (str), `retainer_flat_damage` (int):**
   - Models liveried bodyguards for Nobles, Wall Merchants, and Officers.
   - Retainers intercept **50% of incoming damage** targeted at their employer until destroyed, and deliver counter-attacks on the employer's turn.
6. **`feral_adrenaline_surge` (bool), `surge_temp_hp` (int):**
   - Brute corruption adrenaline rush granting bonus temporary HP at the start of battle.

---

## 4. Example Template (Boilerplate)

```json
{
  "name": "Class Name (Lv5)",
  "archetype": "ClassName",
  "level": 5,
  "hp": 58,
  "ac": 21,
  "fort": 10,
  "ref": 12,
  "will": 11,
  "speed": 25,
  "max_ap": 6,
  "status": 2,
  "civil_spire_legal": true,
  "civil_ac_penalty": 0,
  "unarmed_damage_dice": "1d4",
  "unarmed_bonus": 9,
  "unarmed_flat_dmg": 1,
  "unarmed_traits": ["agile", "nonlethal"],
  "weapons": [
    {
      "name": "+1 Striking Sabre",
      "attack_bonus": 13,
      "damage_dice": "2d6",
      "flat_damage": 3,
      "damage_type": "S",
      "range": 0,
      "ap_cost": 0,
      "traits": ["finesse"],
      "allowed_environments": ["civil_spire", "high_radiant", "low_radiant", "the_neither"]
    }
  ],
  "abilities": {}
}
```

---

## 5. Automated Bulk Generation

To add a new class or re-tune existing classes across Levels 1, 5, and 10:
1. Open [`generate_all_templates.py`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/testing/combat_sim/generate_all_templates.py).
2. Add or modify the class definition in `CLASS_SPECS`.
3. Run:
   ```powershell
   python ClockworkPathfinder/testing/combat_sim/generate_all_templates.py
   ```
4. All corresponding JSON templates will be updated and validated automatically.

