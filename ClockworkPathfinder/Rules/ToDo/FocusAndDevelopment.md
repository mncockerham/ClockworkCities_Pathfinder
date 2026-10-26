# Clockwork Pathfinder — Development & Playtest Roadmap

- **Status:** **Active Backlog & Focus Tracker**
- **Location:** `ClockworkPathfinder/Rules/ToDo/FocusAndDevelopment.md`
- **Purpose:** Identifies rules subsystems, playtest stress-tests, content expansions, and mechanical areas requiring mathematical calibration or deeper narrative polish.

---

## 1. High-Priority Mechanical Systems Needing Calibration & Testing

### A. 3-Step Wound System, Lethal/Nonlethal Buffers, and Bleed-Out Clock
- **Reference:** `ClockworkPathfinder/Rules/Healing.md`, `AISummary/20_Healing.md`
- **Status:** **Rules Standardized & Codified**
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
- **Focus Areas for Playtesting:**
  - **Multi-Encounter Trauma Pacing:** Playtest how parties adapt when carrying the $\text{Level} + \text{CON}$ trauma ceiling during an active expedition in the Warrens or Neither depths.
  - **Chirurgeon Medical Kit Economy:** Balance surgical kit consumable costs and field stabilization DC checks against the 1/hour and 1/minute bleed-out clocks.
  - **Direct Stat Damage Ergonomics:** Ensure table bookkeeping of temporary direct attribute penalties (e.g., –2 Str) is smooth and easily tracked alongside standard conditions.

### B. Firearm Lethality & Aither Dread (Intentional Design)
- **Reference:** `ClockworkPathfinder/Rules/RangedWeapons.md`
- **Design Intent Confirmed:** The extreme lethality of gunpowder firearms in Aither (+1 die type damage, fatal ballistics) is **entirely intentional**. In the setting, weapons in Aither are the exclusive domain of **Elves, high Nobility, and sovereign Merchant magnates**—in all cases, **players should be terrified of them**. Direct gunfights against disciplined riflemen in Aither are meant to be near-suicidal.
- **Soft-Skill Counterplay via Understanding:**
  - The high lethality of Aither firearms makes the new **Understanding** system (`ClockworkPathfinder/Rules/Skills.md`) essential. Rather than engaging in open shootouts, players use institutional insight, guard shift tracking, bribery, and social leverage to bypass armed checkpoints, divert patrols, or negotiate before triggers are pulled.
- **Rules Codified:**
  - **Neither-Tech Energy Weapons:** Not ballistic projectile weapons. Project coherent **Electricity (Arc)** or kinetic **Force (Pulse)**.
  - **Environmental Operating Limits:** 100% operational in Neither; **1/2 damage or 1/2 duration in the Zone**; completely inoperable in pure Aither.
  - **Three Standard Cartridge Sizes (Tripled Capacity):** **Small (~200g, 3 shots / 9 rotary)** for pistols/sidearms; **Medium (~400g, 3–6 shots / 15 slide)** for rifles/carbines; **Large (~800g, 3 shots)** for heavy breakers/cannons.
    - **Civil Cartridges & Radiant Power:** Civil cells hold **1/20th the energy** of weapon cells; power lamps, winches, and tools. Within Spires, Dwarven cities, and Deep One layers, energy is shared wirelessly via **radiant power** through the Neither medium, generated by massive, well-guarded dynamos.
    - **Spire Zone Interception Monopoly:** The Great Spires that physically cross the Zone are the **only places on the planet** where enough electrical energy is harvested to broadcast radiant power across vast, multi-mile urban districts. Dwarven and Deep One stations rely on local geothermal/chemical taps, covering much tighter perimeters.
    - **Secret Biochemical Weapon Catalyst (Spire Factory Monopoly):** Weapon cartridges rely on a secret biochemical compound produced industrially by teams of **Artisans, Scholars, and factory workers** in controlled sterile environments. (By contrast, **Chirurgeons and Mad Bombers** specialize in chaotic, intuitive field improvisation with scavenged ingredients). If directly exposed to Either Neither or Aither, the chemicals are hyper-unstable (detonating or corroding).
    - **Weapon Recharging Constraint:** Draining 20 civil cells into 1 weapon cartridge requires ~4–8 kg of batteries and requires an intact biochemical substrate. Traveling warbands lack dynamos and cannot recharge in the wild, cementing the primacy of cheap, light bows, crossbows, and axes for nomadic fighters.
  - **Two Distinct Classes of Neither Weapons (Standardized):**
    - **Radiant Grid Weapons (Spire Defense & Zone Airships Only):** Feature inductive receivers powered wirelessly by active broadcast dynamos. **Full range (60–150 ft)** and **unlimited ammunition supply**. However, induction takes time: weapons **must cycle for 1 full round to recharge internal capacitors** between shots. No mobile surface dynamos exist—only stationary Great Spires and massive military Airships cruising inside the Zone can generate radiant fields. Grants Spires formidable defensive siege superiority, but **cannot be used for surface conquest** (instantly dead outside the grid).
    - **Portable Cartridge Weapons (Expeditionary / Close-Quarters):** Self-contained capacitor weapons with 3 to 15 shot magazines. Suffer **half range (15–35 ft)** due to fog dispersion without grid collimation. Dominates close-quarters urban combat and room breaching.
    - **Bows & Crossbows (Open-Terrain Dominance):** Longbows (100 ft) and heavy crossbows (120 ft) have **triple to quadruple the range** of cartridge guns. In open Neither wastes, fungal forests, and wilderness ambushes, archers dominate before gunners can close the gap.
    - **Strict Cartridge Logistics:** Cartridges are heavy, costly, and rely on Spire biochemical catalysts. **Zero wilderness resupply** exists; once empty in the wild, guns become dead weight, making bows and melee mandatory for outland expeditions.
- **Focus Areas for Playtesting:**
  - **Ammunition Stress-Testing in Wilderness Delves:** Run multi-day wasteland expeditions where players must track individual cartridge expenditures and decide when to conserve cells in favor of archery and melee.
  - **Engagement Range Scenarios:** Test combat encounters starting at 80–120 ft to observe how Spire arc-gunners handle incoming arrow fire from Orc and Dwarf snipers before closing the distance.
  - **Cartridge Volatility on Critical Fails:** Playtest mechanical failure/jam rules on Natural 1s in high-exposure Zones.

### C. Neither Exposure Affliction Track & Recovery (Finalized in `TheNeither.md`)
- **Reference:** `ClockworkPathfinder/Rules/TheNeither.md`, `AISummary/WorldSummary.md` (Section 4)
- **Status:** **Rules Standardized & Codified**
  - **Air Shift (Physical Decay):** Imposes *Clumsy*, *Enfeebled*, and *Drained* doubling from Level 2 (2) to Level 5 (16), progressing at –1 step per interval (Level 1: 1 month; Level 2: 1 week; Level 3: 3 days; Level 4: 1 day; Level 5: 1 hour).
  - **Food Shift (Mental & Social Decay):** Imposes *Stupefied* and a status penalty to all Int & Cha checks/DCs doubling from Level 2 (–2) to Level 5 (–16), progressing at –1 step per interval (Level 1: 1 month; Level 2: 1 month; Level 3: 1 week; Level 4: 1 day; Level 5: 1 hour).
  - **Healing Modulation:** Total Shift Score scales natural rest healing: 0–1.5 (100%), 2–3.5 (50%), 4–5 (25%), 5.5–6 (0 healing + 1d8/day), 6.5+ (0 healing + 3d8/day).
  - **Downtime Recovery Rule:** 1-week continuous stabilization period, followed by –1 point healed per week of clean native air and diet for both tracks.
  - **Shift-Worker & Commuter Rule:** 28-day cumulative exposure window allowing miners and laborers to log shift hours without triggering lethal healing failure if supplied clean food.
  - **Deep Water Fish Exception:** Types 1 to 4 treat deep saltwater (150+ ft) and deep freshwater fish as neutral native food (0 shift).
- **Focus Areas for Playtesting:**
  - Test the 28-day rolling window in exploration campaigns where parties alternate between surface Warrens and high Spire circles.
  - Calibrate the monetary cost and availability of Chirurgeon clinical purges (*Mela Cleanse*) and high-ward *Hyperbaric Aither Sanatoriums* during extended downtime.

---

## 2. New Class Polish & Subsystem Testing

### A. The Merchant Class (Non-Magical Bard Replacement)
- **Reference:** `ClockworkPathfinder/Classes/Merchant.md`
- **Focus Areas:**
  - **Action Economy:** Test *Commercial Directives* in active combat. Ensure shouting economic incentives and tactical contracts feels as fluid and impactful as Bardic compositions without overshadowing the Officer's secular commands.
  - **Downtime & Social Influence:** Build a robust subsystem for the Merchant's financial investments, trade house credit lines, and merchant fleet contracts.

### B. The Clockwork Engineer vs. Artisan Division
- **References:** `ClockworkPathfinder/Classes/ClockworkEngineer.md`, `ClockworkPathfinder/Classes/Artisan.md`
- **Focus Areas:**
  - **Role Clarity:** Verify that the thematic boundary remains crisp—Clockwork Engineers invent high-concept experimental Neither-tech, arc emitters, and airship apparatuses; Artisans condition materials, reinforce physical armor/weapons, exploit structural flaws, and command mundane tradecraft (forges, tanning vats, masonry).
  - **Field Crafting Economy:** Test the Artisan's *Reinforced Workmanship* (+1 to +3 gear conditioning) to ensure stacking bonuses don't break PF2e's tight numerical math (+1 fundamental rune equivalencies).

### C. The Scholar's Analytical Stratagems
- **Reference:** `ClockworkPathfinder/Classes/Scholar.md`
- **Focus Areas:**
  - Test the three specialties (Architect, Accountant, Natural Philosopher) in complex tactical encounters. Ensure that substituting Intelligence for attack rolls and diagnosing enemy structural flaws remains balanced against the Inspector's pure forensic focus.

---

## 3. World & Narrative Subsystems to Formalize

### A. The Favor Hierarchy as a Downtime Subsystem
- **Reference:** `ClockworkPathfinder/Rules/WorldAndLaw.md` (Section 5)
- **Focus Areas:**
  - Create structured PF2e downtime activities: **Procure a Favor**, **Call in a Debt**, and **Face Exposure / Retaliation**.
  - Provide GMs with clear tables defining the DC and social consequences when a player pushes an NPC to commit an *Obligation* or *Life Debt*.

### B. Status, Standing & Faction Reputation (–99 to +99)
- **Reference:** `ClockworkPathfinder/Rules/SocialClassAndCorruptionRules.md` (Section 1)
- **Focus Areas:**
  - Define numerical milestones for faction standing (e.g., +25 = Requisition Officer Gear, +50 = High Council Audience, +75 = Master Patent Holder; –25 = Monitored by Constables, –50 = Stripped of Guild Rank, –75 = Marked for Arrest).
  - Clarify rules for "Off-the-Books" cash laundering when players accumulate coin beyond their Status tier's liquid hoard cap.

### C. Spire Travel, Tolls & Warrens Navigation
- **Reference:** `ClockworkPathfinder/Rules/WorldAndLaw.md` (Section 2)
- **Focus Areas:**
  - Develop exploration-mode encounter tables for traveling the **Peasant Paths**, bypassing **Warrens toll gates** (Johnny Ralen & Amanda Coren's territories), and navigating the vertical transit lifts between circles.

### D. NPC Subsystem Calibration (Civilized / Protected Tags & Minion Scaling)
- **Reference:** `ClockworkPathfinder/Rules/NPCs.md`
- **Focus Areas:**
  - **Stat Block Templates:** Build standardized GM stat blocks for common Spire civilians (e.g., Level 4 Fungus Farm Laborer, Level 6 Ward Clerk, Level 10 Spire Chief Surgeon, Level 5 Sheltered Noble Officer) featuring the **Civilized** and **Protected** tags.
  - **Action Economy & Morale Ripple:** Stress-test the 1-Action Command/Rally requirement when an NPC suffers Trauma Collapse and the Will save vs. Demoralize on subordinates when a Protected figurehead buckles.
  - **Adversary Minion Design:** Formulate guidelines for building competent high-skill non-combatants (spotters, terminal technicians, lock technicians) who can challenge PCs mechanically without becoming bullet sponges.

### E. Understanding Integration into Character Classes
- **Reference:** `ClockworkPathfinder/Rules/Skills.md`
- **Focus Areas:**
  - **Class Document Updates:** Systematically update all 17 class files under `ClockworkPathfinder/Classes/` to list their starting Understanding allocation formula (`2 Automatic + Class Base [1 to 4] + Cha Modifier`) and suggested starting Focuses.
  - **Phase 1 & Phase 2 Playtesting:** Test the dual-attribute mechanism in heist and investigation scenarios to ensure the DC scaling between Focus and Broad inquiries feels rewarding without stalling social encounters.

### F. Real-World Skill Bounds & Feat Replacement Index
- **Reference:** `ClockworkPathfinder/Rules/Skills.md`
- **Focus Areas:**
  - **Skill Feat Audit:** Catalog all standard PF2e Remaster skill feats for Athletics, Acrobatics, Stealth, and Thievery to flag pseudo-magical feats (e.g., *Cat Fall*, *Wall Jump*, *Cloud Jump*, *Slippery Prey*) and rewrite them as technological equipment dependencies (pneumatic soles, grapple lines, winch harnesses, slicking grease).
  - **Equipment Equivalencies:** Create explicit gear entries for climbing claws, suction plates, and optical smoke canisters so players know what tools are required to accomplish extreme physical feats.

### G. Spire Logistics, Transit Checkpoints & Smuggling Mechanics
- **References:** `ClockworkPathfinder/Rules/NewAvalon.md`, `ClockworkPathfinder/Rules/WorldAndLaw.md` (Section 5)
- **Focus Areas:**
  - **Vertical Transit Turnaround & Schedules:** Formalize travel durations, fare schedules (Pins/Bits/Crowns), and mechanical delay risks for vertical transit along the **Peasant Paths** (South carriages, North freight, East/West commuters) vs. the high-cost **Noble Path** (North express at 10× cost, East Noble-only, West University-only).
  - **Weapon Packaging & Peace-Bonding Checks:** Mechanics for transporting larger weapons through public corridors (`Stealth / Thievery` vs. Constable `Perception / Understanding: Guard & Military`).
  - **Armor Legality & Constable Spot Checks:** Procedures for constables inspecting civilian armor wear in public corridors (padded/leather civilian standard vs. departure exceptions). Establish social standing / badge protocols for off-duty constables traveling to/from work, and military personnel transporting personal arms under active orders.
  - **King's Guard Gear Authentication & Counterfeit Interception:** Subsystem for verifying genuine King's Guard heraldic metallurgy, livery enameling, and hallmark stamps. Define Investigation/Crafting/Understanding DCs for detecting black-market counterfeit regalia, along with escalating legal stakes (arrest, King's Court treason trials) for unauthorized possession.
  - **Veteran Reactivation & Recall Protocols:** Narrative triggers and legal mechanisms for recalling retired King's Guard members into active duty, and auditing personal armaments kept for ceremonial versus reactivation purposes.
  - **Contraband & Cartridge Smuggling:** Rules for smuggling charged military Neither Cartridges or forbidden gunpowder into the interior municipal circles. Establish detection DCs (constabulary galvanic sniffing devices, search dogs, baggage audits) and legal consequences when exposed.
  - **Outer Gate & Military Ward Cartridge Exchange Loop:** Downtime procedure for checking out Neither cartridges (half deposit, half charge), managing ammunition expenditure, and processing returns/refunds for factory-sealed cylinders upon return to the spire.
  - **Crisis Conscription Event Engine:** Structured rules for when a state of emergency (airship siege, Neither storm breach, Warrens insurrection) triggers universal military conscription, including command rank assignments, authorized weapon/armor gear issues, and the return of ordnance when the crisis stands down.

### H. Warrens & Tombs Delving Procedures
- **References:** `ClockworkPathfinder/Rules/NewAvalon.md` (Section 6), `ClockworkPathfinder/Rules/RareHeritages.md`
- **Focus Areas:**
  - **Warrens Gate Toll Standoffs:** Procedures for negotiating or bypassing the **12 Pins to 1 Crown** toll gates into the Warrens, including dealing with Johnny Ralen (North) and Amanda Coren (South) in Ward 13, and bribing Ward Gate Guards to authorize cartridge checkout for deep excursions.
  - **Sewage Conduits & Fungal Cavern Terrain:** Environmental hazards for exploring the chasms between Wards and Warrens—caustic runoff channels, slick fungal shelves, and toxic spore clouds.
  - **Photosensitive Harvest Rules:** Tactical combat complications in fungal cultivation vats where open flame, electric arc discharges, or radiant lamps cause Sycelium crops to rot rapidly, inciting hostile swarm reactions from underclass fungus farmers and goblins.
  - **The Degradation Clock (Goblinization & Troglodyte Drift):** Exploration-mode affliction rules tracking chronic exposure, unpurified sewage diets, and Neither saturation that gradually trigger aberrant physical and cognitive shifts.

### I. Ruin Stratification & Neither Salvage Engine
- **References:** `ClockworkPathfinder/Rules/History.md` (Eras I–V), `AISummary/WorldSummary.md` (Ruins)
- **Focus Areas:**
  - **Epochal Ruin Generator:** Standardized dungeon tables reflecting distinct geological and historical layers:
    - *Era 1 Ruins (Seven Great Kingdoms, 1715–2110):* Rusted locomotives, flooded subway tunnels, locked steel bank vaults, unstable pre-Neither electrical capacitor banks, and fragile paper archives.
    - *Era 3 Ruins (Proto-Spire Kingdoms, 2400–3900):* Collapsed 500-foot stone spires, orc warband shrines, ancient dwarven watermill dynamos, and lost early Neither-steel blades.
    - *Era 4 Ruins (Dwarven Subterranean Citadels, 3900–4100):* Lightless subterranean cities, cat-optic optical traps, geothermal steam taps, and deep-vein mineral caches.
  - **Neither Salvage Decay Rules:** Rules for preserving fragile pre-collapse materials. Salvaged metals, paper, and textiles recovered from Neither mud begin rapid chemical oxidation and crumbling within hours of exposure to fresh air or radiant lamps unless secured in vacuum-sealed canisters.

### J. Cartridge Shelf-Life & Spire Siege Attrition Engine
- **References:** `ClockworkPathfinder/Rules/History.md` (Era IX), `ClockworkPathfinder/Rules/RangedWeapons.md`
- **Focus Areas:**
  - **Cartridge Stability & Decay Die:** A simple check for aging or scavenged Neither ammunition. When firing cartridges older than 90 days or scavenged from wild ruins, roll a flat DC 5 check; on a failure, the cartridge discharges with half effect, squibs inertly, or corrodes the firing chamber.
  - **Spire Siege Attrition Subsystem:** A high-level GM tracking system for besieged spires measuring four weekly attrition dials:
    1. *Cartridge & Munitions Stockpiles* (Defensive arc cannon uptime vs. long-range cartridge bombardment).
    2. *Mela & Sycelium Rations* (Onset of malnutrition and food riots).
    3. *Radiant Power Grid Stability* (Collector rod damage, municipal blackouts, and lift elevator shutdowns).
    4. *Warrens Disease & Goblinization Rate* (Neither fog filtration failures pushing lower circles into epidemic sickness).

### K. Airship 2D Cloud Sea Combat Subsystem
- **References:** `ClockworkPathfinder/Rules/History.md` (Era VII), `AISummary/WorldSummary.md` (Section 2)
- **Focus Areas:**
  - **The Flat Cloud Plane (2D Tactical Naval Combat):** Because the atmospheric density of the Zone naturally forces all airships to float at the exact same equilibrium altitude, dogfighting collapses into 2-dimensional naval tactics.
  - **Boarding Actions & Rigging Combat:** Streamlined rules for firing magnetic grapple cables, swinging across cloud voids between envelopes, and repelling boarders on swaying wooden gantries.
  - **Zone Squall & Lightning Hazards:** Environmental stress checks on uninsulated skyship hulls during combat—sudden updrafts, engine stalls, and static arcs grounding through ship armor.
  - **Arc Cannon Broadsides vs. Cartridge Snipers:** Ship-mounted Zone arc batteries (heavy hull damage) balanced against riflemen taking precision cartridge shots through viewing slits.

---

## 4. Setting Mysteries & Canon Reconciliations (From AISummary/WorldSummary.md)

1. **City Naming Reconciliation:** Reconcile early source document references to "Abelanth" vs. the established capital spire "New Avalon." (Proposed solution: Abelanth is the ancient or original foundation settlement upon which New Avalon was built, or a neighboring sister spire across the sea).
2. **"Perdium" vs. Neithercrete:** Cleanly define the relationship between standard stone, reinforced steel, Neithercrete, and legacy references to "perdium" (e.g., perdium as an alloyed chemical sealant applied to outer Neithercrete walls).
3. **The Aberrant Transformation Rules:** Formalize the exact biological and moral degradation thresholds for how desperate humans in the Warrens turn into Goblins (Type 3a) or Vampires (Type 3b), and how orcs in the Tombs become Troglodytes.

---

## 5. Playtest Scenarios to Design

1. **"The Lower Sump Incursion" (Levels 1–3):**
   - *Test Focus:* Warrens navigation, Neither sickness checks, low-tier melee/fisticuffs (Survivor, Pugilist, Brute, Miner), and 3-step wound recovery with limited supplies.
2. **"The Noble Salon Intrigue" (Levels 4–6):**
   - *Test Focus:* High-status social friction, Dandy fencing duels, Scholar/Inspector forensic audits, calling in Favors, and firearm concealed-carry restrictions in Ward 13/Noble Ward.
3. **"The Zone Airship Boarding" (Levels 7–9):**
   - *Test Focus:* Sky Captain navigation, electrical lightning storms in the Zone, Neither cartridge rifles vs. arc cannons, and vertical rigging combat.
