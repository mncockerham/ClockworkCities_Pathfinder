# Clockwork Pathfinder — Resolved Focus & Development Archive

- **Status:** **Resolved & Codified Rules Archive**
- **Location:** `ClockworkPathfinder/Rules/ToDo/resolvedFocusandDevelopment.md`
- **Purpose:** Tracks subsystems, mechanical architectures, class divisions, and worldbuilding reconciliations that have been finalized and codified into the core rules documents. (Active playtesting and open design items remain in [`FocusAndDevelopment.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Rules/ToDo/FocusAndDevelopment.md)).

---

## 1. Core Mechanical Systems (Standardized & Codified)

### A. 3-Step Wound System, Lethal/Nonlethal Buffers, and Bleed-Out Clock [RESOLVED]
- **Reference:** [`ClockworkPathfinder/Rules/Healing.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Rules/Healing.md), [`AISummary/20_Healing.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/AISummary/20_Healing.md)
- **Codified Mechanics:**
  - **HP Thresholds:** Step size calculated as $\lfloor \text{Max HP} / 4 \rfloor$. Divided into **Mortal Wounds** (Step 1, weeks), **Critical Wounds** (Step 2, days), and **Regular Damage** (Remaining, normal PF2e).
  - **Trauma Ceiling ($\text{Level} + \text{CON}$):** Regular Damage heals per standard PF2e (Treat Wounds, rest), but is capped at $\text{Level} + \text{CON}$ if any Critical or Mortal damage remains unhealed.
  - **Two Damage Trackers & Damage Priority:** Tracks **Total Damage** and **Nonlethal Damage** ($\text{Lethal} = \text{Total} - \text{Nonlethal}$). Lethal damage is **always applied against HP tiers first** (filling Regular Damage first), with nonlethal sitting on top.
  - **Rapid Nonlethal Recovery:** Outside of combat, nonlethal damage naturally heals at **1 point per minute** across all levels.
  - **Unconsciousness vs. Dying Boundary:** At 0 HP, characters are merely **Unconscious and stable** as long as negative lethal has not exceeded their total nonlethal damage.
  - **Deterministic Bleed-Out Clock in Negative HP:** Replaces PF2e flat recovery checks. Once net negative lethal damage $> 0$:
    - **Stage 1 (1 to $\text{Step}$ / Critical capacity):** Takes **1 damage per hour**.
    - **Stage 2 ($\text{Step} + 1$ to $2 \times \text{Step}$ / Acute arterial collapse):** Takes **1 damage per minute**.
    - **Permanent Biological Death:** Occurs when net negative lethal damage reaches $\ge 2 \times \text{Step}$ (Critical + Mortal capacity).
  - **Clinical Recovery Rates & Care Bonus:** Bed rest recovers $\lfloor \frac{1}{5} \text{Level} \rfloor + \text{CON}$ per day (Critical) or per week (Mortal). Skilled medical attention increases this to full $\text{CON}$ per day/week. 1 full day (Critical) or 1 full week (Mortal) of dedicated clinical hospitalization restores all regular Damage HP.
  - **Anatomical Wound Consequence Table (d8):** Standardized PF2e conditions (*Clumsy*, *Enfeebled*, *Stupefied*, *Drained*, Speed penalties) with targeted direct attribute modifier penalties (–2 Str, –3 Dex, etc.) for catastrophic Mortal trauma.

### B. Firearm Lethality, Aither Dread & Neither Weapon Architecture [RESOLVED]
- **Reference:** [`ClockworkPathfinder/Rules/RangedWeapons.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Rules/RangedWeapons.md), [`ClockworkPathfinder/Rules/NeitherTeck/Weapons.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Rules/NeitherTeck/Weapons.md)
- **Codified Mechanics:**
  - **Intentional Aither Firearm Lethality:** Gunpowder firearms in Aither (+1 die type damage, fatal ballistics) are the exclusive domain of Elves, high Nobility, and sovereign magnates; direct gunfights against disciplined Aither riflemen are intentionally near-suicidal, making soft-skill counterplay via **Understanding** essential.
  - **Neither-Tech Energy Weapons:** Project coherent **Electricity (Arc)** or kinetic **Force (Pulse)**. Operate at 100% in Neither, **1/2 damage or 1/2 duration in the Zone**, and are completely inoperable in pure Aither.
  - **Three Standard Cartridge Sizes (Tripled Capacity & Scaled Reloads):**
    - **Small (~200g, 3 shots / 6–9 twin/rotary, `Reload 1`):** `1d8 E` / `1d10 F` pistols and pocket emitters.
    - **Medium (~400g, 3–6 shots / 15 slide, `Reload 2`):** `1d10–1d12 E/F` rifles, lances, blunderbusses, and slide pistols.
    - **Large (~800g, 3 shots, `Reload 3`):** `2d8–2d10 E/F` heavy arquebuses, dragon projectors, and force breakers.
    - Civil cells hold **1/20th the energy** of weapon cells.
  - **Spire Zone Interception & Biochemical Catalyst Monopoly:** Great Spires piercing the Zone broadcast wireless radiant power across urban districts. Military cartridges rely on a secret Spire-manufactured biochemical catalyst (produced by teams of Artisans, Scholars, and factory workers) that detonates or corrodes if directly exposed to Neither or Aither.
  - **Radiant Grid vs. Portable Cartridge Weapons:**
    - *Radiant Grid Weapons:* Powered wirelessly by active broadcast dynamos; full range (`40–200 ft`) and unlimited ammo, cycling 1 round between shots. In Spires, legally mandated to require a detachable **Converter Module** (regulated identically to cartridges). High-energy converters are deliberately bulky and must synchronize with dynamic generator frequency patterns. Using any radiant receiver for a non-intended purpose—especially weaponizing radiant energy outside legal usage—is a major felony.
    - *Portable Cartridge Weapons (Full Range, High Burst, Grind Limited):* Self-contained capacitor weapons restored to **full standard firearm ranges (`30–150 ft`)** with boosted damage (`1d8` to `2d10` base) and full firing rate when wielded with a matching Discipline Tag (waiving the enhancement tier AP tax). Intentionally outperform bows/crossbows in active firefights to reward spending finite cartridges, balanced by **strict ammunition attrition over the 70% grind** and `Reload 1 / 2 / 3` action costs, while bows (`100 ft`, `Reload 0`) and crossbows (`120 ft`) retain unlimited field endurance.
    - *Poor-Quality Battlefield Cartridge Weapons (20% Reload Burnout):* Standard energy weapons do not misfire, but poor-quality/salvaged cartridge weapons found on the battlefield have a **20% chance (1–4 on 1d20) on every reload** that delicate components overheat or burn out. A **Clockwork Engineer** or character with appropriate technical/Crafting skills can attempt a **10-minute Field Repair roll**: on a **Success**, the weapon works again; on a **Failure**, fixing it requires downtime and a **full Clockwork Workshop**.

### C. Neither Exposure Affliction Track & Recovery [RESOLVED]
- **Reference:** [`ClockworkPathfinder/Rules/TheNeither.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Rules/TheNeither.md), [`AISummary/WorldSummary.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/AISummary/WorldSummary.md) (Section 4)
- **Codified Mechanics:**
  - **Air Shift (Physical Decay):** Imposes *Clumsy*, *Enfeebled*, and *Drained* doubling from Level 2 (2) to Level 5 (16), progressing at –1 step per interval (Level 1: 1 month; Level 2: 1 week; Level 3: 3 days; Level 4: 1 day; Level 5: 1 hour).
  - **Food Shift (Mental & Social Decay):** Imposes *Stupefied* and a status penalty to all Int & Cha checks/DCs doubling from Level 2 (–2) to Level 5 (–16), progressing at –1 step per interval (Level 1: 1 month; Level 2: 1 month; Level 3: 1 week; Level 4: 1 day; Level 5: 1 hour).
  - **Healing Modulation:** Total Shift Score scales natural rest healing: 0–1.5 (100%), 2–3.5 (50%), 4–5 (25%), 5.5–6 (0 healing + 1d8/day), 6.5+ (0 healing + 3d8/day).
  - **Downtime Recovery Rule:** 1-week continuous stabilization period, followed by –1 point healed per week of clean native air and diet for both tracks.
  - **Shift-Worker & Commuter Rule:** 28-day cumulative exposure window allowing miners and laborers to log shift hours without triggering lethal healing failure if supplied clean food.
  - **Deep Water Fish Exception:** Types 1 to 4 treat deep saltwater (150+ ft) and deep freshwater fish as neutral native food (0 shift).

### D. NeitherTeck Dual-Economy System [RESOLVED]
- **Reference:** [`ClockworkPathfinder/Rules/NeitherTeck/NeitherTeckRules.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Rules/NeitherTeck/NeitherTeckRules.md), [`Weapons.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Rules/NeitherTeck/Weapons.md), [`TacticalRigs.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Rules/NeitherTeck/TacticalRigs.md), [`AISummary/10_Magic.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/AISummary/10_Magic.md)
- **Codified Mechanics:**
  - **Passive Loadout Capacity ($\text{Key Attribute Mod} + \lfloor \tfrac{\text{Level}}{2} \rfloor + 4$):** Committed during daily prep for continuous protective/environmental gear across three archetype tracks:
    - *Track A (Heavy Martials — Soldier, Brute):* Higher of **STR or CON**.
    - *Track B (Light Martials & Operatives — Dandy, Pugilist, Survivor, Scout, Sky Captain, Officer, Clockwork Rifleman):* Higher of **DEX or CON**.
    - *Track C (Technical & Academic — Scholar, Artisan, Clockwork Engineer, Chirurgeon, Mad Bomber, Inspector, Merchant):* Highest of **INT, STR, or CON**.
    - *Armor Weight Modifiers:* Unarmored (–2 pts), Light (–1 pt), Medium (+0), Heavy (+2 pts). Zero in-combat AP math.
  - **Active Surge AP ($\text{INT mod} + \text{Class Base AP} + \text{Level Progression Bonus}$):** Refreshes per round; spent strictly on Actions and Reactions. Includes Partial Activation / Multi-Round Accumulation rule.
  - **Equipment Discipline Tags & Bespoke GM Tuning:** 9 standardized tags (`[Biochemical]`, `[Mechanical]`, `[Military]`, `[Airships]`, `[Professional]`, `[Technical]`, `[Clandestine]`, `[Subterranean]`, `[Outlands]`) granting a –1 to –2 AP discount (min 1 AP). Restores classic DM agency to drop custom-tagged prototypes to assist struggling players without triggering an optimization arms race.
  - **Hard Dependency & Auxiliary Fallbacks:** NeitherTeck energy weapons are completely dead without power/cartridges or in Aither, but can mount 0-AP physical **affixed bayonets** (1d6 P/S) or **reinforced grips** (1d4 B).

---

## 2. Class Divisions & Role Resolutions

### A. Clockwork Engineer vs. Artisan Division [RESOLVED]
- **References:** [`ClockworkPathfinder/Classes/ClockworkEngineer.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Classes/ClockworkEngineer.md), [`ClockworkPathfinder/Classes/Artisan.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Classes/Artisan.md)
- **Resolution:**
  - **Artisan (Logistical Backbone):** Specializes in **Passive Loadout Capacity**, institutional manufacturing, party-wide equipment conditioning (+1 to +3 non-magical bonuses), structural vulnerability exploitation, and mundane tradecraft. Flagged with a player advisory noting its downtime/support focus.
  - **Clockwork Engineer (Combat Overclocker):** Specializes in **Active Surge prototype overclocks**, unstable mechanical innovations (Armor or Weapon), Overdrive burst damage, and high-risk field discharges.

### B. Survivor: Urban Infiltration & Intrigue [RESOLVED]
- **Reference:** [`ClockworkPathfinder/Classes/Survivor.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Classes/Survivor.md)
- **Resolution:** Established the Survivor as the premier master of **Stealth, Thievery (lockpicking), and Deception** in Spires and urban centers. Added *Urban Infiltration Mastery* (+1 circumstance bonus to lockpicking, hiding, and impersonation in civil settlements) and synergy with `[Clandestine]` and `[Professional]` tags.

### C. Chirurgeon & Mad Bomber: Core Ability AP Autonomy & Spire Volatile Solution Law [RESOLVED]
- **References:** [`ClockworkPathfinder/Classes/Chirurgeon.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Classes/Chirurgeon.md), [`ClockworkPathfinder/Classes/MadBomber.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Classes/MadBomber.md), [`ClockworkPathfinder/Rules/WorldAndLaw.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Rules/WorldAndLaw.md)
- **Resolution:**
  - **0-AP Autonomy:** All personal class features, quick concoctions, field vials, medical sera, auto-injectors, demolition charges, and infused bombs cost **0 Active Surge AP** for the creator. AP costs apply only when handing items to untrained allies or when operating external energy/clockwork tech.
  - **Spire Law on Volatile Solutions (Civil Balance):** Ward Constables and authorities make **no distinction** between normal items and the improvised concoctions of Mad Bombers or Chirurgeons. In the Spires, a Chirurgeon may legally carry **pre-made healing items** (and safe medical precursors that **can only make healing items**). Carrying volatile offensive solutions (acids, poisons, or precursors that can synthesize them) is a severe violation treated **just as harshly as carrying a live grenade**.

### D. Miner Consolidation into Scout & Brute Consolidation into Soldier/Pugilist [RESOLVED]
- **References:** [`ClockworkPathfinder/Classes/Scout.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Classes/Scout.md), [`Soldier.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Classes/Soldier.md), [`Pugilist.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Classes/Pugilist.md), [`Brute.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Classes/Brute.md), [`AISummary/30_ClassEnvironments.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/AISummary/30_ClassEnvironments.md)
- **Resolution:**
  - **Miner $\rightarrow$ Scout:** The standalone Miner class was consolidated into the **Scout** as the subterranean sapper and deep delver path.
  - **Brute $\rightarrow$ Soldier & Pugilist (*Savage Combatant* Feats at Levels 2, 4, 8):** Applying Rule 1, the standalone Brute (Barbarian) class was removed and replaced by a 3-tier **Savage Combatant** feat tree (*Savage Combatant* Lv 2, *Relentless Savagery* Lv 4, *Savage Onslaught* Lv 8) available to both **Soldiers** and **Pugilists**. Modeled after Rage at a lower mechanical impact (`+1` to `+3` melee/unarmed damage, `+2` to `+4` two-handed melee, scaled Temp HP, –1 AC), it strictly prohibits ranged weapon attacks and imposes a **–2 status penalty to all social interaction and Understanding checks (except Intimidate, which gets +1/+2)** during the state and for 10 minutes afterward.

### E. Broad-Use Martial Generalists, Environmental Class Balance & NPC Fragility Philosophy [RESOLVED]
- **References:** [`AISummary/30_ClassEnvironments.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/AISummary/30_ClassEnvironments.md), [`ClockworkPathfinder/Rules/WorldAndLaw.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Rules/WorldAndLaw.md), [`ClockworkPathfinder/Rules/NPCs.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Rules/NPCs.md), [`AISummary/00_RulesFoundation.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/AISummary/00_RulesFoundation.md)
- **Resolution:**
  - **Generalists (Soldier, Sky Captain, Officer):** Confirmed healthy across all combat theaters; they do not need forced S-tier dominance in High Radiant grids.
  - **Environmental Class Balance Audit Resolved:**
    - *Inside the Spire Proper Only (Wards 1–15):* Strict disarmament, mundane `1d4` utility dagger cap, normal-looking padded/leather armor (hiding material upgrades under over-garments while banning clockwork attachments), volatile-solution bans, and direct-exit surveillance make **Pugilists, Dandies, Survivors, Inspectors, and the Influence Trio** the intended stars inside the Spire proper.
    - *Why Rifleman, Mad Bomber & Clockwork Engineer Are Not Underpowered:* The strict ban applies **only inside the enclosed Spire proper**. As soon as characters step outside the Spire proper—**even in the areas contained by the Outer Wall**—weapon and armor restrictions are usually not enforced (workers carry dual-purpose axes; those with money carry pistols). **Airships only have the rules the Captain chooses to and can enforce**, the **Warrens** have zero disarmament laws, and **beyond the actual perimeter of any location in the Neither, none of the rules are enforced**. Thus, Riflemen, Mad Bombers, and Engineers operate at full S/A-tier strength across 4 of the 5 campaign environments.
  - **NPC Fragility & The 15 / 70 / 15 Encounter Rule:** Civilian NPC classes (Laborer, Professional, Commoner, Craftsman) are intentionally fragile so PCs feel superior in the **15% "We Are Heroes"** showcase encounters, while **70% "The Grind"** and **15% "The Boss / Crucible"** encounters use coordinated patrols, monsters, and NPCs built with full PC class levels.

---

## 3. World, Governance, Social Class & Resource Architecture

### A. The Five Player Resource Categories & The Citizen Bulwark [RESOLVED]
- **References:** [`ClockworkPathfinder/Rules/ResourcesAndWealth.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Rules/ResourcesAndWealth.md), [`ClockworkPathfinder/Rules/WorldAndLaw.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Rules/WorldAndLaw.md)
- **Codified Architecture:**
  1. **Monthly Spending Allowance:** Discretionary spending for living *beyond* station, bribes, or personal gambling stakes. All normal lifestyle, housing, and dining at or below status tier are absorbed by the House/Guild ledger.
  2. **Personal Property Cap (`1 × Monthly Spending Limit`):** Players may keep personal items and coin only up to their Monthly Spending Limit. All wealth above this is returned to their organization, or—if unaligned—stolen or spent on fleeting vice.
  3. **Requisitioned Equipment (Organizational Library):** Personal property caps and Citizen Bulwark limits **never apply to items that your organization can afford and believes you need to perform your role or given tasks**, but **these items always belong to the organization, not the players**.
  4. **Retainer Budget:** Earmarked strictly for subordinates/hirelings (or hiring lower-status PCs); **cannot be used directly by the PC** and **must be reallocated every month**.
  5. **The Citizen Bulwark (3-Item PC Exemption):** Ancient militia statute subsidizing upkeep and parts for **1 Protective Armor, 1 Primary Weapon, and 1 Additional Clockwork/Defense Item** outside normal Spire resource limits. The allowed price and tier of each item scales by **Character Level (`Item Level = Character Level`)** per standard PF2e magic item progression (`[GM Core p.58]`).

### B. Crime in the Wards & Warrens ("No Off-the-Books Laundering") [RESOLVED]
- **References:** [`ClockworkPathfinder/Rules/NewAvalon.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Rules/NewAvalon.md), [`ClockworkPathfinder/Rules/WorldAndLaw.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Rules/WorldAndLaw.md), [`ClockworkPathfinder/Rules/ResourcesAndWealth.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Rules/ResourcesAndWealth.md)
- **Resolution:**
  - **Ward 13 Warrens ("Las Vegas" Escape Valve):** Hands-off vice district run by Johnny Ralen and Amanda Coren with a rigid class structure and clear boundaries; since only legal Citizens can leave the Warrens and live regular lives in the Spire, syndicate operators exist under standard citizenship/resource rules.
  - **Lower Warrens (1–12) Out-Migration & Culling:** Any worker or criminal who accumulates enough money to live as a common Ward laborer or buy a small legitimate inn immediately packs up and moves into the Wards, while the Military, King's Guard, and Constabulary covertly and overtly cull anyone accumulating too much power.
  - **Organized Crime in the Wards (Legitimate Fronts):** Crime families in the Wards operate through legitimate fronts (smaller guilds, taverns, bars, restaurants), live within the means of a more profitable version of that front, and are treated by society as that social class. Tolerated as long as they don't cause too much trouble, make people happy, and do not decrease the wealth of the Spire.

### C. Feudal Ownership Chain, Leases, Merchants & The Great Disruption [RESOLVED]
- **References:** [`ClockworkPathfinder/Rules/SocialClasses.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Rules/SocialClasses.md), [`ClockworkPathfinder/Rules/WorldAndLaw.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Rules/WorldAndLaw.md)
- **Resolution:**
  - **Feudal Chain:** The King owns everything $\rightarrow$ delegates to **Great Noble Houses** (the 25 most important hold sections of New Avalon) $\rightarrow$ managed by **Noble Houses**, who collect taxes/rent, manage decent-sized non-dedicated holdings, and fill government offices alongside Collegium-educated non-nobles.
  - **Spire Leases & Housing Mobility:** Leasing a location follows a strict formula (with a regulated surcharge on wealth generation); Nobles collect rent and find new tenants. Citizens move up/down across wards and circles as wealth varies; since most live in guild/family-supplied apartments, maintaining group status is paramount.
  - **Merchants & The Great Disruption:** Merchants sell at scale, run profitable shops (not producer-sellers/restaurants/inns), and command skyship/sea/caravan networks and warehouses. When centuries of clockwork stability grew merchant co-ops until their wealth rivaled or surpassed the Great Houses, it was resolved in two ways: 1) wealthy merchants were allowed to **marry into Noble and Great Noble Houses**, and 2) the King began **leasing grants to properties outside the Spires** directly to top merchants.

### D. Victorian Sexism vs. Cultural Exceptionalism (Cancellation Rule) [RESOLVED]
- **References:** [`ClockworkPathfinder/Rules/SocialClasses.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Rules/SocialClasses.md), [`ClockworkPathfinder/Rules/WorldAndLaw.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Rules/WorldAndLaw.md)
- **Resolution:** Prejudice against women in male-dominated roles (e.g., the 5% female Constabulary) and admiration for succeeding in a difficult field **always cancel out** (0 net mechanical penalty). The reverse applies equally: men in traditionally female crafts are looked down on to the extent that their male advantage cancels out, treating them identically to anyone else in that role.

### E. Storyteller Final Authority & The 3-Tier Decision Structure [RESOLVED]
- **References:** [`AISummary/00_RulesFoundation.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/AISummary/00_RulesFoundation.md), [`ClockworkPathfinder/Rules/ResourcesAndWealth.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Rules/ResourcesAndWealth.md)
- **Resolution:**
  - Players are **members** of a House or Guild (until high level, they do not run them). Institutional questions are resolved via roleplay between player and Storyteller, with the **Storyteller holding the final word**.
  - **3-Tier Decision Hierarchy:** 1) *Is it fun/beneficial to the game?* (Highest priority), 2) *Does it fit the theme and mood of the world?*, 3) *Is it realistic and aligned with other rules?* (Lowest priority; ignored when 1 and 2 are met).

### F. Setting Nomenclature Reconciliations [RESOLVED]
- **Resolution:**
  - All early draft references to "Abelanth" unified under **New Avalon**.
  - All references to "perdium" or "Natherium" unified under **Neithercrete**.

