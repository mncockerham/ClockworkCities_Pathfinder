# Clockwork Cities Character Benchmarks & Test Index (2026-10-30)

This directory contains the fully updated character benchmark suite implementing all core rules codified through October 30, 2026:
1. **The 10-Point Edge System (`edges.md`):** Complete 10-point character creation budget, Status 0–6 entry costs, the +1 retainer surcharge for Wall Merchants / Great Nobles, single-purchase limits, and non-stacking proficiency upgrades.
2. **Proficiency Upgrades:** 3-point armor/weapon step-ups (capping at Expert) and 5-point mastery upgrades (capping at Master for native Experts).
3. **Citizen Bulwark Slots:** 3 player-chosen personal items (weapons, armor, tools, badges) legally shielded from municipal confiscation.
4. **Radiant & Action Point (AP) Economy:** Class Tier active AP bases, Level 5 scaling, Battery Surge feats, and disciplined tag discounts.
5. **Wound & Trauma Bands:** Explicit Mortal ($\lfloor \text{HP}/4 \rfloor$) and Critical ($\lfloor \text{HP}/2 \rfloor$) step thresholds on all stat blocks.
6. **Commercial Gear & Weapons:** Adheres to the Fair Steel Mandate (rapiers in Spire wards), shield reload penalties on cartridge firearms, and Cumbersome traits.

---

## 1. The 6 PC Functional Categories & Representative Builds

| File | Character & Ancestry | Class & Role | Status Tier | Edge Allocation (10 Pts) | Lv 1 HP / AC / AP | Lv 5 HP / AC / AP | Citizen Bulwark Slots |
|---|---|---|:---:|---|:---:|:---:|---|
| [`01_PC_Pugilist_Lv1_Lv5.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/testing/CharacterExamples20261030/01_PC_Pugilist_Lv1_Lv5.md) | **Marcus "Ironjaw" Flint** (Human) | **Pugilist** (Cat 1: Civil Spire Master) | Status 0 (Warrens Outcast) | 3 pt Light Armor, 2 pt Hardened Frame, 2 pt Iron-Gut, 2 pt Neither Lungs, 1 pt Workhorse Bulk | **21 HP** / AC 16 / 5 AP | **73 HP** / AC 22 / 8 AP | Brass Knuckles, Reinforced Tunic, Pit-Fighter Token |
| [`02_PC_ClockworkEngineer_Lv1_Lv5.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/testing/CharacterExamples20261030/02_PC_ClockworkEngineer_Lv1_Lv5.md) | **Theron Vane** (Human) | **Clockwork Engineer** (Cat 2: High Radiant) | Status 2 (Guild Artisan) | 2 pt Status 2, 3 pt Med Armor, 3 pt AP Battery Surge (+2 AP), 2 pt Jury-Rigger | **18 HP** / AC 15 / 7 AP | **58 HP** / AC 21 / 9 AP | Arc Spanner, Armored Coat, Guild Seal |
| [`03_PC_ClockworkRifleman_Lv1_Lv5.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/testing/CharacterExamples20261030/03_PC_ClockworkRifleman_Lv1_Lv5.md) | **Sgt. Donald Kroll** (Half-Elf) | **Clockwork Rifleman** (Cat 3: Low Radiant) | Status 2 (Military Regular) | 2 pt Status 2, 3 pt AP Battery Surge, 3 pt Zone Static Attunement, 2 pt Rigging Reflexes | **19 HP** / AC 16 / 3 AP | **63 HP** / AC 23 / 6 AP | Service Rifle, Serge Coat, Service Medallion |
| [`04_PC_Scout_Lv1_Lv5.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/testing/CharacterExamples20261030/04_PC_Scout_Lv1_Lv5.md) | **Rowan Thorne** (Orc) | **Scout** (Cat 4: The Neither / Outland) | Status 1 (Free Outrider) | 1 pt Status 1, 3 pt Heavy Armor, 2 pt Neither Lungs, 2 pt Iron-Gut, 2 pt Workhorse Bulk | **20 HP** / AC 17 / 4 AP | **68 HP** / AC 22 / 6 AP | Composite Bow, Hunting Parka, Harvester Seal |
| [`05_PC_Soldier_Lv1_Lv5.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/testing/CharacterExamples20261030/05_PC_Soldier_Lv1_Lv5.md) | **Corbin Hall** (Dwarf) | **Soldier** (Cat 5: Broad Generalist) | Status 2 (Military Regular) | 2 pt Status 2, 5 pt Master Broadsword (Native Expert $\to$ Master), 2 pt Stone Anchor, 1 pt Workhorse Bulk | **21 HP** / AC 18 / 4 AP | **73 HP** / AC 24 / 6 AP | Broadsword, Half-Plate, Military Dogtags |
| [`06_PC_Merchant_Lv1_Lv5.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/testing/CharacterExamples20261030/06_PC_Merchant_Lv1_Lv5.md) | **Aldous Sterling** (Human) | **Merchant** (Cat 6: Influence Class) | Status 6 (Wall Merchant) | 7 pt Status 6 (Base 6 + 1 Retainers), 3 pt Martial Weapons (Expert Rapier) | **17 HP** / AC 15 / 4 AP | **53 HP** / AC 21 / 6 AP | Dueling Rapier, Velvet Coat, Merchant Seal |

---

## 2. Standard NPC Classes (5 Archetypes at Level 1 & Level 5)

| NPC Class | In-World Role | Lv 1 HP / AC / Saves | Lv 5 HP / AC / Saves | Key Abilities & Citizen Bulwarks |
|---|---|:---:|:---:|---|
| [`07_NPC_Laborer_Lv1_Lv5.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/testing/CharacterExamples20261030/07_NPC_Laborer_Lv1_Lv5.md) | **Laborer** (Foundry Stoker / Hauler) | 19 HP / AC 14 / Fort +8 | 63 HP / AC 18 / Fort +13 | Heavy Hauler (STR 18 Bulk), Improvised Tools 1d6 B, Union Call (+1 Will). Bulwarks: Sledge, Canvas Apron, Union Token. |
| [`08_NPC_Professional_Lv1_Lv5.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/testing/CharacterExamples20261030/08_NPC_Professional_Lv1_Lv5.md) | **Professional** (Barrister / Auditor) | 15 HP / AC 14 / Will +7 | 43 HP / AC 18 / Will +14 | Institutional Lore Mastery, Bureaucratic Shield, Courtroom Authority. Bulwarks: Walking Cane, Tailored Suit, Legal Briefcase. |
| [`09_NPC_Commoner_Lv1_Lv5.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/testing/CharacterExamples20261030/09_NPC_Commoner_Lv1_Lv5.md) | **Commoner** (Tavern Host / Shopkeeper) | 16 HP / AC 14 / Will +7 | 48 HP / AC 18 / Will +14 | Ward Rumor Network, Behind-Counter Greater Cover (+4 AC), Call the Watch. Bulwarks: Bung-Starter, Linen Apron, Ward Whistle. |
| [`10_NPC_Craftsman_Lv1_Lv5.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/testing/CharacterExamples20261030/10_NPC_Craftsman_Lv1_Lv5.md) | **Craftsman** (Blacksmith / Armorer) | 18 HP / AC 15 / Fort +7 | 58 HP / AC 19 / Fort +12 | Workshop Maintenance (10-min repair), Fire Resistance, Object Hardness Bypass. Bulwarks: Ball-Peen Hammer, Cowhide Apron, Guild Signet. |
| [`11_NPC_Noble_Lv1_Lv5.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/testing/CharacterExamples20261030/11_NPC_Noble_Lv1_Lv5.md) | **Noble Civilian** (Heir / Dilettante) | 15 HP / AC 15 / Will +6 | 43 HP / AC 20 / Will +13 | Hereditary Privilege (Immune to summary arrest), Retinue Call, Fair Steel Mandate. Bulwarks: Dueling Rapier, Silk Coat, Signet Watch. |

---

## 3. Civilian-Template Level 5 PCs

Detailed comparative sheet showing the 6 Level 5 PC builds adjusted with the **Civilian Background / Protected Status Template** (incorporating everyday trade skills, social standing modifiers, and adjusted resilience):
- Located at: [`12_Civilian_PCs_Level5.md`](file:///c:/Users/mncoc/OneDrive/Documents/Git/ClockworkCities_Pathfinder/ClockworkPathfinder/testing/CharacterExamples20261030/12_Civilian_PCs_Level5.md)

