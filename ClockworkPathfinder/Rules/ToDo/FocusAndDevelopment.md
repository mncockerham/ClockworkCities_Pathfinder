# Clockwork Pathfinder — Active Development & Playtest Roadmap

- **Status:** **Active Backlog & Playtest Tracker**
- **Location:** `ClockworkPathfinder/Rules/ToDo/FocusAndDevelopment.md`
- **Archive of Resolved Systems:** All finalized and codified subsystems have been moved to [`resolvedFocusandDevelopment.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Rules/ToDo/resolvedFocusandDevelopment.md).
- **Guiding Design Hierarchy (`[00_RulesFoundation.md]`):**
  1. **Priority 1:** *Is it fun/beneficial to the game?* (If not, why are we doing it this way?)
  2. **Priority 2:** *Does it fit the theme and mood of the game world?*
  3. **Priority 3:** *Is it realistic and aligned with other rules?* (Least important; can be ignored if 1 and 2 are met).

---

## 1. High-Priority Mechanical Systems Needing Calibration & Playtesting

### A. Wound System, Trauma Floor & Chirurgeon Economy Playtesting
- **Reference:** [`ClockworkPathfinder/Rules/Healing.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Rules/Healing.md), [`AISummary/20_Healing.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/AISummary/20_Healing.md)
- **Open Calibration & Playtest Tasks:**
  1. **Low-Level Trauma Ceiling Floor:** Currently, the trauma ceiling for Regular Damage while suffering Critical/Mortal wounds is $\text{Level} + \text{CON mod}$ (only 3 HP at Level 1 with CON +2, meaning a single 4-damage punch immediately dips back into Critical wounds). Evaluate whether low-level characters need a minimum trauma floor (e.g., $\max(\text{Level} + \text{CON}, 5)$) to prevent perpetual trauma loops at Levels 1–3.
  2. **Multi-Encounter Trauma Pacing:** Playtest how parties adapt when carrying the trauma ceiling during an active multi-day expedition in the Warrens or Neither depths.
  3. **Chirurgeon Medical Kit Economy:** Balance surgical kit consumable costs and field stabilization DC checks against the 1/hour and 1/minute bleed-out clocks.
  4. **Direct Stat Damage Ergonomics:** Ensure table bookkeeping of temporary direct attribute penalties (e.g., –2 Str from Mortal trauma) is smooth alongside standard PF2e conditions.

### B. Ranged Weapons, Cartridge Logistics & Grind Playtesting
- **Reference:** [`ClockworkPathfinder/Rules/RangedWeapons.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Rules/RangedWeapons.md), [`ClockworkPathfinder/Rules/NeitherTeck/Weapons.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Rules/NeitherTeck/Weapons.md)
- **Open Calibration & Playtest Tasks:**
  1. **Wilderness Ammunition Stress-Testing (Grind Balance):** Now that Cartridge Weapons have full firearm ranges (`30–150 ft`), boosted damage (`1d8` to `2d10`), `Reload 1 / 2 / 3` by cartridge size, and full firing rate with trained Discipline Tags, run multi-day wasteland delves to test how players ration finite cartridges across the 70% attrition grind vs. falling back to bows/crossbows (`Reload 0` / unlimited resupply).
  2. **Poor-Quality Battlefield Weapon Burnout Pacing:** Playtest the **20% reload burnout rate** and **10-minute Field Repair check** on salvaged/poor-quality cartridge weapons during extended delves.

### C. Neither Exposure Downtime & Medical Purge Pricing
- **Reference:** [`ClockworkPathfinder/Rules/TheNeither.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Rules/TheNeither.md)
- **Open Calibration Tasks:**
  1. **28-Day Rolling Exposure Window:** Playtest the 28-day commuter/shift-worker tracking window in campaigns where parties alternate between the Warrens/surface and upper Spire wards.
  2. **Medical Purge Costs:** Calibrate the monetary cost and ward availability of Chirurgeon clinical purges (*Mela Cleanse*) and high-ward *Hyperbaric Aither Sanatoriums* against the new Monthly Spending Allowance tables.

### D. Secular "Magic Item" Pricing & Skill-Based DC Scaling
- **References:** [`ClockworkPathfinder/Equipment/EquipmentCatalog.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Equipment/EquipmentCatalog.md) (Sections 5 & 7), [`AISummary/10_Magic.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/AISummary/10_Magic.md), [`ClockworkPathfinder/Rules/NeitherTeck/NeitherTeckRules.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Rules/NeitherTeck/NeitherTeckRules.md)
- **Open Design Tasks:**
  1. **Cost & Impact Equilibrium:** Calibrate store prices of *Powered Exoskeletons*, *Protection Suits*, and *Calibrated Nonlethal Munitions* against the new **Citizen Bulwark** level-based item progression (`[GM Core p.58]`) and organizational requisition budgets.
  2. **Spellcasting Proficiency Mirrored via Technical Skills:**
     - Evaluate allowing specialized technical classes (**Scholar, Clockwork Engineer, Artisan, Chirurgeon, Mad Bomber, Inspector**) to substitute their technical skill proficiency bonus/DC (*Crafting: NeitherTeck*, *Medicine*, *Occultism: Neither Dynamics*) when calculating saving throw DCs for calibrated devices and chemical concoctions, mirroring PF2e spellcaster DC progression while generic store munitions retain flat DCs for martials.

---

## 2. Class Polish & Environmental Niche Tuning

### A. The Influence Trio (Merchant, Noble, Black Marketeer) & Combat Directives
- **References:** [`ClockworkPathfinder/Classes/Merchant.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Classes/Merchant.md), [`Noble.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Classes/Noble.md), [`BlackMarketeer.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Classes/BlackMarketeer.md)
- **Open Tasks:**
  1. **Round-by-Round Combat Directives:** Expand active 1-Action and Reaction directives (e.g., *Bounty Designation*, *Retainer Intercept*, *Credit-Line Surge*, *Distracting Bribery*) so Influence classes have dynamic tactical choices on rounds 2–4 beyond *Lucrative Incentive*.
  2. **70/30 Contact & 3/4 Status Loss Playtesting:** Stress-test the 70/30 contact network split and the 3/4 connection loss rule when a Noble (Status < 5) or Merchant (Status < 3) loses their required status tier.

### C. The Scholar's Analytical Stratagems & Savage Combatant Playtesting
- **References:** [`ClockworkPathfinder/Classes/Scholar.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Classes/Scholar.md), [`Soldier.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Classes/Soldier.md), [`Pugilist.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Classes/Pugilist.md)
- **Open Tasks:**
  1. **Scholar Specialties:** Playtest the three academic specialties (Architect, Accountant, Natural Philosopher) in tactical encounters alongside the Inspector and Artisan.
  2. **Savage Combatant (Levels 2, 4, 8):** Playtest the new *Savage Combatant*, *Relentless Savagery*, and *Savage Onslaught* feats on Soldiers and Pugilists to verify the melee damage/Temp HP boost feels rewarding while the ranged ban and 10-minute –2 social penalty create fun roleplay consequences.

---

## 3. World, Resource & Narrative Subsystems to Formalize

### A. Numerical Resource Tables & Lease Formulas (`ResourcesAndWealth.md`)
- **References:** [`ClockworkPathfinder/Rules/ResourcesAndWealth.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Rules/ResourcesAndWealth.md), [`ClockworkPathfinder/Rules/SocialClasses.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Rules/SocialClasses.md)
- **Context:** The 5-category resource architecture (*Monthly Spending Allowance*, *Personal Property Cap = 1 × Monthly Spending*, *Requisitioned Organizational Equipment*, *Retainer Budget*, and *The Citizen Bulwark 3-Item Exemption*) is now codified in [`ResourcesAndWealth.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Rules/ResourcesAndWealth.md).
- **Remaining Numerical & Formula Tasks:**
  1. **The 1–100 Status, Role & Standing Calculation:** Finalize the exact math for the 5 non-sequential Group Status steps (rated 1–100 within each step), Individual Role, and Internal Standing (1–100) so GMs and players know how much **Monthly Spending Allowance** and **Retainer Budget** each tier grants.
  2. **Spire Location Lease & Wealth Surcharge Formula:** Codify the formula used by Noble landlords to calculate rent based on **Ward + Circle/Location + Regulated Wealth-Generation Surcharge**.
  3. **Surplus Wealth $\rightarrow$ Standing Guidelines:** Provide simple Storyteller guidelines for how returning surplus wealth/loot above `1 × Monthly Spending` to a House or Guild boosts Standing or unlocks higher-tier Requisitioned Equipment.

### B. Understanding Integration & Civilian Background Feats
- **References:** [`ClockworkPathfinder/Rules/Skills.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Rules/Skills.md), [`ClockworkPathfinder/Rules/SocialClasses.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Rules/SocialClasses.md)
- **Open Tasks:**
  1. **Class Document Updates for Understanding:** Update all player class files under `ClockworkPathfinder/Classes/` (and character examples) to explicitly list their starting Understanding allocation (`2 Automatic + Class Base [1 to 4] + Cha Modifier`) and suggested Focuses.
  2. **Civilian Background Feats / Trade Traits:** Codify a formal list of working-class background perks (e.g., foundry tool weapon familiarity, guild wholesale discounts, dray handling) in [`SocialClasses.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Rules/SocialClasses.md) or [`AncestriesAndHeritages.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Rules/AncestriesAndHeritages.md).

### C. Real-World Skill Bounds & Feat Replacement Index
- **Reference:** [`ClockworkPathfinder/Rules/Skills.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Rules/Skills.md)
- **Open Tasks:**
  - Audit standard PF2e Remaster skill feats for Athletics, Acrobatics, Stealth, and Thievery to flag pseudo-magical feats (e.g., *Cat Fall*, *Wall Jump*, *Cloud Jump*, *Slippery Prey*) and rewrite them as technological equipment dependencies (pneumatic soles, grapple lines, winch harnesses, slicking grease).

### D. The Favor Hierarchy: Preparation Time & Escalation Rules
- **Reference:** [`ClockworkPathfinder/Rules/WorldAndLaw.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Rules/WorldAndLaw.md) (Section 6)
- **Open Tasks:**
  - Build simple Storyteller guidelines for **downtime preparation time** (hours vs. days) when setting up indirect Opportunity Favors, and mechanics for **Favor Escalation** (requesting an *Obligation* from a contact who only owes a *Boon*).

### E. NPC Stat Block Templates (Civilized / Protected Tags)
- **Reference:** [`ClockworkPathfinder/Rules/NPCs.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Rules/NPCs.md)
- **Open Tasks:**
  - Build standardized GM stat blocks for common Spire civilians (e.g., Level 4 Fungus Farm Laborer, Level 6 Ward Clerk, Level 10 Spire Chief Surgeon, Level 5 Sheltered Noble Officer) featuring the **Civilized** and **Protected** tags, and stress-test the 1-Action Command/Rally morale ripple.

### F. Spire Logistics, Checkpoints & Smuggling Procedures
- **References:** [`ClockworkPathfinder/Rules/NewAvalon.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Rules/NewAvalon.md), [`ClockworkPathfinder/Rules/WorldAndLaw.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Rules/WorldAndLaw.md) (Section 5)
- **Open Tasks:**
  1. **Vertical Transit Schedules & Fares:** Formalize travel durations, fare schedules (Pins/Slivers/Labors), and delay risks along the **Peasant Paths** vs. the **Noble Path** (10× cost).
  2. **Checkpoint Detection DCs:** Define `Stealth / Thievery` vs. Constable `Perception / Understanding` DCs for smuggling unpackaged weapons, illicit low-power radiant converters, volatile solutions, or contraband cartridges/gunpowder, plus `Investigation / Crafting` DCs for detecting counterfeit King's Guard regalia.
  3. **Crisis Conscription Event Engine:** Structured procedures for emergency militia mobilization (rank assignments, temporary cartridge/converter issues, and post-crisis ordnance return).

### G. Warrens, Tombs, Ruins & Airship Subsystems
- **References:** [`ClockworkPathfinder/Rules/NewAvalon.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Rules/NewAvalon.md), [`ClockworkPathfinder/Rules/History.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Rules/History.md)
- **Open Tasks:**
  1. **Warrens & Tombs Exploration Hazards:** Encounter tables for Peasant Paths, Warrens toll gates (12 Pins to 1 Labor), caustic sewage conduits, photosensitive Sycelium crop rot (when exposed to arc flashes/lamps), and the biological **Aberrant Transformation / Degradation Clock** (Goblin, Vampire, Beast, Neanderthal, Troglodyte thresholds).
  2. **Epochal Ruin & Salvage Decay Generator:** Dungeon tables for Era 1 (1715–2110), Era 3 (Proto-Spires), and Era 4 (Dwarven Citadels), plus rapid oxidation/decay rules for pre-collapse salvage exposed to Aither or radiant lamps without vacuum canisters.
  3. **Cartridge Shelf-Life & Spire Siege Attrition:** Flat DC 5 check for firing >90-day-old scavenged cartridges, and the 4-dial GM Spire Siege Attrition tracker (Munitions, Rations, Grid Stability, Warrens Disease).
  4. **Airship 2D Cloud Sea Combat:** Rules for 2D naval-style broadsides on the Zone's buoyancy equilibrium plane, magnetic grapple boarding, and Zone lightning squall hazards.

---

## 4. Playtest Scenarios to Design & Run

1. **"The Lower Sump Incursion" (Levels 1–3):**
   - *Test Focus:* Warrens navigation, Neither sickness checks, low-tier melee/fisticuffs (Survivor, Pugilist, Soldier with *Savage Combatant*, Scout-Miner), and 3-step wound recovery with the low-level trauma ceiling.
2. **"The Noble Salon Intrigue" (Levels 4–6):**
   - *Test Focus:* High-status social friction, Dandy fencing duels, Scholar/Inspector forensic audits, calling in Opportunity Favors, and everyday-wear armor/mundane dagger restrictions in Ward 13 and the Noble Ward.
3. **"The Zone Airship Boarding" (Levels 7–9):**
   - *Test Focus:* Sky Captain navigation, electrical lightning storms in the Zone (half-damage/duration on Neither-tech), cartridge rifles vs. ship-mounted arc cannons, and rigging boarding actions.
