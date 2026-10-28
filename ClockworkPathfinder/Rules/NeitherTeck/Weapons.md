# NeitherTeck & Clockwork Weapons — Cartridge & Radiant Emitters

- **Base System:** Pathfinder 2e Remaster `[Guns & Gears p.150–154]`
- **Location:** `ClockworkPathfinder/Rules/NeitherTeck/Weapons.md`
- **Precedence:** Rules in `AISummary/00_RulesFoundation.md`, `AISummary/10_Magic.md`, and `ClockworkPathfinder/Rules/NeitherTeck/NeitherTeckRules.md`.

---

## 1. Overview of Weapon Categories

NeitherTeck weapons fall into **two distinct mechanical families**:

1. **Cartridge / Charged Weapons (Self-Powered & Universally Functional):**
   - **The Baseline Emitter:** These are the weaker of the two families.
   - **Internal Power Source:** They carry their own contained energy in batteries or pressurized chemical cartridges.
   - **Universal Neither Utility:** Because they carry their own fuel/reaction mass, they **can operate anywhere within the Neither or Zone**, including deep outlands, wild caverns, and ruins completely detached from municipal power grids.
   - **Throughput Cost:** Cost **2 to 3 AP** per Strike based on damage output.

2. **Radiant Power Weapons (Generator-Coupled / Induction Grid):**
   - **Generator Requirement:** These weapons possess no internal battery and require an active external generator broadcasting wireless inductive energy through the Neither to charge the weapon's capacitors.
   - **Spire Converter Module Mandate & Regulation:** Within Spires, radiant weapons are **legally mandated to incorporate a detachable Converter Module** to interface with and harness the ambient radiant grid. Without this module, induction coupling is broken and the weapon is inert. Converter modules are **regulated identically to military cartridges** (banned from interior wards without King's Rite or emergency orders, locked in guardhouses, and checked out via gate depots).
   - **Grid Bleed vs. Dynamic Frequency Shifting:**
     - *Illicit Low-Power Converters:* Because radiant energy bleeds heavily through urban spires from streetlights and transit machinery, bootleg converter modules are easy to assemble illicitly. However, these crude modules can only siphon **low-power radiant energy** (operating at reduced low-power effectiveness).
     - *Dynamic Frequency Shifting:* Early NeitherTeck engineers instituted an essential security measure: municipal and fortress dynamos continuously modulate the **frequency and resonance pattern of broadcast radiant power**.
     - *Deliberate Bulk & Constant Monitoring:* Due to the extreme danger of unregulated high-energy radiant discharge, **High-Energy Radiant Converters are heavily regulated and intentionally manufactured to be extremely large, bulky, and visually conspicuous** (preventing easy concealment). Each unit is closely tracked, stamped with security hallmarks, and strictly monitored on checkout logs.
     - *Generator Energy Release Pattern Alterations:* Spires and stationary dynamos can alter their master pattern of energy release. When this occurs, **all high-radiant converters across the grid require manual/technical adjustments to synchronize with the new pattern**. Any converter not calibrated to the new release pattern is instantly decoupled from high-energy flow.
     - *High-Radiant Calibration & Skill Requirement:* Drawing maximum current for **High-Power Level operation** requires an official **calibrated converter module** that follows the generator's shifting frequency pattern, as well as an operator with the **technical skill** (e.g., trained in NeitherTeck/Arcana/Crafting) to synchronize and adjust the weapon. Without a calibrated module and operator skill, a radiant weapon cannot tap the saturated high-energy fields in spires or near dynamos.
   - **Two Operational Effectiveness Levels:** A radiant weapon can operate at two performance levels depending on proximity to the generator:
     - **High-Power Level (Spire Core & Outpost Generator Proximity):** Requires an active broadcast grid, a **calibrated converter module tracking dynamic frequencies, and operator skill**. Saturation allows the weapon to discharge at maximum capacity, dealing full listed damage and range with optimal capacitor cycling.
     - **Moderate / Low-Power Level (Airships, Extended Perimeters & Uncalibrated/Bootleg Converters):** On military airships, in perimeter zones (up to 5× distance), or when using bootleg/uncalibrated converter modules, radiant energy uptake is limited. Weapons operate at reduced baseline effectiveness (e.g., –1 damage die size, –10 to –20 ft range, or half fatal bonus) due to weaker capacitive step-up.
     - **Beyond 5× Distance:** Outside 5 times the high-power radius, radiant coupling collapses entirely and the weapon becomes completely inert.
   - **Throughput Cost:** Cost **3 to 6 AP** per Strike, strictly scaling with weapon caliber and capacitive draw.

---

## 2. Portable Cartridge Weapons (Active Surge AP)

*Close-to-mid range, self-powered via high-density chemical cells. Half range in dense Neither fog; operates without an ambient broadcast grid as long as cartridges remain. **When cartridges run dry or in pure Aither, these energy mechanisms are completely dead and inoperable.***

| Weapon | Damage & Type | Surge AP | Cartridge Capacity | Tags | Range & Traits |
|---|:---:|:---:|:---:|---|:---:|
| **Neither Arc Pocket Emitter** | **1d6 Electricity** | **2 AP** | Small (3 shots) | `[Professional]`, `[Clandestine]` | 15 ft, Concealable, Fatal d10 |
| **Neither Service Arc Pistol** | **1d6 Electricity** | **2 AP** | Small (3 shots) | `[Military]`, `[Biochemical]` | 20 ft, Concealable, Fatal d10 |
| **Neither Twin-Arc Pistol** | **1d6 Electricity** | **2 AP** | Small (6 shots) | `[Military]`, `[Mechanical]` | 15 ft, Fatal d10 |
| **Neither Revolving Arc Pistol** | **1d6 Electricity** | **2 AP** | Rotary (9 shots) | `[Military]`, `[Mechanical]` | 30 ft, Fatal d10 |
| **Neither Force Dueling Pistol** | **1d8 Force** | **3 AP** | Small (3 shots) | `[Professional]`, `[Airships]` | 30 ft, Concealable, Fatal d12 |
| **Neither Slide Pulse Pistol** | **1d8 Force** | **3 AP** | Medium (15 pulses) | `[Mechanical]`, `[Military]` | 15 ft, Fatal d12 |
| **Neither Service Arc Rifle** | **1d8 Electricity** | **3 AP** | Medium (3 shots) | `[Military]`, `[Technical]` | 35 ft, Fatal d12 |
| **Neither Twin-Arc Rifle** | **1d8 Electricity** | **3 AP** | Medium (6 shots) | `[Military]`, `[Technical]` | 30 ft, Fatal d12 |
| **Neither Shock Cannon** | **1d8 Electricity** | **3 AP** | Medium (3 shots) | `[Military]`, `[Mechanical]` | 15 ft, Scatter 5 ft |
| **Neither Pulse Blunderbuss** | **1d8 Force** | **3 AP** | Medium (3 pulses) | `[Military]`, `[Airships]` | 20 ft, Scatter 10 ft |
| **Neither Dragon Projector** | **1d10 Force** | **3 AP** | Large (3 pulses) | `[Military]`, `[Subterranean]` | 30 ft, Kickback, Scatter 10 ft |
| **Neither Precision Arc Lance** | **1d10 Electricity** | **3 AP** | Medium (3 arcs) | `[Technical]`, `[Military]` | 45 ft, Fatal d12+2 |

---

## 3. Radiant Grid Weapons (Active Surge AP)

*Inductive weapons drawing directly from the Spire or Airship resonant field. Unlimited ammunition (cycles 1 round between shots), full ballistic range, highest damage output. **Outside 5× generator distance or in pure Aither, induction collapses completely and these energy weapons are inert dead weight.***

| Weapon | Radiant Damage & Type | Surge AP | Tags | Range & Traits |
|---|:---:|:---:|---|:---:|
| **Radiant Light Arc Pistol** | **1d6 Electricity** | **3 AP** | `[Professional]`, `[Technical]` | 40 ft, Concealable, Fatal d10 |
| **Radiant Defense Carbine** | **1d8 Electricity** | **4 AP** | `[Military]`, `[Technical]` | 70 ft, Fatal d12 |
| **Radiant Pulse Projector** | **1d8 Force** | **4 AP** | `[Technical]`, `[Mechanical]` | 60 ft, Scatter 10 ft |
| **Radiant Precision Lance** | **1d10 Electricity** | **5 AP** | `[Technical]`, `[Military]` | 90 ft, Fatal d12+2 (Sniper) |
| **Radiant Heavy Arquebus** | **1d10 Electricity** | **5 AP** | `[Technical]`, `[Military]` | 150 ft, Fatal d12+2, Kickback |
| **Spire Force Breaker** | **1d12 Force** | **6 AP** | `[Military]`, `[Technical]` | 50 ft, Kickback, Radiant Induction |
| **Great Spire Arc Cannon** | **2d10 Electricity** | **6 AP** | `[Technical]` | 200 ft, Emplacement / Heavy Rig, Fatal d12+4, Radiant Induction |

---

## 4. Auxiliary Mundane Attachments & Melee Fallbacks

While NeitherTeck energy firing mechanisms are completely dead without power or cartridges, ranged weapons are physical assemblies of steel, hardwood, and brass that can be fitted with mundane close-quarters combat attachments `[Guns & Gears p.152]`:

- **Affixed Bayonet (Rifles & Longarms):**
  - Standard physical bayonet blade (or serrated spade) affixed beneath the barrel.
  - **Damage:** **1d6 Piercing** (or Slashing), Agile, Two-Handed.
  - **Mundane & Unpowered (0 AP):** Requires zero AP, zero cartridges, and zero power grids. If the rifle’s Neither capacitors die, deplete, or enter pure Aither, the weapon can still be wielded as an effective mundane spear/bayonet.
- **Reinforced Grip / Pistol Whipping (Pistols & Hand Emitters):**
  - Heavy brass, weighted steel pommels, or ribbed battery frames.
  - **Damage:** **1d4 Bludgeoning**, Agile, Finesse.
  - **Mundane & Unpowered (0 AP):** Allows any pistol or hand emitter to be swung in close quarters as a light club without spending AP, functioning even when completely inert.

---

## 5. Special Weapon Traits

### Radiant Induction
A weapon with this trait has no magazine or internal cartridge. It draws power wirelessly from an active municipal or Airship radiant dynamo.
- **Unlimited Ammo:** As long as you remain within an active radiant broadcast field (Tier 1 or Tier 2), ammunition is unlimited.
- **Capacitive Cycle (1 Round):** After firing, internal capacitors require 1 full round to recharge from the radiant field before discharging again.
- **Dead in Tier 3:** The weapon is completely non-functional outside radiant broadcast perimeters.

### Cartridge X
Holds a sealed chemical cartridge containing **X** shots. Replacing a spent cartridge requires a 1-action Interact activity (or the *Slinger's Reload* class feature).
