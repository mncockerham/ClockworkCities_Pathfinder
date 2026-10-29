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

### D. Secular "Magic Item" Cost, Impact & Spellcasting Proficiency Skill System (Active Development)
- **References:** `ClockworkPathfinder/Equipment/EquipmentCatalog.md` (Sections 5 & 7), `AISummary/10_Magic.md`, `ClockworkPathfinder/Rules/NeitherTeck/`
- **Current Objective:** Work to balance the monetary cost, tactical impact, and power scaling of reskinned secular "magic items" (clockwork devices, powered chassis, protection suits, and biochemical concoctions), while exploring a skill-based scaling mechanic that mirrors spellcasting proficiency for technical classes.
- **Key Design Areas to Explore:**
  1. **Cost & Impact Equilibrium:**
     - Calibrate flat store costs in Nobels/Slivers against expected PC wealth progression. Ensure that high-impact items (such as *Powered Exoskeletons*, *Resilience Suits*, *Calibrated Dart Rifles*, and *Acoustic Stunners*) provide meaningful tactical value without rendering basic weapons or class features obsolete.
     - Fine-tune the trade-offs of physical stat mod enhancements (+STR/–DEX vs +DEX/–STR) and environmental hazard absorption (the 10-minute "Fresh Seal" rule) across levels 1–20.
  2. **Spellcasting Proficiency Mirrored via Skills:**
     - In standard PF2e, spellcasters scale their spell attack rolls and saving throw DCs through class proficiency (Trained, Expert, Master, Legendary spellcasting). In our non-magical setting, consider tying device saving throw DCs, tactical rig overclocks, and apparatus attack modifiers to **dedicated technical/biomedical skills** (e.g., *Crafting: NeitherTeck*, *Medicine: Toxicology/Surgical*, or *Arcana/Occultism: Neither Dynamics*).
     - **Potential Mechanics to Test:**
       - **Skill-Based DC Scaling:** Allow specialized classes (**Scholar, Clockwork Engineer, Artisan, Chirurgeon, Mad Bomber, Inspector**) to substitute their technical skill proficiency bonus (or skill DC) when determining the save DCs of their calibrated items, gadgets, and chemical concoctions, directly mirroring traditional spellcaster DC progression.
       - **Martial vs. Technical Specialization:** Generic store-bought munitions retain flat DCs for standard martials, while characters investing skill increases and feats into technical disciplines unlock true "spellcaster-level" potency from high-end neither apparatuses and calibrated neurotoxins.
       - **Integration with Intelligence Scaling:** Ensure that skill proficiency bonuses stack cleanly with or replace the flat caps on the new Calibrated Item series without creating runaway math.
  3. **Restoring the Classic GM Tuning Tool (Anti-Catalog Homogenization):**
     - Traditional 3rd Edition and pre-modern D&D allowed GMs to drop custom magic items directly to uplift struggling or casual players who were falling behind the party's optimized power gamers. Modern PF2e and 5e largely stripped this by creating standardized, pre-calculated "shopping catalogs" where power gamers simply buy the best gear.
     - **The Clockwork Cities Solution:** Our system of **Discipline Tags** (`[Military]`, `[Airships]`, `[Professional]`, `[Clandestine]`) combined with **Custom/Uncommon Hardware** explicitly restores this DM tool. By creating an uncommon prototype tailored with a specific player's tag or a bespoke AP/Passive point discount (e.g., –2 AP instead of –1, or a reduced passive load), the GM can directly hand impactful power to a specific character without creating an arms race across the min-maxers.

---

## 2. Class Polish, Subsystem Calibration & Current Open Issues

### A. The Merchant Class: Combat Action Economy & Directives (Active Issue)
- **Reference:** `ClockworkPathfinder/Classes/Merchant.md`
- **Current Issue:** While the Merchant dominates socially and financially in Spires (Rating A), their turn-by-round combat options on a tactical battlemap feel undefined beyond firing a light pistol or shouting broad directives.
- **Focus Areas:**
  - **Tactical Directives:** Codify 3–4 specific, active combat Actions and Reactions (e.g., *Bounty Designation*, *Retainer Intercept*, *Credit-Line Surge*, *Distracting Bribery*) so the Merchant has engaging choices on rounds 2, 3, and 4.
  - **Financial Subsystems:** Balance credit-line procurement of high-tier `[Military]` or `[Professional]` Neither items against downtime investment returns.

### B. The Clockwork Engineer vs. Artisan Division (Active Issue)
- **References:** `ClockworkPathfinder/Classes/ClockworkEngineer.md`, `ClockworkPathfinder/Classes/Artisan.md`
- **Current Issue:** Both are Type 4 High-NeitherTeck classes keying off Intelligence and Crafting. At the table, players need a sharp distinction between their roles.
- **Resolved Division:**
  - **Artisan (Logistical Backbone):** Specializes in **Passive Loadout Capacity**, institutional manufacturing, party-wide equipment conditioning (+1 to +3 non-magical bonuses), structural vulnerability exploitation, and mundane tradecraft.
  - **Clockwork Engineer (Combat Overclocker):** Specializes in **Active Surge prototype overclocks**, unstable mechanical innovations (Armor or Weapon), Overdrive burst damage, and high-risk field discharges.

### C. The Scholar's Analytical Stratagems
- **Reference:** `ClockworkPathfinder/Classes/Scholar.md`
- **Focus Areas:**
  - Test the three specialties (Architect, Accountant, Natural Philosopher) in complex tactical encounters. Ensure that substituting Intelligence for attack rolls and diagnosing enemy structural flaws remains balanced against the Inspector's forensic debuffs.

### D. Survivor: Urban Infiltration & Intrigue [RESOLVED]
- **Reference:** `ClockworkPathfinder/Classes/Survivor.md`
- **Resolution:** Updated to establish the Survivor as the premier master of **Stealth, Thievery (lockpicking), and Deception** in Spires and urban centers. Added *Urban Infiltration Mastery* (+1 circumstance bonus to lockpicking, hiding, and impersonation in civil settlements) and synergy with `[Clandestine]` and `[Professional]` tags.

### E. Chirurgeon & Mad Bomber: Core Ability AP Autonomy [RESOLVED]
- **References:** `ClockworkPathfinder/Classes/Chirurgeon.md`, `ClockworkPathfinder/Classes/MadBomber.md`, `ClockworkPathfinder/Rules/NeitherTeck/NeitherTeckRules.md`
- **Resolution:** All personal class features, quick concoctions, field vials, medical sera, auto-injectors, demolition charges, and infused bombs cost **0 Active Surge AP** for the creator. AP costs apply only when handing items to untrained allies or when operating external energy/clockwork tech.

### F. Miner Consolidation into Scout [RESOLVED]
- **Reference:** `ClockworkPathfinder/Classes/Scout.md`, `AISummary/30_ClassEnvironments.md`
- **Resolution:** The Miner class was consolidated into the **Scout** as the subterranean sapper and deep delver path. All standalone Miner files and references were purged, and Scout now commands both surface outriding and deep excavation.

### G. NeitherTeck Dual-Economy System [RESOLVED & STANDARDIZED]
- **Reference:** `ClockworkPathfinder/Rules/NeitherTeck/NeitherTeckRules.md`, `Weapons.md`, `TacticalRigs.md`, `AISummary/10_Magic.md`, `AISummary/30_ClassEnvironments.md`
- **Codified Mechanics:**
  - **Dual-System Resource Split:**
    - **Passive Loadout Capacity:** $\text{Higher of Str or Con mod} + 1\text{ per even level}$ (Scholars, Artisans, Merchants use best of Int, Str, Con). Committed once during morning prep for breathing units, hazard filters, and ballistic linothorax. **Zero combat round math.**
    - **Active Surge AP:** $\text{INT mod} + \text{Class Base AP} + \text{Level Progression Bonus}$. Refreshes per round; spent strictly on Actions and Reactions.
  - **Equipment Discipline Tags & Synergy Discounts:** Standardized 9 tags (`[Biochemical]`, `[Mechanical]`, `[Military]`, `[Airships]`, `[Professional]`, `[Technical]`, `[Clandestine]`, `[Subterranean]`, `[Outlands]`). Trained classes gain an innate **–1 to –2 AP discount** (min 1 AP), eliminating the martial attribute tax.
  - **Hard Dependency Rule:** NeitherTeck energy firing mechanisms have **zero mundane fallback**; outside radiant grids (>5× generator distance), out of cartridges, or in pure Aither, energy weapons are completely dead.
  - **Auxiliary Attachments:** Ranged weapons can equip physical **affixed bayonets** (1d6 piercing/slashing) or **reinforced grips** (1d4 bludgeoning pistol whips) that function unpowered at 0 AP.

### H. Environmental Class Balance Audit & Niche Tuning (Active Focus)
- **References:** `AISummary/30_ClassEnvironments.md`, `AISummary/WorldSummary.md`, `ClockworkPathfinder/Classes/`
- **Core Design Principles:**
  - **Classes are Skill Sets, Not Fixed Social Castes:** A "Clockwork Rifleman" is a master marksman, not necessarily a soldier or outland vagrant. If a character is born a Noble or Wall Merchant, their social class and legal permissions grant dueling sidearms or social access, regardless of whether their character class is Soldier, Rifleman, Scholar, or Dandy. 
  - **No Arbitrary Class-Based Legal Exceptions:** Exceptions to municipal law are risky. Aside from defined legal privileges tied to social status (e.g., Nobles/Wall Merchants legally wearing rapiers/dueling swords, or sworn King's Guards on duty), **the law treats everyone equally**. If we carve out arbitrary weapon-carry exemptions for one class without an airtight in-world social rationale, every other group will logically find workarounds, eroding the peace-bonded nature of civilized Spires.
  - **Generalists vs. Specialists:** Classes that perform solidly across most environments (Tier-2/Tier-3 generalists like Soldier, Sky Captain, Officer) do not need to be dominant in any single area.
- **Classes Requiring Focused Development (Tuning Priority):**
  1. **Too Powerful / At Risk of Over-Dominance (Needs Mechanical Levers & Drawbacks):**
     - **Brute (S in Neither, A in Civil Spires, B in Low Radiant):**
       - *The Issue:* With massive 12 HP/level, high Fortitude, and flat Rage damage, a Brute wielding an ordinary legal utility dagger (1d4) or bare fists can easily out-brawl specialized duelists, constables, and pugilists in polite society, while dominating the outlands with axes.
       - *Development Focus:* Codify strict civil drawbacks for Rage in civilized spires (e.g., immediate legal escalation to "Lethal Affray," high civic infamy, inability to access Favors or social Understanding during or shortly after Rage). Add fatigue or collateral damage costs when raging without protective heavy gear.
     - **Chirurgeon (A in High Radiant, A in Low Radiant, A in The Neither, B in Civil Spires):**
       - *The Issue:* Chemical concoctions and medical sera operate at 0 AP, bypass wireless grid restrictions, ignore cartridge laws, and are easily concealed as medical supplies. With high healing, poisons, and buffs, the Chirurgeon has almost no environmental blind spot.
       - *Development Focus:* Introduce strict consumable shelf-life limits, reagent degradation in polluted Neither fog, and high economic/supply costs for stabilizing compounds. Make illicit narcotics or concentrated toxins carry severe legal contraband classifications if inspected by constables.
     - **Survivor (A in Civil Spires, A in The Neither, B in High/Low Radiant):**
       - *The Issue:* *Urban Infiltration Mastery* (+1 circumstance bonus to Stealth, Thievery, Deception) combined with full Sneak Attack on legal utility daggers makes the Survivor risk crowding out the Inspector and Dandy in municipal intrigue while remaining apex in wilderness survival.
       - *Development Focus:* Ensure Sneak Attack requires specific tactical conditions (such as dirty tricks or positioning) that become harder against disciplined Spire constables or alert guards, and clearly delineate social-investigative boundaries so Survivor doesn't replace Inspector or Scholar.
  2. **Underpowered / Severely Handicapped in Domestic Wards:**
     - **Clockwork Rifleman (D in Civil Spires, D in Influence, B in The Neither, S in Low Radiant):**
       - *The Reality:* **Crossbows ARE fully available** (Master proficiency at Level 1 per Gunslinger rules, benefiting from *Singular Expertise*, deeds, and *Slinger's Reload*). With heavy crossbows and arbalests, the Rifleman is an effective wilderness sniper in the unpowered Neither (Rating **B**).
       - *The Real Bottleneck (Civil Spires & Social):* The weakness is municipal law: open longarms and military crossbows must be boxed and peace-bonded at checkpoints for all citizens.
       - *Universal Solutions (Not Arbitrary Exemptions):*
         1. **Social Class Dictates Carry Rights:** A Clockwork Rifleman of Noble or Merchant status has the legal right to carry a dueling rapier/sword or a gentleman's sidearm, just like any other citizen of that caste.
         2. **Universal Civil Options:** Focus development on skills common to marksmanship that fit municipal law—such as **concealed pocket sidearms** (derringers, small hand crossbows), **0-AP stock/butt strikes and bayonets**, and **exploration-mode overwatch/spotting** rather than giving the class artificial legal passes.
     - **Mad Bomber (D in Civil Spires, D in Influence, A in Outlands/Grids):**
       - *The Issue:* Explosives are universally banned at Spire checkpoints.
       - *Development Focus:* Create non-lethal, mundane preparations (flash powders, choking soot, instant adhesive gums) that legally pass inspection as domestic cleaning, hearth-lighting, or trade goods.
     - **Clockwork Engineer (C in Civil Spires, C in The Neither, C in Influence):**
       - *The Issue:* Heavy prototype rigs and pulse projectors shut down completely outside radiant grids, while bulky gear is barred or peace-bonded in civilized wards.
       - *Development Focus:* Provide clockwork mechanical spring-wound (non-radiant) fallback mechanisms, compact deployable micro-turrets/utilities, and integrated tool proficiencies so the Engineer contributes meaningfully without active radiant power.
  3. **Broad-Use Generalists (Confirmed Healthy — Do Not Force S-Tier Dominance):**
     - **Soldier, Sky Captain, Officer:** Intentionally designed to maintain solid Tier-2/Tier-3 utility across all combat theaters. Their lack of S-tier dominance in High Radiant grids is an intended design trade-off for their unmatched versatility across varied campaign arcs.
  4. **The Influence Trio (70/30 Separation & Status Retention Calibration):**
     - **Merchant, Noble, Black Marketeer:** Ensure combat Directives provide dynamic round-by-round action economy options while playtesting the 70/30 contact separation rule and enforcing the 3/4 connection loss penalty upon loss of required Status.


---

## 3. World & Narrative Subsystems to Formalize

### A. The Favor Hierarchy: Opportunity Actions & Downtime Preparation
- **Reference:** `ClockworkPathfinder/Rules/WorldAndLaw.md` (Section 6)
- **Status:** **Core Concept Refined**
- **Opportunity-Driven Activation (Not a Rigid Downtime Activity):**
  - Calling in a favor is fundamentally an **Opportunity Action** that resolves dynamically within active roleplay or narrative infiltration.
  - **Immediate Opportunity (On-Site Contact):** If the contact who owes a debt or obligation is already present at the scene (e.g., the night watchman at the warehouse gate owes you a *Debt*), no downtime is required. The player simply calls in the marker on the spot to unlock the door, look the other way, or pass through the checkpoint.
  - **Downtime Preparation (Creating the Opportunity):** If the contact is not directly at the target location, calling in the favor requires **Downtime preparation** to arrange the angle of approach or procure the operational cover:
    - *Example:* The party needs to infiltrate a high-society manor. Their contact is a merchant who holds a catering contract for the event. The party spends a day of downtime tracking down the merchant, negotiating the request, and procuring delivery carts, passes, and kitchen uniforms to walk right through the servant's entrance.
- **Focus Areas for System Polish:**
  - Build simple guidelines for GMs outlining **preparation time** (hours vs. days) when setting up indirect favors.
  - Detail mechanics for "Favor Escalation" (what happens if a player asks for an *Obligation* from someone who only owes a *Boon*—social pushback, blackmail risk, or spending additional coin/favors to close the gap).

### B. Status, Standing & Faction Reputation (–99 to +99)
- **Reference:** `ClockworkPathfinder/Rules/SocialClassAndCorruptionRules.md` (Section 1)
- **Focus Areas:**
  - **No "Off-the-Books" Laundering:** Clarify why true off-the-books cash laundering does not exist in the setting. Your Family, Guild, or Profession knows precisely what you should make and own; anything beyond your Status tier's liquid allowance is impossible to keep safely. What your group doesn't take, you have no secure place to store, and nobody will stop others from stealing it (after all, one cannot legally report theft of wealth that officially doesn't exist, and admitting it exists risks immediate expulsion or ruin). Furthermore, human nature dictates that surplus illicit coin is rapidly burned on transient luxuries, food, drink, and entertainment beyond one's means—expending resources that can never be recovered.

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
  - **Class Document Updates:** Systematically update all 16 player class files under `ClockworkPathfinder/Classes/` to list their starting Understanding allocation formula (`2 Automatic + Class Base [1 to 4] + Cha Modifier`) and suggested starting Focuses.
  - **Phase 1 & Phase 2 Playtesting:** Test the dual-attribute mechanism in heist and investigation scenarios to ensure the DC scaling between Focus and Broad inquiries feels rewarding without stalling social encounters.

### F. Real-World Skill Bounds & Feat Replacement Index
- **Reference:** `ClockworkPathfinder/Rules/Skills.md`
- **Focus Areas:**
  - **Skill Feat Audit:** Catalog all standard PF2e Remaster skill feats for Athletics, Acrobatics, Stealth, and Thievery to flag pseudo-magical feats (e.g., *Cat Fall*, *Wall Jump*, *Cloud Jump*, *Slippery Prey*) and rewrite them as technological equipment dependencies (pneumatic soles, grapple lines, winch harnesses, slicking grease).
  - **Equipment Equivalencies:** Create explicit gear entries for climbing claws, suction plates, and optical smoke canisters so players know what tools are required to accomplish extreme physical feats.

### G. Spire Logistics, Transit Checkpoints & Smuggling Mechanics
- **References:** `ClockworkPathfinder/Rules/NewAvalon.md`, `ClockworkPathfinder/Rules/WorldAndLaw.md` (Section 5)
- **Focus Areas:**
  - **Vertical Transit Turnaround & Schedules:** Formalize travel durations, fare schedules (Pins/Slivers/Labors), and mechanical delay risks for vertical transit along the **Peasant Paths** (South carriages, North freight, East/West commuters) vs. the high-cost **Noble Path** (North express at 10× cost, East Noble-only, West University-only).
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
  - **Warrens Gate Toll Standoffs:** Procedures for negotiating or bypassing the **12 Pins to 1 Labor** toll gates into the Warrens, including dealing with Johnny Ralen (North) and Amanda Coren (South) in Ward 13, and bribing Ward Gate Guards to authorize cartridge checkout for deep excursions.
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

### L. Stress-Test Gaps & Mechanical Vulnerabilities (Audit from Character Examples 2026-10-28)
- **Reference:** `ClockworkPathfinder/testing/CharacterExmples20261028/`
- **Context:** Building 6 archetypal PCs (Lv 1 & Lv 5), 5 standard NPC classes, and the civilian-template conversions revealed several key gaps and balance friction points in our current rules:
  1. **Level 5 Martial Weapon Scaling vs. NeitherTeck Weapon Costs:**
     - *The Gap:* At Level 5, martials gain `Weapon Mastery` (Master proficiency, +2 hit, critical specialization) while technical classes remain at Trained/Expert. When purchasing +1 Striking weapons, the cost increases by **+1 AP** (3 AP $\rightarrow$ 4 AP for pistols, 4 AP $\rightarrow$ 5 AP for rifles).
     - *Issue:* Martials with 0 Base AP cannot fire enhanced NeitherTeck weapons without tagging discounts or class features, while Technical classes take huge turn-resource hits to fire striking energy weapons.
     - *Action Item:* Clarify and stress-test whether weapon runes on NeitherTeck devices should increase AP cost linearly, or if higher-tier tuning/capacitors absorb the drain.
  2. **NPC Fragility is Intentional (PCs Feel Superior):**
     - *Design Clarification:* NPC classes (Laborer, Professional, Commoner, Craftsman) lack martial armor/weapon progression and remain fragile by design. This is an intentional feature, not a bug: **NPCs represent everyday people that PCs get to feel distinctly superior to**.
     - *Combat Role:* These NPCs populate the **15% "We Are Heroes"** encounters (unruly mobs, corrupt bailiffs, parlor brawls) where PCs easily overpower them, or serve as vulnerable bystanders/retinues that PCs must actively defend.
     - *NPCs with Class Levels:* Important adversaries, military commanders, or elite assassins do not use civilian NPC classes; they use standard PC classes (Soldier, Officer, Scout, Clockwork Engineer) under standard rules. No artificial "Civilian Defense Floor" is needed.
  3. **Civilian Background Mechanical Value:**
     - *The Gap:* When creating civilian-template Level 5 PCs, trade lore and everyday background perks (e.g. foundry tools dealing 1d6 B, wholesale guild discounts, dray cover bonuses) were implemented narratively rather than through codified setting feats.
     - *Action Item:* Codify a formal **Civilian Background Feats / Trade Traits list** in `ClockworkPathfinder/Rules/AncestriesAndHeritages.md` or `ClockworkPathfinder/Rules/SocialClasses.md` so players picking working-class origins get standardized mechanics.
  4. **Understanding Integration Lag:**
     - *The Gap:* While Understanding is codified in `Rules/Skills.md`, character stat blocks currently calculate standard Perception and Lore without showing their **Focus vs. Broad Understanding pools**.
     - *Action Item:* Prioritize Section E of this roadmap: update class templates and character sheets to explicitly show starting Understanding points (`2 Auto + Base + Cha Mod`).
  5. **Trauma Ceiling Math at Low Levels:**
     - *The Gap:* The trauma ceiling for Regular Damage while suffering Critical/Mortal wounds is $\text{Level} + \text{CON mod}$. At Level 1 with CON +2, max regular HP is only **3 HP**. A single 4-damage punch immediately dips back into Critical wounds.
     - *Action Item:* Evaluate whether low-level characters need a minimum trauma floor (e.g., $\max(\text{Level} + \text{CON}, 5)$) to avoid perpetual trauma loops at levels 1–3.

### M. Campaign Encounter Pacing & Combat Threat Spectrum (The 15 / 70 / 15 Rule)
- **References:** `ClockworkPathfinder/Rules/Combat.md`, `AISummary/00_RulesFoundation.md`, `AISummary/20_Healing.md`
- **Core Design Philosophy:** Combat in Clockwork Cities is not uniform. The game must deliver a deliberate rhythm of empowerment, grueling survival, and high-stakes mortal peril. Encounters should be structured across three calibrated bands:
  1. **15% — "We Are Heroes" (Showcase / Low Risk):**
     - *Tone:* Players get to flex their abilities, display superior tactics/training, and mow down weaker opposition without serious danger.
     - *Typical Opponents:* Uncoordinated slum thugs, petty pickpockets, drunken dockers, routine goblin scavengers, or lone sentries (Party Level –2 to Level –4).
     - *Resource Drain:* Minimal. Consumes cheap ammunition or a few Slivers; almost zero chance of dipping into Critical wounds. Validates player power and class progression.
  2. **70% — "The Grind" (Grueling Attrition / Tension & Resource Consumption):**
     - *Tone:* Hard-fought, tactical engagements where resources are meaningfully burned, positioning matters, and players genuinely sweat over survival.
     - *Typical Opponents:* Coordinated military patrols, fortified barricades, disciplined orc raiders, savage Neither predators, or rival syndicate hit squads (Party Level –1 to Level +1).
     - *Wound Impact:* **Attrition is real.** 0 to several PCs will have their Regular Damage depleted and dip into **Critical (days to heal)** or even **Mortal (weeks to heal)** wounds depending on tactical mistakes, cover choices, or enemy critical hits. Consumes finite Neither cartridges, auto-injector stims, and shield HP.
  3. **15% — "The Boss / Mortal Crucible" (High Lethality / Permanent Stakes):**
     - *Tone:* Climax encounters where reckless play or arrogance leads directly to character death, limb loss, or permanent trauma. Requires planning, recon, environmental exploitation, and flawless teamwork.
     - *Typical Opponents:* Clockwork Colossi, Corrupted Apex Behemoths, Great House Champion Strike Teams, deep-abyss abominations, or Spire High Inquisitors (Party Level +2 to Level +4).
     - *Wound Impact:* Deep systemic trauma. PCs routinely suffer severe Mortal anatomical penalties; party death is a distinct possibility if approached without respect, proper hazard gear, and escape contingencies.

### N. The 1–100 Tiered Status, Standing & Resource Architecture (Exploration Concept)
- **References:** `ClockworkPathfinder/Rules/SocialClassAndCorruptionRules.md`, `AISummary/WorldSummary.md` (Section 7)
- **Core Concept:** Moving status from a narrow 1–9 scale to a rich, granular **1 to 100 Status Scale**, driven by three interacting pillars: **Group Status**, **Individual Role**, and **Internal Standing**:
  1. **Group Status Bands (5 Non-Sequential Steps):**
     - Every institution (from a Laborer union or criminal crew up to a Great House or High Guild) has **5 distinct Status tiers** it can exist at within the world's 1–100 hierarchy (these steps do not need to be contiguous or sequential).
     - Within a tier, the group's health/reputation is rated **1 to 100**. Falling below 1 causes the group to drop to its next lower status step; exceeding 100 elevates the group to the next higher step. Dropping below 1 at the lowest step forces a catastrophic collapse or reorganization of what the group fundamentally is.
  2. **Character Pillars (Role & Standing):**
     - **Fixed Role in House/Guild:** The character's formal station (e.g., apprentice, field agent, heir, senior barrister, military captain).
     - **Standing (1 to 100):** How the character is currently perceived and trusted by their peers and superiors within that role.
  3. **The Four Resource Streams (Determined by Status, Role & Standing):**
     - **Monthly Spending Allowance (Discretionary & Excess Expenses Only):**
       - **All Expected Social Costs Absorbed by the House:** The sponsoring institution directly covers all normal lifestyle expenses appropriate to a person of that status tier and reputation. Dining at restaurants of your status tier (or below), boarding in appropriate quarters, routine carriage travel, and even hosting or treating a small party of colleagues/guests within reason **is automatically charged to the house ledger and never costs personal coin**.
       - **When Personal Spending is Used:** Liquid spending money is only spent when a character chooses to **live beyond their station** (e.g., a Status 2 laborer booking a luxury private box in Ward 13, bribing officials, gambling beyond their social means, or purchasing unauthorized black-market goods).
     - **Requisitioned Equipment (The Institutional Library & Task Exemption):**
       - **Personal Limits Never Apply to Organizational Gear:** Personal Property Caps and Citizen Bulwark limits **never apply to items that your organization can afford and believes you need to perform your role or given tasks**, though **these items always belong to the organization, never the player**.
       - Rather than fixed, permanent purchases, equipment acts as an **adaptable institutional library**.
       - Whenever a character returns to their house, guildhall, barracks, or family estate, they can **swap out and reconfigure their equipped items** to match their next assignment, class needs, or expected environment (e.g., swapping a civil parlor cane for a heavy trench respirator and ballistic rig before a Neither expedition).
       - **Bound by Institutional Profile:** A character can only draw what their specific group or family would reasonably have access to (e.g., a Blacksmith's Guild provides masterwork metallurgy and pneumatic tools, but cannot issue an elven gunpowder dueling pistol; a Great House armory provides ancestral plate and rapiers, but does not stock illegal Warrens gas grenades).
     - **Retainer Budget (Nobles, Merchants & Commanders):**
       - Funds and resources earmarked for hiring, equipping, and provisioning household guards, runners, clerks, and apprentice hirelings (or hiring lower-status PCs).
       - **Cannot Be Used Directly by the PC:** Retainer Budget can never be spent on or used directly by the PC for their own personal gear or expenses.
       - **Monthly Reallocation:** Does not accumulate; must be **reallocated every month**.
     - **The Citizen Bulwark (3-Item PC Upkeep & Resource Exemption):**
       - **Lore & Legal History:** Clockwork technologies require constant upkeep and spare parts far beyond what most Spire residents can afford. This is offset by one of the oldest laws in the realm: **The Citizen Bulwark**. The statute grants skilled citizens funding and parts access to maintain **1 suit of protective armor, 1 weapon, and 1 additional clockwork item** (spare weapon, shield, or other item that can aid in the defense of the Spire). Participating citizens agree to serve in the militia in times of need—though more recent laws have long since made militia service mandatory for *all* citizens, leaving the Bulwark's voluntary wording as a testament to how ancient the law is.
       - **Mechanical Budget Rule & PF2e Progression Alignment:** Every PC can keep and maintain **3 items (1 Armor, 1 Weapon, 1 Additional Clockwork/Defense Item) completely outside of the normal resource limits in the Spire** (exempt from the Personal Property Cap, upkeep drain, and routine house repossession). The allowed price and tier of each of the 3 items is **adjusted by Character Level (up to Item Level = Character Level) and aligns directly with the normal Pathfinder 2e permanent magic item progression** (`[GM Core p.58]`), ensuring all PCs can maintain level-appropriate fundamental enhancements (`+1 Niracrest`, `Striking`, `Resilient`, `+2 Mitheral`, etc.) regardless of social class.
     - **Personal Property Cap (`1 × Monthly Spending Limit`):**
       - With core combat gear exempted by the Citizen Bulwark, players may keep personal items and coin **only up to their Monthly Spending Limit**.
       - **Surplus Wealth Disposal:** All wealth above the `1 × Monthly Spending Limit` (excluding the 3 Citizen Bulwark items and items formally granted for *exceptional service to house or crown*) is **returned to the organization** they are part of, or—if the character is **unaligned**—is rapidly **stolen or spent** on fleeting luxuries/vice (since private secure vaults and off-the-books banking do not exist in the Spire).
     - **Gambling Stakes & Windfalls:**
       - **Gambling Stakes Rule:** If a character intends to keep their gambling winnings as personal wealth, the initial stakes **must be staked out of personal wealth/spending cash**, never house credit. If house credit is used to gamble, any winnings are automatically claimed by the house ledger.
       - **Rapid Windfall Disposal:** Any windfall or illicit score pushing a character above their `1 × Monthly Spending Limit` cannot be hoarded; if not spent immediately, it is returned to their organization or lost to theft, extortion, or vice back down to the `1 × Monthly Spending Limit`.

  4. **Inter-Party Wealth, Asset Requisition & Social Boundaries (Session Pre-Brief Decisions):**
     - **Inter-Party Gear Loaning:** A Noble or high-status PC can allow an ally to carry and use items they purchase or check out. However, the item legally remains the Noble's property and adheres to the Noble's wealth and repossession rules.
     - **Retainer PC Contracts:** A lower-status PC can be hired under another PC's **Retainer Budget**, provided the player agrees to work for them and the requisitioned gear is appropriate to the task.
     - **The Return of Surplus Gear & Wealth:** High-tier gear and excess windfalls above the `1 × Monthly Spending Limit` inevitably return to the house or guild treasury (or are stolen/spent if unaligned). The impact/standing earned depends on the current wealth and supply needs of the guild.
     - **Status Progression Drivers:** Individual status shifts up or down based on three clear pillars: **Societal Recognition**, **Service to the Group**, and **Tangible Group Contribution**.
     - **Equipment Loss & Quartermasters:** The severity of losing requisitioned house equipment is evaluated like a military Quartermaster: judged against the cost/rarity of the lost gear and whether it was lost in honorable service vs negligence.
     - **Social Exposure Realism:** Players have free will, but a recognized Noble slumming in low-class Warrens gambling dens where copper Pins are staked has far graver social and political survival issues to worry about than merely dirtying their hands with base coinage.
---

## 4. Setting Mysteries & Canon Reconciliations (From AISummary/WorldSummary.md)

1. **City Naming Reconciliation [RESOLVED]:** All references to the early draft name "Abelanth" have been removed and unified under **New Avalon** as the sole canon capital spire.
2. **"Perdium" vs. Neithercrete [RESOLVED]:** All references to "perdium" have been replaced with **Neithercrete** as the singular canon building material for spires.
3. **The Aberrant Transformation Rules:** Formalize the exact biological and moral degradation thresholds for how desperate humans in the Warrens turn into Goblins (Type 3a) or Vampires (Type 3b), and how orcs in the Tombs become Troglodytes.

---

## 5. Playtest Scenarios to Design

1. **"The Lower Sump Incursion" (Levels 1–3):**
   - *Test Focus:* Warrens navigation, Neither sickness checks, low-tier melee/fisticuffs (Survivor, Pugilist, Brute, Miner), and 3-step wound recovery with limited supplies.
2. **"The Noble Salon Intrigue" (Levels 4–6):**
   - *Test Focus:* High-status social friction, Dandy fencing duels, Scholar/Inspector forensic audits, calling in Favors, and firearm concealed-carry restrictions in Ward 13/Noble Ward.
3. **"The Zone Airship Boarding" (Levels 7–9):**
   - *Test Focus:* Sky Captain navigation, electrical lightning storms in the Zone, Neither cartridge rifles vs. arc cannons, and vertical rigging combat.
