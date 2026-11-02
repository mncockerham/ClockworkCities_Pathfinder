"""
Script to enforce the Municipal Spire Weapon Disarmament Mandate across generate_all_templates.py:
Rule:
In the Civil Spire, ALL weapons and unarmed strikes are strictly 1d4 mundane,
EXCEPT:
- Noble: 1d6 dueling blade
- Merchant: 1d6 dueling blade
- Noble Rake: 1d6 dueling blade (Fair Steel Salon Rapier)

Specifically:
1. Pugilist:
   - In Civil Spire, Brass Knuckles / Unarmed attacks are non-enhanced street fists: 1d4 damage dice!
   - (Outside Spire in High/Low/Neither, Brass Knuckles scale to 1d6/2d6/3d6 as normal).
2. Officer:
   - In Civil Spire, Officer cannot carry 2d6 Officer's Sabre (unless on military mobilization).
   - Change Officer's Sabre allowed_environments to ["high_radiant", "low_radiant", "the_neither"].
   - Add a Civil Spire sidearm for Officer: "Sidearm Utility Dagger" -> 1d4 damage dice.
   - Retainers in Civil Spire: Retainers in Civil Spire cannot carry 1d8/1d6 military weapons; they are retainers/valets with 1d4 cudgels or fists, or retainers are not deployed as armed escorts without status clearance.
3. Survivor:
   - Utility Dagger / Shiv in Civil Spire has base 1d4 (no striking runes in Spire; striking runes are outland).
   - In Civil Spire, Utility Dagger is 1d4.
4. Scout:
   - Utility Skinning Knife in Civil Spire is 1d4 (no striking runes in Spire).
5. GreyMarketeer:
   - Black-Market Stiletto in Civil Spire is 1d4 (no striking runes).
   - Retainers in Civil Spire use 1d4 saps/fists.
6. Chirurgeon:
   - Surgical Scalpel / Lancet in Civil Spire is 1d4.
7. Rake:
   - Salon Rapier in Civil Spire is strictly 1d6 (as mandated: "1d6 for Noble, Merchant, and Noble Rake").
8. Noble & Merchant:
   - Already 1d6 dueling rapier in Civil Spire!
"""

with open("ClockworkPathfinder/testing/combat_sim/generate_all_templates.py", "r", encoding="utf-8") as f:
    text = f.read()

# Let's inspect and patch Pugilist:
# We should give Pugilist an outland_weapons for striking brass knuckles, and standard weapons brass knuckles 1d4 in civil spire!
# Or let's see how weapons are defined.

