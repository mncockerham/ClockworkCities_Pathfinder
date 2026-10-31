# Active Priority Queue

## 1. NeitherTeck Striking Rune AP Drain vs. Martial Scaling
- **Problem:** Martials gain `Weapon Mastery` at Level 5 (+2 hit, critical specialization) while maintaining 0 Base AP. If fundamental weapon runes add +1 AP per tier (Striking = +1 AP, Greater Striking = +2 AP), martials are completely priced out of firing enhanced NeitherTeck weapons, while Technical classes take disproportionate turn-resource penalties.
- **Task:** Calibrate whether higher-tier materials/capacitors (Niracrest, Mitheral) absorb the extra AP drain, or if fundamental weapon runes increase damage without increasing action AP cost.

## 2. Low-Level Trauma Ceiling Floor [RESOLVED]
- **Resolution:** Simplified step sizing and low-level threshold rules in `AISummary/20_Healing.md`:
  - $\text{Total HP} \le 16 \implies \text{Mortal} = 3\text{ HP (1–3)}, \text{Critical} = 3\text{ HP (4–6)}, \text{Regular} = 7 \text{ to Max HP}$. (At 16 HP, 10 regular HP).
  - $\text{Total HP} \ge 17 \implies \text{Step} = \lfloor \text{Total HP} / 4 \rfloor$. (At 17 HP: 4 Mortal, 4 Critical, 9 regular HP).
  - First wound condition trigger starts at **1 point** of wound damage (applied post-combat per adrenaline buffer). Field facility care restores full Regular HP.
