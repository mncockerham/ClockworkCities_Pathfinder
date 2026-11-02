# Chirurgeon

- **Base Class:** Alchemist (Chirurgeon) `[Player Core 2 p.44]`
- **Status:** **Modified** (Split from Alchemist; specialized exclusively in restorative concoctions, antidotes, acids, and poisons; mutagen and familiar feats removed)
- **Availability:** **Primary PC Class** (Full 1–20 progression)
- **Discipline / Trait:** Concoctions (Biomedical & Toxicological)

---

## 1. Setting Overview
*The spore-brewers, field triage directors, and clockwork swarm-surgeons of the Great Spires—commanding chittering hordes of miniature mechanical constructs to deliver biomedical elixirs to allies and corrosive solvents to foes.*

### The 3-Tier Medical Hierarchy in Spire Society
Medical practice in the Spires follows a distinct Victorian division:
- **Tier 1 — The Doctor / Medical Researcher (Scholar):** Aristocratic physicians and university chairs (Status 4–6) operating high-cost hospital dynamos, diagnostic cleanrooms, and long-term inpatient surgery.
- **Tier 2 — The Paramedic / Clinic Worker (Chirurgeon):** Working-class medical practitioners (Status 2–4) managing street clinics, ambulance triage, spore-brewing, auto-injectors, and emergency Adrenal Injectors.
- **Tier 3 — The Field Medic (Chirurgeon Archetype):** Soldiers, Scouts, and Survivors with emergency trauma training who keep allies alive when full doctors are miles away.

- **In-World Identity:** Trained practitioners from the University Medical Faculty, hospital attendants in the Luxury and Craft Wards, or field surgeons who patch together soldiers and laborers in the Warrens and Lower Circles. 
- **Typical Social Class & Backing:** Professional / University Graduate (Status 4–5), Guild Apothecary (Status 2–3), or private physician retained by a Lesser Noble or Merchant House.
- **Physical / Scientific Explanation:** Deep knowledge of Neither fungi biochemistry (cultivated Sycelium, Deep strains), biological catalysts, coagulation agents, antiseptics, caustic acids, and organic toxins. They stabilize volatile compounds for immediate clinical or field application.

---

## 2. Core Class Features
*At baseline, Chirurgeon class features match the Pathfinder 2e Remaster Alchemist [Player Core 2 p.44–53], restricted to restorative items, antidotes, poisons, and acids.*

### Chirurgeon Advancement (Levels 1–20)
*Reference: Table 2–2: Alchemist Advancement [Player Core 2 p.46]*

| Level | Class Features Gained |
|:---:|---|
| **1** | Ancestry and background, initial proficiencies, Advanced Concoctions, Versatile Vials, Chirurgeon Field (Restorative/Antidote/Acid/Poison), Formula Book, Quick Concoction, Biomedical Autonomy (0 AP), Galvanic Ward Rig, Hemostatic Coagulants, Daily Spore Incubator (Prophylactic DR & Solvents), Neither-Bio Resonance, 1st-level Chirurgeon feat |
| **2** | Chirurgeon feat, skill feat |
| **3** | General feat, skill increase, Field Specialty (Medicine via Crafting) |
| **4** | Chirurgeon feat, skill feat, Clockwork Micro-Drone Swarm (Autonomous Delivery & Interception) |
| **5** | Attribute boosts (4 attributes), Field Discovery, skill increase, Powerful Concoctions |
| **6** | Chirurgeon feat, skill feat |
| **7** | Concoction Expertise (class DC to Expert), general feat, Iron Will (Will to Expert), skill increase, Weapon Specialization |
| **8** | Chirurgeon feat, skill feat, Surgical Swarm Array (Extended Range & Multi-Target Administration) |
| **9** | Double Brew, Alertness (Perception to Expert), skill increase |
| **10** | Attribute boosts (4 attributes), Chirurgeon feat, skill feat |
| **11** | General feat, Great Fortitude (Fortitude to Master), skill increase, Simple Weapon Expertise |
| **12** | Chirurgeon feat, skill feat |
| **13** | Greater Field Discovery, Unarmored Defense Expertise, skill increase |
| **14** | Chirurgeon feat, skill feat |
| **15** | Attribute boosts (4 attributes), Evasion (Reflex to Master), general feat, Concoction Mastery (class DC to Master), skill increase |
| **16** | Chirurgeon feat, skill feat |
| **17** | Concoction Alacrity, skill increase |
| **18** | Chirurgeon feat, skill feat |
| **19** | General feat, Unarmored Defense Mastery, skill increase |
| **20** | Attribute boosts (4 attributes), Chirurgeon feat, skill feat |

---

### Dual-Attribute Foundation: INT & WIS Mathematical Scaling (The 'Stat Trick')
*The Chirurgeon functions on a pure Spellcaster chassis (unarmored / simple weapons only), deriving all armor defense, saving throw triggers, and operational competence strictly from mental faculties (INT & WIS) rather than physical attributes:*

- **Analytical Defense (INT Replaces DEX for AC):**
  - The Chirurgeon calculates trajectory vectors and biological threat corridors purely through analytical spatial modeling.
  - The Chirurgeon uses their **Intelligence modifier in place of Dexterity** when calculating their **Armor Class (AC)**:
    $$\text{AC} = 10 + \text{Proficiency Bonus} + \text{INT Modifier}$$
  - Because the Chirurgeon relies on clinical lab coats and unarmored attire (Spellcaster armor progression), there is **no Dexterity cap** limiting this Intelligence contribution.

- **Neither-Bio Resonance (Universal Skill Substitution in the Neither/Wilds):**
  - Through symbiotic acclimation to Neither fungi and the micro-drone swarm tethered to their harness, the Chirurgeon does not rely on brute muscle or reflexive agility when outside civilized Spire wards.
  - When operating in **The Neither, the Warrens, or wild Zone perimeters**, the Chirurgeon uses their **Intelligence modifier in place of Dexterity for all Dexterity-based skill checks** (Stealth, Thievery, Acrobatics), and uses their **Wisdom modifier in place of Strength for all Strength-based skill checks** (Athletics).
  - *Natural Balance:* The Chirurgeon remains capped by standard skill proficiency ranks (Trained/Expert). They will never out-perform specialized Rogues or Soldiers who invest in Master/Legendary skill feats, but they effortlessly pull their own weight in field navigation and casualty evacuation.

- **Saving Throw Delivery on Enemy Effects (Class DC vs. Enemy Saves):**
  - Unlike martial attacks that make attack rolls against AC, **all offensive Chirurgeon concoctions, micro-drone swarm injections, caustic solvents, and neuro-spores require an immediate Saving Throw** (Fortitude or Reflex) by the target against the Chirurgeon's **Class DC** ($10 + \text{Proficiency} + \text{INT Modifier}$).
  - *Degrees of Success:* Critical Success (no effect), Success (half effect / 1 round), Failure (full effect), Critical Failure (double effect / persistent).

- **Strict Multiplier Scaling: Every Ability Impacts as X * INT or X * WIS:**
  1. **Galvanic Ward (Temp HP):** Grants **$\text{Level} \times \text{INT modifier}$** Temporary Hit Points (min $2 \times \text{INT}$ at Lv 1).
  2. **Mycological Solvents (Strip Enemy Hardness / DR):** Reduces target's Hardness and Damage Resistance by **$2 \times \text{INT modifier}$** on a failed save ($1 \times \text{INT}$ on success).
  3. **Micro-Drone Interception Barrier:** Micro-drones absorb incoming strike damage equal to **$2 \times \text{INT modifier}$** before shattering.
  4. **Restorative Concoctions & Salves (Regular HP Heal):** Healing formulas restore baseline dice plus **$2 \times \text{WIS modifier}$** Hit Points.
  5. **Prophylactic Dermal Inoculation (Party DR):** Grants Damage Reduction (Resistance) to chosen damage types equal to **$1 \times \text{WIS modifier}$** (Lv 1–4) or **$2 \times \text{WIS modifier}$** (Lv 5+).
  6. **Neuro-Spore Metabolic Depression:** On a failed Fortitude save, target suffers a status penalty to saves and perception equal to **$\lfloor \text{WIS modifier} / 2 \rfloor$** (min –1).

- **Spellcaster Weapon & Armor Chassis (The Pure Medic Trade-Off):**
  - **Armor:** Trained in Unarmored Defense only (advances to Expert at Level 13, Master at Level 19). They wear no heavy plates or bulky gear.
  - **Weapons:** Trained in Simple Weapons and Unarmed attacks only (advances to Expert at Level 11, never Master).
  - **The Self-Enforcing Balance:** With caster weapon proficiencies and all abilities scaling strictly with INT and WIS, taking martial stats (STR/DEX) cripples their AC, destroys their save DCs, and zeroes out their multipliers. Committing 100% to INT and WIS makes them the ultimate field-survival and triage commander.

---

### Core Class Feature Details
| Level | Feature | Base Reference | Status | Notes / Clockwork Cities Adaptation |
|---|---|---|---|---|
| 1 | Hit Points | `[Player Core 2 p.44]` | **Unchanged** | 8 + Constitution modifier per level. |
| 1 | Key Attribute | `[Player Core 2 p.44]` | **Unchanged** | Intelligence. |
| 1 | Initial Proficiencies & Analytical Defense | `[Player Core 2 p.44]` | **Modified** | **Caster Proficiency Chassis.**<br>• Perception: Trained.<br>• Saves: Fortitude: Expert, Reflex: Trained, Will: Expert.<br>• Skills: Trained in Crafting, Medicine, plus 3 + Int mod.<br>• Attacks: Trained in simple weapons and unarmed attacks (advances to Expert at Lv 11, never Master).<br>• Defenses: Trained in **unarmored defense only** (advances to Expert at Lv 13, Master at Lv 19).<br>• Class DC: Trained in Chirurgeon class DC (scales with INT).<br>• **Analytical Defense:** You calculate physical threat vectors analytically. You use your **Intelligence modifier in place of Dexterity** for your **Armor Class (AC)**: $\text{AC} = 10 + \text{Proficiency} + \text{INT Modifier}$ (no Dex cap unarmored).<br>• **Neither-Bio Resonance:** In the Neither, Warrens, or Wilds, replace **Dexterity with Intelligence** for all DEX skills (Stealth, Thievery, Acrobatics), and replace **Strength with Wisdom** for all STR skills (Athletics).<br>• **All Enemy Effects Trigger Saves:** Offensive concoctions, solvents, neuro-spores, and drone injections do not use attack rolls; they trigger **Fortitude or Reflex saves** against your **Class DC** ($10 + \text{Prof} + \text{INT}$). |
| 1 | Starting Social Skills (`Understanding`) & Social Advancement | `[Skills.md]` | **New** | **Total Starting Pool (Trained):** `2 Automatic + 2 Class Base + CHA Modifier` (min 1 selectable).<br>• **2 Automatic Broad Entries:** Choose 2 from **Bureaucracy & University Connections** (*Sanatoriums, Chirurgery & Public Health*, *University Collegium & Natural Philosophy*) or **Trade Guilds & Commercial Houses** (*Alchemists, Apothecaries & Spore-Brewers*).<br>• **Selectable Starting Broad Groups:** Choose your `2 + CHA Mod` entries from **Bureaucracy & University Connections** (*Public Health/Sanatoriums/Coroners*), **Trade Guilds & Commercial Houses** (*Apothecaries/Spore-Brewers*), **Military** (*Crown Army Regiments / Field Hospitals*), **Labor Organizations** (*Agricultural Combines & Mela Vat Workers*, *Subterranean Miners & Sump Crews*), or **Criminal Underworld** (*Fences, Pawnshops & Back-Alley Stitchers*, *Warrens Rookeries*).<br>• **Narrow Aspect Choice (Scope vs. Impact):** For each Broad Skill chosen, select its specificity tier: **1) Broad Only** (`+0`, widest reach across the Spire), **2) Singular Sub-Group** (`+1`, specific apothecary guild/medical faculty), **3) Specific Place** (`+2`, single hospital/sanatorium/ward clinic), or **4) Specific Person** (`+3` & auto-Phase 1 intel on one named individual).<br>• **Tier 3 Social Advancement Track (Separate from Skill Increases):** Gain **6 Social Advancements** across Levels 1–20 (**every 3 levels: `3, 6, 9, 12, 15, 18`**). Spend each to **add a new Broad Social Skill (Trained)** OR **deepen an existing entry's Proficiency Tier** (**Expert** at Lv 5+, **Master** at Lv 11+, **Legendary** at Lv 18+; max 1 Legendary entry in your core sphere). May swap up to **2** entries per level-up. |
| 1 | Biomedical Autonomy (0 AP Cost) | New | **New** | All personal healing tonics, restorative sera, versatile vials, auto-injectors, and medical concoctions you prepare, administer, or use cost **0 Active Surge AP** for you. AP costs only apply if you hand a concoction to an ally to self-administer, or when you operate complex external clockwork/energy devices outside your medical craft. |
| 1 | Galvanic Ward Rig | New | **New** | **Personal Emergency Force Field (1/Hour).** A compact waist-mounted clockwork condenser pack. Once per hour as a Single Action [A] (or Reaction [R] when targeted by an attack), you activate the ward to gain Temporary Hit Points equal to **$\\text{Level} \\times \\text{INT modifier}$** (min  \\times \\text{INT}$ at Level 1; lasts 1 minute or until depleted). Incoming damage drains Temporary HP first; while this barrier holds, damage cannot puncture downward into Critical or Mortal wound thresholds (AISummary/20_Healing.md). |
| 1 | Hemostatic Coagulants | New | **New** | **Combat Bleed Removal.** Pressurized fibrin foam / carbolic spray. As a Single Action [A] (or Reaction [R] when an adjacent ally takes piercing or slashing damage), you instantly end any active **persistent bleed damage** on yourself or an ally without requiring a flat check. |
| 1 | Daily Spore Incubator (Prophylaxis & Solvents) | New | **New** | **Modular Daily Formulations.** Each morning during daily prep, you cultivate living fungal strains from your field incubator. You prepare two signature modular assets:<br>• **1. Prophylactic Dermal Inoculation (DR):** Topical bio-resins that harden against environmental harm. Choose 1 damage type at Lv 1–4 (Acid, Cold, Electricity, Fire, Piercing shrapnel, or Slashing) to grant **Damage Reduction (Resistance)** equal to **$1 \times \text{WIS modifier}$** to yourself and up to 4 allies for 1 hour. At Lv 5+, choose up to 2 types granting **$2 \times \text{WIS modifier}$** DR (e.g. 8–10 DR). At Lv 10+, choose up to 4 types granting **$2 \times \text{WIS modifier}$** DR.<br>• **2. Mycological Solvents (Strip Enemy DR/Hardness):** Deep-Neither spore cultures that dissolve armor, scales, and constructs. Delivered via micro-drone swarm or aerosol. Target must attempt a **Reflex saving throw** against your Class DC. On a Failure, the target's **Damage Resistance or Hardness is reduced by $2 \times \text{INT modifier}$** for 1 minute ($1 \times \text{INT}$ on a Success; $3 \times \text{INT}$ on a Critical Failure). |
| 1 | Advanced Concoctions & Versatile Vials | [Player Core 2 p.47] | **Modified** | Create temporary infused items during daily prep and on the fly. **Restriction:** May ONLY craft items with the **Healing**, **Antidote / Antiplague**, **Poison**, **Acid**, or **Adrenaline / Stimulant** traits (including the Adrenal Injector [AISummary/20_Healing.md §2] and Combat Surge Auto-Injectors). Cannot brew mutagens or explosive ordnance.<br>**WIS Healing Potency:** When administering an infused healing concoction or salve, add ** \\times \\text{WIS modifier}$** to the total Regular HP restored.<br>**Spire Law & Volatile Solutions (Crucial Balance Rule):** Ward Constables and checkpoint inspectors **do not make any legal distinction** between standard hazardous items and the improvised concoctions of Chirurgeons. Inside civilized Spire wards, carrying volatile offensive solutions (acids, lethal poisons, or reactive chemical precursors capable of synthesizing them) is a severe criminal violation treated just as harshly as carrying a live grenade. |
| 1 | Field Specialization: Chirurgy | [Player Core 2 p.47] | **Modified** | You can use your proficiency rank in Crafting in place of your proficiency rank in Medicine for Treat Wounds, Battle Medicine, and medical skill checks. |
| 1 | Quick Concoctions | [Player Core 2 p.48] | **Modified** | Rapidly mix a versatile vial into a single dose of a known healing salve, antidote, acid vial, or poison using 1 action. |
| 4 | Clockwork Micro-Drone Swarm | New | **New** | **Autonomous Delivery & Interception (30 ft).** You deploy a localized swarm of miniature clockwork arachnid scuttlers and winged syringe-drones tethered to your harness. Commanded via acoustic whistle or magnetic pulse:<br>• **Allied Triage:** Scuttler-drones crawl or fly up to **30 feet** to instantly deliver healing tonics, hemostatics, or prophylactic resins to any willing ally (auto-administered, no roll required).<br>• **Offensive Swarming:** Micro-drones swarm an enemy within 30 feet to deliver corrosive solvents, neuro-spores, or acids. The target must attempt a **Fortitude or Reflex save** against your Class DC ($10 + \text{Prof} + \text{INT}$).<br>• **Mechanical Interception:** Once per round as a Reaction [R], when an adjacent ally is targeted by a physical strike, a cloud of micro-drones interposes itself, absorbing damage equal to **$2 \times \text{INT modifier}$** before shattering. |
| 5 | Powerful Concoctions | [Player Core 2 p.48] | **Unchanged** | Save DCs for your concoctions scale with your class DC if higher than standard item DC. |
| 8 | Surgical Swarm Array | New | **New** | **Extended Swarm Radius & Multi-Vector Delivery (60 ft).** Your clockwork horde expands into a coordinated multi-drone network:<br>• **Extended Range:** Delivery and swarming radius increases to **60 feet**.<br>• **Multi-Target Inoculation:** By expending 1 additional Versatile Vial, your swarm splits into sub-vectors, delivering a restorative salve, hemostatic foam, or prophylactic resin to **up to 3 separate allies** across the battlefield in a single 2-action command.<br>• **Swarm Screen:** While your micro-drones orbit you or an ally, they provide **Lesser Cover (+1 circumstance bonus to AC)** against ranged attacks. |
| 9 | Double Brew | [Player Core 2 p.48] | **Unchanged** | Spend 2 actions and 2 vials to rapidly prepare 2 concoctions simultaneously. |
| 13 | Greater Field Discovery | `[Player Core 2 p.48]` | **Modified** | When creating healing or restorative concoctions using Advanced Concoctions, you gain additional batches per reagent. |
| 17 | Concoction Alacrity | `[Player Core 2 p.49]` | **Unchanged** | Quick Concoction costs only 1 action for two items or free action triggers. |

---

## 3. Class Feats
*Mutagen and Familiar feats are completely **Removed**.*

### Feat Status & Adaptations
| Level | Feats Available / Status | Base Reference | Status | Clockwork Cities Adaptation / Rationale |
|---|---|---|---|---|
| **1st** | Alchemical Familiar | `[PC2 p.54]` | **Removed** | No homunculi/familiars in setting. |
| **1st** | Quick Bomber, Far Lobber | `[PC2 p.54]` | **Removed** | Reserved for Mad Bomber. |
| **1st** | subtle delivery, alchemical crafting | `[PC2 p.54]` | **Unchanged** | Blowgun/injector delivery and crafting baseline. |
| **2nd** | Revivifying Mutagen | `[PC2 p.55]` | **Removed** | Mutagens removed from setting. |
| **2nd** | Poison Weapon, Demolition Charge | `[PC2 p.55]` | **Modified** | Poison Weapon: **Unchanged**; Demolition Charge: **Removed** (Mad Bomber only). |
| **4th** | Healing Vapor | `[PC2 p.56]` | **Unchanged** | Aerosolize an elixir of life / healing tonic into an area burst. |
| **4th** | Efficient Alchemy, Tenacious Toxins | `[PC2 p.56]` | **Unchanged** | Faster batch preparation and persistent poison damage. |
| **6th** | Combine Elixirs | `[PC2 p.56]` | **Modified** | Combine two curative, antidote, or poison effects into a single dose. Mutagens cannot be included. |
| **6th** | Collar of the Shifting Ape | `[PC2 p.56]` | **Removed** | Mutagen-based; removed. |
| **8th** | Perpetually Infused, Sticky Poison | `[PC2 p.57]` | **Unchanged** | Unlimited low-tier curative/acid vials; weapon poison lasts multiple strikes. |
| **10th** | Merciful Elixir | `[PC2 p.58]` | **Unchanged** | Healing concoctions remove conditions (clumsy, enfeebled, stupefied, paralyzed). |
| **12th** | Invigorating Elixir, Uncanny Chemist | `[PC2 p.59]` | **Unchanged** | Grants temporary metabolic stamina and emergency preparation. |
| **14th** | True Debilitating Poison | `[PC2 p.59]` | **Unchanged** | Toxic strikes inflict debilitating status penalties. |
| **16th** | Eternal Elixir | `[PC2 p.60]` | **Modified** | Extend a minute-duration curative or physiological buff. Mutagens cannot be extended. |
| **18th** | Miracle Worker | `[PC2 p.60]` | **Unchanged** | Once per day, a potent restorative concoction brings a creature back from the threshold of death (within 1 round of dying). |
| **20th** | Crafting Paragon, Perfect Medicine | `[PC2 p.61]` | **Unchanged** | Master-level chemical formulation and instant critical medical success. |

---

## 4. Spells & Apparatus (If Applicable)
*Not applicable.* The Chirurgeon uses the Concoction crafting system (Versatile Vials, Infused Reagents, and Quick Concoction) rather than spell slots. Per `AISummary/20_Healing.md`, Chirurgeon healing concoctions restore **regular Damage Hit Points only**; they cannot instantly heal Critical or Mortal wounds.

---

## 5. Multiclass Archetype (Field Medic / Chirurgeon Dedication)
*Known across Spire army regiments, constabulary squads, and frontier caravans as the **Field Medic**, this archetype allows martials, scouts, and operatives to master combat triage, life-saving stimulants, and emergency Neither-biochemical first aid.*

- **Field Medic Dedication (Chirurgeon Dedication — Feat 2):** `[Player Core 2 p.218]`  
  - **Prerequisites:** Intelligence 14 (+2), Trained in Crafting or Medicine.
  - **Benefits:** Trained in Chirurgeon class DC; gain a modest pool of Versatile Vials each day. You can craft temporary infused items with the **Healing**, **Antidote**, **Acid**, or **Poison** traits only. Gain the Chirurgy benefit (use Crafting for Medicine).
- **Basic Concoctions (Feat 4):** Gain a 1st- or 2nd-level Chirurgeon feat.
- **Chirurgeon's Resiliency (Feat 4):** Gain 3 additional HP for each Chirurgeon archetype feat taken.
- **Advanced Concoctions (Feat 6):** Gain a Chirurgeon feat up to half your character level.
- **Expert Concoctor (Feat 12):** Expert proficiency in Chirurgeon class DC.
