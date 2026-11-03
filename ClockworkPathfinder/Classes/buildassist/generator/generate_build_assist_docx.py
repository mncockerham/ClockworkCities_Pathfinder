"""
Build Assist Generator: Master Class Creation Workbook (Levels 1–10)
Outputs:
1. ClockworkPathfinder/Classes/buildassist/Clockwork_Classes_Build_Assist_Lv1-10.docx
2. ClockworkPathfinder/Classes/buildassist/Clockwork_Classes_Build_Assist_Lv1-10.md
"""

import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn
from pathlib import Path

CLASSES_DATA = [
    {
        "name": "Soldier",
        "base": "Fighter [Player Core p.136]",
        "role": "Frontline Anchor / Chokepoint Defender (Target Weight 13)",
        "hp": "10 + CON mod per level",
        "key_attr": "Strength or Dexterity",
        "perception": "Expert (Master at Lv 9)",
        "saves": "Fortitude: Expert, Reflex: Expert, Will: Trained (Expert at Lv 3)",
        "armor": "Trained in all armor (unarmored, light, medium, heavy) and shields. Expert at Lv 11.",
        "weapons": "Expert in simple and martial weapons, advanced weapons trained. Master at Lv 5.",
        "skills": "Trained in Athletics or Acrobatics, plus 3 + INT mod additional skills.",
        "social": "Tier 4 Track (5 advancements). Base: 2 Auto + 1 Class + CHA. Focus: Military & Watch.",
        "subclass_prompt": "Combat Specialty / Fighting Style (e.g. Shield & Board, Great Weapon, Dual Wield)",
        "feats": {
            1: ["Point-Blank Shot", "Reactive Strike (Standard)", "Snagging Strike", "Sudden Charge", "Double Slice"],
            2: ["Aggressive Block", "Assisting Shot", "Brutal Shove", "Dueling Parry", "Intimidating Strike"],
            4: ["Dual-Handed Assault", "Knockdown", "Parting Shot", "Powerful Shove", "Shield Bash Mastery"],
            6: ["Advanced Weapon Training", "Disorienting Opening", "Furious Focus", "Reflexive Shield", "Shield Warden"],
            8: ["Blind-Fight", "Disarming Twist", "Felling Strike", "Positioning Assault", "Sudden Leap"],
            10: ["Certain Strike", "Combat Reflexes (Extra Reaction)", "Debilitating Shot", "Disruptive Stance", "Overpowering Attack"]
        }
    },
    {
        "name": "Survivor",
        "base": "Rogue [Player Core p.168]",
        "role": "Deadly Skirmisher / Evasive Finisher / Urban Scavenger (Target Weight 12)",
        "hp": "8 + CON mod per level",
        "key_attr": "Dexterity (or Strength / Charisma / Intelligence)",
        "perception": "Expert (Master at Lv 7, Legendary at Lv 13)",
        "saves": "Fortitude: Trained (Expert at Lv 9), Reflex: Expert (Master at Lv 7), Will: Expert (Master at Lv 17)",
        "armor": "Trained in light armor and unarmored defense. Expert at Lv 13.",
        "weapons": "Trained in simple weapons, rapiers, sap, shortbow, shortsword. Expert at Lv 5.",
        "skills": "Trained in Stealth or Thievery, plus 7 + INT mod additional skills (Skill increase EVERY level).",
        "social": "Tier 3 Track (6 advancements). Base: 2 Auto + 2 Class + CHA. Focus: Underworld & Warrens.",
        "subclass_prompt": "Racket / Survival Focus (Scoundrel, Ruffian, Thief, Mastermind)",
        "feats": {
            1: ["Nimble Dodge", "Trap Finder", "You're Next", "Twin Feint", "Overwatch Reaction"],
            2: ["Mobility", "Quick Draw", "Minor Magic (Tech Rig)", "Distracting Feint", "Underhanded Assault"],
            4: ["Dread Striker", "Poison Weapon (Chemical)", "Scout's Warning", "Twin Distraction", "Reactive Evasion"],
            6: ["Analyze Weakness", "Gang Up", "Light Step", "Skirmish Strike", "Watch Your Back"],
            8: ["Blind-Fight", "Bullseye", "Nimble Roll", "Sly Striker", "Opportune Backstab"],
            10: ["Sneak Savant", "Tactical Entry", "Precise Debilitations", "Uncanny Dodge"]
        }
    },
    {
        "name": "Pugilist",
        "base": "Monk [Player Core 2 p.140]",
        "role": "Heavy Frontline Brawler / Maneuver Disruptor (Target Weight 12)",
        "hp": "10 + CON mod per level",
        "key_attr": "Strength or Dexterity",
        "perception": "Trained (Expert at Lv 5, Master at Lv 15)",
        "saves": "Expert in Fortitude, Reflex, and Will saves (All 3 saves start Expert!).",
        "armor": "Expert in unarmored defense (Master at Lv 13, Legendary at Lv 17).",
        "weapons": "Trained in unarmed attacks and monk weapons. Expert at Lv 5, Master at Lv 15.",
        "skills": "Trained in Athletics or Acrobatics, plus 4 + INT mod additional skills.",
        "social": "Tier 4 Track (5 advancements). Base: 2 Auto + 1 Class + CHA. Focus: Street Clubs & Docks.",
        "subclass_prompt": "Brawling Style / Stance (Bare-Knuckle, Iron Guard, Haymaker, Grappler)",
        "feats": {
            1: ["Flurry of Blows (Standard)", "Dragon Stance", "Gorilla Stance", "Wolf Stance", "Crane Stance", "Brawling Clinch"],
            2: ["Brawling Focus", "Crushing Grab", "Dancing Leaf", "Deflect Arrows/Bolts", "Shooting Star Stance"],
            4: ["Defensive Posture", "Flurry of Maneuvers", "Guarded Movement", "Stand Still (Reaction)", "Knockout Blow"],
            6: ["Crane Flutter", "Dragon Roar", "Water Dance", "Careful Grapple", "Haymaker Surge"],
            8: ["Iron Bones", "Wall Run", "Mixed Martial Arts", "Clinch Crusher", "Stunning Blows"],
            9: ["Metal Fists (Count as Cold Iron/Silver)"],
            10: ["Knockout Mastery", "Sleeper Hold", "Wind Stance Strike", "Relentless Flurry"]
        }
    },
    {
        "name": "Rake",
        "base": "Swashbuckler [Player Core 2 p.176]",
        "role": "Mobile Duelist / High-AC Skirmisher / Panache Flanker (Target Weight 11)",
        "hp": "10 + CON mod per level",
        "key_attr": "Dexterity",
        "perception": "Expert (Master at Lv 11)",
        "saves": "Fortitude: Trained (Expert at Lv 9), Reflex: Expert (Master at Lv 7), Will: Expert (Master at Lv 15)",
        "armor": "Trained in light armor and unarmored defense. Expert at Lv 13.",
        "weapons": "Trained in simple, martial, and agile/finesse weapons. Expert at Lv 5, Master at Lv 13.",
        "skills": "Trained in Acrobatics, Style skill, plus 4 + INT mod additional skills.",
        "social": "Tier 2 Track (10 advancements). Base: 2 Auto + 3 Class + CHA. Focus: High Society & Salons.",
        "subclass_prompt": "Swashbuckler Style (Braggart, Fencer, Gymnast, Battledancer, Wit)",
        "feats": {
            1: ["Confident Finisher (Standard)", "Dueling Parry", "Disarming Flair", "One-For-All", "You're Next"],
            2: ["After You", "Antagonize", "Charmed Life", "Finishing Follow-Through", "Tumble Behind"],
            4: ["Flamboyant Athlete", "Goading Feint", "Leading Dance", "Swaggering Initiative", "Twin Parry"],
            6: ["Agile Maneuvers", "Bleeding Finisher", "Combination Finisher", "Exemplary Finisher"],
            8: ["Bleeding Riposte", "Dueling Riposte (Reaction)", "Nimble Dodge", "Stunning Finisher"],
            10: ["Buckler Flurry", "Derring-do", "Mobile Riposte", "Targeted Finisher"]
        }
    },
    {
        "name": "Officer",
        "base": "Champion [Player Core 2 p.18]",
        "role": "Tactical Commander / Line Anchor / Vanguard Aegis (Target Weight 11)",
        "hp": "10 + CON mod per level",
        "key_attr": "Strength or Dexterity",
        "perception": "Trained (Expert at Lv 11)",
        "saves": "Fortitude: Expert, Reflex: Trained (Expert at Lv 9), Will: Expert (Master at Lv 11)",
        "armor": "Trained in all armor and shields. Expert at Lv 7, Master at Lv 13, Legendary at Lv 17.",
        "weapons": "Trained in simple and martial weapons. Expert at Lv 5, Master at Lv 11.",
        "skills": "Trained in Warfare Lore, Athletics or Diplomacy, plus 3 + INT mod additional skills.",
        "social": "Tier 3 Track (6 advancements). Base: 2 Auto + 2 Class + CHA. Focus: Crown Courts & Guard.",
        "subclass_prompt": "Commission / Command Doctrine (King's Guard Aegis, Trench Captain, Sump Marshal)",
        "feats": {
            1: ["Iron Command / Intercept Reaction", "Weight of Guilt", "Vanguard Stance", "Rallying Cry"],
            2: ["Assisting Shot", "Coordinated Strike", "Shield Warden", "Commanding Presence", "Hold the Line"],
            4: ["Aura of Courage", "Defensive Shield Team", "Disarming Command", "Knockdown Order"],
            6: ["Attack of Opportunity (Command)", "Shield Ally Master", "Tactical Reposition", "Smite Resistance"],
            8: ["Greater Intercept", "Advance Order!", "Quick Shield Block", "Unfaltering Vanguard"],
            10: ["Shield of Grace", "Mass Command Directive", "Aura of Steadfast Resolve"]
        }
    },
    {
        "name": "Clockwork Engineer",
        "base": "Inventor [Guns & Gears p.14]",
        "role": "Defensive Mesh Frontliner / Shoulder Turret / Construct Master (Target Weight 11)",
        "hp": "8 + CON mod per level",
        "key_attr": "Intelligence",
        "perception": "Trained (Expert at Lv 7, Master at Lv 15)",
        "saves": "Fortitude: Expert, Reflex: Trained (Expert at Lv 9), Will: Expert (Master at Lv 17)",
        "armor": "Trained in light and medium armor. Expert at Lv 13.",
        "weapons": "Trained in simple and martial weapons. Expert at Lv 5, Master at Lv 15.",
        "skills": "Trained in Crafting, plus 3 + INT mod additional skills.",
        "social": "Tier 4 Track (5 advancements). Base: 2 Auto + 1 Class + CHA. Focus: Craft Guilds & Foundries.",
        "subclass_prompt": "Innovation Type: [Combat Backpack (Turret + Temp HP)] or [Construct Companion] or [Armor/Weapon Innovation]",
        "feats": {
            1: ["Combat Backpack Module (+1 AC, Turret Fire, Temp HP)", "Explosive Leap", "Variable Core", "Tamper"],
            2: ["Collapse Armor/Weapon", "Reverse Engineer", "Searing Restoration (Alchemical Steam)", "Clockwork Pet"],
            4: ["Automated Turret Overwatch", "Gadget Specialist", "Megavolt Shock", "Overdrive Mastery"],
            6: ["Clockwork Shield Rig", "Megaton Strike", "Deflective Mesh Upgrade (+2 Temp HP/Lv)"],
            8: ["Gigavolt Discharge", "Overclocked Servos", "Persistent Deflection Ring"],
            10: ["Endless Gadgets", "Distortion Capacitor", "Electromagnetic Pulse Blast"]
        }
    },
    {
        "name": "Clockwork Rifleman",
        "base": "Gunslinger [Guns & Gears p.106]",
        "role": "Long-Range Sniper / Overwatch Artillery / Ballistic Slayer (Target Weight 10)",
        "hp": "8 + CON mod per level",
        "key_attr": "Dexterity",
        "perception": "Expert (Master at Lv 7, Legendary at Lv 13)",
        "saves": "Fortitude: Trained (Expert at Lv 9), Reflex: Expert (Master at Lv 7), Will: Trained (Expert at Lv 3, Master at Lv 17)",
        "armor": "Trained in light armor and unarmored defense. Expert at Lv 13.",
        "weapons": "Expert in simple and martial firearms and crossbows. Master at Lv 5, Legendary at Lv 13.",
        "skills": "Trained in Acrobatics or Crafting, plus 3 + INT mod additional skills.",
        "social": "Tier 4 Track (5 advancements). Base: 2 Auto + 1 Class + CHA. Focus: Armories & Enclaves.",
        "subclass_prompt": "Way of the Rifle (Way of the Sniper, Way of the Vanguard, Way of the Pistolero)",
        "feats": {
            1: ["Cover Fire", "Crossbow Crack Shot", "Hit the Dirt!", "One Shot One Kill", "Munitions Crafter"],
            2: ["Defensive Armament", "Fake Out (Reaction)", "Quick Draw", "Warning Shot", "Pistol Twirl"],
            4: ["Alchemical Shot", "Black Powder Boost", "Paired Shots", "Running Reload", "Sniper's Aim"],
            6: ["Advanced Munitions", "Bullet Split", "Pistolero's Retort", "Covering Fire Reaction"],
            8: ["Grit and Tenacity", "Incredible Aim", "Leap and Fire", "Smoke Curtain Shot"],
            10: ["Call Shot", "Deflecting Shot", "Piercing Shot", "Trick Shot Ballistics"]
        }
    },
    {
        "name": "Scout",
        "base": "Ranger [Player Core p.152]",
        "role": "Wilderness Tracker / Range Recon / Ambush Specialist (Target Weight 10)",
        "hp": "10 + CON mod per level",
        "key_attr": "Dexterity or Strength",
        "perception": "Expert (Master at Lv 7, Legendary at Lv 15)",
        "saves": "Fortitude: Expert, Reflex: Expert, Will: Trained (Expert at Lv 3, Master at Lv 15)",
        "armor": "Trained in light and medium armor. Expert at Lv 13.",
        "weapons": "Trained in simple and martial weapons. Expert at Lv 5, Master at Lv 13.",
        "skills": "Trained in Nature or Survival, plus 4 + INT mod additional skills.",
        "social": "Tier 4 Track (5 advancements). Base: 2 Auto + 1 Class + CHA. Focus: Outlands, Caravans, Sump.",
        "subclass_prompt": "Hunter's Edge (Flurry, Precision, Outwit)",
        "feats": {
            1: ["Hunt Prey (Standard)", "Crossbow Ace", "Animal Companion", "Gravity Weapon", "Twin Takedown"],
            2: ["Hunter's Aim", "Quick Draw", "Monster Hunter", "Distracting Shot", "Far Shot"],
            4: ["Companion's Cry", "Disrupt Prey (Reaction)", "Running Reload", "Scout's Warning", "Twin Parry"],
            6: ["Hazard Finder", "Skirmish Strike", "Swift Tracker", "Master Monster Hunter"],
            8: ["Blind-Fight", "Deadly Aim", "Warden's Step", "Camouflage"],
            10: ["Penetrating Shot", "Targeting Shot", "Warden's Boon", "Master's Edge"]
        }
    },
    {
        "name": "Noble",
        "base": "Modified Bard [Player Core p.94]",
        "role": "High Influence / Retainer Wall / Court Authority (Target Weight 9)",
        "hp": "8 + CON mod per level",
        "key_attr": "Charisma",
        "perception": "Expert (Master at Lv 11)",
        "saves": "Fortitude: Trained (Expert at Lv 9), Reflex: Trained (Expert at Lv 11), Will: Expert (Master at Lv 7)",
        "armor": "Trained in light armor and unarmored defense (plus rapier/dueling blade exemption).",
        "weapons": "Trained in simple weapons, rapiers, shortswords, dueling canes. Expert at Lv 11.",
        "skills": "Trained in Society, Diplomacy, plus 4 + INT mod additional skills.",
        "social": "Tier 1 Track (13 advancements). Base: 2 Auto + 4 Class + CHA. Focus: Nobility & High Society.",
        "subclass_prompt": "House Lineage & Standing (Imperial Line, Merchant Patrician, Diplomatic Ambassador)",
        "feats": {
            1: ["Aristocratic Retainer (Meatshield Wall - absorbs 50% dmg)", "Courtly Graces", "Noble Composure"],
            2: ["Peer Authority", "Bodyguard Reaction Intercept", "Entourage Expansion (2nd Retainer)", "Inspire Fortitude"],
            4: ["Legal Immunity Directive", "Diplomatic Leverage", "Heraldic Mandate", "Noble Duellist"],
            6: ["Aura of Majesty", "Elite Retainer Guard (Armored)", "Call In Sovereign Marker"],
            8: ["Commanding Aristocracy", "House Retinue (3rd Retainer)", "Untouchable Social Status"],
            10: ["Peerless Patronage", "Sovereign Decrees", "Inviolable Diplomatic Immunity"]
        }
    },
    {
        "name": "Merchant",
        "base": "Modified Bard [Player Core p.94]",
        "role": "Financial Leverage / Factor Networks / Mercenary Bodyguards (Target Weight 9)",
        "hp": "8 + CON mod per level",
        "key_attr": "Charisma or Intelligence",
        "perception": "Expert (Master at Lv 11)",
        "saves": "Fortitude: Trained (Expert at Lv 9), Reflex: Trained (Expert at Lv 11), Will: Expert (Master at Lv 7)",
        "armor": "Trained in light armor and unarmored defense.",
        "weapons": "Trained in simple weapons, light crossbows, heavy canes. Expert at Lv 11.",
        "skills": "Trained in Society, Deception, Accounting Lore, plus 4 + INT mod additional skills.",
        "social": "Tier 1 Track (13 advancements). Base: 2 Auto + 4 Class + CHA. Focus: Commercial Houses & Guilds.",
        "subclass_prompt": "Trading Charter Focus (Neither-Tech Factor, Spore & Spice Guild, Sky-Dock Shipper)",
        "feats": {
            1: ["Hired Muscle (Retainer Bodyguard absorbs 50% dmg)", "Bargain Hunter", "Guild Factorship"],
            2: ["Double Bookkeeping", "Mercenary Contract Expansion", "Material Requisition (+20% Gear Fund)"],
            4: ["Expedited Customs Clearance", "Black Market Buy-In", "Bribery Matrix", "Defensive Contract"],
            6: ["Armed Caravan Retinue", "Cartel Monopoly", "Heavy Plate Mercenary Guard"],
            8: ["Market Cornering", "Syndicate Buying Power", "Mercenary Commander"],
            10: ["Commercial Hegemony", "Infinite Line of Credit", "Unbreakable Guild Retinue"]
        }
    },
    {
        "name": "Grey Marketeer",
        "base": "Modified Bard [Player Core p.94] + Rogue Skills",
        "role": "Underworld Broker / Smuggler / Black-Market Infiltrator (Target Weight 9)",
        "hp": "8 + CON mod per level",
        "key_attr": "Charisma or Dexterity",
        "perception": "Expert (Master at Lv 9)",
        "saves": "Fortitude: Trained (Expert at Lv 9), Reflex: Expert (Master at Lv 7), Will: Expert (Master at Lv 9)",
        "armor": "Trained in light armor and unarmored defense. Expert at Lv 13.",
        "weapons": "Trained in simple weapons, hand crossbows, concealed daggers. Expert at Lv 9.",
        "skills": "Trained in Deception, Stealth, Underworld Lore, plus 5 + INT mod additional skills.",
        "social": "Tier 2 Track (10 advancements). Base: 2 Auto + 3 Class + CHA. Focus: Underworld & Syndicates.",
        "subclass_prompt": "Syndicate Specialty (Contraband Runner, Fence & Counterfeiter, Shadow Broker)",
        "feats": {
            1: ["Concealed Smuggler Compartments", "Underworld Slang", "Shadow Asset (Concealed Retainer)"],
            2: ["Fence Stolen Goods", "Distracting Payoff", "False Identity Papers", "Slip into Shadows"],
            4: ["Black Market Procurement", "Blind Spot Bribery", "Underground Safehouse", "Poison Network"],
            6: ["Shadow Syndicate Node", "Lookout Warnings (Reaction)", "Smuggler's Escape Route"],
            8: ["Syndicate Enforcer Cohort", "Deep Cover Infiltration", "Ghost Contraband"],
            10: ["Underworld Kingpin", "Shadow Network Immunity", "Unseen Syndicate Cell"]
        }
    },
    {
        "name": "Chirurgeon",
        "base": "Alchemist (Chirurgeon) [Player Core 2 p.44]",
        "role": "Triage Field Medic / Drone Protector / Convalescence Doctor (Target Weight 7)",
        "hp": "8 + CON mod per level (53 HP at Lv 5)",
        "key_attr": "Intelligence",
        "perception": "Trained (Expert at Lv 9)",
        "saves": "Fortitude: Expert (Master at Lv 15), Reflex: Trained (Expert at Lv 7), Will: Expert (Master at Lv 11)",
        "armor": "Trained in light armor and unarmored defense. Expert at Lv 13.",
        "weapons": "Trained in simple weapons, scalpels, surgical saws, injector pistols. Expert at Lv 11.",
        "skills": "Trained in Medicine, Crafting, Academia Lore, plus 4 + INT mod additional skills.",
        "social": "Tier 3 Track (6 advancements). Base: 2 Auto + 2 Class + CHA. Focus: Sanatoriums & Health.",
        "subclass_prompt": "Medical Doctrine: Field Triage, Surgical Prosthetics, or Chemical Antidotes",
        "feats": {
            1: ["Clockwork Triage Drone (Intercept Reaction -8 dmg)", "Field Triage (2-Action In-Combat Heal)", "Active Convalescence"],
            2: ["Battle Medicine", "Revivifying Mutagen / Stimulant", "Antidote Synthesis", "Surgical Precision"],
            4: ["Automated Drone Sentry", "Continuous Convalescence", "Elixir of Life Formulation", "Field Surgery"],
            6: ["Combined Elixirs", "Drone Armor Deflection Upgrade", "Emergency Resuscitation Injection"],
            8: ["Greater Field Triage (3d6+6)", "Permanent Stabilizer Drones", "Advanced Convalescence (2d6/INT)"],
            10: ["True Medical Miracle", "Panacea Formulation", "Master Drone Interception (-12 dmg)"]
        }
    },
    {
        "name": "Scholar",
        "base": "Modified Investigator [Player Core 2 p.40]",
        "role": "Predictive Tactical Buffer / Actuarial AC Evasion / Ballistic Calculus (Target Weight 7)",
        "hp": "8 + CON mod per level (53 HP at Lv 5)",
        "key_attr": "Intelligence",
        "perception": "Expert (Master at Lv 9, Legendary at Lv 17)",
        "saves": "Fortitude: Trained (Expert at Lv 11), Reflex: Trained (Expert at Lv 7), Will: Expert (Master at Lv 5, Legendary at Lv 15)",
        "armor": "Trained in light armor and unarmored defense. Expert at Lv 13.",
        "weapons": "Trained in simple weapons, rapiers, shortswords, canes. Expert at Lv 5, Master at Lv 17.",
        "skills": "Trained in Society, Academia Lore, plus 5 + INT mod additional skills (Skill increase EVERY level).",
        "social": "Tier 2 Track (10 advancements). Base: 2 Auto + 3 Class + CHA. Focus: Universities & Bureaucracy.",
        "subclass_prompt": "Academic Specialty: [Accountant/Actuary (AC Defense)] or [Architect (Hardness)] or [Natural Philosopher (Attack)]",
        "feats": {
            1: ["Analytical Assessment (1 AP Intellect Strike)", "Actuarial Risk Assessment (+1/+2 AC Broadcast)", "Known Weakness"],
            2: ["Tactical Instruction (Party Telemetry)", "Encyclopedic Recall", "Combat Cartography (Difficult Terrain Denial)"],
            4: ["NeitherTeck Tuning (+2 Max AP)", "Applied Ballistics", "Forensic Audit Matrix"],
            6: ["Predictive Counter-Measure (Reaction +3 AC to self or ally)", "Blueprint Memory", "Tactical Evade"],
            8: ["NeitherTeck Advanced Calibration (+2 Max AP)", "Zone & Neither Theory", "Stress-Point Demolition"],
            10: ["Actuarial Certainty (Reroll <10 Stratagems)", "Civic Authority Mandate", "Mass Predictive Defense Grid"]
        }
    }
]

def create_master_workbook():
    doc = docx.Document()
    
    # Configure 0.5-inch margins for dense, printable worksheets
    for s in doc.sections:
        s.top_margin = Inches(0.5)
        s.bottom_margin = Inches(0.5)
        s.left_margin = Inches(0.5)
        s.right_margin = Inches(0.5)
        
    # Styling helpers
    def set_cell_background(cell, fill_hex):
        tcPr = cell._tc.get_or_add_tcPr()
        shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
        tcPr.append(shd)

    def set_cell_margins(cell, top=60, bottom=60, left=100, right=100):
        tcPr = cell._tc.get_or_add_tcPr()
        tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
        tcPr.append(tcMar)

    # TITLE COVER
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_title = p_title.add_run("CLOCKWORK CITIES PATHFINDER\nMASTER CLASS CREATION & PROGRESSION WORKBOOK")
    r_title.font.name = "Arial"
    r_title.font.size = Pt(20)
    r_title.font.bold = True
    r_title.font.color.rgb = RGBColor(30, 45, 70)
    
    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = p_sub.add_run("Rapid Build Sheets & Curated Feat Menus for Levels 1 through 10\n13 Core Classes | Victorian Steampunk / Neither-Tech Setting")
    r_sub.font.name = "Arial"
    r_sub.font.size = Pt(11)
    r_sub.font.italic = True
    r_sub.font.color.rgb = RGBColor(90, 90, 90)

    doc.add_paragraph().paragraph_format.space_after = Pt(12)

    # TABLE OF CONTENTS / QUICK INDEX
    t_idx = doc.add_table(rows=1, cols=3)
    t_idx.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr = t_idx.rows[0].cells
    hdr[0].text = "Class Name"
    hdr[1].text = "Base Chassis & Role"
    hdr[2].text = "Target Weight & Niche"
    for c in hdr:
        set_cell_background(c, "2C3E50")
        for p in c.paragraphs:
            p.runs[0].font.bold = True
            p.runs[0].font.color.rgb = RGBColor(255, 255, 255)
            p.runs[0].font.size = Pt(9.5)

    for cdata in CLASSES_DATA:
        row = t_idx.add_row().cells
        row[0].text = cdata["name"]
        row[1].text = f"{cdata['base'].split('[')[0].strip()} | {cdata['role'].split('(')[0].strip()}"
        row[2].text = cdata["role"].split('(')[-1].replace(')', '')
        for c in row:
            for p in c.paragraphs:
                p.runs[0].font.size = Pt(8.5)
                
    doc.add_page_break()

    # GENERATE EACH CLASS SPREAD
    for idx, cdata in enumerate(CLASSES_DATA):
        # PAGE 1: FILL-IN PROGRESSION WORKSHEET
        p_cname = doc.add_paragraph()
        r_cn = p_cname.add_run(f"CLASS: {cdata['name'].upper()}")
        r_cn.font.name = "Arial Black"
        r_cn.font.size = Pt(16)
        r_cn.font.color.rgb = RGBColor(35, 55, 85)
        
        p_info = doc.add_paragraph()
        p_info.paragraph_format.space_after = Pt(4)
        r_inf = p_info.add_run(f"Base: {cdata['base']} | Role: {cdata['role']}\nKey Attribute: {cdata['key_attr']} | Hit Points: {cdata['hp']}")
        r_inf.font.size = Pt(9.5)
        r_inf.font.bold = True

        # Header stats table
        t_stats = doc.add_table(rows=3, cols=2)
        t_stats.alignment = WD_TABLE_ALIGNMENT.CENTER
        t_stats.autofit = False
        
        stat_rows = [
            ("Initial Proficiencies:", f"Perception: {cdata['perception']}\nSaves: {cdata['saves']}\nArmor: {cdata['armor']}\nWeapons: {cdata['weapons']}"),
            ("Class Skills & Social:", f"Trained Skills: {cdata['skills']}\nSocial Advancement: {cdata['social']}"),
            ("Character & Subclass:", f"Character Name: _______________________ Player: __________________ Level: [____]\n{cdata['subclass_prompt']}: __________________________________________")
        ]
        
        for r_i, (lbl, val) in enumerate(stat_rows):
            c_lbl, c_val = t_stats.rows[r_i].cells
            c_lbl.width = Inches(2.0)
            c_val.width = Inches(5.5)
            c_lbl.text = lbl
            c_val.text = val
            set_cell_background(c_lbl, "EAECEE")
            set_cell_margins(c_lbl, 40, 40, 60, 60)
            set_cell_margins(c_val, 40, 40, 60, 60)
            c_lbl.paragraphs[0].runs[0].font.bold = True
            c_lbl.paragraphs[0].runs[0].font.size = Pt(8.5)
            c_val.paragraphs[0].runs[0].font.size = Pt(8.5)

        doc.add_paragraph().paragraph_format.space_after = Pt(4)

        # PROGRESSION FILL-IN TABLE (LEVELS 1-10)
        p_prog_lbl = doc.add_paragraph()
        r_prg = p_prog_lbl.add_run("LEVEL-BY-LEVEL BUILD PROGRESSION (LEVELS 1–10)")
        r_prg.font.bold = True
        r_prg.font.size = Pt(10)
        r_prg.font.color.rgb = RGBColor(35, 55, 85)
        p_prog_lbl.paragraph_format.space_after = Pt(2)

        t_prog = doc.add_table(rows=11, cols=3)
        t_prog.alignment = WD_TABLE_ALIGNMENT.CENTER
        t_prog.autofit = False
        
        p_hdrs = t_prog.rows[0].cells
        p_hdrs[0].width = Inches(0.8)
        p_hdrs[1].width = Inches(2.2)
        p_hdrs[2].width = Inches(4.5)
        p_hdrs[0].text = "Level"
        p_hdrs[1].text = "Standard Advancements"
        p_hdrs[2].text = "Your Specific Selections & Build Notes"
        for c in p_hdrs:
            set_cell_background(c, "34495E")
            for p in c.paragraphs:
                p.runs[0].font.bold = True
                p.runs[0].font.color.rgb = RGBColor(255, 255, 255)
                p.runs[0].font.size = Pt(8.5)

        levels_data = [
            ("Level 1", "Subclass, 1st Class Feat, Initial Skills", "Subclass: ___________________________________________________\nClass Feat: ________________________________________________\nStarting Rig/Weapon: _______________________________________"),
            ("Level 2", "Class Feat, Skill Feat, Social Advancement", "Class Feat: __________________ Skill Feat: __________________\nSocial Advancement: _______________________________________"),
            ("Level 3", "General Feat, Skill Increase, Class Feature", "General Feat: ________________ Skill Inc: __________________\nClass Feature Upgrade: ____________________________________"),
            ("Level 4", "Class Feat, Skill Feat, Social Advancement", "Class Feat: __________________ Skill Feat: __________________\nSocial Advancement: _______________________________________"),
            ("Level 5", "4 Ability Boosts, Skill Increase, Tier 2 Tech/Strike", "Boosts: [  ]STR  [  ]DEX  [  ]CON  [  ]INT  [  ]WIS  [  ]CHA\nSkill Inc: __________________ Tech/Strike Upgrade: ___________"),
            ("Level 6", "Class Feat, Skill Feat, Social Advancement", "Class Feat: __________________ Skill Feat: __________________\nSocial Advancement: _______________________________________"),
            ("Level 7", "General Feat, Skill Increase, Class Feature", "General Feat: ________________ Skill Inc: __________________\nClass Feature Upgrade: ____________________________________"),
            ("Level 8", "Class Feat, Skill Feat, Social Advancement", "Class Feat: __________________ Skill Feat: __________________\nSocial Advancement: _______________________________________"),
            ("Level 9", "Ancestry Feat, Skill Increase, Class Feature", "Ancestry Feat: ________________ Skill Inc: __________________\nClass Feature Upgrade: ____________________________________"),
            ("Level 10", "4 Ability Boosts, Class Feat, Skill Feat, Social Adv.", "Boosts: [  ]STR  [  ]DEX  [  ]CON  [  ]INT  [  ]WIS  [  ]CHA\nClass Feat: __________________ Skill Feat: __________________\nSocial Advancement: _______________________________________")
        ]

        for i, (lvl, std, fill) in enumerate(levels_data):
            row = t_prog.rows[i+1].cells
            row[0].width = Inches(0.8)
            row[1].width = Inches(2.2)
            row[2].width = Inches(4.5)
            row[0].text = lvl
            row[1].text = std
            row[2].text = fill
            set_cell_margins(row[0], 25, 25, 40, 40)
            set_cell_margins(row[1], 25, 25, 40, 40)
            set_cell_margins(row[2], 25, 25, 40, 40)
            row[0].paragraphs[0].runs[0].font.bold = True
            row[0].paragraphs[0].runs[0].font.size = Pt(8.5)
            row[1].paragraphs[0].runs[0].font.size = Pt(8.0)
            row[2].paragraphs[0].runs[0].font.size = Pt(8.0)
            if i % 2 == 1:
                set_cell_background(row[0], "F8F9F9")
                set_cell_background(row[1], "F8F9F9")
                set_cell_background(row[2], "F8F9F9")

        # PAGE BREAK TO FEAT MENU SPREAD
        doc.add_page_break()

        # PAGE 2: CURATED FEAT MENU
        p_fhdr = doc.add_paragraph()
        r_fhd = p_fhdr.add_run(f"{cdata['name'].upper()} — CURATED CLASS FEAT OPTIONS MENU (LEVELS 1–10)")
        r_fhd.font.name = "Arial Black"
        r_fhd.font.size = Pt(13)
        r_fhd.font.color.rgb = RGBColor(35, 55, 85)
        
        p_fsub = doc.add_paragraph()
        r_fsub = p_fsub.add_run("Use this reference menu to choose your Class Feats when leveling up. All feats are setting-verified for Clockwork Cities.")
        r_fsub.font.italic = True
        r_fsub.font.size = Pt(8.5)
        r_fsub.font.color.rgb = RGBColor(100, 100, 100)

        t_feats = doc.add_table(rows=7, cols=2)
        t_feats.alignment = WD_TABLE_ALIGNMENT.CENTER
        t_feats.autofit = False
        
        f_hdrs = t_feats.rows[0].cells
        f_hdrs[0].width = Inches(1.2)
        f_hdrs[1].width = Inches(6.3)
        f_hdrs[0].text = "Feat Level"
        f_hdrs[1].text = "Available Clockwork & Base Class Feat Options"
        for c in f_hdrs:
            set_cell_background(c, "2C3E50")
            for p in c.paragraphs:
                p.runs[0].font.bold = True
                p.runs[0].font.color.rgb = RGBColor(255, 255, 255)
                p.runs[0].font.size = Pt(9.0)

        for f_idx, lvl in enumerate([1, 2, 4, 6, 8, 10]):
            row = t_feats.rows[f_idx+1].cells
            row[0].width = Inches(1.2)
            row[1].width = Inches(6.3)
            row[0].text = f"Level {lvl} Feats"
            feat_list = cdata["feats"].get(lvl, ["See Class Document"])
            row[1].text = " • " + "\n • ".join(feat_list)
            set_cell_margins(row[0], 30, 30, 50, 50)
            set_cell_margins(row[1], 30, 30, 50, 50)
            row[0].paragraphs[0].runs[0].font.bold = True
            row[0].paragraphs[0].runs[0].font.size = Pt(8.5)
            row[1].paragraphs[0].runs[0].font.size = Pt(8.5)
            if f_idx % 2 == 1:
                set_cell_background(row[0], "F4F6F6")
                set_cell_background(row[1], "F4F6F6")

        # Page return between classes (except after the final class)
        if idx < len(CLASSES_DATA) - 1:
            doc.add_page_break()

    out_path = Path("ClockworkPathfinder/Classes/buildassist/Clockwork_Classes_Build_Assist_Lv1-10.docx")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    doc.save(out_path)
    print(f"Successfully generated DOCX workbook: {out_path}")

if __name__ == "__main__":
    create_master_workbook()

