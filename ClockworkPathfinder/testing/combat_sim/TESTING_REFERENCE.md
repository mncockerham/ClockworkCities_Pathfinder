# Combat Simulator Testing Architecture & Benchmark Reference

> **Directory:** `ClockworkPathfinder/testing/combat_sim/`  
> **Last Updated:** October 2026 (Exotic Save Creature & Neither-Tech Pulse Integration)

This document records the exact operational rules, architectural extensions, command patterns, and calibrated baseline findings for the **Combat Simulator** (`combat_sim.py`) to streamline future testing cycles.

---

## 1. Core Mechanics & Architecture Codified in `combat_sim.py`

### A. PF2e Saving Throw & Exotic Ability Engine
- **Method:** `Simulator._execute_save_ability(attacker, defender, weapon)`
- **4-Degree PF2e Logic:**
  - `Crit Success (diff >= +10)`: 0 damage.
  - `Success (diff >= 0)`: Half damage (`base_dmg // 2`).
  - `Failure (diff < 0)`: Full damage (`base_dmg`).
  - `Crit Failure (diff <= -10)`: Double damage (`base_dmg * 2`).
  - **Natural 20 / Natural 1:** Shifts degree up or down by 1 step.
- **Weapon Schema Fields:**
  - `save_type`: `'ref'`, `'fort'`, or `'will'` (triggers save resolution instead of AC attack roll).
  - `save_dc`: Integer DC (e.g. DC 20 for Lv 5, DC 26 for Lv 10).
  - `save_damage_dice`: String (e.g. `'3d8'`, `'6d8'`).
  - `save_flat_damage`: Integer flat bonus (e.g. 4, 8).
  - `action_cost`: AP/actions required (typically 2 for area attacks).
  - `cooldown_rounds`: Rounds between uses (0 = spammable every round).

### B. Neither-Tech Pulse Generators (Harmonic Defense)
- **JSON Object Key:** `abilities.pulse_defense` inside character templates:
  ```json
  "pulse_defense": {
    "name": "Tier 1 Agile Shunt Node",
    "ap_cost": 1,
    "ref_bonus": 3,
    "ref_dr": 2,
    "fort_bonus": 0,
    "fort_dr": 0,
    "will_bonus": 0,
    "will_dr": 0,
    "civil_spire_legal": false
  }
  ```
- **Rules Enforced in Code:**
  1. **Reactive AP Cost (Min 1):** Triggered against incoming saving throw attacks; character must possess unspent AP.
  2. **Zero AC Impact:** Does not alter physical AC or trigger on physical attacks (`B`, `P`, `S`).
  3. **Mutual Shield Exclusion:** Automatically suppressed if `shield_block: true` or `shield_hp > 0`.
  4. **Two-Handed Weapon / Rifle Incompatibility:** Suppressed if `active_weapon_is_two_handed` is true.
  5. **Civil Spire Ban:** Suppressed in `civil_spire` environment unless explicitly marked legal.
  6. **Vector-Specific Damage Reduction (DR):** Pulse DR only applies against the matching save vector (Reflex, Fortitude, or Will). Mismatched saves receive 0 bonus and 0 DR.

---

## 2. Creature Template Roster

Creatures live in `ClockworkPathfinder/testing/combat_sim/creatures/`.

### A. Physical Wilderness Fauna (Brute / Melee)
- `creature_bear_lv*.json` (Levels 1, 3, 5, 7, 10): High HP, high physical melee damage, low AC.
- `creature_wolf_pack_lv*.json`: Pack tactics, high mobility, agile piercing damage.
- Both **Berserk** (fight to 0 HP) and **Flee** (flee at 50% HP) variants exist.

### B. Exotic Saving Throw Creatures (Levels 1, 3, 5, 7, 10)
- **Acid Spitter (`creature_acid_spitter_*.json`):**
  - Save: **Reflex** (Dexterity).
  - Damage: Acid / Corrosive burst.
  - Lv 5: DC 20, `3d8+4` acid. Lv 10: DC 26, `6d8+8` acid.
- **Spore Sprayer (`creature_spore_sprayer_*.json`):**
  - Save: **Fortitude** (Constitution).
  - Damage: Toxic / Biological pulmonary spores.
  - Lv 5: DC 20, `3d8+4` poison. Lv 10: DC 26, `6d8+8` poison.
- **Disorientor (`creature_disorientor_*.json`):**
  - Save: **Will** (Wisdom).
  - Damage: Non-Lethal psychic / neural shockwave.
  - Lv 5: DC 20, `3d8+4` mental. Lv 10: DC 26, `6d8+8` mental.

---

## 3. Calibrated Benchmark Baselines

### A. The "Encounter Reduction" Rule for Wilderness Exploration
- When evaluating wilderness survival for backline / technical classes (e.g. Scholar, Artisan):
  - **Equal-Level 1v1 Duels (Lv 5 vs Lv 5):** Technical classes win 15% to 35% of fights, lasting ~2.8 to 3.2 rounds.
  - **-2 to -3 Level Reduction (Standard Wilderness Exploration Encounter):**
    - Lv 5 Scholar vs Lv 3 Creature: **92% to 94% win rate** in Flee mode.
    - Lv 10 Scholar vs Lv 7 Creature: **91% to 93% win rate** in Flee mode.
  - *Design Rule:* Always test backline survival with a -2 to -3 level buffer when simulating standard travel hazards, or test in party composition rather than 1v1.

### B. Survival Impact of Pulse Devices
- **Death Round Extension on Loss:** Extends survival by **+0.25 to +0.50 rounds** for squishy classes (Scholar), and **+0.10 to +0.20 rounds** for sturdy classes (Engineer).
- **Win Rate Gain:** Translates to **+3% to +5% win rate** for Scholar, and **+9% to +12% win rate** for Clockwork Engineer against matched threats.
- **Party Multiplier:** In a 4-PC party, a +0.5 round delay before dropping buys **3 to 9 additional ally actions**, turning party wipes into tactical victories.

---

## 4. Key CLI Commands & Validation Scripts

### Run Template Validation
Always run before starting simulations to verify schema compliance:
```powershell
python ClockworkPathfinder/testing/combat_sim/validate_templates.py
```

### Standard Head-to-Head Duel
```powershell
python ClockworkPathfinder/testing/combat_sim/combat_sim.py --char_a ClockworkPathfinder/testing/combat_sim/templates/scholar_lv5.json --char_b ClockworkPathfinder/testing/combat_sim/creatures/creature_acid_spitter_flee_lv5.json --env low_radiant --iters 500
```

### Batch Audits & Generator Scripts
- `generate_save_creatures.py`: Regenerates all 30 exotic saving throw creature templates across levels 1, 3, 5, 7, 10.
- `generate_1v1_creatures.py`: Generates physical bear/wolf templates.
- `run_wilderness_gauntlet.py`: Runs multi-thousand battle matrix across all classes and environments.

