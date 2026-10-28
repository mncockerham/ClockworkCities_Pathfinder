# Social Class, Wealth & Neither Exposure Rules

- **Topic:** Game Mechanics for Social Status, Permanent vs. Transitory Wealth, Currency, and Neither Corruption / Environmental Exposure
- **Status:** **Draft (Mechanics with TBD Conversion Sections)**
- **Authoritative Reference:** `AISummary/WorldSummary.md`

---

## 1. Social Class & Status Ladder

In Clockwork Cities, social class is not merely flavor—it dictates a character's legal protections, baseline gear, access to restricted wards, and NPC reactions.

### Status Tiers & Standing

Social standing is tracked on a numeric tier scale (-1 to 9), with a character's internal faction reputation represented by **Standing (-99 to +99)** within their sponsoring institution:

| Status Tier | Social Category | Typical Social Roles | Voting Weight | Lifestyle / Housing Guarantee |
|:---:|---|---|:---:|---|
| **–1 to 0** | **Outcasts & Warrens** | Indentured debtors, fungal farmhands, alley fixers, goblins | 0 | Unsanitary squats, raw fungal broth |
| **1 to 3** | **Free Citizens & Laborers** | Foundry workers, quarrymen, junior clerks, day-laborers | 1/10 | Tenement flats in Lower/Mid Worker Wards |
| **2 to 5** | **Guild Members & Artisans** | Blacksmiths, tanners, masons, machinists, guild factors | 1/2 | Guild hall lodgings or private Ward 11 flats |
| **2 to 5** | **Military & Constabulary** | Enlisted regulars (2), sergeants (3), commissioned officers (4–5) | 1/10 to 1 | Barracks quarters or subsidized military housing |
| **4 to 6** | **Academia & University** | Graduate fellows (4), tenured professors (5), college deans (6) | 1 (BA+) | Faculty apartments in University Ward |
| **3 to 8** | **Merchant Houses** | Shopkeepers (3), house scions (4–6), Wall Merchants (8) | 1 | Luxury estates in Wards 13 & 14 |
| **5 to 9** | **Nobility & Great Houses** | Country estate nobility (5), city nobles (7), 25 Great Houses (9) | Direct Petition | Private manicured manors in Noble & Royal Wards |

### Status Mechanics & Upkeep
- **Lifestyle Upkeep:** Characters must expend wealth commensurate with their status tier each month. Failing to maintain appearances causes a loss of status tier or standing within their house/guild.
- **Institutional Backing:** If an artisan leaves their guild, a soldier deserts, or a merchant house goes bankrupt, their status immediately drops to Citizen (Status 1) or Indentured (Status –1).
- **Social Friction:** Characters interacting with social strata significantly above or below their own suffer circumstance penalties to social skill checks (Diplomacy, Deception, Intimidation) proportional to the gap, unless introduced by a recognized patron.

---

## 2. Wealth System: Permanent vs. Transitory Wealth

Because personal cash is secondary to institutional credit, wealth is partitioned into two distinct systems:

### 1. Permanent Wealth (Institutional Backing)
Permanent wealth represents the resources provided by your sponsor (Family House, Trade Guild, Crown Regiment, or University):
- **Guaranteed Necessities:** Provides room, board, professional workrooms, standard daily rations, uniforms/clothing appropriate to your station, and trade tools without spending coin.
- **Credit Lines & Requisition:** High-status characters can requisition specialized equipment, carriages, guards, or laboratory facilities through formal bureaucratic requests rather than paying out of pocket.
- **Durable vs. Fragile Wealth:**
  - *Noble Wealth:* Durable, anchored in land grants, mines, and Crown patents. If a noble estate burns down, the Crown helps rebuild.
  - *Merchant Wealth:* Liquid and fragile, anchored in airship cargoes, bills of exchange, and warehouse goods. A lost convoy can bankrupt a merchant house overnight.

### 2. Transitory Wealth (Personal Cash & Gear Limits)
Transitory wealth represents the physical coinage, pocket cash, and unbonded gear carried by the character:
- **Max Liquid Cash (The Hoard Ceiling):** The maximum physical coin a character can carry or squirrel away before their institution notices. True "off-the-books laundering" does not exist in the Spire: your Family, Guild, or Military unit knows exactly what you should earn and own. Anything not claimed by your group cannot be safely stored—you cannot own private secure vaults, and no constable or court will investigate theft of coin that legally cannot exist (and admitting you had it risks immediate expulsion or criminal charges). Consequently, illicit or surplus coin cannot be hoarded permanently; characters inevitably burn it on fleeting luxuries, illicit entertainment, fine dining, or bribes—expending resources that never yield durable long-term wealth.
- **Personal Wealth vs. House Assortment:**
  - *Personal Wealth:* Items, garments, and sidearms you own outright and keep even if discharged from your house or guild.
  - *House Assortment:* High-tier gear, masterwork armor, arc weaponry, industrial vehicles, or airships issued by your sponsor. These items remain property of the House/Crown and are immediately repossessed if your Standing drops or you leave your post.
- **Item Wear & Fragility [TBD]:** Neither-tech devices and experimental firearms undergo rapid wear. Precision mechanisms operating under high stress suffer durability loss on critical failures (such as a natural 1 on an attack or a jammed cartridge), requiring maintenance by an Artisan or Clockwork Engineer to prevent permanent breakdown.

### Currency System (Decimal Standard)

Coinage in Arclean is strictly decimalized, based on standard stamped denominations:

| Coin | Abbreviation | Relative Value | Composition / Common Usage |
|---|:---:|:---:|---|
| **Pin** | P | 1 P | Copper pin; cost of a bowl of raw fungal stew or a newspaper |
| **Bit** | B | 10 P | Stamped brass token; cost of basic street transit or a loaf of Mela bread |
| **Crown** | CR | 10 B (100 P) | Standard silver-plated coin; daily laborer wage, tavern meal & pint |
| **Imperial** | I | 10 CR (1,000 P) | Solid silver coin; standard trade unit for durable goods, boots, tools |
| **Silver Imperial** | S | 10 I (10,000 P) | Heavy hallmarked silver; bulk trade, fine tailored suits, weapons |
| **Gold Imperial** | G | 10 S (100,000 P) | Pure refined gold; property leases, airship passage, luxury jewelry |
| **Silver Bar** | SB | 10 G | Heavy mint bar (equal to 110 Silver Imperials in metal weight) |
| **Gold Bar** | GB | 10 SB | Standard reserve bullion held in central bank vaults |

---

---

## 3. Atmospheric Exposure & Neither Corruption

> [!IMPORTANT]
> **Core Neither Mechanics Relocated:**
> For full rules on atmospheric layers, the 6-strata air distance matrix, dietary shift half-points, combined Total Shift Scores, and the temporal combustion surge cycle, see the dedicated reference module: [TheNeither.md](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Rules/TheNeither.md).

### Quick Reference: Total Shift Score (Air + Food)
- **Air Shift Levels:** Integer steps (0 to 5) determined by biological distance from your Heritage's native layer.
- **Food Shift Levels:** 0.5-point increments based on diet (e.g. 50% Mela + 50% raw Sycelium = 0.5 Shift).
- **Combined Penalty Track:**
  - **Score 0.0:** Equilibrium (normal healing/rest).
  - **Score 0.5–1.0:** Mild Imbalance (rest healing takes 50% longer, –1 Fortitude vs. disease).
  - **Score 1.5–2.0:** Chronic Degradation (*Clumsy 1* or *Enfeebled 1*, resting HP recovery halved).
  - **Score 2.5–3.0:** Severe Cellular Stress (*Clumsy 1*, *Enfeebled 1*, *Stupefied 1*).
  - **Score 3.5–4.0:** Acute Breakdown (*Drained 1*, *Stupefied 2*, weekly Fortitude save vs. *Acute Neither Sickness*).
  - **Score 4.5+:** Systemic Failure / Mutation (*Drained 2*, *Doomed 1*; 3 months = Aberrant Speciation into Goblins, Neanderthals, or Troglodytes).

### Environmental Mitigations
- **Architecture:** Standard Neithercrete rooms reduce effective Air Shift by **1 Level**; hermetic deep vaults reduce by **2 Levels**.
- **Sealed Respirators:** Oiled leather filters reduce effective Air Shift by **1 Level** for up to 8 hours.
- **Storm Depth:** Mine depth reduces Neither Storm intensity by **1 Level per 100 feet** (at 300+ feet, storm damage is completely negated).

