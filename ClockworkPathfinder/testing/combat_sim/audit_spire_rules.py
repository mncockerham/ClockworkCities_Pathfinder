import json
from pathlib import Path

# Load generate_all_templates.py and inspect all classes' civil spire weapons and unarmed strikes
with open("ClockworkPathfinder/testing/combat_sim/generate_all_templates.py", "r", encoding="utf-8") as f:
    text = f.read()

# Requirements:
# "Make sure Spire template is 1d4 for everyone except Noble, Merchant and Noble Rake"
# That means:
# 1. Noble: 1d6 dueling blade
# 2. Merchant: 1d6 dueling blade
# 3. Rake (when high status / Noble Rake): 1d6 dueling blade
# 4. Everyone else (Officer, Grey Marketeer, Survivor, Scout, Soldier, Rifleman, Scholar, Engineer, Chirurgeon, Pugilist):
#    In Civil Spire, weapons must be 1d4 (mundane utility dagger/shiv/scalpel/fists).
#    Unarmed for everyone except Pugilist is already 1d4. Pugilist unarmed in Civil Spire: fists are 1d4 or brass knuckles capped? The instruction says:
#    "Make sure Spire template is 1d4 for everyone except Noble, Merchant and Noble Rake"

# Let's check Officer: Officer's Sabre was "1d6" if lvl==1 else ("2d6" if lvl==5 else "3d6").
# But Officer is not Noble/Merchant/Noble Rake! In civil spire, an Officer cannot carry a military sabre unless in uniform on duty, or it's a 1d4 knife/fist, or Officer's Sabre shouldn't have civil_spire.
# If Officer carries an Officer's Sabre, it shouldn't be allowed in civil_spire, or in civil_spire it's a 1d4 utility knife!

print("Script template ready.")

