# Clockwork Cities — Healing & Wound Thresholds
Status: **Draft**. Base rules: Rest & Recovery [Player Core p.427], Treat Wounds [Player Core p.240]. Precedence per 00_RulesFoundation.md.

## Core Principle — Replaced
Hit Points represent three distinct tiers of trauma rather than an undifferentiated pool. Superficial cuts, fatigue, and bruises heal quickly, while deep systemic trauma (Critical and Mortal wounds) requires extended real-world recuperation time.

---

## 1. Hit Point Categories & Thresholds
A character's maximum Hit Points are divided into deep trauma tiers and regular damage using **Step Size**:

### Step Sizing & Thresholds
- **Total HP $\le 16$:** Flat wound tier allocation:
  - **Mortal Wounds:** 1 to 3 HP (3 HP band)
  - **Critical Wounds:** 4 to 6 HP (3 HP band)
  - **Regular Damage:** 7 to Max HP (e.g. at 16 HP, 10 regular HP; at 14 HP, 8 regular HP; at 12 HP, 6 regular HP)
- **Total HP $\ge 17$:** Standard formula:
  $$\text{Step} = \left\lfloor \frac{\text{Total Hit Points}}{4} \right\rfloor$$
  - **Mortal Wounds (Step 1):** $1 \text{ to } \text{Step}$
  - **Critical Wounds (Step 2):** $(\text{Step} + 1) \text{ to } (2 \times \text{Step})$
  - **Regular Damage (Remaining):** $(2 \times \text{Step} + 1) \text{ to } \text{Max HP}$

| Tier | Category | HP Range (from 0) | Natural Healing Rate | Penalties (Post-Combat when depleted) | Allowed Healing Sources |
|---|---|---|---|---|---|
| **Step 1** | **Mortal Wounds** | $1 \text{ to } \text{Step}$ | **Weeks** of bed rest | **Major penalties** | Long-term natural recovery / specialized clinical care |
| **Step 2** | **Critical Wounds** | $(\text{Step} + 1) \text{ to } (2 \times \text{Step})$ | **Days** of rest | **Minor penalties** | Days-scale rest and medical recuperation |
| **Remaining** | **Damage** (Regular) | $(2 \times \text{Step} + 1) \text{ to } \text{Max HP}$ | **Normal PF rules** (hours/rest) | None | Normal PF resting, Treat Wounds, Concoctions, Tech |

> *Comparison at the Transition Point:*
> - **At 16 HP ($\le 16$ rule):** 3 Mortal (1–3), 3 Critical (4–6), **10 Regular HP** (7–16).
> - **At 17 HP ($\lfloor 17/4 \rfloor = 4$):** 4 Mortal (1–4), 4 Critical (5–8), **9 Regular HP** (9–17). *(Exactly 1 fewer regular HP than 16 HP, smoothly bridging into martial scaling).*
>
> *Example (Mid-Level)*: A character with 42 total HP has a Step size of $\lfloor 42 / 4 \rfloor = 10$.
> - **Mortal Wounds (Step 1)**: HP 1–10 (10 HP band) &mdash; major penalties
> - **Critical Wounds (Step 2)**: HP 11–20 (10 HP band) &mdash; minor penalties
> - **Damage (Remaining)**: HP 21–42 (22 HP band) &mdash; no penalties

---


## Combat Damage Tracking & Sheet Protocol (Zero Mid-Combat Math)

To eliminate spreadsheet accounting and condition lookups during active combat initiative, wound tiers and penalties are tracked **exclusively outside of combat**. During an encounter, players track only two running numbers: **Lethal Damage** and **Nonlethal Damage**.

> [!NOTE]
> **Storyteller Guidance: The Price of Running (Health Level Assistance)**
> As a Storyteller, **expect to—and always be available to—recalculate health levels with and for your players after every fight and before every fight**.
> While the system is clean and predictable, players have varying levels of comfort with tiered health math, trauma ceilings, and post-combat nonlethal recovery.
> - *After combat:* The ST proactively walks the table through: *"Drop your nonlethal, tell me what remaining damage you took, and let us step it down through your Regular, Critical, and Mortal tiers together and note any penalties."*
> - *Before combat:* The ST prompts: *"Quick pre-fight check—did anyone drink an elixir or bandage up during rest? Let us lock in your new Available HP box before initiative."*
> Providing this active, patient guidance keeps the table moving fast, eliminates bookkeeping anxiety, and lets players focus on the gritty tactical story.

### 1. Character Sheet Layout (Three Health Tiers)
On the character sheet, maximum and current values are recorded for the three baseline health tiers:

| Tier | Maximum Capacity | Current Available HP | Notes / Recovery |
| :--- | :---: | :---: | :--- |
| **Regular Damage** | [Max Regular HP] | [Current Regular] | Heals via normal PF2e rest, Treat Wounds, tonics, tech. |
| **Critical Wounds** | [Max Critical HP] | [Current Critical] | Deep structural tissue trauma; heals over days. |
| **Mortal Wounds** | [Max Mortal HP] | [Current Mortal] | Organ/skeletal trauma; heals over weeks. |

### 2. Pre-Combat Setup: The Health Audit (Verification Only, Not Free Rest)
At any time between scenes—and specifically **right before rolling initiative for combat**—the Storyteller conducts a quick 30-second Health Audit. **This is not a free extra healing window or retro-action period; it is purely an accounting check for things players often forget to write down:**

1. **The Pre-Fight Verification Checklist:**
   - *Did you rest for several days or have clinical downtime that was not recorded?*
   - *Did you receive infused elixirs, hemostatic sprays, or tonics from the Chirurgeon during morning prep that you forgot to log?*
   - *Did you consume any rations, biomedical tonics, or field dressings earlier in the dungeon/ward that were not marked off?*
   - *Trauma Ceiling Check:* If you have unhealed Critical or Mortal wounds, confirm your Regular HP is properly capped at your field Trauma Ceiling ($	ext{Level} + 	ext{CON}$, min 1).
   - *Do your three health tiers on the sheet accurately reflect reality right now?*
2. **Sum Available HP:**
   - Sum the verified current values across all three tiers:
     $$	ext{Available HP} = 	ext{Current Regular} + 	ext{Current Critical} + 	ext{Current Mortal}$$
3. **Lock In the Combat Box:**
   ```
   ┌────────────────────────────────────────────────────────┐
   │ AVAILABLE HP: [  42  ]                                 │
   │                                                        │
   │ Total Damage Taken: [ ___ ]    Nonlethal Pool: [ ___ ] │
   └────────────────────────────────────────────────────────┘
   ```

### 3. Mid-Combat Tracking: Standard PF2e Flow
During combat, tracking functions **identically to standard Pathfinder 2e**:
- **All Damage is Damage:** When hit by ANY attack (lethal or nonlethal), add the incoming damage directly to your running **Total Damage** tally.
- **Track Nonlethal in Parallel:** If the attack was nonlethal (e.g. sap, unaugmented fist, stun baton), also add that amount to your **Nonlethal Pool**.
- **Unconsciousness Check:**
  - The moment $\text{Total Damage} \ge \text{Available HP}$, the character collapses **Unconscious**.
  - **The Dying vs. Stable Check (Simple Comparison):**
    - Calculate **Net Lethal Damage Taken** = $\text{Total Damage} - \text{Nonlethal Pool}$.
    - **Stable Cushion:** If $\text{Net Lethal Damage Taken} < \text{Available HP}$, the character is simply **unconscious and stable** (no dying condition, no bleed clock, and no wound tier advancement).
    - **Dying / Bleed Trigger:** If $\text{Net Lethal Damage Taken} \ge \text{Available HP}$, the character enters the **Dying / Bleed Clock** per standard rules (§5).

### 4. Post-Combat Resolution: Nonlethal Drop & Tiered Trauma
Once combat ends (initiative drops, adrenaline fades, and the scene resolves):
1. **Heal Nonlethal (Drop Nonlethal Damage):**
   - The body immediately recovers from superficial blunt stunning, breath loss, and pain shock: **Heal damage equal to your current Nonlethal Pool** (or simply deduct Nonlethal from Total Damage to determine net lasting trauma):
     \text{Net Damage to Apply} = \max(0, \text{Total Damage} - \text{Nonlethal Pool})
2. **Apply Remaining Damage Downward Across Tiers:**
   - **Step A (Current Regular):** Apply damage against **Current Regular HP** until depleted.
   - **Step B (Current Critical):** Any remaining damage overflows downward into **Current Critical HP** until depleted.
   - **Step C (Current Mortal):** Any further remaining damage overflows downward into **Current Mortal HP**.
3. **Verify & Record Health Tier Penalties on Character Sheet:**
   - Check the resulting health tiers:
     - **Critical Tier Punctured:** If Current Critical HP took damage, verify and record the appropriate **minor anatomical trauma penalty** (§4.C / §4.D, e.g., clumsy, enfeebled, or speed penalty).
     - **Mortal Tier Punctured:** If Current Mortal HP took damage, verify and record the appropriate **major anatomical trauma penalty**.
     - **Dropped to 0 HP:** If completely reduced to 0 HP, record the **direct attribute penalty** (§4.E, e.g., –2 to primary physical/mental attributes).
4. **Reset Active Combat Box:**
   - Erase the **Total Damage** and **Nonlethal Pool** tallies.
   - Recalculate and write down the new **Available HP** ($=\text{Current Regular} + \text{Current Critical} + \text{Current Mortal}$) for the next encounter.

---

## The 3-Tier Medical Hierarchy (Social & Practical Division)
Across the Great Spires, military cohorts, airship crews, and outland expeditionary companies, medical expertise is distributed across a strict societal pyramid:
- **Field Medics / Chirurgeon Archetype (~1 in 30 to 1 in 50 individuals):** Roughly 1 in 30 to 1 in 50 people have cross-trained emergency medical skills (the Chirurgeon Archetype / Field Medic). These are company corpsmen, airship hands, and trench soldiers who know basic trauma triage, sutures, and emergency stimulants. Full, primary Chirurgeons who command dedicated micro-drone swarms and run clinical apothecaries are even rarer specialists.
- **Scholar Doctors / Chief Physicians (~1 in 150 individuals):** True university-educated medical researchers and hospital physicians are scarce (roughly 1 in 150 people). They are almost exclusively focused in **safe, centralized, high-infrastructure locations**—Spire university cleanrooms, sanatorium dynamos, and aristocratic luxury wards—and almost never venture out into the Neither mud or frontline trenches.

In Victorian Spire healthcare, medical roles are divided across three clear social and operational tiers:
1. **Tier 1 — The Doctor / Medical Researcher (Scholar Class):** High academic fellows and university chairs (Status 4–6). They design and operate expensive clinical clockwork technology (heart-lung dynamos, vacuum distillation towers, cellular diagnostic meters) and synthesize the most refined elixirs in pristine cleanrooms. They perform long-term inpatient surgeries in established medical facilities (clearing Critical/Mortal trauma during 2-day or 1-week inpatient care), but rarely venture into field trenches.
2. **Tier 2 — The Paramedic / Clinic Worker & Spore-Cultivator (Chirurgeon Class):** Hands-on medical workhorses, spore-brewers, and triage directors (Status 2–4). 
   - **Spellcaster Chassis & Analytical Defense:** Operates on an unarmored/simple weapon chassis, calculating threat corridors mentally so that **Intelligence replaces Dexterity for Armor Class (AC)** ($10 + \text{Prof} + \text{INT}$) with no Dex cap.
   - **Neither-Bio Resonance:** In the Neither, Warrens, or Wilds, symbiotic fungal acclimation replaces **Dexterity with Intelligence** for all DEX skills (Stealth, Thievery, Acrobatics) and **Strength with Wisdom** for all STR skills (Athletics).
   - **Clockwork Micro-Drone Horde:** Deploys miniature brass scuttlers and winged syringe-drones to administer 2-action field triage injections at range (30 ft) and absorb single lethal hits via a 1/round Reaction [R] ( \times \text{INT}$ damage absorb;  \times \text{Level}$ daily uses).
   - **Hemostatic Coagulant Spray (First Aid Check):** Pressurized fibrin spray ends persistent bleed damage on a First Aid (Medicine/Crafting) check against $\text{DC } 15 + \text{Bleed Rate}$.
   - **Modular Daily Formulations (WIS/INT Multipliers):** Cultivates daily spore strains granting targeted damage resistance (Resistance =  \times \text{WIS}$ against chosen environmental/physical damage types) and caustic solvents that strip enemy armor/DR ( \times \text{INT}$ on a failed save).
3. **Tier 3 — The Emergency Responder / Corpsman (Field Medic Archetype):** Combatants (Soldiers, Scouts, Survivors) who take the Chirurgeon Dedication because Tiers 1 and 2 are dead or miles away. Their kit is brutal and practical: tourniquets, crude cautery irons, smelling salts, and emergency adrenaline auto-injectors strapped to armor. When frontline allies collapse in the mud, they drag them behind cover, slam a stim into their chest, and keep the squad fighting.

---

## 2. Technology & Concoction Limits
- **Damage Only (Standard Baseline)**: Concoctions (biomedical tonics, stims) and Clockwork Technology (cellular repair gizmos, suture mechanisms) **can only restore regular Damage**.
- **No Instant Surgery**: Standard technology and concoctions cannot instantly knit ruptured organs or re-anchor shattered bones represented by Critical or Mortal wounds.
- **Emergency Exception — Adrenal Injector:** A specialized 1-charge chemical stim injector (`EquipmentCatalog.md §3`) can chemically mask and remove active wound damage during combat, but inflicts severe Exhaustion post-combat until a full night's rest. Subsequent injections between fights cause severe physiological strain, dealing **1d6 damage**; excess damage flows through standard wound tiers into mortal (and can result in PC death).
  - **Chirurgeon Calibration (Level 5):** A Level 5+ Chirurgeon crafts **daily doses equal to their INT modifier** without consuming infused reagents.
  - **Improved Adrenal Injector (Level 10):** At Level 10, a Chirurgeon modifies their injectors with stabilized bio-buffers so subsequent uses deal **only a flat 2 points of damage** (instead of 1d6), preventing accidental cardiac death.

---

## 3. Healing Order & Progression
- **Hierarchical Recovery**: As a general rule, healing progresses from the deepest trauma upward. The earlier levels must be healed before later damage can be recovered:
  1. **Mortal Wounds (Step 1)** heal first (measured in weeks).
  2. Once Mortal Wounds are fully cleared, **Critical Wounds (Step 2)** heal (measured in days).
  3. Once Critical Wounds are resolved, remaining **Damage** heals per standard Pathfinder rules (Treat Wounds, overnight rest).

### Regular Damage & The Trauma Ceiling ($\text{Level} + \text{CON}$)
- **Standard PF2e Healing:** Regular Damage heals per standard PF2e rules (Treat Wounds, rest, tonics, tech devices).
- **The Trauma Ceiling (Field / Unstabilized):** In the field without facility stabilization, if a character has **any unhealed Critical or Mortal wounds**, their maximum Regular Damage pool is capped at:
  $$\text{Max Regular HP} = \text{Level} + \text{CON modifier} \quad (\text{min } 1)$$
  Field healing beyond this ceiling is lost until deeper wounds are resolved or clinical care is received.

### Clinical Recuperation & Medical Facility Care
Receiving inpatient medical care in a proper medical facility stabilizes the patient's trauma, unlocking normal healing of their regular hit points and freeing them from the field Trauma Ceiling ($\text{Level} + \text{CON}$):
- **Critical Care (2 Days):** After **2 full days of proper medical care** in a medical facility when suffering Critical wounds, the patient is **no longer limited by the $\text{Level} + \text{CON}$ Trauma Ceiling**. They can heal their Regular Damage pool back to full through normal rest, Treat Wounds, or biomedical tonics, and **continue to heal regular damage normally** as long as they do not suffer another critical or mortal point of damage.
  - While this Regular Damage pool remains intact, **wound conditions do not apply**.
  - Critical wound HP itself heals at **$\text{CON}$ HP / day** (or $\lfloor \frac{1}{5} \text{Level} \rfloor + \text{CON}$ / day via simple bed rest).
- **Mortal Care (1 Full Week):** After **1 full week of proper medical care** in a medical facility when suffering Mortal wounds, the patient is stabilized and is **no longer limited by the $\text{Level} + \text{CON}$ Trauma Ceiling**. They can heal their Regular Damage pool back to full and **heal regular damage normally** as long as they do not take another critical or mortal point of damage.
  - While this Regular Damage pool remains intact, **wound conditions do not apply**.
  - Mortal wound HP itself heals at **$\text{CON}$ HP / week** (or $\lfloor \frac{1}{5} \text{Level} \rfloor + \text{CON}$ / week via simple bed rest).
- **Re-injury Clause:** If at any point the character takes a point of Critical or Mortal damage, the surgical repairs rupture, the Trauma Ceiling immediately reasserts itself, and the wound conditions reactivate until proper facility care is received again.

### D. Active Chirurgical Convalescence (Accelerated Wound Recovery)
While instant field surgery during active combat or short rests remains impossible, a trained Chirurgeon provides vital specialized clinical care during extended travel, camp maintenance, and downtime:

1. **Full Chirurgeon Class (1d6 per INT Modifier):**
   - **Critical Wound Recovery (Daily):** If an injured character completes **1 full day with No Strenuous Activity** under a Chirurgeon's care, the Chirurgeon rolls **1d6 per point of INT modifier** (e.g. 4d6 at +4 INT) to reduce/heal the patient's **Critical Wound damage**.
   - **Mortal Wound Recovery (Weekly):** If an injured character completes **1 full week with No Strenuous Activity** under a Chirurgeon's care, the Chirurgeon rolls **1d6 per point of INT modifier** to reduce/heal the patient's **Mortal Wound damage**.
2. **Chirurgeon Archetype / Field Medic (1d4 per INT Modifier):**
   - Characters possessing the Chirurgeon Archetype / Dedication possess this capability, but roll **1d4 per point of INT modifier** (instead of 1d6) for daily Critical recovery and weekly Mortal recovery.
3. **Activity Requirements & Environmental Shift Limit:**
   - **No Strenuous Activity (Replaces Strict Bed Rest):** Patients are **not required to be bedridden**. They can perform normal camp life, standard overland travel, wagon riding, cooking, reading, and light watch duty. They simply cannot engage in combat ("fight or flight"), sprinting, heavy lifting, forced marching, or hard excavation labor.
   - **Environmental Penalty Ceiling (Total Shift $\le 2.0$):** To receive this convalescent healing, the patient's total environmental displacement penalty must be manageable: **Total Shift Score ($	ext{Air Shift} + 	ext{Food Shift}$) cannot exceed 2.0**. In extreme foreign biomes where Total Shift is $> 2.0$ (severe atmospheric/cellular strain per `§6`), biological stress is too high for natural cellular regeneration, and convalescence healing cannot function until the patient moves to cleaner air or receives native food/filtration.
   - **Daily / Weekly Cap:** A patient can benefit from this accelerated convalescence roll **strictly once per day** for Critical wounds, and **strictly once per week** for Mortal wounds.

## 4. Anatomical Trauma & Wound Consequences
When a blow is severe enough to shatter body structures, characters suffer escalating anatomical consequences and status conditions.

### A. Wound Incurrence Rule (Knocked to Negative HP)
- **Trauma Trigger:** Wounds (Critical and Mortal damage) **only occur when a character is knocked to negative HP by damage greater than their Mortal HP total**. (This can be adjusted later if playtesting reveals it to be too rare). Superficial strikes that merely reduce HP to 0 without overcoming the Mortal threshold cause unconsciousness/bleeding without inflicting structural anatomical wounds.

### B. Adrenaline Buffer: Post-Combat Application
- **Combat Adrenaline:** During active combat / encounter initiative, physiological shock and surges of adrenaline mask the debilitating impact of deep physical trauma.
- **Onset After the Fight:** **Critical and Mortal wound conditions and condition severity increases do NOT apply mid-combat.** They only manifest and take effect **after the fight is complete** (once initiative ends, adrenaline fades, and the body registers systemic damage).
- *Exception — Incapacitation & Death:* Reaching 0 HP or suffering lethal bleed-out still immediately affects consciousness and dying status in combat. However, ongoing action-penalty conditions and attribute drain take effect once the encounter concludes (or upon revival post-combat).

### C. Threshold-Based Condition Triggers (1, 5, 10, 15, and 20 Points)
Critical and Mortal tiers align in how trauma conditions are inflicted. Damage sustained in these tiers is tallied during combat, and once the fight ends, conditions are applied according to cumulative damage within the tier:
- **At 1 point of wound damage:** Inflicts the first minor condition / baseline trauma.
- **At 5 points of wound damage:** Inflicts an additional condition or increases severity of the existing penalty.
- **At 10 points of wound damage:** Inflicts another condition or steps severity to higher tier values.
- **At 15 points of wound damage:** Inflicts further condition accumulation or escalating penalties.
- **At 20 points of wound damage:** Maximum anatomical trauma state for the tier.

> *Note on Alignment & Condition Suppression:* Once stabilized through proper medical care (2 days for Critical, 1 week for Mortal), **wound conditions do not apply** and regular damage can heal normally. Conditions only re-apply if the character takes another Critical or Mortal point of damage.

### D. Anatomical Trauma by Damage Type (Trauma Table)
When a wound threshold is triggered, determine the specific condition based on the incoming damage type using the table below (or by DM narrative call):

| Damage Type | Roll (d%) | Injury / Anatomical Effect | Mechanical Condition |
| :--- | :---: | :--- | :--- |
| **Blunt / Concussive** | 01–35% | Severe Concussion / Cranial Rattling | **Stupefied 1** (or +1 value) |
| | 36–70% | Shattered Ribs / Internal Contusion | **Enfeebled 1** (or +1 value) |
| | 71–00% | Fractured Knee / Crushed Foot | **Speed –5 ft** (or –10 ft) |
| **Piercing / Ballistic** | 01–35% | Punctured Lung / Thoracic Perforation | **Enfeebled 1** & persistent bleed 1 |
| | 36–70% | Severed Tendon / Muscle Tear | **Clumsy 1** (or +1 value) |
| | 71–00% | Hamstrung / Arterial Leg Wound | **Speed –5 ft** & persistent bleed 1 |
| **Slashing** | 01–40% | Deep Visceral Laceration | **Enfeebled 1** & persistent bleed 1 |
| | 41–75% | Tendon Cleave / Mangled Hand | **Clumsy 1** (or Disarm vulnerability) |
| | 76–00% | Deep Leg Gash / Severed Calf | **Speed –5 ft** (or –10 ft) |
| **Acid / Corrosive** | 01–40% | Chemical Skin Flensing / Nerve Burning | **Clumsy 1** (agony on movement) |
| | 41–70% | Caustic Vapor Inhalation / Bronchial Burn | **Drained 1** (or +1 value) |
| | 71–00% | Corroded Muscle Fiber & Flesh Sloughing | **Enfeebled 1** |
| **Poison / Toxic** | 01–40% | Neurotoxic Tremors / Motor Seizures | **Clumsy 1** |
| | 41–70% | Systemic Hemotoxin / Organ Strain | **Drained 1** |
| | 71–00% | Mind-Clouding Delirium / Synaptic Shock | **Stupefied 1** |

*(Percentages and values can be tuned through playtesting or overridden by DM call).*

### E. Direct Attribute Modifier Penalties (Reaching 0 HP)
- **Trigger at 0 HP:** Direct attribute modifier penalties (e.g., –2 Str, –3 Dex for broken limbs; –2 Con for visceral/gut trauma; –2 Int/Wis for severe cranial concussion) occur **only if a character reaches 0 HP**.
- **Duration & Recovery:** Once inflicted by dropping to 0 HP, these direct attribute penalties **persist continuously until all Critical Wounds are fully healed** (i.e., throughout Mortal recovery and until the Critical Wound tier is completely cleared). Once the character is restored past Critical damage into Regular Damage, the direct attribute penalties are removed.

## 5. Lethal vs. Nonlethal Damage, Negative HP & Death
- **Two Trackers:** **Total Damage** and **Nonlethal Damage** ($\text{Lethal} = \text{Total} - \text{Nonlethal}$).
- **Nonlethal Protection:** **Nonlethal damage does not advance the Critical or Mortal wound track.** It can only deplete regular HP and render a target Unconscious.
- **Attacking Unconscious Foes:** Attackers striking an unconscious foe may choose to **convert any nonlethal attack into a lethal attack at their choosing** (e.g., executing a subdued enemy or delivering a coup-de-grace).
- **Damage Priority:** Lethal damage is **always applied against HP tiers first** (regardless of order taken), with nonlethal placed on top. Lethal trauma fills Regular Damage before dipping into deeper tiers.
- **Fast Nonlethal Recovery:** After **5 minutes have elapsed since the last point of damage taken**, nonlethal damage begins to heal naturally at a rate of **1 point per minute** across all levels.
- **Reaching 0 HP:** When Total Damage reduces HP to 0:
  - **Unconscious (Nonlethal Cushion):** If negative lethal damage $\le$ Nonlethal Damage, the creature is Unconscious and stable (no bleed).
  - **Dying / Bleed Clock:** Starts only when negative lethal damage matches and exceeds total Nonlethal Damage ($\text{Net Negative Lethal} > 0$).
  - **Stabilization at 0 HP (Administer First Aid / Recovery Check):**
    - An ally can Administer First Aid using Medicine: **DC 15** (minor bleed / Stage 1) or **DC 20** (severe hemorrhage / Stage 2).
    - Success on the Medicine check stops deterioration immediately. Additionally, a successful or supportive stabilization check allows the dying character to make an immediate **DC 10 flat recovery roll (modified by negative damage: DC $10 + \text{current negative HP}$)** to become stable and halt the bleed clock on their own turn.
  - **Regaining Consciousness from 0 HP:** A stabilized creature at 0 HP does not simply wake up after 10 minutes. Consciousness is only regained:
    1. **After a full night's rest (8 hours of undisturbed sleep/rest)**, or
    2. **Immediately upon receiving active healing from Clockwork technology or biomedical solutions** (e.g. *Cellular Restorative Serum*, biomedical tonic, or suture gizmo).
- **Bleed-Out Deterioration Clock:**
  - **Stage 1 (1 to $\text{Step}$ / Critical capacity):** Takes **1 damage per hour**.
  - **Stage 2 ($\text{Step} + 1$ to $2 \times \text{Step}$):** Takes **1 damage per minute**.
- **Permanent Biological Death:** Occurs when Net Negative Lethal damage equals Critical + Mortal capacity:
  $$\text{Death} \ge 2 \times \text{Step}$$
  No resurrection magic exists in the setting.
- **Massive & Environmental Instant Death:** Outside of lethal bleed-out, instant biological death occurs **only** via:
  1. **Massive Damage:** A single lethal strike dealing damage $\ge \text{Total Max HP}$.
  2. **Defined Environmental Catastrophes:**
     - Crossing the Zone barrier and being struck by an uncontrolled energy/arc discharge blast.
     - Terminal vertical falls exceeding **200 feet** from spire bridges, chasms, or airship scaffolding. Falls up to 200 feet deal standard falling damage capped at **18d6 lethal bludgeoning damage** (the maximum dice rolled for falls before terminal impact).
     - Full immersion in Neither energy / industrial reactor core dissolution.
  *(No other instant-death or save-or-die effects exist in the setting).*

---

## 6. Environmental Exposure Interaction (Shift Scores & Healing)
Natural healing of regular HP and wound tiers is strictly modulated by the **Total Shift Score** ($\text{Air Shift} + \text{Food Shift}$) per `WorldSummary.md §4` and `ClockworkPathfinder/Rules/TheNeither.md`. Total Shift measures extreme biological displacement (e.g., a human living in a deep-zone Deep One environment eating subterranean dwarven fungi, or an orc trapped in the high Aither eating half-elf food):

| Total Shift Score | Healing Rate & Regeneration Effect | Clinical & Field Impact |
| :---: | :--- | :--- |
| **0.0 to 1.5** | **100% Normal Healing Rate** | Standard recovery for regular damage, critical wounds, and mortal wounds. |
| **2.0 to 3.5** | **50% Normal Healing Rate** | Rest and medical recovery take twice as long. |
| **4.0 to 5.0** | **25% Normal Healing Rate** | Sluggish recovery; 1/4 normal HP restored per day/week. |
| **5.5 to 6.0** | **0% Natural Healing + (1d8 + 5) Necrosis Damage/Day** | Natural recovery stops completely. Damage begins **24 hours after exposure** (severe cellular necrosis & organ failure). |
| **6.5 or Higher**| **0% Natural Healing + (3d8 + 10) Collapse Damage/Day** | Acute biological breakdown & toxic shock; damage begins **24 hours after exposure** (rapid fatal dissolution). |

### Starvation / Food Refusal Shift
- **Refusing to Eat:** Completely refusing to eat any food is treated as a **+0.5 Food Shift accumulation per shift/day** of starvation (metabolic stress forcing the body to consume its own unaligned tissue).
- *Example (Orc in High Aither):* An Orc trapped in the Aither (Air Shift 3.0) who refuses to eat foreign food accumulates:
  - **Day 1 (0 days fasting):** Air 3.0 + Starvation 0.0 = **Total 3.0**
  - **Day 2 (1 day fasting):** Air 3.0 + Starvation 0.5 = **Total 3.5**
  - **Day 3 (2 days fasting):** Air 3.0 + Starvation 1.0 = **Total 4.0**
  - **Day 4 (3 days fasting):** Air 3.0 + Starvation 1.5 = **Total 4.5**
  - **Day 5 (4 days fasting):** Air 3.0 + Starvation 2.0 = **Total 5.0**
  - **Day 6 (5 days fasting):** Air 3.0 + Starvation 2.5 = **Total 5.5** (Zero natural healing begins).
  - **Day 7 (24 hours after reaching 5.5):** First **(1d8 + 5) necrosis damage** triggers, repeating every 24 hours.

### Convalescence & Recovery
- Healing from severe shift damage requires a **7-day stabilization period** in an equilibrium environment eating native food (or deep-water fish), followed by **3 points healed per week** of clean living.

---

## Open Questions
- None currently active. All core health tiers, wound triggers, stabilization mechanics, environmental shift damage, and instant death thresholds are codified.
