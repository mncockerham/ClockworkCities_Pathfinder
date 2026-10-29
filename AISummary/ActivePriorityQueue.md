# Active Priority Queue

## 1. NeitherTeck Striking Rune AP Drain vs. Martial Scaling
- **Problem:** Martials gain `Weapon Mastery` at Level 5 (+2 hit, critical specialization) while maintaining 0 Base AP. If fundamental weapon runes add +1 AP per tier (Striking = +1 AP, Greater Striking = +2 AP), martials are completely priced out of firing enhanced NeitherTeck weapons, while Technical classes take disproportionate turn-resource penalties.
- **Task:** Calibrate whether higher-tier materials/capacitors (Niracrest, Mitheral) absorb the extra AP drain, or if fundamental weapon runes increase damage without increasing action AP cost.

## 2. Low-Level Trauma Ceiling Floor
- **Problem:** The trauma ceiling for Regular Damage while suffering Critical or Mortal wounds is $\text{Level} + \text{CON mod}$. At Level 1 with CON +2, maximum regular HP is capped at 3 HP. A single 4-damage hit immediately forces characters back into Critical trauma, causing perpetual wound loops at levels 1–3.
- **Task:** Establish a minimum baseline floor for the trauma ceiling (e.g., $\max(\text{Level} + \text{CON}, 5)$) so low-level PCs can function without being trapped in continuous systemic trauma.
