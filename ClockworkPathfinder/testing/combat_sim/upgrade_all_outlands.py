import sys, os
from pathlib import Path

# Update generate_all_templates.py to give all classes proper outland loadouts:
# 1. ClockworkRifleman:
#    - Civil: Concealed small-bore cartridge gun (1-shot)
#    - Outland: Heavy Long Rifle (large cartridge, capacity 6, deadly range 120 ft) + combat bayonet + outland armor
# 2. Survivor:
#    - Civil: 1d4 mundane utility dagger
#    - Outland: Paired Niracrest trench daggers / shortswords (1d6+striking, agile, deadly), hand crossbow / repeating pistol
# 3. ClockworkEngineer:
#    - Civil: Disarmed / wrench only
#    - Outland: Full powered exoskeleton (+2 AC), Heavy Neither Carbine (2d8 cartridge, fatal_d10, cap 6), clockwork shield block
# 4. Scout:
#    - Outland: Reinforced composite longbow (deadly d10, reload 0), climbing pick / hatchet, outland leather (AC 24)
# 5. Officer:
#    - Outland: Commissioned officer saber, repeating service revolver (cap 6), reinforced officer breastplate (AC 24), heavy shield
# 6. Merchant / Noble:
#    - Outland: Hired expedition guards (Type 4 outland guards), heavy traveling duster, masterwork dueling sword / repeating pistol
# 7. Chirurgeon:
#    - Outland: Galvanic Ward (20-50 Temp HP), Drone horde (DR 8, save DC 21)

print("Preparing comprehensive outland upgrade script...")
