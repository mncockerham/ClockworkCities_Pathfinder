# Edges & Character Creation Customization (Working Ideas & Draft Concepts)

- **Status:** **Working Brainstorm & Concept Draft** (Collection of ideas; not yet codified as a locked rule)
- **Location:** `ClockworkPathfinder/Rules/edges.md`
- **Core Problem Being Addressed:** 
  - Why isn't every character born a high-status Noble or wealthy Wall Merchant? 
  - High social rank naturally grants massive monthly spending allowances, legal privileges (open-carrying dueling rapiers), carriage passes, and social deference.
  - Simply adding complex social restrictions or roleplay penalties does not deter power gamers or rules lawyers; in fact, detailed rules often provide more opportunities to game the system or justify anti-party behavior (*"It's what my character would do"*).
  - Solution: An **Opportunity Cost Engine** using **Edge Points** at character creation. If being a Noble costs hard character-creation points, players have fewer points left for armor proficiencies, extra AP, or racial combat edges.

---

## 1. The Core 12-Point Edge Budget Concept

Every character receives a budget of **10 Edge Points** during character creation.

### The Baseline Status Rule & Social Class Entry Costs (12 Edge Points Budget)

Every character starts with **12 Edge Points** to build their personal and institutional background. Social class for an unaffiliated character defaults to **Status $\le 0$ (Non-Citizen / Warrens Outcast)**; Edge Points are spent to purchase your starting Social Class rank.

> [!IMPORTANT]
> **Lineage, Marriage, Adoption & Explaining Your Social Class:**
> - **Parental Conferred Status:** For most characters, parents grant you a starting Social Class **equal to their own**. However, **if the parent holds a leadership role** in a group, house, or organization (e.g. Guildmaster, House Patriarch, Fortress Commandant, Merchant Baron), **the PC starts just below them** (reflecting junior family standing rather than apex organizational control).
> - **Marriage & Adoption (The Open Door):** Through **marriage or formal adoption**, a player character can have **any social status they buy with their Edge Points**. If your character was adopted into a Great House or married into a Wall Merchant dynasty, that purchase is fully legitimate and recognized across the Spire.
> - **Unaffiliated & Non-Household Characters (The Simple Explanation):** For characters who were **not born, adopted, or married into a recognized house, merchant firm, or guild livery**, you need only **provide a simple, believable in-world explanation for how you hold that social class** (e.g. an exceptional battlefield commission, discovering a lucrative pre-collapse relic that bought a trade charter, or a retired magistrate's mentorship). A single believable sentence or brief anecdote is all that is required.

#### Starting Social Class Edge Cost Table (Budget: 12 Edge Points):
The cost to purchase a starting Social Class equals:
$$\text{Cost} = \left\lceil \frac{\text{Lowest Status in Bracket}}{10} \right\rceil$$
*(Freemen/Women are fixed at 5 points due to high income and zero guild/family debts. Standard Nobles, Wall Merchants, and Great House Nobles include a +1 surcharge for legal sword rights and armed retainers).*

| Social Class & Category | Status Range | Lowest Status | Base Cost | Surcharge / Reason | **Final Edge Cost** | Points Left (out of 12) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Non-Citizen / Warrens Outcast** | $\le 0$ | 0 | 0 | — | **0 Points** | **12 Remaining** |
| **Physical Labor (Unskilled / Zero Trust)** | 6–10 | 6 | 1 | — | **1 Point** | **11 Remaining** |
| **Trusted Laborers** | 11–15 | 11 | 2 | — | **2 Points** | **10 Remaining** |
| **Freemen / Freewomen (Unaffiliated)** | 16–20 | 16 | 2 | **High income, zero guild/family obligations** | **5 Points** | **7 Remaining** |
| **Apprentices & Enlisted Recruits** | 21–25 | 21 | 3 | — | **3 Points** | **9 Remaining** |
| **Guild Craftsmen & Artisans** | 26–55 | 26 | 3 | — | **3 Points** | **9 Remaining** |
| **Military & Constabulary Regulars** | 26–65 | 26 | 3 | — | **3 Points** | **9 Remaining** |
| **Standard Merchants** | 30–70 | 30 | 3 | — | **3 Points** | **9 Remaining** |
| **Academia & University Collegium** | 45–70 | 45 | 5 | — | **5 Points** | **7 Remaining** |
| **Lesser Nobility (Working Gentry)** | 55–60 | 55 | 6 | **Working gentry; no sword rights** | **6 Points** | **6 Remaining** |
| **Standard Nobility (Landed Peers)** | 65–75 | 65 | 7 | **+1 Sword Rights (Dueling Blade)** | **8 Points** | **4 Remaining** |
| **Wall Merchants** | 80–90 | 80 | 8 | **+1 Sword Rights & Retainers** | **9 Points** | **3 Remaining** |
| **Great House Nobles** | 85–95 | 85 | 9 | **+1 Sword Rights & Retainers** | **10 Points** | **2 Remaining** |


## 2. Potential Edge Options (Menu of Working Ideas)

> [!CAUTION]
> **The Single-Purchase Rule (No Stacking Edge Exploits):**
> **Each specific upgrade or option from this menu can only be purchased ONCE per character.** 
> Players cannot stack multiple purchases of the same edge to build absurd degenerate exploits (e.g., spending 10 points to start a Level 1 character with 5 bonus general feats, stacking unarmored all the way to heavy armor, or purchasing multiple AP surges). Once an edge option is selected, it is locked.

*Remaining Edge Points can be spent on bonus feats, stat adjustments, armor upgrades, and heritage/racial capabilities.*

### A. Combat & Tactical Edges
- **Armor / Weapon Step-Up (3 Points — 1-Time Purchase Only, Max Expert):**
  - You are trained in the next tier of armor or weapon above your class baseline (e.g. Unarmored $\rightarrow$ Light Armor, Light $\rightarrow$ Medium Armor, Medium $\rightarrow$ Heavy Armor, or Simple Weapons $\rightarrow$ Martial Weapons).
  - **Caps at Expert:** This 3-point purchase scales with your character's career up to a **maximum of Expert proficiency** (one tier below Master). **Strict Limit:** 1-time purchase only during character creation.
- **Master Mastery Upgrade (5 Points — Max Master, Requires Native Expert):**
  - For martial specialists who want to push their combat discipline to the supreme apex: if your class chassis natively progresses to **Expert** in a weapon category or armor type, this 5-point purchase allows that proficiency to advance to **Master** at the appropriate high level (matching dedicated Soldiers).
  - **Caps at Master:** Unlocks the maximum Master tier for classes that already have the prerequisite Expert chassis.
- **AP Battery Surge (4 Points):**
  - Gain **+1 Base AP** at Level 1, plus an additional **+1 AP** at Levels 5 and 15. Massively enhances NeitherTeck and radiant firing rates, allowing non-technical classes to operate devices without starving their action economy.
- **Hardened Combat Frame (2 Points):**
  - Gain +1 flat Hit Point per character level, or gain a bonus physical general feat (such as *Diehard* or *Toughness*).

---

### B. Physiological & Heritage Edges (Racial / Biological Trait Boosts)
*Allows characters to lean into the unique physiology of the 6 human adaptations using outcome upgrades, resistances, and rerolls rather than flat static numbers. (Note: Vision upgrades like low-light/darkvision are intentionally excluded to prevent "must-have" feat taxes for stealth/scout archetypes).*

#### 1. Universal & Center-Strata Traits (Humans & Orcs)
- **Iron-Gut & Natural Poison Immunity (2 Points):**
  - **Outcome Step-Up:** When rolling a saving throw against natural poisons, venoms, or toxic fungal spores, treat any **Success as a Critical Success**.
- **Neither-Conditioned Lungs & Exposure Resilience (2 Points):**
  - **3 Rerolls Between Rests:** Gain **3 Fortune Rerolls between full rests** that can be spent on saving throws against Neither sickness, atmospheric shock, or suffocating dust. (You keep the higher of the two rolls).
- **Physical Attribute Boost (4 Points, Max 1):**
  - Gain a +1 boost to Strength, Dexterity, or Constitution at character creation (adhering to normal starting attribute caps).
- **Workhorse Bulk & Industrial Stamina (1 Point):**
  - Treat Strength as +2 higher for carrying Bulk; ignore encumbrance penalties caused by heavy industrial tools and work implements, and treat successes on forced march or heavy labor Fortitude saves as **Critical Successes**.

#### 2. Half-Elf Traits (Layer 2 / Zone-Striders & Aeronauts)
- **Zone Static Attunement & Dielectric Grounding (2 Points):**
  - **Scales Lifelong:** Gain **Electricity Resistance equal to $\max(2, \text{CON mod})$**.
  - **Outcome Step-Up:** Whenever you succeed on a Reflex save against an electrical effect or lightning discharge, it becomes a **Critical Success**.
  - **Static Burst:** Taking electrical damage or surviving an electrical discharge grants you a +10 ft status bonus to Speed for 1 round.
- **Rigging Reflexes & Catwalk Agility (2 Points):**
  - **Outcome Step-Up:** When rolling an Acrobatics check to Balance on narrow airship spars, cables, high-spire catwalks, or ledges, treat a **Success as a Critical Success**.
  - **Fall Mitigation:** You instinctively catch wind drafts and rigging ropes; you treat all falls as if they were **20 feet shorter** (scaling to 40 ft at Lv 10).
- **Barometric Weather Sense (1 Point):**
  - You sense micro-barometric air pressure shifts in your eardrums and sinuses; you predict oncoming storms, Zone squalls, or heavy Neither surges **1 hour in advance** without needing survival checks.

#### 3. Dwarf Traits (Layer 5 / Lightless Subterranean Sappers)
- **Dense Stature & Stone Anchor (2 Points):**
  - **Outcome Step-Up:** Treat successes on Fortitude saves or Reflex DCs against **Shove, Trip, or Reposition** as **Critical Successes**.
  - **Unyielding Frame:** Gain a +4 circumstance bonus to your Fortitude DC against forced movement while your boots touch stone, rock, or Neithercrete.
- **Subterranean Sapper / Mineral Cleaver (2 Points):**
  - **Hardness Bypass:** When striking stone, masonry, Neithercrete, or mineral constructs, you **ignore 5 points of object Hardness** (scaling to ignore 10 Hardness at Lv 10).
  - **Masonry Sense:** Gain a +2 circumstance bonus to Perception to detect structural collapse hazards, unstable ceilings, and hollow secret doors.
- **Feline Pupillary Dilation (1 Point):**
  - *(Ocular Adjustment — NOT vision granting):* Your reflective pupils dilate instantly; you recover from **Dazzled or Blinded** conditions caused by bright light flashes or flashbangs in **half the normal duration** (minimum 1 round).
- **Tremor Resonance (3 Points):**
  - Gain imprecise **Tremorsense 15 feet** while touching unworked bedrock or Neithercrete masonry, allowing you to pinpoint unseen or burrowing creatures through vibrations in the stone without needing line of sight.

---

### C. Skill, Technical & Practical Edges
- **Extra Trained Skill (1 Point):**
  - Gain training in one additional skill of your choice.
- **Bonus 1st-Level General or Skill Feat (2 Points):**
  - Select one additional 1st-level feat from the general or skill feat lists.
- **Jury-Rigger / Scrap Savant (2 Points):**
  - Can field-repair broken or burned-out NeitherTeck devices in 10 minutes instead of hours, using half the normal salvage scrap.
- **Street Anonymity (1 Point):**
  - Gain a +2 circumstance bonus to Stealth and Deception checks when blending into crowds in Wards 1–12 or the Warrens.

---

## 3. Core Design Mandate: Edges Must Scale and Remain Valuable at All Levels

> [!IMPORTANT]
> **Avoid Front-Loaded, Flat Numbers with Diminishing Returns:**
> In d20 systems, flat bonuses (like a flat "+1 to Fortitude saves" or "+2 to a skill") are powerful at Level 1 but become mathematically irrelevant and forgotten by Level 10–15. Conversely, unlocking **capabilities, proficiencies, action economy, and scaling dice** maintains tremendous value across a character's entire career (Levels 1 to 20).

### D. Social Standing & Patronage Edges
- **Social Patron (2 Points — Merchant / Lesser-to-Middle Noble Backing):**
  - You possess a powerful institutional or high-society patron (a Wall Street merchant firm, commercial venture house, or Lesser/Middle Noble family).
  - **No Physical Combat Risk:** Your patron **will not physically risk themselves or fight for you**.
  - **Political, Legal & Transit Intercession:** Your patron provides political and legal backing, interceding through their solicitors if you run afoul of the Spire Constabulary, and grants you access to travel through carriage avenues, transit gates, and Spire circles **as if you possessed their social status**.
  - **Reaction Manifold Maintenance & Ordnance Sponsorship:** If you are a lower social class (Status 0–2), having this Patron satisfies the institutional maintenance requirement to own, maintain, reconfigure, and reload a **Reaction Manifold** (Bombardier device), with the patron covering the cost of replacement chemical salts and grenade casings as standard operational gear support.
- **Great Patron (3 Points — Wall Merchant / Great Noble House Backing):**
  - You are backed by the highest tier of Spire power: a dynastic Wall Merchant cartel or one of the 25 Great Noble Houses.
  - Grants all benefits of a 2-point Patron, but with **Great House / Wall Merchant authority**: supreme legal deference against local ward constables, carriage access to elite high-spire avenues (Wards 14–15), and access to Great House cleanroom workshops and royal patent formula archives.

---

### What Scales Well Across 1–20 vs. What Stagnates:
- **Scaling Edges (High Lifelong Value):**
  - **Armor Step-Up:** Gaining access to Medium or Heavy Armor scales permanently because your Armor Class and item bonuses scale with every level and potency rune, keeping you alive at Level 15 just as much as at Level 1.
  - **Weapon Category Access:** Unlocks weapon types (e.g., Heavy Cartridge Rifles, Halberds) that utilize weapon specialization and extra damage dice at higher levels.
  - **AP Scaling (+1 AP at 1, 5, 15):** Directly scales with NeitherTeck power tiers, allowing high-level characters to fire multiple radiant bursts or power complex exoskeletons that lower-AP characters cannot sustain.
  - **Per-Level HP Scaling (+1 HP per character level):** Scales with level progression ($+1 \times \text{Level}$) rather than being a one-time flat 3 HP bump.
  - **Outcome Upgrades Over Flat Modifiers:** Rather than "+1 Fortitude", an edge that grants *"Success on saves against Neither sickness becomes a Critical Success"* (or allows rerolling a failed save once per day) remains life-saving at Level 15.

---

## 4. Status Mobility, Loss & The "Recognized Heir" Rule

### A. Loss of Status & Reclaiming Your Proper Rank
- **Status Points Are Not Automatically Restored When Lost:** If a character suffers financial ruin, legal censure, or social demotion, their active status drops and is **not automatically restored**; they must actively resolve the underlying cause (debts, legal trials, family exile). Furthermore, they receive **zero Edge Point refunds** on demotion.
- **Reclaiming Lost Status vs. Unearned Upward Mobility:** While falling in status strips active privileges (carriage access, spending allowances, dueling rights), **reclaiming a lost status rank that you previously paid for or held is far easier than trying to climb into a new status without having paid the cost**. Society already recognizes your lineage, upbringing, manners, and former standing; once debts are settled or names cleared, the threshold to reclaim that proper status is significantly lower.
- **Purchasing a Higher Status Than Currently Used:** A player character **can deliberately purchase a higher Social Class at character creation than the station they currently inhabit** (e.g. paying 9 points for Wall Merchant Status 80 or 8 points for Standard Noble Status 65, while starting play as a disowned gutter-dweller or barracks private).
- **Player Controls How & When Proper Status is Reclaimed:** When a player buys a higher status upfront, **the player retains total narrative control over how and when their character reclaims their proper status**. The Storyteller does not gatekeep or block this return; whenever the player decides their personal arc has arrived at the right turning point (producing a hidden signet ring, settling the feud, receiving news of an inheritance, or performing a redeeming deed), their full purchased status is restored.

### B. The 2-Tier Social Mobility Cap (Except by King’s Proclamation)
- **Rigid Societal Stratification:** Spire society is deeply conservative and stratified. **Natural in-game social mobility is strictly capped at a maximum increase of 2 Status Tiers above your starting baseline**:
  - A Status 1 Laborer can realistically climb to Status 2 (Craftsman) or Status 3 (independent shopkeeper / senior clerk).
  - An ambitious Status 2 Artisan can rise to Status 4 (senior guild officer or master craftsperson).
  - Without an explicit royal decree, society will not accept or acknowledge a Warrens rat (Status 0) or day-laborer (Status 1) suddenly presenting themselves as a landed Noble (Status 5) or Wall Merchant (Status 6), regardless of how much coin they carry.
- **The Royal Exception (The King's Proclamation):** The King's word is law. A decree or act of the King—or made in his name—may bypass the 2-Tier cap and establish any appointment, office, property grant, privilege, or class status, including Noble or Royal status, regardless of ordinary succession rules. No institution or legal process can invalidate it; only rebellion can stop the King. Society still shapes the consequences: granting Arthor More a noble title and Noble District property is an ordinary, accepted act; his title, property, rights, obligations, and inheritance match those of any noble at the status granted. Ennobling ten people every month would be legally effective but politically destabilizing and likely to provoke serious resistance. These examples are illustrative, not fixed thresholds. Social expectations constrain the King's choices, not his authority. Without such a royal act, Noble and Royal classes follow their ordinary hereditary rules, base Merchant status can be attained through sufficient resources and standing, and rare elevation to Wall Merchant status follows Merchant House succession.

### C. The "I Should Be an X" Archetype (The Disowned, Disgraced, or Unrecognized Heir)
- **The Concept:** A player may want to play a character who is currently living in the gutter or working a mundane trade, but whose backstory is: *"My father is a Wall Merchant (or Great House Lord); if he ever recognizes me, my birthright will be restored!"* or *"I was a disgraced officer/scion exiled from my noble house, and I am biding my time to clear my name and reclaim my seat."*
- **The Edge Point Rule (Upfront Investment):** Because their potential social ceiling, family connections, genetic pedigree, and future inheritance represent immense institutional leverage, **the player MUST spend the full Edge Point cost of the targeted high status (e.g. 9 points for Wall Merchant (Status 80–90)) during character creation**:
  - *In Play:* They start with the physical status and daily realities of their current low situation, but they hold the dormant bloodline/claims.
  - *Advantage:* When the family recognizes them, the inheritance is unlocked, or the disgrace is forgiven, **they bypass the 2-Tier mobility cap instantly** and assume their full status without needing royal intervention, because they paid the character-creation opportunity cost upfront.
- **Player Agency Over Timing (Player in Charge of Progression):**
  - Unlike standard class progressions or DM-gated status bumps, **the player is strictly in charge of when this restoration occurs**.
  - While the Storyteller can naturally offer narrative hooks, opportunities, and family encounters during the campaign, **at any time the player can supply the narrative justification** (e.g., *"My character receives a letter that the rival cousin died,"* *"I produce the family signet ring and force a private audience,"* or *"I perform a deed that wipes away the family's public disgrace"*).
  - Because **the player already paid the full Edge Point cost for this status at character creation**, the Storyteller does not gatekeep or block this transition—the player simply decides when their character's personal redemption arc reaches its turning point.

### D. Storyteller Advice: Breaking the 2-Tier Limit & Party Equity
> [!TIP]
> **Storyteller Note on High-Tier Narrative Promotions:**
> If you run a storyline where a character earns a direct royal charter, high office, or massive corporate succession that **elevates them beyond the natural 2-Tier mobility limit**, careful thought must be given to **fairly treating the rest of the party**. The King may also directly grant Noble or Royal class; a royal charter can make such a grant legally true, though its political and social consequences may be immense:
> - When one character gains massive social standing, high-altitude estates, and royal favors that break standard limits, the remaining party members should **likewise receive an equivalent game-breaking reward or distinct systemic advantage**.
> - **Examples of Party Equity Rewards:**
>   - An **Extra Citizen Bulwark Slot** (expanding their permanent retained item slots from 3 to 4, granted directly in the King's Name).
>   - An **Autonomous Commission or Crown Dispensation** giving immunity from constabulary search and seizure.
>   - A **Permanent Masterwork Workshop / Lab Grant** at the Lower University or foundry wards with subsidized supplies.
>   - Direct **King's Rites** allowing personal carriage of restricted NeitherTeck or cartridge firearms without checkout logs.

---

## 5. Class Overlap & Proficiency Scaling (3-Pt vs 5-Pt Tiers)

- **The Two Proficiency Upgrade Tiers:**
  - **The 3-Point Upgrade (Max Expert):** Steps up your armor or weapon category by one tier (e.g. Unarmored $\rightarrow$ Light, Light $\rightarrow$ Medium, Medium $\rightarrow$ Heavy, or Simple $\rightarrow$ Martial). This tier **caps strictly at Expert proficiency** over the course of your career. It gives non-martial or lighter classes great mid-to-late game survivability without encroaching on martial supremacy.
  - **The 5-Point Upgrade (Max Master — Requires Native Expert Chassis):** Dedicated combatants whose class natively progresses to **Expert** can spend 5 points to allow that category to scale all the way to **Master** at higher levels.
- **Why This Prevents Toxic Overlap:**
  - Non-martials (like Scholars or Chirurgeons) can only ever buy the 3-point tier and cap at Expert—they can never buy Master because their class chassis lacks native Expert progression.
  - Reaching Master requires committing half of your starting Edge budget (5 points) on top of an already martially inclined class build.

---

## 6. Open Design Questions to Consider

1. **Calibration of Point Costs:**
   - Does a 1-Point-per-Status-Tier model with a +1 Retainer surcharge feel balanced against 3-point armor step-ups, 4-point AP surges, and 5-point Master upgrades during actual character generation?
2. **AP Surge Stacking:**
   - Ensure the +1 AP Battery Surge (at Lv 1, 5, 15) integrates cleanly with Tier 0 and Tier 1 class AP ceilings.
