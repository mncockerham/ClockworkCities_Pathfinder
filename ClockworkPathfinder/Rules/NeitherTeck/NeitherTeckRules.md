# NeitherTeck & Clockwork Systems — Core Rules & Activation Mechanics

- **Base System:** Pathfinder 2e Remaster `[Player Core, Guns & Gears]`
- **Location:** `ClockworkPathfinder/Rules/NeitherTeck/NeitherTeckRules.md`
- **Precedence:** Rules in `AISummary/00_RulesFoundation.md`, `AISummary/10_Magic.md`, and world facts in `AISummary/WorldSummary.md`.
- **Companion Files:**
  - Weapons: [`Weapons.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Rules/NeitherTeck/Weapons.md)
  - Tactical Rigs & Apparatuses: [`TacticalRigs.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Rules/NeitherTeck/TacticalRigs.md)
- **Uncommon Gear, Prototypes & Outland Hardware:** The equipment values and costs in these rules reflect **standardized, mass-manufactured Spire hardware**. Non-standard gear—such as **Uncommon or Rare items**, experimental prototypes, salvaged Era 1 relics, bespoke noble masterworks, or crude Orcish outland rigs—**may not follow standard Spire baselines**. Depending on engineering quality, these items may have **higher or lower passive equipped point costs**, require **more or less active surge AP**, or yield modified capabilities.

---

## 1. Setting Overview & Environmental Medium Dependency

NeitherTeck and Clockwork devices fundamentally rely on the physical and electromagnetic medium of the **Neither (including the Zone)** to function. 
- **Absolute Environmental Dependency:** Without the ambient resonance, conductive fog, and reactive particle flux of the Neither or Zone, these technologies **cannot operate and are completely useless outside these areas**.
- **In Pure Aither:** Capacitors bleed to zero, energy discharges fail to bridge, mechanical flywheels lock or stall, and biochemical catalysts inertly decompose or dissolve into corrosive sludge. NeitherTeck energy weapons, radiant induction grids, and biochemical concoctions become dead weight.
- **In Phase One:** Both technologies share the same throughput mechanics: NeitherTeck reflects biological/chemical reactions catalyzed by Neither fog, while Clockwork utilizes radiant electro-physical gear and kinetic escapements.

Where a battle occurs within the Neither and Zone radically alters class balance:

```
[ Tier 1a: Saturated Tactical Siege/Warrens ] ── Saturated Energy + No Weapon Laws ─► Artisans, Scholars & Riflemen dominate
[ Tier 1b: Civil Spire Core / High Society ] ── Saturated Energy + Strict Disarmament ─► Dandies & Pugilists rule parlor fights
[ Tier 2: Radiant Outposts/Airships ] ───────── Moderate Local Energy ──────────────► Balanced tactical combined arms
[ Tier 3: Outlands & Deep Wilds ] ───────────── Zero Radiant Energy ────────────────► Pure Martials dominate with steel & bows
[ Outside the Neither (Pure Aither) ] ───────── Inoperable (0 Energy) ──────────────► Technology completely dead; steel & elven powder
```

### Environmental Tiers

| Tier | Environment & Grid Access | Ambient Energy Status | Combat Dynamics & Law Status |
|:---:|---|---|---|
| **Tier 1a: Saturated Warfare (Sieges, Warrens & Forward Dynamos)** | Spire exterior battlements/walls, the **Warrens** (unpoliced under-spire), defended military encampments, locations directly outside a Spire during a siege, or **within ~50 feet of an active primary military/mining dynamo** | **Virtually Unlimited / Saturated Radiant Power (100% Output)** | **Zero Weapon/Armor Restrictions; Artisans, Scholars & Riflemen Dominate.** Full plate, powered exoskeletons, heavy siege cannons (`1d12` to `2d12`, reaching `3d10`), and chemical demolition charges operate openly. Operators must possess a calibrated converter module **attuned/synchronized to the local generator's dynamic frequency pattern** to tap full saturated power. Martials provide the essential frontline shield bastion. |
| **Tier 1b: Civil Spire Core (High-Society Wards & Promenades)** | Interior enclosed Spire wards (Wards 1–15, excluding the Warrens) | **Saturated Radiant Grid (Utilities, Lifts, Lighting)** | **Strict Civil Disarmament & Direct-Exit Surveillance; Dandies & Pugilists Dominate.** Wearing armor heavier than normal-looking leather/cloth or displaying clockwork attachments/exoskeletons is strictly prohibited. Weapons of war must be boxed/peace-bonded and under transit surveillance. Only utility daggers (`1d4`) or dueling rapiers (Nobles and Wall Merchants only) are permitted. Military cartridges, converter modules, and volatile solutions are major felonies. |
| **Tier 2: Moderate / Low Radiant Field** | Military SkyShips cruising the Zone, perimeter encampments extending **2 to 3 or more times beyond high-radiant cores**, or **within ~4 miles of New Avalon's outer walls** | **Moderate / Constrained Radiant Power** | **Balanced Combined Arms; Captain / Local Rule.** Inductive coupling operates at stepped-down capacity (`1d10` to `2d10`, –10 to –20 ft range). Grid weapons remain operational with unlimited inductive trickle, but heavy rigs require local capacitors. Outside Spire walls, workers carry dual-purpose axes, the wealthy carry pistols, and airships follow captain's decree. Martials are fully competitive. |
| **Tier 3: The Wild & Deep Outlands** | Lower Neither wastes, unpowered ruins, deep sunken valleys, barbarian territory beyond 5× generator perimeter | **Zero Radiant Energy** | **Martials (Soldiers, Scouts, Pugilists) Dominate.** All NeitherTeck must supply its own power via scarce, sealed Military Cartridges. Once cartridges deplete across the 70% attrition grind, devices go completely dead. Traditional bows, heavy crossbows, armor, and raw physical steel reign supreme. |

---

## 2. The Dual-System Economy: Passive Loadout & Active Surge

NeitherTeck and Clockwork equipment fall into two distinct mechanical categories, preventing turn-by-turn math fatigue while maintaining deep tactical options.

### A. Passive Loadout Capacity (Defensive & Environmental Gear)

Passive equipment includes items that provide ongoing protection or physiological functions without requiring an action in combat: breathing units, environmental respirators, active ballistic linothorax, kinetic dampeners, servo-assisted exoskeletons, and sensory goggles.

To prevent penalizing non-Strength characters (avoiding MAD), classes use one of three **Archetype Calculation Tracks** based on their physical conditioning, reflex tuning, or technical expertise:

$$\mathbf{\text{Passive Loadout Capacity}} = \mathbf{\text{Key Attribute Modifier}} + \mathbf{\lfloor \tfrac{\text{Level}}{2} \rfloor} + \mathbf{\text{Class Base 4}}$$

#### The Three Archetype Tracks
1. **Track A: Physical Load-Bearing (Heavy Martials):**
   - **Classes:** **Soldier** (including *Savage Combatants*).
   - **Key Attribute:** Higher of **Strength** or **Constitution** modifier. (Skeletal density and muscle conditioning to carry heavy hydraulic frames and thick ballistic plates).
2. **Track B: Ergonomic & Agile Tuning (Light Martials & Operatives):**
   - **Classes:** **Dandy, Pugilist, Survivor, Scout, Sky Captain, Officer, Clockwork Rifleman**.
   - **Key Attribute:** Higher of **Dexterity** or **Constitution** modifier (or **Strength** for Strength-based Pugilists). (Precision balance, kinetic posture, and reflex articulation).
3. **Track C: Precision Engineering & Bespoke Tailoring (Technical & Academic):**
   - **Classes:** **Scholar, Artisan, Clockwork Engineer, Chirurgeon, Mad Bomber, Inspector, Merchant, Noble, Black Marketeer**.
   - **Key Attribute:** Higher of **Intelligence**, **Strength**, or **Constitution** modifier. (Ergonomic micro-cables, custom-calibrated pressure regulators, and tailored linings).

#### Armor-Weight Passive Modifiers
Installing passive enhancements (linothorax layers, resilient save harnesses, exoskeletons) into lighter suits is faster and requires less load-bearing structural support:
- **Unarmored / Explorer's Silks:** **–2 Passive Points** to the cost of equipped defensive suites (minimum 1 point).
- **Light Armor (Padded Frock Coat, Trench Duster, Wire Shirt):** **–1 Passive Point** to defensive enhancement costs (minimum 1 point).
- **Medium Armor (Constable Vest, Cuirass, Hazmat Canvas):** **+0 (Baseline Cost)**.
- **Heavy Armor (Full Heavy Plate Harness):** **+2 Passive Points** (demands massive structural reinforcement).

- **Zero In-Combat Math:** Passive items are calibrated and committed during daily preparation or rest. Once equipped within your Passive Capacity, they provide their benefits continuously and **do not consume or interact with your Active Surge AP in combat**.

### B. Active Surge AP (Actions, Reactions & Discharges)

Active Surge points power offensive discharges, weapon supercharges, chemical spray nozzles, and instantaneous reaction barriers.

- **Calculation:**
  $$\text{Active Surge AP per Round} = \text{Intelligence Modifier} + \text{Class Base AP} + \text{Level Progression Bonus}$$
- **Governing Attribute:** **Intelligence** governs Active Surge for all classes (cognitive calculation, frequency matching, and trigger timing).
- **Combat Round Economy:** Refreshes at the start of each round. Points are spent strictly when using **Actions or Reactions**.

### C. Weapon Operations & Active Surge Costs

NeitherTeck weapons rely entirely on active capacitive induction or sealed chemical reaction mass. **They do not possess a mundane backup mechanism:**

- **Dead Without Power or Fuel:** If a radiant weapon is outside an active power grid (>5× generator distance), or if a cartridge weapon runs out of chemical cartridges, **the weapon is completely dead and inert**. It cannot be fired or swung as a functional weapon (an arc rifle with dead capacitors is dead weight).
- **Inert in Pure Aither:** In pure Aither (above the Zone or in Elven sanctuaries), Neither catalytic capacitors bleed out instantly and **NeitherTeck ceases to function entirely**.
- **The Martial Distinction:** This absolute dependency is what gives non-technical martial classes (**Soldier**, **Brute**, **Scout**, **Pugilist**) their crucial role. When expeditions venture into the unpowered outlands, deep caves, or Aither peaks where high-tech weapons fail, the party must rely on **conventional steel (broadswords, halberds, warhammers), traditional bows and crossbows, or bare fists**.
- **Active AP Cost on Strike & Tag Firing Rate:** When functional, firing or striking with a NeitherTeck weapon requires paying its listed **Active Surge AP cost** on that Action. Trained discipline tags provide a **–1 or –2 AP discount** and **waive Enhancement Tier AP escalation** on matching weapons, ensuring trained operators can maintain their full firing rate (2+ attacks per round) at all levels.
- **Cumbersome Weapon Bracing (Free-Hand Lockout):** High-powered two-handed NeitherTeck weapons (Large Cartridge weapons dealing `2d8–2d10` damage and heavy Radiant longarms/cannons) carry the **Cumbersome** trait. Due to the extreme weight, grounding cables, and capacitor recoil harness, if a character fires or plans to fire a Cumbersome weapon on their turn, **they cannot use any action or activity that requires a free hand for that entire turn (either before or after firing)**. This prevents stacking free-hand brawling maneuvers (Grapple, Trip, *Snagging Strike*) or drawing items on the same turn as firing siege-caliber weapons.

### D. Partial Activation & Multi-Round Accumulation Rule

When a character attempts to activate a NeitherTeck device, apparatus, or weapon whose required AP cost exceeds their per-round Active Surge AP pool (or when they have insufficient AP remaining in the current round):

- **Staged Powering / Priming:** A character may begin charging or priming the device by spending **1 or more Active Surge points** toward its activation cost in a round.
- **Continuous Commitment Condition:** So long as the character spends **all of their available Active Surge points** in each subsequent round toward that same device, the accumulated energy is retained in the device's secondary capacitors.
- **Activation Payoff:** The device **becomes available and triggers on the round in which the total accumulated AP spent equals or exceeds the total activation cost**.
- **Interruption / Dissipation:** If a character fails to commit all available Active Surge points toward the device on a subsequent round (e.g., they spend AP on a different reaction or fail to commit on their turn), the accumulated charge safely bleeds off into the ambient Neither and is lost; priming must restart from 0.
- **Example:** A *Defensive Arc Cannon* requires **5 AP** to operate, and a low-AP character generates only **2 AP per round**.
  - *Round 1:* The character commits **1 AP** (reserving 1 AP for an emergency reaction).
  - *Round 2:* The character commits **2 AP** (all available AP; running total = 3 AP).
  - *Round 3:* The character commits **2 AP** (all available AP; running total = 5 AP).
  - *Outcome:* The *Defensive Arc Cannon* fully charges and fires on **Round 3**.


---

### 3. Equipment Category Tags & Bespoke GM Item Tuning

Items possess standardized tags indicating their manufacturing origin, ergonomic design, and power couplings. When a character wields gear aligned with their trained discipline, they gain operational advantages (such as a **–1 or –2 AP discount** on active surges or reduced passive capacity load):

> [!TIP]
> **The GM's Balancing Lever (Bespoke Hardware & Tag Tuning):**
> Modern D&D 5e and PF2e often suffer from "catalog homogenization," where players simply purchase pre-calculated items from a book, stripping the GM of the classic tool to quietly support struggling players. In Clockwork Cities, **Tags and Custom Hardware are the GM's primary balancing lever**:
> - If a casual or thematic player is falling behind the party's power gamers in tactical effectiveness, the GM can drop an **Uncommon custom-tagged prototype** specifically crafted with their discipline tag (`[Professional]`, `[Airships]`, `[Clandestine]`) or with an **overclocked AP/Passive discount** (e.g., –2 AP instead of –1, or a reduced passive load).
> - Because a power gamer with a mismatched discipline tag gets zero discount from that item, the GM can hand targeted, game-changing power directly to a specific character without triggering an arms race across the rest of the party!

| Tag | Discipline & Typical Equipment | Tactical Flavor & Synergy |
|---|---|---|
| `[Biochemical]` | Chirurgeons, Mad Bombers, Apothecaries | Auto-injectors, catalytic sera, dermal washes, caustic aerosols. Operates independent of electrical broadcast fields. |
| `[Mechanical]` | Clockwork Engineers, Artisans, Siphoners | Spring-wound gears, flywheel dampeners, escapement locks, pneumatic pistons. High physical durability. |
| `[Military]` | Soldiers, Officers, Clockwork Riflemen | Trench breakers, heavy recoil compensators, service bayonets, ballistic linothorax. Built for rugged frontline abuse. |
| `[Airships]` | Sky Captains, Aerial Marines, Riggers | Lightweight alloys, grapple winches, high-altitude breathers, wind-cutting cutlasses. Optimized for Zone buoyancy and boarding actions. |
| `[Professional]` | Inspectors, Scholars, Dandies, Merchants | Concealed derringers, sword canes, forensic diagnostic lenses, bespoke protective silks. Easily passes Spire security checkpoints. |
| `[Technical]` | Clockwork Engineers, Scholars, Artisans | High-draw inductive arquebuses, portable dynamos, resonant grid receivers, complex diagnostic arrays. Demands high technical tuning. |
| `[Clandestine]` | Survivors, Inspectors, Dandies | Hidden compartments, silence baffles, disguised resonators, spring-flick wrist blades, palm-dampened needle guns. Designed to bypass security checkpoints and scanners. |
| `[Subterranean]` | Scouts (Deep Sappers, Tunnelers) | Tremorsense compasses, reinforced mattocks, acoustic cave-in dampeners, low-light flares. |
| `[Outlands]` | Scouts (Outriders), Survivors | Sealed cartridge adapters, dust scrubbers, ruggedized scavenged chassis operable in zero-radiant dead zones. |

---

## 4. Class Progression Tiers (Active Surge AP)

Active Surge points reflect round-by-round cognitive timing, circuit alignment, and escapement pacing. In Clockwork Cities, technology is delicate, resource-hungry, and underperforms compared to high-fantasy magic.

$$\mathbf{\text{Active Surge AP per Round}} = \mathbf{\text{Intelligence Modifier}} + \mathbf{\text{Class Base AP}} + \mathbf{\text{Level Progression Bonus}}$$

| Technical Tier | Base AP (Lv 1) | Progression Scaling | Target Classes & Tactical Role |
|:---:|:---:|:---:|---|
| **Tier 3 (Technical Masters)** | **+2 AP** | **+1 AP at Levels 4, 8, 12, 16, 20** | **Scholar, Clockwork Engineer, Artisan**. Master designers capable of firing multiple energy shots or operating complex apparatuses. |
| **Tier 2 (Technical Specialists)** | **+1 AP** | **+1 AP at Levels 5, 10, 15, 20** | **Inspector, Clockwork Rifleman, Chirurgeon, Mad Bomber**.<br>• *Clockwork Rifleman:* Features **Singular Neither Efficiency**, reducing the AP cost to fire any NeitherTeck ranged weapon by **–1 AP at 1st, –2 AP at 6th, –3 AP at 12th, and –4 AP at 18th level** (minimum 1 AP).<br>• *Chirurgeon & Mad Bomber Autonomy:* Personal class features, quick field vials, medical sera, and infused bombs cost **0 AP** for the creator. |
| **Tier 1 (Tactical Operatives)** | **+0 AP** | **+1 AP at Levels 6, 12, 18** | **Officer, Sky Captain, Survivor, Scout**. Tactical skirmishers relying on signature sidearms and mobility gadgets. |
| **Tier 0 (Dedicated Martials)** | **+0 AP** | **+1 AP at Levels 10, 20** | **Soldier, Brute, Pugilist, Dandy**. Pure martial backbone relying on steel, bows, and brawn. |
| **Influence Category** | **+1 AP** | **+1 AP at Levels 6, 12, 18** | **Merchant** (Commercial directives, mercenary contracts, credit-line triggers). |

### Progression Table (Levels 1–20 Base AP Before INT Modifier)

*Note: Add the character's Intelligence modifier to all values below.*

| Level | Tier 3 (Academics) | Tier 2 (Specialists) | Tier 1 (Tactical) | Tier 0 (Martials) |
|:---:|:---:|:---:|:---:|:---:|
| **1** | **2** | **1** | **0** | **0** |
| **2** | 2 | 1 | 0 | 0 |
| **3** | 2 | 1 | 0 | 0 |
| **4** | **3** | 1 | 0 | 0 |
| **5** | 3 | **2** | 0 | 0 |
| **6** | 3 | 2 | **1** | 0 |
| **7** | 3 | 2 | 1 | 0 |
| **8** | **4** | 2 | 1 | 0 |
| **9** | 4 | 2 | 1 | 0 |
| **10** | 4 | **3** | 1 | **1** |
| **11** | 4 | 3 | 1 | 1 |
| **12** | **5** | 3 | **2** | 1 |
| **13** | 5 | 3 | 2 | 1 |
| **14** | 5 | 3 | 2 | 1 |
| **15** | 5 | **4** | 2 | 1 |
| **16** | **6** | 4 | 2 | 1 |
| **17** | 6 | 4 | 2 | 1 |
| **18** | 6 | 4 | **3** | 1 |
| **19** | 6 | 4 | 3 | 1 |
| **20** | **7** | **5** | 3 | **2** |

### Equipment Costs & Tier Escalation Rules

To prevent untrained characters from spamming high-level energy weaponry like cantrips while ensuring trained specialists can maintain their **full firing rate**, gear costs follow a clear tag-efficiency rule:

1. **Consumables & Combat Injections:** Cost **1 to 2 AP** (e.g., standard stims, flash charges, caustic aerosols).
2. **Base Mundane Weapons (Level 1–4):**
   - **Small Cartridge Pistols & Emitters (1d8 E / 1d10 F, Reload 1):** **3 AP** (drops to **2 AP** with `[Military]`, `[Professional]`, or matching discipline tag).
   - **Medium Cartridge Rifles, Lances & Blunderbusses (1d10–1d12 E/F, Reload 2):** **4 AP** (drops to **3 AP** with matching tag).
   - **Large Cartridge Heavy Arquebuses & Breakers (2d8–2d10 E/F, Reload 3):** **5 AP** (drops to **3 AP** with matching tag).
3. **Enhancement Tier Cost Escalation (Waived by Matching Discipline Tags):**
   - **Trained Tag Efficiency (Full Firing Rate):** When a character wields an enhanced weapon (`+1 Niracrest Striking`, `+2 Mitheral Greater Striking`, or `+3 Major Striking`) that **matches one of their trained Discipline Tags** (or via the Clockwork Rifleman's *Singular Neither Efficiency*), the weapon's precision tuning **waives the enhancement tier AP increase**. It continues to cost its base Tagged AP (**2 AP** for Small Cartridge pistols, **3 AP** for Medium/Large weapons—or **1 AP** for a Clockwork Rifleman), allowing full 2-attack/round firing cadence at all levels!
   - **Untagged / Cross-Discipline Escalation:** When wielded **without** a matching Discipline Tag, enhanced weapons cost **+1 AP per enhancement tier** above base:
     - **Tier 1 (+1 Niracrest / Striking, Lv 4–5):** **+1 AP** untagged (Small: 4 AP; Medium: 5 AP; Large: 6 AP).
     - **Tier 2 (+2 Mitheral / Greater Striking, Lv 10–12):** **+2 AP** untagged (Small: 5 AP; Medium: 6 AP; Large: 7 AP).
     - **Tier 3 (Legendary / Major Striking, Lv 16–18):** **+3 AP** untagged (Small: 6 AP; Medium: 7 AP; Large: 8 AP).

---

## 5. Tactical Asymmetry & Archetype Roles in the Grounded Economy

1. **The Technical Master & Specialist (Scholar, Clockwork Engineer, Artisan, Clockwork Rifleman, Inspector):**
   - **Firing Cadence Benchmarks (Full Firing Rate with Tags):**
     - *Level 1–3:* Can fire a tagged Small Cartridge pistol (`1d8 E` / `1d10 F`, 2 AP) or Medium Cartridge rifle (`1d10 E`, 3 AP) at full firing rate (2 attacks per round while loaded, or 1–2 attacks with reload/support actions).
     - *Level 4–20:* Because matching Discipline Tags waive the Enhancement Tier AP tax, trained characters maintain their **full 2-shot/round firing cadence** with `+1 Striking` and `+2 Greater Striking` Cartridge Weapons, restricted only by Cartridge Reload actions (**Reload 1** Small, **Reload 2** Medium, **Reload 3** Large) and finite cartridge logistics.
   - **The Multi-Attack Penalty (MAP) & Grind Limitation:** While Cartridge Weapons deal superior per-shot damage at full standard firearm ranges (`30–150 ft`), they are strictly balanced by **ammunition scarcity across the 70% attrition grind** and multi-action reload windows on Medium/Large cells.

2. **The Dedicated Martial (Soldier, Brute, Pugilist, Scout):**
   - **Firing Cadence Benchmarks:**
     - *Levels 1–9 (+0 INT, 2 AP floor with minimal stat/prep):* Can fire a tagged pistol (2 AP) **once per turn**, spending their other 2 actions moving, raising a shield, or striking with masterwork steel or bows (0 AP).
     - *Level 10+ (+0 INT, 3–4 AP):* Can fire a tagged pistol **twice** ($2 \times 2 = 4\text{ AP}$) or a Medium/Large Cartridge weapon once (3 AP).
   - **Why Martials Still Dominate Head-to-Head Fights (Even Against Boosted Cartridge Weapons):**
     - **Superior HP & Trauma Thresholds:** Martials have **10 to 12 HP per level** (plus higher Constitution) vs. **6 to 8 HP per level** for Technical/Influence classes. Under the 3-Step Wound System (`[Healing.md]`), a Martial's **Regular Damage buffer and Critical/Mortal step size ($\lfloor \text{Max HP}/4 \rfloor$) are 35% to 60% larger**, meaning a Technical gunner drops into debilitating Critical Wounds and hits their Trauma Ceiling far earlier in a shootout.
     - **Higher AC & Saves:** Martials wear **Medium and Heavy Armor** (`+1` to `+2` higher baseline AC, scaling to **Expert/Master armor proficiency** earlier) and carry **Shields** (*Raise a Shield* for `+2 AC` + *Shield Block* damage reduction). That `+2` to `+4` effective AC swing directly shuts down the `Fatal d12` / `Fatal d12+4` critical hits that Cartridge Weapons rely on for spike damage.
     - **Superior Weapon Proficiency & Action-Compression Combat Feats:** Dedicated Martials scale to **Expert/Master/Legendary weapon proficiency (+2 to hit and crit)** and gain **premier combat feats** (*Point-Blank Stance*, *Double Shot*, *Triple Shot*, *Reactive Strike*, *Sudden Charge*, *Snagging Strike*, *Running Reload*, *Intimidating Strike*). While a Technical class spends raw actions firing and 2–3 actions manually reloading Medium/Large cartridges, a Martial compresses actions, disrupts reloads with *Reactive Strike*, and lands crits on a lower die roll.
     - **Result:** Boosted Cartridge Weapons let a Technical specialist or Rifleman contribute meaningful, exciting firepower while their cartridges hold out—without ever dethroning the Dedicated Martial in a stand-up fight.

3. **High Society & Disarmed Wards (Dandies & Pugilists):**
   - In elite Spire districts where carrying military energy weapons is illegal and peace-bonding is enforced, high-AP weaponry cannot be brought through checkpoints. Dandies and Pugilists dominate with concealed canes, fisticuffs, and dueling finesse without needing any external power grid.
