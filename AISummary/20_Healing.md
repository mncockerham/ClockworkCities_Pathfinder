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

### PC Exception (Heroic Reserve)
- **PCs can always heal up to their character level in regular Damage**, regardless of how many Mortal or Critical wounds remain unhealed.
- This allows active player characters to apply field dressings, inject emergency stimulants, or use clockwork devices to gain an operational cushion of HP (equal to their level) to keep moving and fighting despite carrying debilitating long-term injuries.

---

## 4. Wound Penalties
When a character's regular Damage Hit Points are entirely depleted and damage cuts into deeper wound tiers, they suffer functional impairment:
- **Step 2 (Critical Wounds)**: The character suffers **minor penalties** (e.g., status penalties to checks, DCs, or Speed; minor conditions like Clumsy 1 / Enfeebled 1).
- **Step 1 (Mortal Wounds)**: The character suffers **major penalties / trauma** (e.g., severe condition values, halved Speed, severe physical impairment).

---

## Open Questions
- Exact condition tags and values for minor penalties (Step 2) and major penalties (Step 1).
- Exact interaction with the **Dying** and **Wounded** conditions [Player Core p.411] when dropping to 0 HP from Mortal Wounds.
- **Environmental Exposure Interaction (Resolved in `TheNeither.md`):** Natural healing of regular HP and wound tiers is modulated by Total Shift Score (0–1.5: 100%; 2–3.5: 50%; 4–5: 25%; 5.5–6: 0 healing + 1d8/day damage; 6.5+: 0 healing + 3d8/day damage). Convalescence requires a 7-day stabilization period followed by 1 point healed per week of clean living.
- Long-term Medicine skill checks (e.g., expanded Treat Condition / long-term care) to reduce recovery time from weeks/days.
