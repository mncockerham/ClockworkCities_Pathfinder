# Clockwork Pathfinder — Healing, Hit Points, and Mortality

- **Status:** **Core Rules System (In Development)**
- **Location:** `ClockworkPathfinder/Rules/Healing.md`
- **Base Rules:** Rest & Recovery [Player Core p.427], Treat Wounds [Player Core p.240], Dying, Unconscious, & Wounded [Player Core p.410–412]. Precedence per [00_RulesFoundation.md](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/AISummary/00_RulesFoundation.md).

---

## 1. Overview & Core Philosophy

In Pathfinder 2e Remaster, Hit Points represent an abstract, undifferentiated pool of stamina, luck, and minor flesh wounds that can easily be refreshed to maximum between encounters using 10-minute Medicine skill checks.

In **Clockwork Cities**, Hit Points are split into **three distinct anatomical tiers**:
1. **Damage (Regular HP):** Superficial cuts, muscle strains, winded breath, and bruises. Heals rapidly through standard first aid, field tonics, clockwork suture devices, and short rests.
2. **Critical Wounds:** Deep lacerations, fractured ribs, severe burns, internal bleeding, and concussive shock. Requires days of quiet recuperation and bed rest.
3. **Mortal Wounds:** Ruptured internal organs, compound bone breaks, catastrophic arterial trauma, and systemic shock. Requires weeks of continuous bed rest, specialized clinical oversight, or surgical intervention.

This system preserves tactical combat flexibility during active encounters while introducing gritty long-term attrition, systemic consequences for near-death experiences, and clear boundaries between field triage and clinical hospital medicine.

---

## 2. Hit Point Categories & Thresholds

A character’s maximum Hit Points are divided into three tiers based on their **Step Size**:

$$\text{Step} = \left\lfloor \frac{\text{Total Maximum Hit Points}}{4} \right\rfloor$$

| Tier | Category | Hit Point Range (from 0) | Natural Recovery Scale | Functional Condition Penalties | Allowed Healing Methods |
|---|---|---|---|---|---|
| **Step 1** | **Mortal Wounds** | $1 \text{ to } \text{Step}$ | **Weeks** of bed rest | **Major Penalties** (severe physical impairment) | Long-term natural bed rest, advanced clinical surgery |
| **Step 2** | **Critical Wounds** | $(\text{Step} + 1) \text{ to } (2 \times \text{Step})$ | **Days** of quiet rest | **Minor Penalties** (moderate impairment) | Days-scale convalescence, clinical medical care |
| **Remaining** | **Damage** (Regular) | $(2 \times \text{Step} + 1) \text{ to } \text{Max HP}$ | **Hours / Normal PF2e** | **None** (operational stamina intact) | Standard Treat Wounds, Concoctions, Tech Devices, Overnight Rest |

> ### Example Calculation
> A character with **42 Maximum Hit Points** calculates their Step as $\lfloor 42 / 4 \rfloor = 10$:
> - **Mortal Wounds (Step 1):** HP 1 to 10 (10 HP band) &mdash; Major trauma & penalties.
> - **Critical Wounds (Step 2):** HP 11 to 20 (10 HP band) &mdash; Minor trauma & penalties.
> - **Damage (Remaining):** HP 21 to 42 (22 HP band) &mdash; Standard operational buffer; no penalties.

---

## 3. Technology, Concoctions & First Aid Limitations

In a world devoid of divine miracle healing and supernatural magic:
- **Regular Damage Only:** Field concoctions (biomedical stims, coagulant sprays, cellular tinctures) and Clockwork tech devices (pneumatic bone clamps, mechanical suture staples) can **only restore regular Damage HP**.
- **No Instant Clinical Recovery:** Field medicine cannot instantly mend crushed viscera, realign fractured spines, or reattach severed blood vessels represented by Critical or Mortal wound steps.
- **The Chirurgeon Exception:** Highly trained **Chirurgeons** utilizing surgical kits, clinical cleanrooms, and long downtime procedures can perform specialized operations to stabilize and accelerate recovery from deeper wound tiers (see Section 6).

---

## 4. Healing Order & The Heroic Reserve

### A. Hierarchical Recovery (Deepest Upward)
When recovering naturally or under extended medical care, the human body repairs systemic anatomical damage first before rebuilding superficial reserve stamina:
1. **Mortal Wounds (Step 1)** must be completely healed first (measured in weeks).
2. Once Mortal Wounds are fully restored to full capacity, **Critical Wounds (Step 2)** heal (measured in days).
3. Once Critical Wounds are fully cleared, regular **Damage** can be replenished per standard rules (overnight sleep, standard Treat Wounds).

### B. Regular Damage Healing & The Trauma Ceiling ($\text{Level} + \text{CON}$)
- **Standard Pathfinder Recovery:** Regular Damage heals **exactly like standard Pathfinder 2e Remaster**:
  - Rest & Recovery: A full night’s rest (8 hours) restores $\text{CON modifier} \times \text{Character Level}$ HP (minimum 1 HP) per [Player Core p.427].
  - Medicine Skill: The **Treat Wounds** exploration activity [Player Core p.240] functions normally to restore regular Damage using standard Medicine DCs and healing dice (2d8, 4d8, etc.).
  - Concoctions & Tech: Biomedical serums, healing tonics, and clockwork suture devices restore regular Damage as written.
- **The Trauma Ceiling ($\text{Level} + \text{CON}$):**
  - If a character has **any unhealed Critical Wounds or Mortal Wounds**, their operational capacity is biologically constrained by their internal injuries.
  - While carrying any Critical or Mortal trauma, **the maximum Regular Damage Hit Points a character can have at any one time is capped at:**
    $$\text{Max Regular HP} = \text{Character Level} + \text{Constitution Modifier} \quad (\text{minimum } 1)$$
  - *Example:* A 5th-level Soldier with a $+3$ Constitution modifier has a normal Regular Damage buffer of 25 HP. 
    - When completely healthy, they can heal up to their full 25 Regular HP.
    - If they suffer deep internal trauma and currently carry **Critical or Mortal damage**, their active stamina cannot exceed their body's fractured state. Their Regular Damage pool is capped at $5 + 3 = \mathbf{8\text{ HP}}$. 
    - They can use Treat Wounds, sleep, or drink healing tonics to recover up to this **8 HP ceiling** to stay on their feet and fight, but any healing beyond 8 is lost until their deeper Critical and Mortal wounds are medically repaired.

---

### C. Clinical Recuperation & Medical Care Rates
When recovering from deep structural trauma, healing occurs on an extended timescale determined by the quality of rest and medical intervention:

| Wound Tier | Baseline Bed Rest (Clean Environment) | Skilled Medical Attention (Daily Treatment) | Full Skilled Care Bonus (Hospitalization / Sanitarium) |
|---|---|---|---|
| **Critical Wounds (Step 2)** | **$\lfloor \frac{1}{5} \text{Level} \rfloor + \text{CON}$ HP per day** (min 1) | **$\text{CON}$ HP per day** (minimum 1, uses full CON modifier) | **1 full day** of dedicated clinical care restores **all regular Damage HP** regardless of trauma ceiling. |
| **Mortal Wounds (Step 1)** | **$\lfloor \frac{1}{5} \text{Level} \rfloor + \text{CON}$ HP per week** (min 1) | **$\text{CON}$ HP per week** (minimum 1, uses full CON modifier) | **1 full week** of continuous clinical surgery/monitoring restores **all regular Damage HP**. |

- **Medical Attention Requirement:** Requires a character trained in Medicine or a professional Chirurgeon to spend at least 1 hour each day (or week) tending to sutures, changing sterile dressings, and monitoring vitals (DC 15 for Critical, DC 20 for Mortal).
- **Environmental Hazard Warning:** If resting in high Neither exposure (Total Shift Score $\ge 4$), natural healing is cut by 75% or halted entirely per [TheNeither.md](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Rules/TheNeither.md). Deep recovery requires clean Aither wards, sealed airlocks, or hyperbaric sanitariums.

---

## 5. Anatomical Trauma & Wound Consequences

When an attack or hazard cuts through a character's regular Damage buffer and bites into **Critical Wounds** or **Mortal Wounds**, the character sustains a specific, debilitating anatomical injury. 

### A. Determining the Wound
Whenever a character enters a deeper wound tier (or when taking damage while already within that tier from a new hit):
- The player or GM rolls on or selects from the **Anatomical Wound Consequence Table** based on the damage type (bludgeoning, piercing, slashing, fire, electrical arc, acid/caustic, or poison/chemical).
- The narrative description of the blow reflects the mechanical impairment (e.g., shattered kneecap, punctured lung, cranial concussive tremor).
- **Severity Levels:**
  - **Critical Tier Injury:** Moderate impairment. Employs standard PF2e conditions (*Clumsy 1*, *Enfeebled 1*, *Stupefied 1*) along with targeted speed penalties.
  - **Mortal Tier Injury:** Severe anatomical disruption. Doubles or compounds standard conditions (*Clumsy 2*, *Enfeebled 2*, *Drained 1–2*, *Stupefied 2*) and can impose **direct attribute modifier penalties** for traumatic localized destruction.
- **Duration:** An anatomical consequence remains active until the underlying wound tier (Critical or Mortal) is fully repaired through convalescence or surgery.

### B. Anatomical Wound Consequence Table (d8 or Choice)

| d8 | Hit Location & Last Blow | Critical Wound Consequence (Tier 2) | Mortal Wound Consequence (Tier 1) | Narrative & Damage Types |
|:---:|---|---|---|---|
| **1** | **Leg / Knee / Foot** | **Speed –5 ft**, *Clumsy 1* (or –1 Dex check penalty). | **Speed –10 ft**, *Clumsy 2*, plus **–2 Strength & –3 Dexterity** modifier penalty. | Shattered tibia, ruptured Achilles, mangled knee joint (Bludgeoning, Piercing, Arc shock). |
| **2** | **Arm / Shoulder / Hand** | *Enfeebled 1* (or –1 Str/Dex check penalty); dropped off-hand item. | *Enfeebled 2*, plus **–3 Strength & –2 Dexterity** modifier penalty; arm broken (cannot use 2-handed weapons or off-hand). | Compound fracture of humerus, severed forearm tendons, crushed hand (Bludgeoning, Slashing, Piercing). |
| **3** | **Torso / Ribs / Punctured Lung** | *Enfeebled 1*, *Clumsy 1*; DC 10 Flat check to use 3-action activities without coughing blood. | *Drained 2*, *Enfeebled 2*, **–5 ft Speed**; severe internal hemorrhaging; breathing causes agonizing spasms. | Flail chest, punctured pleura, cracked sternum (Bludgeoning, Bullets, Shrapnel). |
| **4** | **Head / Concussion / Cranial Shock** | *Stupefied 1* (–1 status to Int/Wis/Cha checks/DCs; DC 5 flat check to maintain concentration). | *Stupefied 2*, plus **–2 to Intelligence & Wisdom** modifiers; flat check DC 7 to cast concoctions/devices; blurred vision (*Concealed* to all targets beyond 30 ft). | Skull fissure, severe traumatic brain injury, ocular burst (Bludgeoning, Concussive blast, Shockwave). |
| **5** | **Abdomen / Visceral Rupture** | *Drained 1* (Max HP reduced by 1 per level); nauseated by solid food. | *Drained 2*, *Enfeebled 2*, plus **–2 to Constitution** modifier; internal laceration of spleen/liver. | Gut puncture, bayonet wound, high-caliber gut shot, deep acid burn (Piercing, Slashing, Acid). |
| **6** | **Neurochemical Shock / Toxin Burden** | *Stupefied 1*, –1 status penalty to Perception and Initiative; thinking feels sluggish. | *Stupefied 2*, *Clumsy 1*, plus **–3 to Wisdom & Charisma** modifiers; memory gaps, nerve tremors, hallucinations. | Caustic Neither lung rot, neurotoxin injection, bio-alchemical sepsis (Poison, Neither gas, Caustic venom). |
| **7** | **Sensory Organs (Eyes / Ears / Face)** | Blinded in one eye (*Dazzled* permanently until healed) OR Deafened. | Total sensory blackout: **Blinded** (or *Clumsy 2* if partially blinded) and **–2 Charisma** from gruesome facial destruction. | Flash powder, arc flash, shrapnel spray, vitriol splash (Fire, Electricity, Acid). |
| **8** | **Extensive Burns / Cellular Necrosis** | Persistent damage vulnerability; *Enfeebled 1*, skin charred and agonizing to move. | *Drained 1*, *Clumsy 2*, *Enfeebled 2*; widespread skin graft failure, severe infection risk; moving costs 1 additional action once per round. | Boiling steam pipe burst, high-exposure Zone flare, incendiary grenade (Fire, Neither-burn, Caustic). |

> *Note on Direct Stat Damage:* Where direct attribute penalties are listed (e.g., –2 Strength), they directly reduce that ability's final modifier, reducing all dependent attack rolls, damages, checks, and DCs. Once the character heals out of the Mortal wound tier into Critical, the direct stat penalty drops to the corresponding Critical condition (*Enfeebled 1* or *Clumsy 1*).

---

## 6. Lethal vs. Nonlethal Damage & Tracking

Clockwork Pathfinder uses a clean, two-pool damage hierarchy: **Total Damage** and **Nonlethal Damage** ($\text{Lethal Damage} = \text{Total Damage} - \text{Nonlethal Damage}$).

### A. Lethal Damage Takes Precedence in Wound Tiers
- **Lethal Damage is Always Counted First:** Regardless of the actual chronological order in which hits were received during combat, **all lethal damage is applied against the character's Hit Point tiers first**.
- **Nonlethal Sits on Top:** Nonlethal damage (concussions, exhaustion, blunt trauma, sedation) is applied only *after* lethal damage has been positioned against the HP pool.
- *Example:* A character has **40 Max HP** (Regular Damage: 21–40 [20 HP], Critical: 11–20 [10 HP], Mortal: 1–10 [10 HP]). 
  - If they take **15 Lethal damage** and **15 Nonlethal damage** in a fight (Total Damage = 30):
  - The 15 Lethal damage is counted first, residing entirely within the **Regular Damage tier** (40 down to 25). It does **not** count as Critical or Mortal wound trauma.
  - The 15 Nonlethal damage sits on top (25 down to 10), temporarily placing their current effective HP at 10.
  - Because the nonlethal damage will dissipate rapidly after the fight, the character's underlying real biological body has only suffered superficial, easily healed regular damage—their deeper organs and bones are intact!

### B. Post-Combat Recovery of Nonlethal Damage
- **Universal Fast Recovery:** Nonlethal damage represents temporary breathlessness, concussive disorientation, and superficial bruising rather than structural cellular destruction.
- **1 Point Per Minute:** Once combat ends and a character can catch their breath, **all Nonlethal damage naturally heals at a rate of 1 point per minute**, regardless of character level or tier.
  - A character carrying 15 points of nonlethal damage completely clears it in just 15 minutes of rest, restoring their effective HP back up to their true lethal HP line without expending any medical supplies.

### C. Reaching 0 HP (Unconscious vs. Dying Boundary)
- When **Total Damage reduces effective HP to 0**, the character is incapacitated and drops out of combat.
- **Unconscious (Protected by Nonlethal Cushion):** Because lethal damage is counted first, if total lethal damage does not exceed Maximum HP, the character has not suffered fatal anatomical destruction. They are **Unconscious and stable**—knocked out cold, but not bleeding or dying.
- **Transition to Bleed-Out Clock:** A character only enters the active Bleed-Out Clock (taking damage over time in negative HP) once **negative lethal damage matches and exceeds their total Nonlethal Damage** ($\text{Net Negative Lethal} > 0$).

---

## 7. Negative Hit Points, Bleeding Out, and Death

Clockwork Pathfinder replaces the standard PF2e flat-check recovery system with a deterministic biological bleed-out clock based on the character's **Step Size** ($\text{Step} = \lfloor \text{Max HP} / 4 \rfloor$):

### A. Entering Negative Hit Points & The Nonlethal Threshold
- When Total Damage reduces HP to 0, incoming lethal damage drives the character into negative hit points ($-\text{HP}$).
- **The Nonlethal Offset:** If a character took nonlethal damage, their body was knocked out before suffering full anatomical destruction. Lethal damage into negative HP must first match their total **Nonlethal Damage** before active tissue collapse begins:
  - $\text{Net Negative Lethal} = \text{Total Negative Damage} - \text{Total Nonlethal Damage}$.
  - While $\text{Net Negative Lethal} \le 0$, the character is **Unconscious and stable**.
  - Once $\text{Net Negative Lethal} > 0$, true arterial bleed-out begins.

### B. Bleed-Out Deterioration Clock
Once lethal damage exceeds the nonlethal cushion and cuts into true negative flesh, the character takes automatic bleed damage over time until stabilized:

1. **Slow Hemorrhage Stage (1 point per hour):**
   - While Net Negative Lethal damage is between **1 and $\text{Step}$** (within their Critical capacity):
   - The character takes **1 point of lethal damage every hour**.
   - *Narrative effect:* Deep systemic shock, internal oozing, or slow organ failure. The party has a substantial operational window (several hours) to rescue, evacuate, or administer surgical aid.
2. **Acute Arterial Collapse Stage (1 point per minute):**
   - When Net Negative Lethal damage exceeds the Critical threshold (from $\text{Step} + 1$ up to $2 \times \text{Step}$):
   - Bleed-out dramatically accelerates: the character takes **1 point of lethal damage every minute** (10 combat rounds).
   - *Narrative effect:* Severe arterial rupture, cranial hemorrhage, or organ rupture. Rapid terminal decline requiring immediate stabilization within minutes.

### C. Biological Death Threshold
- A character suffers **Permanent Biological Death** when their net negative lethal damage equals the combined capacity of their **Critical and Mortal damage tiers**:
  $$\text{Net Negative Lethal} \ge 2 \times \text{Step}$$
- At this threshold, irreversible cellular destruction or brain death occurs. Because supernatural resurrection magic does not exist in the Clockwork Cities setting, the character is permanently dead.

> ### Concrete Example
> A character with **40 Maximum Hit Points** has a Step size of $\lfloor 40 / 4 \rfloor = 10$:
> - **Mortal capacity:** 10 HP
> - **Critical capacity:** 10 HP
> - **Regular Damage buffer:** 20 HP
> - **Death Threshold:** Net negative lethal damage of 20 ($2 \times 10$).
> 
> **Combat Scenario:**
> 1. The character takes **12 points of Nonlethal damage** (fists/clubs) and **28 points of Lethal damage** (sword cuts).
> 2. Total Damage = 40. Current HP = 0.
> 3. The character falls **Unconscious**. Because the lethal damage (28) has not exceeded their 40 Max HP (negative lethal has not matched their 12 nonlethal), they are knocked out cold but **stable**—not dying or bleeding.
> 4. If an enemy stabs them while down for **15 points of Lethal damage**:
>    - Total lethal damage is now 43 (3 points into true negative lethal).
>    - Negative lethal (3) now exceeds the nonlethal threshold!
>    - Net Negative Lethal = 3.
>    - The character enters **Stage 1 Bleed-Out**: taking **1 damage per hour**. They have 7 hours before reaching Stage 2 (Net Negative 11+), and 17 hours before Death (Net Negative 20).

### D. Massive Damage
- If a creature suffers a single strike where the leftover lethal damage equals or exceeds their Maximum Hit Points, catastrophic anatomical destruction occurs (decapitation, total torso rupture, complete incineration), causing instant death without entering the bleed-out track.

---

## 8. Environmental & Atmospheric Interactions

As established in [TheNeither.md](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Rules/TheNeither.md) and [WorldSummary.md](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/AISummary/WorldSummary.md):
- **Neither Exposure Modulation:** Natural recuperation is directly suppressed by high Total Shift Scores:
  - **Score 0–1.5:** 100% normal recovery.
  - **Score 2–3.5:** 50% recovery rate.
  - **Score 4–5:** 25% recovery rate.
  - **Score 5.5–6:** 0 natural healing, plus 1d8 damage/day from cellular collapse.
  - **Score 6.5+:** 0 natural healing, plus 3d8 damage/day.
- **Convalescence in Clean Air:** True biological recovery from deep wound steps requires access to clean native air (Aither for Types 1–3, Neither for Type 5, etc.) or pressurized hyperbaric sanatoriums.
