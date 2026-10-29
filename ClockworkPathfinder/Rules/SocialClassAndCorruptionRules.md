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
- **Class Fluidity vs. Influence Class Status Dependency:**
  - Most classes (Soldiers, Brutes, Scouts, Pugilists, Alchemists) can easily shift across social classes without affecting their combat effectiveness, directives, or class features outside standard social reaction penalties.
  - **The Noble & Merchant 3/4 Connection Loss Rule:** By contrast, the **Noble** and **Merchant** classes rely intrinsically on institutional legitimacy:
    - **Nobles** must maintain **Noble Status (Status 5+)**. If stripped of rank, disowned, or exiled, they retain directives and combat feats, but **immediately lose 3/4 (75%) of all primary domain high-society connections, patrons, and council favors**. The **player chooses which 1/4 (25%) remains loyal**.
    - **Merchants** must maintain **Merchant Status (Status 3+)**. If bankrupted, defaulted, or blacklisted by the guilds, they retain directives and skills, but **immediately lose 3/4 (75%) of all primary domain commercial connections, trade credit, and guild favors**. The **player chooses which 1/4 (25%) remains loyal**.
- **Social Friction:** Characters interacting with social strata significantly above or below their own suffer circumstance penalties to social skill checks (Diplomacy, Deception, Intimidation) proportional to the gap, unless introduced by a recognized patron.

### Institutional Legacy & Lineage Succession (Mitigating the Cost of Character Death)
In a setting where 15% of encounters are lethal Boss Crucibles and 70% are grinding attrition fights, character death is an inevitable, looming reality. To ensure players do not lose the institutional and political progress they have spent months advancing, Clockwork Cities features the **Lineage Succession System**:
- **The Core Premise:** *"Individuals die; the House, the Guild, and the Regiment endure."*
- **Encouraged (But Not Mandatory) House/Guild Continuity:**
  - When a character dies, the player is **strongly encouraged (though never forced)** to create their next character within the same **Family House, Trade Guild, Military Regiment, or Syndicate**.
  - *Example:* If an Artisan smith dies in the deep Zone, their replacement might be their ambitious journeyman apprentice, an older brother serving as an engineer in the same guild, or a cousin from a branch workshop sent to settle the estate.
- **What Is Preserved (The Inherited Legacy):**
  - **Faction Standing & Favors:** The new character inherits the deceased character's accumulated **Standing (-99 to +99)** and institutional trust within that sponsor, modified by a minor "re-proving" tax (starting at the old Standing –10, minimum 0).
  - **Permanent Institutional Wealth:** Housing rights, laboratory access, workshop benches, carriage allotments, and guild credit lines remain fully intact and immediately transfer to the successor.
  - **The Transitory Hoard Rule:** The deceased character's **House-issued gear** (chassis, military rifles, armor) is officially reclaimed by the sponsor and re-issued to the successor without cost. Only personal transitory pocket cash and unbonded street gear are lost or left with the corpse.
  - **Contact & Understanding Hand-off:** The successor automatically inherits up to **half (rounded down)** of the deceased character's specific social contacts and Focus Understandings, representing family diaries, shared workshop ledgers, or briefing notes passed through the institution.
- **Freedom to Pivot:** If the player chooses *not* to continue the lineage and instead rolls an entirely new character from a different social tier (e.g., abandoning the Machinists' Guild to play a Warrens Survivor or an outland Scout), they start fresh at standard party level and baseline wealth for that new social tier, while their previous house remains in the world as potential allies or rivals.

---

## 2. Wealth, Player Resources & Currency

> [!IMPORTANT]
> **Money & Resource Rules Relocated:**
> All mechanics for **Permanent vs. Transitory Wealth**, the **Five Player Resource Categories** (*Monthly Spending Allowance*, *Personal Property Cap*, *Requisitioned Organizational Equipment*, *Retainer Budget*, and *The Citizen Bulwark*), and the **Industrial Hard-Alloy Currency System** (`Pin` through `Sovereign`) have been moved to the dedicated resource module: [`ResourcesAndWealth.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/Rules/ResourcesAndWealth.md).

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

