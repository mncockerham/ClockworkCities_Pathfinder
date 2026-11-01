# Bombardier Skill & Reaction Manifolds

- **Topic:** The Bombardier Skill, Specialized Grenade Synthesizers/Dispensers, Ballistics, and Spell-Equivalent Ordnance
- **Location:** `ClockworkPathfinder/Rules/Bombardier.md`
- **Primary Classes:** Influence Classes (**Noble**, **Merchant**, **Grey Marketeer**)
- **Core Concept:** In a world without supernatural spellcasters, incredibly expensive miniaturized clockwork-chemical devices exist that synthesize, prime, and safely store specialized tactical grenades. These deliver area-of-effect and single-target attacks (poison clouds, incendiaries, static discharges, high explosives, blinding flashes, and debilitating chemical debuffs). Instead of magical incantations, the character uses the **Bombardier** skill to calculate trajectory, prime the payload, and set the detonation threshold.

---

## 1. The Bombardier Proficiency Tracks & Class Access

Bombardier advances along structured proficiency tracks depending on class role, representing access to institutional patronage, laboratories, and specialized reaction manifolds:

### Track A: Primary Influence Classes (Noble, Merchant, Grey Marketeer)
*Full 1–20 Progression (Wizard Spellcasting Parity)*
- **Trained (Level 1):** Unlocks **1 chosen effect profile**; dispenser stabilizes **3 grenade slots per effect**. Reservoir stores **15 total charges** ($5 \times \text{Capacity}$). You can create and hold only Tier 1 grenades.
- **Expert (Level 7):** Unlocks **2 chosen effect profiles**; dispenser capacity increases to **4 grenade slots per effect** (up to 8 ready grenades). Reservoir stores **20 total charges per effect** ($5 \times \text{Capacity}$). You can create and hold grenades up to Tier 2.
- **Master (Level 15):** Unlocks **3 chosen effect profiles**; dispenser capacity increases to **5 grenade slots per effect** (up to 15 ready grenades). Reservoir stores **25 total charges per effect** ($5 \times \text{Capacity}$). You can create and hold grenades up to Tier 3.
- **Legendary (Level 19):** Unlocks **4 chosen effect profiles**; dispenser capacity increases to **6 grenade slots per effect** (up to 24 ready grenades). Reservoir stores **30 total charges per effect** ($5 \times \text{Capacity}$). You can create and hold grenades up to Tier 4.

---

### Track B: Technical & Scholastic Specialists (Clockwork Engineer, Scholar, Artisan)
*Delayed Start & Capped Progression (Boosting Technical Specialists)*
Technical classes gain access to Bombardier through university research, guild workshops, and precision machining, but begin their training later than high-society patrons and cap at Expert or Master:
- **Starting Level (Trained):** Begins at **Level 3** (or Level 5 depending on class feature/archetype dedication). Unlocks **1 chosen effect profile** with **3 ready slots** and a 15-charge reservoir. You can create and hold only Tier 1 grenades.
- **Expert (Level 9 or 11):** Unlocks **2 chosen effect profiles** with **4 ready slots each** (8 total ready grenades) and 40 reservoir charges. You can create and hold grenades up to Tier 2.
- **Master (Level 17, Scholar/Engineer Cap):** Unlocks **3 chosen effect profiles** with **5 ready slots each** (15 total ready grenades) and 75 reservoir charges. You can create and hold grenades up to Tier 3. *(Artisans cap at Expert; Scholars and Clockwork Engineers can reach Master; neither can reach Legendary without an Influence Class)*.

---

### Track C: Influence Archetypes (Multiclass Dedication)
*Archetype Progression for Other Classes (Capped at Expert)*
Characters of other classes (such as Soldiers, Inspectors, or Dandies) who take an **Influence Archetype** (Noble Dedication, Merchant Dedication, or Grey Marketeer Dedication) can gain access to Bombardier through their new social sponsor:
- **Archetype Dedication (Feat 4 or 6):** Grants **Trained** proficiency in Bombardier and an issued baseline Reaction Manifold (1 Effect Profile, 3 ready slots, 15-charge reservoir). You can create and hold only Tier 1 grenades.
- **Advanced Munitions Feat (Feat 12):** Upgrades proficiency to **Expert** (2 Effect Profiles, 4 ready slots each, 40-charge reservoir). You can create and hold grenades up to Tier 2.
- **Strict Cap:** Archetype access is **strictly capped at Expert**. They cannot reach Master or Legendary without full primary class progression.

---

### Progression Summary Table

| Class Track                                               |   Trained    |   Expert    |    Master    |  Legendary   | Max Effects / Max Ready Slots  |
| --------------------------------------------------------- | :----------: | :---------: | :----------: | :----------: | :----------------------------: |
| **Primary Influence** (*Noble, Merchant, Grey Marketeer*) |   **Lv 1**   |  **Lv 7**   |  **Lv 15**   |  **Lv 19**   | 4 Profiles / 24 Ready Grenades |
| **Scholars & Clockwork Engineers**                        |   **Lv 3**   |  **Lv 9**   |  **Lv 17**   | — *(Capped)* | 3 Profiles / 15 Ready Grenades |
| **Artisans**                                              |   **Lv 5**   |  **Lv 11**  | — *(Capped)* | — *(Capped)* | 2 Profiles / 8 Ready Grenades  |
| **Influence Archetypes** (*Dedication Feats*)             | **Feat 4/6** | **Feat 12** | — *(Capped)* | — *(Capped)* | 2 Profiles / 8 Ready Grenades  |

### Manifold Reaction Selection (Dual & Triple Effect Generation)
Rather than locking a dispenser slot into a single rigid payload, the internal pneumatic manifold expands to synthesize alternative reactive payloads for each tier:
- **Maximum Grenade Tier:** Your Bombardier proficiency rank limits the highest-tier grenades you can create, load, or hold: Trained allows Tier 1, Expert Tier 2, Master Tier 3, and Legendary Tier 4. You can still create and hold grenades of any lower tier you have unlocked.
- **Level 1 (Single Effect):** The Tier 1 generator stabilizes 1 chosen chemical reaction (e.g., *Concentrated Acid*).
- **Level 3 (Dual Reaction Generator — Tier 1):** The Tier 1 manifold expands to store **2 distinct reactions**. When drawing a Tier 1 ready grenade, the Bombardier chooses which of the 2 reactions to prime and toss.
- **Level 5 (Triple Reaction Generator — Tier 1):** The Tier 1 manifold expands to store **3 distinct reactions** (e.g., choosing on use between *Acid*, *Shrapnel*, or *Rime Pellet*).
- **Level 7 (Tier 2 Unlocked — Single Reaction):** Unlocks Tier 2 payloads with 1 chosen reaction (e.g., *Fireball*).
- **Level 9 (Dual Reaction Generator — Tier 2):** The Tier 2 manifold expands to store **2 distinct reactions**.
- **Level 11 (Triple Reaction Generator — Tier 2):** The Tier 2 manifold expands to store **3 distinct reactions**.
- **Level 15 (Tier 3 Unlocked — Single Reaction):** Unlocks Tier 3 payloads with 1 chosen reaction.
- **Level 17 (Dual Reaction Generator — Tier 3):** The Tier 3 manifold expands to store **2 distinct reactions**.
- **Level 19 (Tier 4 Unlocked — Dual Reaction):** Unlocks Tier 4 apex payloads with 2 distinct reactions; Tier 3 expands to **3 distinct reactions**.
- **Level 20 (Apex Masterwork — Triple Reaction All Tiers):** The Tier 4 manifold achieves masterwork calibration, expanding to **3 distinct reactions**. At Level 20, **every active tier (Tiers 1, 2, 3, and 4) offers 3 distinct effects on use**.

#### Choosing & Reconfiguring Stored Reactions (Workshop, Supply Lines & Military Logistics)
- **Selection by Dispenser Tier (1 to 3 Items):** Depending on the dispenser\'s calibration and character level, players choose the **1 to 3 items** it makes for each active tier manifold (e.g. 1 at Lv 1, 2 at Lv 3, 3 at Lv 5).
- **Workshop & Raw Materials Requirement:** Changing a configured reaction is not a simple field swap; it requires **direct access to a proper workshop and raw materials for the new items, including the specific empty grenade casings and chemical catalysts**.
- **Spire Ease vs. Remote Locations:**
  - **In a Spire / Guild Home Base:** This reconfiguration is easily done at your sponsoring Guildhouse, Great House armory, or Wall Merchant estate. Materials and specialized casings are provided as normal operational gear support (money is not an issue), provided your guild/family has access and your level meets the tier requirement.
  - **Guild-Controlled Outposts (Pre-Arranged Logistics):** Changes can also be made at remote branch offices or forward holdings controlled by the Guild or Family, provided **advance arrangements were made for the specific replacement casings and reagents to be shipped there**.
  - **The Field Restriction (No Field Swapping / Reloading):** Swapping configured abilities or reloading depleted reservoirs is **not normally available in the field** unless **military-level logistical support has been explicitly arranged** (such as an accompanied heavy military supply wagon, forward mobile ordnance workshop, or airship quartermaster tender). Out in the sumps, ruins, or deep wild without such military logistics, a Bombardier is strictly locked to what they carried.

---

### Device Architecture (Single Modular Chassis vs. Multiple Linked Dispensers)
- **Modular Multi-Chamber Housing:** A high-level dispenser can be engineered as a single, multi-valved brass harness worn across the chest or belt, with independent pneumatic pressurized chutes for each unlocked effect profile. Alternatively, a Bombardier may carry separate linked canister modules clipped into a master priming rig. Either way, the total ready slots and consumable reservoirs are maintained per effect.

### Bombardier DC Calculation
When a grenade detonates, targets in the area of effect roll saving throws against the user's **Bombardier DC**:
$$\mathbf{\text{Bombardier DC}} = 10 + \text{Key Attribute Modifier} + \text{Bombardier Proficiency Bonus}$$
*(Proficiency Bonus: Trained = Level + 2, Expert = Level + 4, Master = Level + 6, Legendary = Level + 8)*.  
- Key Attribute: **Intelligence** (calculation, chemical precision) or **Charisma** (as designated by class feature).

---

## 2. Standardized Reaction Manifolds Across All Users

The physical devices themselves are **standardized across all individuals trained in the skill**. Rather than forcing different classes to carry different mechanical contraptions, every Reaction Manifold operates under the exact same standardized engineering:
- **Universal Chassis & Spell-Level Restrictions:** The physical dispenser is identical whether wielded by a Grand Duke, an underground Grey Marketeer, a University Scholar, or an Artisan. What dictates what the device can do is strictly the user's **Bombardier proficiency rank and character level**, which limits the spell-rank equivalence of the synthesized payloads.
- **Unreachable Market Cost:** These devices represent the pinnacle of clockwork miniaturization, hermetic pneumatic valves, and stabilized catalytic chemistry. On the open or illicit market, a dispenser carries an **astronomical, effectively unreachable price tag** (priced in tens of thousands of gold pieces / multiple Sovereigns and Princes)—far beyond the legal personal wealth or lifetime earnings of ordinary citizens and common soldiers. They simply cannot be bought off a shelf.
- **Institutional Backing & Sponsorship Requirement (Collegium, Merchant, Noble, or Patron):**
  - Owning, maintaining, and reloading a Reaction Manifold is **strictly restricted** by social and institutional standing. Because the apparatus requires ongoing supplies of expensive volatile salts, pre-formed brass casings, and guild cleanroom calibration, an operator **must possess one of the following institutional backings**:
    1. **University Collegium Standing:** Academic fellows, certified Scholars, Chirurgeons, or Clockwork Engineers backed by university laboratories.
    2. **Merchant House Standing:** Merchants (Status 3+) or Wall Merchants (Status 6+) with commercial credit lines and company armories.
    3. **Noble Estate Backing:** Nobles (Status 4+) or Great Nobles (Status 6+) with hereditary house armories.
    4. **The Social Patron Edge (For Lower Status PCs):** Characters of lower social rank (Status 0–2, such as Warrens survivors or mercenary soldiers) **must purchase the 2-Point Patron Edge (Merchant/Noble) or 3-Point Patron Edge (Wall Merchant/Great Noble)** (or be the sworn retainer of a PC Noble/Merchant). Their patron intercedes legally, covers replacement chemical salts/casings, and grants workshop access.
  - **Free Issued Apparatus:** Anyone who meets the institutional training and backing requirements **receives their baseline Reaction Manifold completely for free** from their sponsoring institution. The sponsor views the trained Bombardier as a premier tactical investment.
- **Reload & Synthesis Cycle (8 Hours, 15 Minutes):**
  - **Total Reload Time:** Restocking expended grenades requires **8 hours and 15 minutes** (15 minutes of hands-on calibration + 8 hours of uninterrupted internal chemical synthesis during a long rest).
  - **Step 1 — Active Prep (15 Minutes):** The Bombardier spends 15 minutes of manual maintenance aligning clockwork gears, measuring volatile salts, and priming the chemical manifold.
  - **Step 2 — Automatic Processing (8 Hours):** Over the next 8 hours, the sealed internal mechanism safely synthesizes and restocks all expended grenades back up to full ready capacity (consuming charges from the reservoir).
  - **Tactical Impact:** Because a reload requires **8 hours and 15 minutes**, ready grenades **cannot be reloaded mid-combat or during a short rest**. A Bombardier\'s ready slots represent their strict daily combat limit.
  - **Consumable Reservoir:** Stored grenades remain inert in shock-dampened ports until primed. Each device reservoir holds enough bulk chemical charges for **5 full reloads** (5 cycles of 8 hrs 15 min each), providing multi-day autonomous operation before needing laboratory or guild replenishment.

---

### Storyteller Guidance: Long Expeditions & In-World Solutions
- **Tension vs. Long-Term Play:** The 5-reload reservoir limit and workshop casing requirements exist to drive tactical tension and resource management within an expedition arc—**never to render a Bombardier permanently useless or unplayable** during extended multi-month journeys into unknown lands.
- **Reasonable Field Discoveries:** When an adventure keeps players far from home for extended periods, reasonable Storytellers will introduce in-world replenishment opportunities:
  - An abandoned prospector workshop or ruined alchemy cache containing raw chemical salts and salvageable casings.
  - A fortified Dwarven mining clan or independent frontier trading post capable of servicing clockwork gear.
  - A captured supply wagon or airship cache.
- The Storyteller may place sensible narrative limits on what specific compounds can be recharged abroad, but should always ensure the player has the basic means to keep their class functional.

---

### Storyteller Guidance: Long Expeditions & In-World Solutions
- **Tension vs. Long-Term Play:** The 5-reload reservoir limit and workshop casing requirements exist to drive tactical tension and resource management within an expedition arc—**never to render a Bombardier permanently useless or unplayable** during extended multi-month journeys into unknown lands.
- **Reasonable Field Discoveries:** When an adventure keeps players far from home for extended periods, reasonable Storytellers will introduce in-world replenishment opportunities:
  - An abandoned prospector workshop or ruined alchemy cache containing raw chemical salts and salvageable casings.
  - A fortified Dwarven mining clan or independent frontier trading post capable of servicing clockwork gear.
  - A captured supply wagon or airship cache.
- The Storyteller may place sensible narrative limits on what specific compounds can be recharged abroad, but should always ensure the player has the basic means to keep their class functional.

---

## 3. Activation & Ballistics (Tossing & Detonation)

Using a dispenser grenade requires a **2-Action sequence on the same turn**:

```
[one-action] Prime Grenade + [one-action] Toss Grenade (Same Turn)
```

1. **Action 1 — Prime Payload (`[one-action]`):** Draw the canister from the dispenser's pneumatic port, dial the mechanical fuse delay, and twist the chemical rupture collar.
2. **Action 2 — Bombardier Toss ([one-action]):** Lob the grenade at a designated target square using the munition's base range increment (Standard: **15 ft**; Short/Heavy: **5-10 ft**; Aerodynamic: **20 ft**).
   - **At Your Feet (Drop / Self-Square Detonation - No Roll Required):** If the Bombardier targets the **exact square they are currently standing in** (such as dropping a smokescreen at their feet to escape, planting an ink shroud, or deploying an emergency neutralizer mist on themselves), **no toss check or roll is necessary**. The grenade lands with 100% automatic precision in their own square with zero scatter. *(Note: Unless the payload specifically excludes the user or is a beneficial neutralizer, the thrower must roll saving throws against their own grenade blast!).*

### Pathfinder Range Increments & Scatter Roll (DC 10)
Tossing a grenade at a target square is a **Bombardier check against a flat DC 10**. Bombardier training grants a **+3 bonus** to this toss check; the level 6 *Calculated Trajectory* feat increases this to **+7 total**. Apply standard Pathfinder range increment penalties to the check:
- **Range Increments (Cumulative -2 per increment, max -8 at 5th increment):**
  - **1st Increment (0 to Base Range):** No penalty (Flat DC 10 check).
  - **2nd Increment (Base+1 to 2x Base):** **-2 circumstance penalty** to toss check.
  - **3rd Increment (2x+1 to 3x Base):** **-4 circumstance penalty** to toss check.
  - **4th Increment (3x+1 to 4x Base):** **-6 circumstance penalty** to toss check.
  - **5th Increment (4x+1 to 5x Base, Maximum Range):** **-8 circumstance penalty** to toss check. Beyond 5 increments, the grenade cannot be thrown.
  - *(Example with Standard 15 ft Base: 0-15 ft = no penalty; 16-30 ft = -2; 31-45 ft = -4; 46-60 ft = -6; 61-75 ft = -8).*
- **Success (Final check result of 10 or higher):** **Direct Hit.** The grenade lands cleanly in the targeted square and detonates on arrival.
- **Failure (Final check result below 10):** **Scatter / Bounce.** The grenade misses its intended mark. It bounces or rolls **5 feet (1 square) away from the target for every point the final result is below 10** before detonating.
  - **Scatter Distance Cap:** **Scatter distance on a miss is capped at a maximum of half the thrown distance.** For example, throwing at a target 10 feet away caps bounce/scatter at 5 feet (1 square); throwing 20 feet caps scatter at 10 feet (2 squares).
  - **Scatter Direction (d8):** Roll a **d8** to determine the direction the grenade scatters:
    - **1:** North (Up 1 square)
    - **2:** Northeast (Up-Right diagonal)
    - **3:** East (Right 1 square)
    - **4:** Southeast (Down-Right diagonal)
    - **5:** South (Down 1 square)
    - **6:** Southwest (Down-Left diagonal)
    - **7:** West (Left 1 square)
    - **8:** Northwest (Up-Left diagonal)
  - *Example:* A throw targeted 20 feet away rolls a 6 (missing DC 10 by 4 points). Normally this would scatter 4 squares (20 feet), but half the thrown distance is 10 feet (2 squares). The scatter is capped at 2 squares (10 feet) in the direction rolled on the d8 before detonating.
- **Friendly Fire Warning:** **Friendly fire is very real.** Grenades detonate instantly upon reaching their destination square (whether direct hit or scattered). The payload blast does not differentiate between friends, foes, retainers, bystanders, or the thrower themselves. Anyone caught within the burst radius must roll saving throws and suffer full payload effects.
- **Influence Class Feat (Level 6 — *Calculated Trajectory*):**
  - **Feat Requirement:** 6th Level, Influence Class only (**Noble**, **Merchant**, **Grey Marketeer**), Trained in Bombardier.
  - **Benefit:** Your Bombardier toss bonus increases from **+3 to +7 total** against the flat DC 10 toss check, reducing the chance and distance of scatter.

---

## 4. Detonation & Saving Throws

The moment the grenade lands (whether on target or after scattering):
1. **Payload Burst:** The grenade ruptures, releasing its payload centered on the square it landed in (single square or designated burst radius, e.g. 10-ft burst, 15-ft cone, 20-ft cloud).
2. **Saving Throw vs. Bombardier DC:** Every creature in the area of effect must immediately roll the appropriate saving throw (Reflex, Fortitude, or Will depending on the payload type) against the user's **Bombardier DC**:
   - **Critical Success:** Unaffected.
   - **Success:** Half damage, or reduced condition duration.
   - **Failure:** Full damage and secondary conditions (blindness, sickened, prone, persistent fire/acid).
   - **Critical Failure:** Double damage and full critical secondary penalties.

---

### Consistent Saving Throw Triad Alignment (Reflex, Fortitude, Will)

To ensure intuitive, predictable adjudication at the game table, every munition's saving throw maps directly to the physical nature of the hazard:

|   Save Type   | Threat Dynamic                                   | Physical Triggers & Conditions                                                                                                                       | Example Payload Profiles                                                                                            |
| :-----------: | ------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
|  **Reflex**   | **Speed, Agility & Blast Evasion**               | Instantaneous kinetic detonations, directional shrapnel, shockwaves, arc-lightning jumps, and dodging splashes of burning oil or caustic acid pools. | *High-Explosive Concussion, Shrapnel Flechettes, Arc Lightning, Incendiary Flame, Acid Flasks, Tripwire Adhesives.* |
| **Fortitude** | **Biological Resilience & Bodily Constitution**  | Inhaled toxic vapors, corrosive airborne gases, blinding phosphorus flashes, debilitating sickness, cryogenic shock, and muscular poisons.           | *Choking Fungal Spores, Chlorine Gases, Blinding Glare Pellets, Cryo-Freezing Canisters, Neurotoxins.*              |
|   **Will**    | **Mental Fortitude, Nerve & Sensory Resistance** | Psychoactive vapors, sedative gases, neural-ether clouds, hallucinogenic spore mists, and terrifying concussive acoustic shockwaves.                 | *Soporific Ether, Laughing Gas, Paralyzing Hallucinogens, Confusion Spores, Disorientation Whistles.*               |

### Range, Area & Sustained Control Rules (The Trade-Off Principle)
- **Standard Baseline Range (15 ft / 3 squares):** The standardized base range increment for most munitions is **15 feet (3 squares)**. This safely clears a 10-ft burst radius while remaining within easy tossing distance. Maximum reach at 5 increments is **75 feet** (with cumulative -2 to -8 penalties).
- **Extended Range / Aerodynamic Shells (20 ft / 4 squares - Slight Degraded Effect):** Streamlined, fin-stabilized shells achieve a **20-foot base range increment** (max 100 ft). Because the casing requires aerodynamic fins, stabilizers, or lightweight aluminum/brass walls, internal payload volume is reduced: **raw damage is slightly degraded** (e.g. -1 die size or -1 damage die) or debuff duration is shortened.
- **Short-Range / Heavy Payloads (5-10 ft / 1-2 squares - Increased Impact):** Heavy, thick-walled, or viscous payloads (dense slag, super-heavy vitriol, concentrated Neither cores) are too bulky for long flight, limited to a **5-foot or 10-foot base range increment** (max 25-50 ft). Because the casing carries maximum concentrated reagent volume, **payload effects are significantly boosted** (e.g. +1 damage die, persistent damage riders, or wider secondary conditions). Throwers must take care or move back to avoid catching themselves in the blast!
- **Target Area Scaling (The 1-Square [5x5 ft] Standard vs. Multi-Square Bursts):**
  - **1 Square (5x5 ft Point Detonation):** Several precision munitions affect strictly **one single 5-foot square (1 square)** upon impact. Because the chemical payload is not diluted across a wide room, 1-square munitions deal **full concentrated damage or severe single-target afflictions** (e.g. *Concentrated Acid Flask, Serrated Flechettes, Shock Dart, Sleep Ether Dart, Vitriol Deluge*). Most importantly: **so long as the toss does not fail (no scatter), a 1-square grenade carries ZERO risk of friendly fire to adjacent squares**, making it the indispensable tactical tool when fighting in tight 5-foot Spire hallways or melee scrums beside allied retainers!
  - **Area Bursts (2 to 5 Squares / 10–25 ft radius):** Disperses payload across multiple squares (e.g., 2 squares / 10 ft, 3 squares / 15 ft, 4 squares / 20 ft). To preserve game balance: **as the burst area expands beyond 1 square (5x5 ft), raw damage and condition severity are proportionally diluted** compared to concentrated 1-square munitions, and friendly fire risk increases dramatically.
- **Sustained Battlefield Control & Obscurement (Darkness & Fog):**
  - Specialized canisters release dense chemical clouds, thermal aerosol smoke, or optical light-absorbing Neither-particulates that persist for multiple rounds (typically **3 rounds** or up to **1 minute** if sheltered from heavy squalls).
  - *Obscurement & Total Darkness:* Creates areas of **Concealment**, **Hidden**, or **Magical Darkness equivalents** (preventing line of sight, imposing flat checks to target, or shutting down normal vision).
- **Damage Trade-Off for Sustained / Repeated Area Damage:**
  - A Bombardier can trade high upfront instantaneous blast damage for **lingering, hazard-zone ground cover that inflicts repeated damage over time** to any creature that enters or starts its turn within the affected squares:
    - *Immediate Blast vs. Repeated Field:* For example, trading a 5d6 upfront Fireball for a persistent **Napalm Field** dealing **2d6 Fire damage per round for 3 rounds**, or trading an acid splash for a **Vitriol Muddle** dealing **1d8 Acid per round + difficult terrain**.
    - *Area Denial:* This gives support classes powerful tactical tools to choke narrow corridors, deny vault doorways, force enemy archers out of cover, and control the flow of combat without exceeding martial single-target burst.

---

## 5. Spell-Equivalent Payload Options Catalog

Below is a starting catalog of specialized grenade payloads adapted from Pathfinder 2e Remaster spells across the Arcane, Divine, Occult, and Primal traditions, converted into physical clockwork-chemical munitions:

### Tier 1 Payloads (Trained — 1st-Rank Spell Equivalents)

| Munition Model                       |              Source Spell Reference              |     Base Range      |              Target Area / Size              |  Save DC  | Damage / Effect Trade-Off                                                                                                                                                                                                         | Clockwork / Chemical Explanation                                              |
| ------------------------------------ | :----------------------------------------------: | :-----------------: | :------------------------------------------: | :-------: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| **Concentrated Acid Flask**          |             *Acid Grip* [PC1 p.314]              | **10 ft** *(Heavy)* |              1 Square (5x5 ft)               |  Reflex   | **2d8 Acid + 1d6 persistent acid**. (Boosted damage for heavy 10-ft flask).                                                                                                                                                       | Highly corrosive vitriol in heavy leaded glass capsule.                       |
| **Serrated Shrapnel Shell**          |            *Needle Darts* [PC1 p.352]            |      **15 ft**      |              1 Square (5x5 ft)               |  Reflex   | **3d4 Piercing + 1 bleed**. (Heavy focused ballistics).                                                                                                                                                                           | Compressed coil spring releasing barbed clockwork flechettes.                 |
| **Wide-Burst Incendiary Canister**   |            *Breathe Fire* [PC1 p.318]            |      **15 ft**      |      **3 Squares** (15-ft line/spread)       |  Reflex   | **2d4 Fire** (Damage diluted from 2d6 to account for 3-square area).                                                                                                                                                              | Aerosolized volatile mushroom spirits ignited by a sulfur striker.            |
| **Aerodynamic Shock Dart**           |           *Shocking Grasp* [PC1 p.368]           | **20 ft** *(Aero)*  |              1 Square (5x5 ft)               |  Reflex   | **2d6 Electricity** (Degraded from 2d12 to 2d6 due to light finned casing). Metallic armor gives -2 to target save.                                                                                                               | Streamlined brass dart fitted with an endothermic static capacitor.           |
| **Phosphorus Blinding Pellet**       |           *Color Spray* `[PC1 p.324]`            |        15 ft        |       **2 Squares** (10-ft cone/burst)       | Fortitude | **Dazzled 1 round** on Success; **Blinded 1 round** on Failure.                                                                                                                                                                   | Magnesium-potassium flash charge producing intense arc-lamp glare.            |
| **Choking Spore Smoke Canister**     |             *Goblin Pox* [PC1 p.337]             |      **15 ft**      |         **3 Squares** (15-ft cloud)          | Fortitude | **Sickened 1** on Failure (**Sickened 2** on Critical Failure). No raw HP damage.                                                                                                                                                 | Powdered dried lightless shelf-fungus spores causing violent coughing spasms. |
| **Adhesive Pitch Bomb**              |       *Grease / Tanglefoot* `[PC1 p.338]`        |        15 ft        |         **2 Squares** (10-ft patch)          |  Reflex   | Target square becomes uneven ground; target takes **-10 ft circumstance speed penalty**.                                                                                                                                          | Viscous petroleum-tar and vulcanized rubber resin.                            |
| **Neuro-Sedative Vapour**            |               *Sleep* [PC1 p.370]                |      **15 ft**      |              1 Square (5x5 ft)               |   Will    | Single target takes **Stupefied 1** on Success; falls **Unconscious (Sleep)** on Failure.                                                                                                                                         | Micro-aerosolized ether and poppy alkaloids.                                  |
| **Lampblack Smokescreen**            |        *Smoke Cloud / Mist* `[PC1 p.350]`        |        15 ft        |         **3 Squares** (15-ft cloud)          |   None    | **Sustained Control (3 Rounds):** Dense carbonaceous fog creates **Concealed** terrain for all inside/behind; blocks line of sight beyond 5 ft.                                                                                   | Compressed charcoal dust and paraffin smoke generator.                        |
| **Volatile Spatter-Burn Pitch**      |         *Persistent Burning Area* [New]          | **10 ft** *(Heavy)* |          **2 Squares** (10-ft zone)          |  Reflex   | **Repeated Damage (3 Rounds):** Upfront **1d6 Fire**; deals **1d6 Fire per round** to any creature entering or starting turn in the zone. (Boosted for heavy 10-ft payload).                                                      | Sticky pressurized petroleum distillate adhering to cobblestone.              |
| **Dense Caliginous Ink Shroud**      |           *Darkness (1st)* [PC1 p.326]           |      **15 ft**      |         **2 Squares** (10-ft cloud)          |   None    | **Sustained Darkness (3 Rounds):** Heavy aerosolized black pigment completely absorbs light; area is treated as **Total Darkness** (creatures inside are Blinded unless possessing Tremorsense).                                  | Refined deep-squid ink extract mixed with lightless Neither particulates.     |
| **Pneumatic Repulsion Shell**        | *Hydraulic Push / Gust of Wind* [PC1 p.339, 340] |      **15 ft**      | Single Square or **2 Squares** (10-ft burst) |  Reflex   | **Kinetic Blast:** Pushes targets **5 ft away** on Success; **10 ft away and knocked Prone** on Failure; **15 ft away, Prone, and Stunned 1** on Critical Failure. Deals no lethal damage.                                        | Directional high-pressure steam/compressed air expansion canister.            |
| **Phosphor Tracer Canister**         | *Faerie Fire / Revealing Light* [PC1 p.333, 363] |      **15 ft**      |         **3 Squares** (15-ft burst)          |   None    | **Sustained Marking (1 Minute):** Coats targets in luminous micro-dust. Strips **Concealed** and **Hidden/Invisible** status; ranged attacks against marked targets ignore concealment flat checks.                               | Aerosolized chemical phosphor dust clinging to skin and gear.                 |
| **Endothermic Rime Pellet**          |    *Chilling Spray / Rime Slick* [PC1 p.322]     |      **15 ft**      |         **2 Squares** (10-ft patch)          | Fortitude | **Flash Freeze (3 Rounds):** Creates slippery Difficult Terrain (Reflex DC 15 to balance). Targets in burst failing Fortitude save become **Clumsy 1** for 2 rounds from muscular frost shock.                                    | Dual-chamber ammonium nitrate endothermic siphon freezing standing liquid.    |
| **Aerosolized Neutralizer Canister** |  *Cleanse Affliction / Purify Air* [PC1 p.323]   |      **15 ft**      |         **2 Squares** (10-ft burst)          |   None    | **Chemical Counter-Agent:** Instantly neutralizes and disperses active gas/smoke/spore clouds in the area. Allies in burst gain an immediate saving throw with a **+2 circumstance bonus** against active inhaled poisons/spores. | Pressurized alkaline/carbolic mist neutralizing airborne contaminants.        |

---

### Tier 2 Payloads (Expert — Up to 4th-Rank Spell Equivalents)

| Munition Model                         |           Source Spell Reference            |     Base Range      |      Target Area / Size      |  Save DC  | Damage / Effect Trade-Off                                                                                                                                                                                            | Clockwork / Chemical Explanation                                              |
| -------------------------------------- | :-----------------------------------------: | :-----------------: | :--------------------------: | :-------: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| **Compressed Detonation Bomb**         |           *Fireball* [PC1 p.334]            |      **15 ft**      | **4 Squares** (20-ft burst)  |  Reflex   | **5d6 Fire/Bludgeoning** (Wide 4-square spread; damage slightly dialed back from standard 6d6).                                                                                                                      | High-pressure clockwork casing packed with stabilized Neither-sulfur.         |
| **Aerodynamic Arc Javelin**            |        *Lightning Bolt* [PC1 p.346]         | **20 ft** *(Aero)*  |  **4 Squares** (20-ft line)  |  Reflex   | **3d8 Electricity** (Degraded from 4d8 to 3d8 due to stabilizing fins).                                                                                                                                              | High-density zinc-carbon voltaic cell with trailing copper grounding wires.   |
| **Caustic Vitriol Deluge**             |         *Acid Arrow* `[PC1 p.314]`          |        15 ft        |      1 Square (5x5 ft)       |  Reflex   | **4d8 Acid + 2d6 persistent acid**. Heavy focused melting.                                                                                                                                                           | Multi-chambered pressurized canister spraying concentrated fuming vitriol.    |
| **Mass Soporific Cloud**               |          *Sleep (4th)* [PC1 p.370]          |      **15 ft**      | **3 Squares** (15-ft cloud)  |   Will    | Multi-target sedative: **Stupefied 1** on Success; **Unconscious** on Failure.                                                                                                                                       | Pressurized liquefied laughing gas and refined fungal soporific vapor.        |
| **Cryo-Endothermic Shell**             |     *Cone of Cold (Light)* [PC1 p.324]      |      **15 ft**      | **3 Squares** (15-ft burst)  | Fortitude | **4d6 Cold**; targets failing save become **Clumsy 1** (ice encasement).                                                                                                                                             | Rapid endothermic chemical siphon freezing ambient moisture instantly.        |
| **Aerosolized Neurotoxin Grenade**     |       *Stinking Cloud* `[PC1 p.372]`        |        15 ft        | **3 Squares** (15-ft cloud)  | Fortitude | Creates 1-minute persistent cloud: creatures entering become **Sickened 1 and Slowed 1**.                                                                                                                            | Synthesized organic Neither-spore toxin attacking nervous system.             |
| **Incendiary Gel Quagmire**            | *Wall of Fire / Flaming Sphere* [PC1 p.380] | **10 ft** *(Heavy)* |  **3 Squares** (15-ft zone)  |  Reflex   | **Repeated Damage (3 Rounds):** Boosted to **3d6 Fire per round** to any creature inside, entering, or ending turn in burning gel (heavy petroleum payload). Difficult terrain.                                      | Gelatinized mineral oil that sticks to flooring and boots.                    |
| **Caustic Sump Mire Shell**            |   *Acid Pool / Acid Storm* `[PC1 p.314]`    |        15 ft        | **3 Squares** (15-ft puddle) |  Reflex   | **Repeated Damage (3 Rounds):** Deals **2d6 Acid per round**; dissolves non-magical footwear/tires, inflicting **-10 ft circumstance speed penalty**.                                                                | Fuming industrial vitriol held in an endothermic gel matrix.                  |
| **Absolute Pitch Shroud**              |       *Darkness (2nd)* `[PC1 p.326]`        |        15 ft        | **3 Squares** (15-ft cloud)  |   None    | **Sustained Darkness (1 Minute / Combat):** Suppresses low-light and non-magical light sources; suppresses torches and arc lanterns; creatures without darkvision are effectively **Blinded**.                       | Neither-reactive vacuum catalyst absorbing electromagnetic visible spectra.   |
| **Acoustic Resonant Concussion Shell** |  *Sound Burst / Shatter* [PC1 p.368, 370]   |      **15 ft**      | **2 Squares** (10-ft burst)  | Fortitude | **2d10 Sonic/Concussion**. Targets failing save are **Deafened for 1 minute** (**Deafened + Stunned 1** on Crit Fail). Deals double damage to brittle glass, ceramic, crystal vials, and brittle Neither components. | Tuned mechanical acoustic diaphragm detonating at harmonic shatter frequency. |

---

### Tier 3 Payloads (Master — Up to 8th-Rank Spell Equivalents)

| Munition Model                        |              Source Spell Reference               |     Base Range      |          Target Area / Size           |  Save DC  | Damage / Effect Trade-Off                                                                                                                                                             | Clockwork / Chemical Explanation                                                    |
| ------------------------------------- | :-----------------------------------------------: | :-----------------: | :-----------------------------------: | :-------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| **Apex Concussion Colossus**          |        *Cataclysm (Miniature)* [PC1 p.321]        | **10 ft** *(Heavy)* |      **5 Squares** (25-ft burst)      |  Reflex   | **10d8 Fire, Bludgeoning & Piercing**; knockdown prone on Failure. (Massive concentrated core payload).                                                                               | Concentrated Neither-catalyst explosive charge shattering Neithercrete walls.       |
| **Voltaic Chain Emitter**             |          *Chain Lightning* `[PC1 p.322]`          |        15 ft        | **4 Squares** (Jumps up to 4 targets) |  Reflex   | **7d10 Electricity**; arcs between targets wearing metal or standing in sump water.                                                                                                   | Overcharged radiant converter capacitor releasing self-propagating electrical arcs. |
| **Lethal Asphyxiation Cloud**         |              *Cloudkill* [PC1 p.323]              |      **15 ft**      | **4 Squares** (20-ft creeping cloud)  | Fortitude | **7d8 Poison/Chemical**; creatures failing are **Drained 2 & Sickened 2**.                                                                                                            | Heavy-density chlorine-sulfur nerve agent creeping along floor level.               |
| **Shattering Permafrost Core**        |              *Polar Ray* [PC1 p.359]              | **20 ft** *(Aero)*  |           1 Square (5x5 ft)           | Fortitude | **8d10 Cold** (Slightly degraded from 9d10 due to light long-range shell); target suffers **Drained 2** and is **Immobilized** in brittle rime.                                       | Vacuum-sealed liquid gas canister detonating on impact.                             |
| **Radiant Arc Field Barrier**         | *Wall of Force / Lightning Barrier* `[PC1 p.381]` |        15 ft        |    **4 Squares** (20-ft line/zone)    |  Reflex   | **Repeated Damage & Control (3 Rounds):** Continuous electrical discharge dealing **3d10 Electricity per round** to anyone attempting to cross; forces Stunned 1 on Critical Failure. | Self-grounding copper anchor rods radiating overcharged capacitor arcs.             |
| **Creeping White-Phosphorus Furnace** |          *Incendiary Cloud* [PC1 p.342]           | **10 ft** *(Heavy)* |  **4 Squares** (20-ft creeping zone)  |  Reflex   | **Repeated Damage (3 Rounds):** Boosted to **4d8 Fire + 2d8 Bludgeoning per round** across a creeping 4-square zone (heavy phosphorus load); creates total visual obscuration.        | Micro-pellets of self-igniting phosphorus sustained by atmospheric oxygen.          |

---

### Tier 4 Payloads (Legendary — Up to 10th-Rank Apex Ordnance)

| Munition Model                     |  Source Spell Reference   | Base Range |         Target Area / Size          |  Save DC  | Damage / Effect Trade-Off                                                                                                         | Clockwork / Chemical Explanation                                                      |
| ---------------------------------- | :-----------------------: | :--------: | :---------------------------------: | :-------: | --------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| **Sovereign Arc Thermobaric Core** | *Cataclysm* `[PC1 p.321]` |   15 ft    | **5 Squares** (25-ft massive burst) |  Reflex   | **12d10 Bludgeoning, Fire & Electricity**; obliteration threshold.                                                                | Military-grade biochemical catalyst detonating a secondary vacuum fuel-air shockwave. |
| **Apex Neurological Nerve Gas**    |  *Massacre* [PC1 p.348]   | **15 ft**  |     **5 Squares** (25-ft cloud)     | Fortitude | High lethal threshold: Creatures with 70 HP or less that fail save drop to **0 HP (Mortal Trauma)**; others take **10d8 Poison**. | Pure weaponized synthetic toxin derived from Abyssal lightless predator venom.        |
