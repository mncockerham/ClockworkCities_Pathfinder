# Clockwork Cities — Healing & Wound Thresholds
Status: **Draft**. Base rules: Rest & Recovery [Player Core p.427], Treat Wounds [Player Core p.240]. Precedence per 00_RulesFoundation.md.

## Core Principle — Replaced
Hit Points represent three distinct tiers of trauma rather than an undifferentiated pool. Superficial cuts, fatigue, and bruises heal quickly, while deep systemic trauma (Critical and Mortal wounds) requires extended real-world recuperation time.

---

## 1. Hit Point Categories & Thresholds
A character's maximum Hit Points are divided using a calculated **Step Size**:

$$\text{Step} = \left\lfloor \frac{\text{Total Hit Points}}{4} \right\rfloor$$

| Tier | Category | HP Range (from 0) | Natural Healing Rate | Penalties (when Damage depleted) | Allowed Healing Sources |
|---|---|---|---|---|---|
| **Step 1** | **Mortal Wounds** | $1 \text{ to } \text{Step}$ | **Weeks** of bed rest | **Major penalties** | Long-term natural recovery / specialized clinical care |
| **Step 2** | **Critical Wounds** | $(\text{Step} + 1) \text{ to } (2 \times \text{Step})$ | **Days** of rest | **Minor penalties** | Days-scale rest and medical recuperation |
| **Remaining** | **Damage** (Regular) | $(2 \times \text{Step} + 1) \text{ to } \text{Max HP}$ | **Normal PF rules** (hours/rest) | None | Normal PF resting, Treat Wounds, Concoctions, Tech |

> *Example*: A character with 42 total HP has a Step size of $\lfloor 42 / 4 \rfloor = 10$.
> - **Mortal Wounds (Step 1)**: HP 1–10 (10 HP band) &mdash; major penalties
> - **Critical Wounds (Step 2)**: HP 11–20 (10 HP band) &mdash; minor penalties
> - **Damage (Remaining)**: HP 21–42 (22 HP band) &mdash; no penalties

---

## 2. Technology & Concoction Limits
- **Damage Only**: Concoctions (biomedical tonics, stims) and Clockwork Technology (cellular repair gizmos, suture mechanisms) **can only restore regular Damage**.
- **No Instant Surgery**: Technology and concoctions cannot instantly knit ruptured organs or re-anchor shattered bones represented by Critical or Mortal wounds.

---

## 3. Healing Order & Progression
- **Hierarchical Recovery**: As a general rule, healing progresses from the deepest trauma upward. The earlier levels must be healed before later damage can be recovered:
  1. **Mortal Wounds (Step 1)** heal first (measured in weeks).
  2. Once Mortal Wounds are fully cleared, **Critical Wounds (Step 2)** heal (measured in days).
  3. Once Critical Wounds are resolved, remaining **Damage** heals per standard Pathfinder rules (Treat Wounds, overnight rest).

### Regular Damage & The Trauma Ceiling ($\text{Level} + \text{CON}$)
- **Standard PF2e Healing:** Regular Damage heals per standard PF2e rules (Treat Wounds, rest, tonics, tech devices).
- **The Trauma Ceiling:** If a character has **any unhealed Critical or Mortal wounds**, their maximum Regular Damage pool is capped at:
  $$\text{Max Regular HP} = \text{Level} + \text{CON modifier} \quad (\text{min } 1)$$
  Healing beyond this ceiling is lost until deeper wounds are resolved.

### Clinical Recuperation & Medical Care Rates
- **Critical Wounds:** Heals at **$\lfloor \frac{1}{5} \text{Level} \rfloor + \text{CON}$ / day** (bed rest) or **$\text{CON}$ / day** (with skilled medical attention). **1 full day** of skilled clinical care restores all regular Damage HP.
- **Mortal Wounds:** Heals at **$\lfloor \frac{1}{5} \text{Level} \rfloor + \text{CON}$ / week** (bed rest) or **$\text{CON}$ / week** (with skilled medical attention). **1 full week** of skilled clinical care restores all regular Damage HP.

---

## 4. Anatomical Trauma & Wound Consequences
When an attack enters Critical or Mortal wound tiers, the player/GM determines an anatomical consequence based on damage type and hit location (d8 table in `Healing.md`):
- **Critical Tier:** Standard PF2e conditions (*Clumsy 1*, *Enfeebled 1*, *Stupefied 1*, Speed –5 ft).
- **Mortal Tier:** Severe conditions (*Clumsy 2*, *Enfeebled 2*, *Drained 2*, *Stupefied 2*, Speed –10 ft) and direct attribute modifier penalties (e.g., –2 Str, –3 Dex for broken leg; –2 Con for gut rupture; –2 Int/Wis for cranial trauma).
- **Duration:** Penalties persist until the underlying wound tier is healed. When rising from Mortal to Critical, direct stat damage converts down to Critical condition values.

## 5. Lethal vs. Nonlethal Damage, Negative HP & Death
- **Two Trackers:** **Total Damage** and **Nonlethal Damage** ($\text{Lethal} = \text{Total} - \text{Nonlethal}$).
- **Damage Priority:** Lethal damage is **always applied against HP tiers first** (regardless of order taken), with nonlethal placed on top. Lethal trauma fills Regular Damage before dipping into deeper tiers.
- **Fast Nonlethal Recovery:** Outside of combat, nonlethal damage heals naturally at **1 point per minute** across all levels.
- **Reaching 0 HP:** When Total Damage reduces HP to 0:
  - **Unconscious (Nonlethal Cushion):** If negative lethal damage $\le$ Nonlethal Damage, the creature is Unconscious and stable (no bleed).
  - **Dying / Bleed Clock:** Starts only when negative lethal damage matches and exceeds total Nonlethal Damage ($\text{Net Negative Lethal} > 0$).
- **Bleed-Out Deterioration Clock:**
  - **Stage 1 (1 to $\text{Step}$ / Critical capacity):** Takes **1 damage per hour**.
  - **Stage 2 ($\text{Step} + 1$ to $2 \times \text{Step}$):** Takes **1 damage per minute**.
- **Permanent Biological Death:** Occurs when Net Negative Lethal damage equals Critical + Mortal capacity:
  $$\text{Death} \ge 2 \times \text{Step}$$
  No resurrection magic exists in the setting.
- **Massive Damage:** Single lethal strike exceeding Max HP causes instant death.

---

## Open Questions
- Exact condition tags and values for minor penalties (Step 2) and major penalties (Step 1).
- Nonlethal recovery mechanics (e.g. rate of recovery per 10-minute rest or Treat Wounds).
- Actions/DCs to stabilize bleeding in negative HP (e.g., Medicine Administer First Aid vs. Chirurgeon serums).
- **Environmental Exposure Interaction (Resolved in `TheNeither.md`):** Natural healing of regular HP and wound tiers is modulated by Total Shift Score (0–1.5: 100%; 2–3.5: 50%; 4–5: 25%; 5.5–6: 0 healing + 1d8/day damage; 6.5+: 0 healing + 3d8/day damage). Convalescence requires a 7-day stabilization period followed by 1 point healed per week of clean living.
- Long-term Medicine skill checks (e.g., expanded Treat Condition / long-term care) to reduce recovery time from weeks/days.
