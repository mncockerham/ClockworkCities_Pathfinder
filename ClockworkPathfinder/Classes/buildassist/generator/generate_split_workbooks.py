"""
Generators for Build Assist System:
Options:
  --bw / -bw : Generate minimal-ink black-and-white versions starting with bw_
  default    : Generate full-color styled versions

Outputs:
  ClockworkPathfinder/Classes/buildassist/Clockwork_Class_Build_Progression_Lv1-10.docx
  ClockworkPathfinder/Classes/buildassist/Clockwork_Class_Feats_Menu_Lv1-10.docx
  (or bw_ equivalents when -bw flag is passed)
"""

import sys
import argparse
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls
from pathlib import Path

# --- COMMON STYLING HELPERS ---
def set_cell_background(cell, fill_hex, is_bw=False):
    if is_bw:
        return
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=60, bottom=60, left=100, right=100):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def add_xml_field(run, field_name):
    fldSimple = parse_xml(f'<w:fldSimple {nsdecls("w")} w:instr="{field_name}"/>')
    run._r.append(fldSimple)

from datetime import datetime

def setup_section_footer(section, class_name, is_bw=False):
    footer = section.footer
    footer.is_linked_to_previous = False
    
    # Use a borderless 1-row, 2-column table to place date on left, class/page on right
    footer.paragraphs[0].text = "" # clear default paragraph
    tbl = footer.add_table(rows=1, cols=2, width=Inches(7.5))
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    c_left, c_right = tbl.rows[0].cells
    c_left.width = Inches(2.5)
    c_right.width = Inches(5.0)
    
    # Left: MM/DD/YY date
    p_left = c_left.paragraphs[0]
    p_left.alignment = WD_ALIGN_PARAGRAPH.LEFT
    date_str = datetime.now().strftime("%m/%d/%y")
    r_date = p_left.add_run(f"Created: {date_str}")
    r_date.font.size = Pt(8.0)
    r_date.font.color.rgb = RGBColor(90, 90, 90) if is_bw else RGBColor(110, 120, 140)
    
    # Right: Class & Page #
    p_right = c_right.paragraphs[0]
    p_right.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r_cls = p_right.add_run(f"Clockwork Cities Pathfinder  |  {class_name}  |  Page ")
    r_cls.font.size = Pt(8.0)
    r_cls.font.color.rgb = RGBColor(90, 90, 90) if is_bw else RGBColor(100, 110, 130)
    
    r_pg = p_right.add_run()
    r_pg.font.size = Pt(8.0)
    r_pg.font.color.rgb = RGBColor(90, 90, 90) if is_bw else RGBColor(100, 110, 130)
    add_xml_field(r_pg, "PAGE")

# --- CLASS DEFINITIONS WITH CITATIONS & BOOK REFERENCES ---
CLASSES_DATA = [
    {
        "name": "Soldier",
        "base": "Fighter [Player Core p.136]",
        "source_book": "Player Core [p.136-149]",
        "role": "Frontline Anchor / Chokepoint Defender",
        "hp": "10 + CON mod per level",
        "key_attr": "Strength or Dexterity",
        "perception": "Expert (Master at Lv 9)",
        "saves": "Fortitude: Expert, Reflex: Expert, Will: Trained (Expert at Lv 3)",
        "armor": "Trained in all armor and shields. Expert at Lv 11.",
        "weapons": "Expert in simple and martial weapons. Master at Lv 5.",
        "skills": "Trained in Athletics or Acrobatics, plus 3 + INT mod additional skills.",
        "social": "Tier 4 Track (5 advancements). Base: 2 Auto + 1 Class + CHA.",
        "subclass_prompt": "Combat Specialty / Fighting Style (e.g. Shield & Board, Great Weapon, Dual Wield)",
        "feats": {
            1: ["Point-Blank Shot [PC p.140]", "Reactive Strike (Standard) [PC p.138]", "Snagging Strike [PC p.140]", "Sudden Charge [PC p.140]", "Double Slice [PC p.140]"],
            2: ["Aggressive Block [PC p.141]", "Assisting Shot [PC p.141]", "Brutal Shove [PC p.141]", "Dueling Parry [PC p.141]", "Intimidating Strike [PC p.141]"],
            4: ["Dual-Handed Assault [PC p.142]", "Knockdown [PC p.142]", "Parting Shot [PC p.142]", "Powerful Shove [PC p.142]", "Shield Bash Mastery [PC p.142]"],
            6: ["Advanced Weapon Training [PC p.143]", "Disorienting Opening [PC p.143]", "Furious Focus [PC p.143]", "Reflexive Shield [PC p.143]", "Shield Warden [PC p.143]"],
            8: ["Blind-Fight [PC p.144]", "Disarming Twist [PC p.144]", "Felling Strike [PC p.144]", "Positioning Assault [PC p.144]", "Sudden Leap [PC p.144]"],
            10: ["Certain Strike [PC p.145]", "Combat Reflexes [PC p.145]", "Debilitating Shot [PC p.145]", "Disruptive Stance [PC p.145]", "Overpowering Attack [PC p.145]"]
        }
    },
    {
        "name": "Survivor",
        "base": "Rogue [Player Core p.168]",
        "source_book": "Player Core [p.168-181]",
        "role": "Deadly Skirmisher / Evasive Finisher / Urban Scavenger",
        "hp": "8 + CON mod per level",
        "key_attr": "Dexterity (or Strength / Charisma / Intelligence)",
        "perception": "Expert (Master at Lv 7, Legendary at Lv 13)",
        "saves": "Fortitude: Trained (Expert at Lv 9), Reflex: Expert (Master at Lv 7), Will: Expert (Master at Lv 17)",
        "armor": "Trained in light armor and unarmored defense. Expert at Lv 13.",
        "weapons": "Trained in simple weapons, rapiers, sap, shortbow, shortsword. Expert at Lv 5.",
        "skills": "Trained in Stealth or Thievery, plus 7 + INT mod additional skills (Skill increase EVERY level).",
        "social": "Tier 3 Track (6 advancements). Base: 2 Auto + 2 Class + CHA.",
        "subclass_prompt": "Racket / Survival Focus (Scoundrel, Ruffian, Thief, Mastermind)",
        "feats": {
            1: ["Urban Infiltration Mastery [New]", "Nimble Dodge [PC p.172]", "Trap Finder [PC p.172]", "You're Next [PC p.172]", "Twin Feint [PC p.172]"],
            2: ["Mobility [PC p.173]", "Quick Draw [PC p.173]", "Minor Magic (Tech Rig) [PC p.173]", "Distracting Feint [PC p.173]", "Underhanded Assault [PC p.173]"],
            4: ["Dread Striker [PC p.174]", "Poison Weapon (Chemical) [Modified]", "Scout's Warning [PC p.174]", "Twin Distraction [PC p.174]", "Reactive Evasion [PC p.174]"],
            6: ["Analyze Weakness [PC p.175]", "Gang Up [PC p.175]", "Light Step [PC p.175]", "Skirmish Strike [PC p.175]", "Watch Your Back [PC p.175]"],
            8: ["Blind-Fight [PC p.176]", "Bullseye [PC p.176]", "Nimble Roll [PC p.176]", "Sly Striker [PC p.176]", "Opportune Backstab [PC p.176]"],
            10: ["Sneak Savant [PC p.177]", "Tactical Entry [PC p.177]", "Precise Debilitations [PC p.177]", "Uncanny Dodge [PC p.177]"]
        }
    },
    {
        "name": "Pugilist",
        "base": "Monk [Player Core 2 p.140]",
        "source_book": "Player Core 2 [p.140-155]",
        "role": "Heavy Frontline Brawler / Maneuver Disruptor",
        "hp": "10 + CON mod per level",
        "key_attr": "Strength or Dexterity",
        "perception": "Trained (Expert at Lv 5, Master at Lv 15)",
        "saves": "Expert in Fortitude, Reflex, and Will saves (All 3 start Expert!).",
        "armor": "Expert in unarmored defense (Master at Lv 13, Legendary at Lv 17).",
        "weapons": "Trained in unarmed attacks and monk weapons. Expert at Lv 5.",
        "skills": "Trained in Athletics or Acrobatics, plus 4 + INT mod additional skills.",
        "social": "Tier 4 Track (5 advancements). Base: 2 Auto + 1 Class + CHA.",
        "subclass_prompt": "Brawling Style / Stance (Bare-Knuckle, Iron Guard, Haymaker, Grappler)",
        "feats": {
            1: ["Flurry of Blows (Standard) [PC2 p.144]", "Dragon Stance [PC2 p.144]", "Gorilla Stance [PC2 p.144]", "Wolf Stance [PC2 p.144]", "Crane Stance [PC2 p.144]"],
            2: ["Brawling Focus [PC2 p.145]", "Crushing Grab [PC2 p.145]", "Dancing Leaf [PC2 p.145]", "Deflect Arrows/Bolts [PC2 p.145]", "Shooting Star Stance [PC2 p.145]"],
            4: ["Defensive Posture [PC2 p.146]", "Flurry of Maneuvers [PC2 p.146]", "Guarded Movement [PC2 p.146]", "Stand Still (Reaction) [PC2 p.146]", "Knockout Blow [PC2 p.146]"],
            6: ["Crane Flutter [PC2 p.147]", "Dragon Roar [PC2 p.147]", "Water Dance [PC2 p.147]", "Careful Grapple [PC2 p.147]"],
            8: ["Iron Bones [PC2 p.148]", "Wall Run [PC2 p.148]", "Mixed Martial Arts [PC2 p.148]", "Clinch Crusher [PC2 p.148]"],
            10: ["Knockout Mastery [PC2 p.149]", "Sleeper Hold [PC2 p.149]", "Wind Stance Strike [PC2 p.149]", "Relentless Flurry [PC2 p.149]"]
        }
    },
    {
        "name": "Rake",
        "base": "Swashbuckler [Player Core 2 p.176]",
        "source_book": "Player Core 2 [p.176-191]",
        "role": "Mobile Duelist / High-AC Skirmisher / Panache Flanker",
        "hp": "10 + CON mod per level",
        "key_attr": "Dexterity",
        "perception": "Expert (Master at Lv 11)",
        "saves": "Fortitude: Trained (Expert at Lv 9), Reflex: Expert (Master at Lv 7), Will: Expert (Master at Lv 15)",
        "armor": "Trained in light armor and unarmored defense. Expert at Lv 13.",
        "weapons": "Trained in simple, martial, and agile/finesse weapons. Expert at Lv 5.",
        "skills": "Trained in Acrobatics, Style skill, plus 4 + INT mod additional skills.",
        "social": "Tier 2 Track (10 advancements). Base: 2 Auto + 3 Class + CHA.",
        "subclass_prompt": "Swashbuckler Style (Braggart, Fencer, Gymnast, Battledancer, Wit)",
        "feats": {
            1: ["Confident Finisher (Standard) [PC2 p.180]", "Dueling Parry [PC2 p.180]", "Disarming Flair [PC2 p.180]", "One-For-All [PC2 p.180]", "You're Next [PC2 p.180]"],
            2: ["After You [PC2 p.181]", "Antagonize [PC2 p.181]", "Charmed Life [PC2 p.181]", "Finishing Follow-Through [PC2 p.181]", "Tumble Behind [PC2 p.181]"],
            4: ["Flamboyant Athlete [PC2 p.182]", "Goading Feint [PC2 p.182]", "Leading Dance [PC2 p.182]", "Swaggering Initiative [PC2 p.182]", "Twin Parry [PC2 p.182]"],
            6: ["Agile Maneuvers [PC2 p.183]", "Bleeding Finisher [PC2 p.183]", "Combination Finisher [PC2 p.183]", "Exemplary Finisher [PC2 p.183]"],
            8: ["Bleeding Riposte [PC2 p.184]", "Dueling Riposte (Reaction) [Modified]", "Nimble Dodge [PC2 p.184]", "Stunning Finisher [PC2 p.184]"],
            10: ["Buckler Flurry [PC2 p.185]", "Derring-do [PC2 p.185]", "Mobile Riposte [PC2 p.185]", "Targeted Finisher [PC2 p.185]"]
        }
    },
    {
        "name": "Officer",
        "base": "Champion [Player Core 2 p.18]",
        "source_book": "Player Core 2 [p.18-35]",
        "role": "Tactical Commander / Line Anchor / Vanguard Aegis",
        "hp": "10 + CON mod per level",
        "key_attr": "Strength or Dexterity",
        "perception": "Trained (Expert at Lv 11)",
        "saves": "Fortitude: Expert, Reflex: Trained (Expert at Lv 9), Will: Expert (Master at Lv 11)",
        "armor": "Trained in all armor and shields. Expert at Lv 7, Master at Lv 13.",
        "weapons": "Trained in simple and martial weapons. Expert at Lv 5.",
        "skills": "Trained in Warfare Lore, Athletics or Diplomacy, plus 3 + INT mod additional skills.",
        "social": "Tier 3 Track (6 advancements). Base: 2 Auto + 2 Class + CHA.",
        "subclass_prompt": "Commission / Command Doctrine (King's Guard Aegis, Trench Captain, Sump Marshal)",
        "feats": {
            1: ["Officer's Reaction (Vanguard Intercept) [Modified]", "Weight of Guilt [PC2 p.24]", "Vanguard Stance [PC2 p.24]", "Rallying Cry [PC2 p.24]"],
            2: ["Assisting Shot [PC2 p.25]", "Coordinated Strike [PC2 p.25]", "Shield Warden [PC2 p.25]", "Commanding Presence [PC2 p.25]", "Hold the Line [New]"],
            4: ["Aura of Courage [PC2 p.26]", "Defensive Shield Team [PC2 p.26]", "Disarming Command [PC2 p.26]", "Knockdown Order [PC2 p.26]"],
            6: ["Attack of Opportunity (Command) [PC2 p.27]", "Shield Ally Master [PC2 p.27]", "Tactical Reposition [PC2 p.27]"],
            8: ["Greater Intercept [PC2 p.28]", "Advance Order! [PC2 p.28]", "Quick Shield Block [PC2 p.28]"],
            10: ["Shield of Grace [PC2 p.29]", "Mass Command Directive [PC2 p.29]", "Aura of Steadfast Resolve [PC2 p.29]"]
        }
    },
    {
        "name": "Clockwork Engineer",
        "base": "Inventor [Guns & Gears p.14]",
        "source_book": "Guns & Gears [p.14-29]",
        "role": "Defensive Mesh Frontliner / Shoulder Turret / Construct Master",
        "hp": "8 + CON mod per level",
        "key_attr": "Intelligence",
        "perception": "Trained (Expert at Lv 7, Master at Lv 15)",
        "saves": "Fortitude: Expert, Reflex: Trained (Expert at Lv 9), Will: Expert (Master at Lv 17)",
        "armor": "Trained in light and medium armor. Expert at Lv 13.",
        "weapons": "Trained in simple and martial weapons. Expert at Lv 5.",
        "skills": "Trained in Crafting, plus 3 + INT mod additional skills.",
        "social": "Tier 4 Track (5 advancements). Base: 2 Auto + 1 Class + CHA.",
        "subclass_prompt": "Innovation Type: [Combat Backpack (Turret + Temp HP)] or [Construct Companion] or [Armor/Weapon Innovation]",
        "feats": {
            1: ["Combat Backpack Module [New Innovation]", "Explosive Leap [G&G p.18]", "Variable Core [G&G p.18]", "Tamper [G&G p.18]"],
            2: ["Collapse Armor/Weapon [G&G p.19]", "Reverse Engineer [G&G p.19]", "Searing Restoration [G&G p.19]", "Clockwork Pet [G&G p.19]"],
            4: ["Automated Turret Overwatch [New]", "Gadget Specialist [G&G p.20]", "Megavolt Shock [G&G p.20]", "Overdrive Mastery [G&G p.20]"],
            6: ["Clockwork Shield Rig [G&G p.21]", "Megaton Strike [G&G p.21]", "Deflective Mesh Upgrade [New]"],
            8: ["Gigavolt Discharge [G&G p.22]", "Overclocked Servos [G&G p.22]", "Persistent Deflection Ring [New]"],
            10: ["Endless Gadgets [G&G p.23]", "Distortion Capacitor [G&G p.23]", "Electromagnetic Pulse Blast [G&G p.23]"]
        }
    },
    {
        "name": "Clockwork Rifleman",
        "base": "Gunslinger [Guns & Gears p.106]",
        "source_book": "Guns & Gears [p.106-121]",
        "role": "Long-Range Sniper / Overwatch Artillery / Ballistic Slayer",
        "hp": "8 + CON mod per level",
        "key_attr": "Dexterity",
        "perception": "Expert (Master at Lv 7, Legendary at Lv 13)",
        "saves": "Fortitude: Trained (Expert at Lv 9), Reflex: Expert (Master at Lv 7), Will: Trained (Expert at Lv 3)",
        "armor": "Trained in light armor and unarmored defense. Expert at Lv 13.",
        "weapons": "Expert in simple and martial firearms and crossbows. Master at Lv 5, Legendary at Lv 13.",
        "skills": "Trained in Acrobatics or Crafting, plus 3 + INT mod additional skills.",
        "social": "Tier 4 Track (5 advancements). Base: 2 Auto + 1 Class + CHA.",
        "subclass_prompt": "Way of the Rifle (Way of the Sniper, Way of the Vanguard, Way of the Pistolero)",
        "feats": {
            1: ["Singular Neither Efficiency [New]", "Cover Fire [G&G p.110]", "Crossbow Crack Shot [G&G p.110]", "Hit the Dirt! [G&G p.110]", "Munitions Crafting [Modified]"],
            2: ["Defensive Armament [G&G p.111]", "Fake Out [G&G p.111]", "Quick Draw [G&G p.111]", "Warning Shot [G&G p.111]", "Pistol Twirl [G&G p.111]"],
            4: ["Alchemical Shot [G&G p.112]", "Black Powder Boost [G&G p.112]", "Paired Shots [G&G p.112]", "Running Reload [G&G p.112]", "Sniper's Aim [G&G p.112]"],
            6: ["Advanced Munitions [G&G p.113]", "Bullet Split [G&G p.113]", "Pistolero's Retort [G&G p.113]", "Covering Fire Reaction [G&G p.113]"],
            8: ["Grit and Tenacity [G&G p.114]", "Incredible Aim [G&G p.114]", "Leap and Fire [G&G p.114]", "Smoke Curtain Shot [G&G p.114]"],
            10: ["Call Shot [G&G p.115]", "Deflecting Shot [G&G p.115]", "Piercing Shot [G&G p.115]", "Trick Shot Ballistics [G&G p.115]"]
        }
    },
    {
        "name": "Scout",
        "base": "Ranger [Player Core p.152]",
        "source_book": "Player Core [p.152-167]",
        "role": "Wilderness Tracker / Range Recon / Ambush Specialist",
        "hp": "10 + CON mod per level",
        "key_attr": "Dexterity or Strength",
        "perception": "Expert (Master at Lv 7, Legendary at Lv 15)",
        "saves": "Fortitude: Expert, Reflex: Expert, Will: Trained (Expert at Lv 3)",
        "armor": "Trained in light and medium armor. Expert at Lv 13.",
        "weapons": "Trained in simple and martial weapons. Expert at Lv 5.",
        "skills": "Trained in Nature or Survival, plus 4 + INT mod additional skills.",
        "social": "Tier 4 Track (5 advancements). Base: 2 Auto + 1 Class + CHA.",
        "subclass_prompt": "Hunter's Edge (Flurry, Precision, Outwit)",
        "feats": {
            1: ["Hunt Prey (Standard) [PC p.156]", "Crossbow Ace [PC p.156]", "Animal Companion [PC p.156]", "Gravity Weapon [PC p.156]", "Twin Takedown [PC p.156]"],
            2: ["Hunter's Aim [PC p.157]", "Quick Draw [PC p.157]", "Monster Hunter [PC p.157]", "Distracting Shot [PC p.157]", "Far Shot [PC p.157]"],
            4: ["Companion's Cry [PC p.158]", "Disrupt Prey (Reaction) [PC p.158]", "Running Reload [PC p.158]", "Scout's Warning [PC p.158]", "Twin Parry [PC p.158]"],
            6: ["Hazard Finder [PC p.159]", "Skirmish Strike [PC p.159]", "Swift Tracker [PC p.159]", "Master Monster Hunter [PC p.159]"],
            8: ["Blind-Fight [PC p.160]", "Deadly Aim [PC p.160]", "Warden's Step [PC p.160]", "Camouflage [PC p.160]"],
            10: ["Penetrating Shot [PC p.161]", "Targeting Shot [PC p.161]", "Warden's Boon [PC p.161]", "Master's Edge [PC p.161]"]
        }
    },
    {
        "name": "Noble",
        "base": "Modified Bard [Player Core p.94]",
        "source_book": "Player Core [p.94-105] / Clockwork Cities Rules",
        "role": "High Influence / Retainer Wall / Court Authority",
        "hp": "8 + CON mod per level",
        "key_attr": "Charisma",
        "perception": "Expert (Master at Lv 11)",
        "saves": "Fortitude: Trained (Expert at Lv 9), Reflex: Trained (Expert at Lv 11), Will: Expert (Master at Lv 7)",
        "armor": "Trained in light armor and unarmored defense (plus rapier/dueling blade exemption).",
        "weapons": "Trained in simple weapons, rapiers, shortswords, dueling canes. Expert at Lv 11.",
        "skills": "Trained in Society, Diplomacy, plus 4 + INT mod additional skills.",
        "social": "Tier 1 Track (13 advancements). Base: 2 Auto + 4 Class + CHA.",
        "subclass_prompt": "House Lineage & Standing (Imperial Line, Merchant Patrician, Diplomatic Ambassador)",
        "feats": {
            1: ["Aristocratic Retainer (Meatshield Wall) [New]", "Courtly Graces [PC p.254]", "Noble Composure [New]"],
            2: ["Peer Authority [New]", "Bodyguard Reaction Intercept [New]", "Entourage Expansion (2nd Retainer) [New]", "Inspire Fortitude [PC p.98]"],
            4: ["Legal Immunity Directive [New]", "Diplomatic Leverage [New]", "Heraldic Mandate [New]", "Noble Duellist [New]"],
            6: ["Aura of Majesty [New]", "Elite Retainer Guard (Armored) [New]", "Call In Sovereign Marker [New]"],
            8: ["Commanding Aristocracy [New]", "House Retinue (3rd Retainer) [New]", "Untouchable Social Status [New]"],
            10: ["Peerless Patronage [New]", "Sovereign Decrees [New]", "Inviolable Diplomatic Immunity [New]"]
        }
    },
    {
        "name": "Merchant",
        "base": "Modified Bard [Player Core p.94]",
        "source_book": "Player Core [p.94-105] / Clockwork Cities Rules",
        "role": "Financial Leverage / Factor Networks / Mercenary Bodyguards",
        "hp": "8 + CON mod per level",
        "key_attr": "Charisma or Intelligence",
        "perception": "Expert (Master at Lv 11)",
        "saves": "Fortitude: Trained (Expert at Lv 9), Reflex: Trained (Expert at Lv 11), Will: Expert (Master at Lv 7)",
        "armor": "Trained in light armor and unarmored defense.",
        "weapons": "Trained in simple weapons, light crossbows, heavy canes. Expert at Lv 11.",
        "skills": "Trained in Society, Deception, Accounting Lore, plus 4 + INT mod additional skills.",
        "social": "Tier 1 Track (13 advancements). Base: 2 Auto + 4 Class + CHA.",
        "subclass_prompt": "Trading Charter Focus (Neither-Tech Factor, Spore & Spice Guild, Sky-Dock Shipper)",
        "feats": {
            1: ["Hired Muscle (Mercenary Retainer) [New]", "Bargain Hunter [PC p.253]", "Guild Factorship [New]"],
            2: ["Double Bookkeeping [New]", "Mercenary Contract Expansion [New]", "Material Requisition (+20% Gear Fund) [New]"],
            4: ["Expedited Customs Clearance [New]", "Black Market Buy-In [New]", "Bribery Matrix [New]", "Defensive Contract [New]"],
            6: ["Armed Caravan Retinue [New]", "Cartel Monopoly [New]", "Heavy Plate Mercenary Guard [New]"],
            8: ["Market Cornering [New]", "Syndicate Buying Power [New]", "Mercenary Commander [New]"],
            10: ["Commercial Hegemony [New]", "Infinite Line of Credit [New]", "Unbreakable Guild Retinue [New]"]
        }
    },
    {
        "name": "Grey Marketeer",
        "base": "Modified Bard [Player Core p.94] + Rogue Skills",
        "source_book": "Player Core [p.94, p.168] / Clockwork Cities Rules",
        "role": "Underworld Broker / Smuggler / Black-Market Infiltrator",
        "hp": "8 + CON mod per level",
        "key_attr": "Charisma or Dexterity",
        "perception": "Expert (Master at Lv 9)",
        "saves": "Fortitude: Trained (Expert at Lv 9), Reflex: Expert (Master at Lv 7), Will: Expert (Master at Lv 9)",
        "armor": "Trained in light armor and unarmored defense. Expert at Lv 13.",
        "weapons": "Trained in simple weapons, hand crossbows, concealed daggers. Expert at Lv 9.",
        "skills": "Trained in Deception, Stealth, Underworld Lore, plus 5 + INT mod additional skills.",
        "social": "Tier 2 Track (10 advancements). Base: 2 Auto + 3 Class + CHA.",
        "subclass_prompt": "Syndicate Specialty (Contraband Runner, Fence & Counterfeiter, Shadow Broker)",
        "feats": {
            1: ["Jitter Shunt (Bootleg Arc Deflector) [New]", "Contraband Cache [New]", "Underworld Slang [New]", "Shadow Asset (Concealed Retainer) [New]"],
            2: ["Fence Stolen Goods [New]", "Distracting Payoff [New]", "False Identity Papers [New]", "Slip into Shadows [PC p.173]"],
            4: ["Black Market Procurement [New]", "Blind Spot Bribery [New]", "Underground Safehouse [New]", "Poison Network [New]"],
            6: ["Shadow Syndicate Node [New]", "Lookout Warnings (Reaction) [New]", "Smuggler's Escape Route [New]"],
            8: ["Syndicate Enforcer Cohort [New]", "Deep Cover Infiltration [New]", "Ghost Contraband [New]"],
            10: ["Underworld Kingpin [New]", "Shadow Network Immunity [New]", "Unseen Syndicate Cell [New]"]
        }
    },
    {
        "name": "Chirurgeon",
        "base": "Alchemist (Chirurgeon) [Player Core 2 p.44]",
        "source_book": "Player Core 2 [p.44-59] / AISummary/20_Healing.md",
        "role": "Triage Field Medic / Drone Protector / Convalescence Doctor",
        "hp": "8 + CON mod per level (53 HP at Lv 5)",
        "key_attr": "Intelligence",
        "perception": "Trained (Expert at Lv 9)",
        "saves": "Fortitude: Expert (Master at Lv 15), Reflex: Trained (Expert at Lv 7), Will: Expert (Master at Lv 11)",
        "armor": "Trained in light armor and unarmored defense. Expert at Lv 13.",
        "weapons": "Trained in simple weapons, scalpels, surgical saws, injector pistols. Expert at Lv 11.",
        "skills": "Trained in Medicine, Crafting, Academia Lore, plus 4 + INT mod additional skills.",
        "social": "Tier 3 Track (6 advancements). Base: 2 Auto + 2 Class + CHA.",
        "subclass_prompt": "Medical Doctrine: Field Triage, Surgical Prosthetics, or Chemical Antidotes",
        "feats": {
            1: ["Clockwork Triage Drone [New]", "Field Triage [Modified]", "Active Convalescence [New]", "Alchemical Crafting [PC2 p.46]"],
            2: ["Battle Medicine [PC p.254]", "Revivifying Mutagen / Stimulant [PC2 p.50]", "Antidote Synthesis [PC2 p.50]", "Surgical Precision [New]"],
            4: ["Automated Drone Sentry [New]", "Continuous Convalescence [New]", "Elixir of Life Formulation [PC2 p.52]", "Field Surgery [New]"],
            6: ["Combined Elixirs [PC2 p.53]", "Drone Armor Deflection Upgrade [New]", "Emergency Resuscitation Injection [New]"],
            8: ["Greater Field Triage (3d6+6) [New]", "Permanent Stabilizer Drones [New]", "Advanced Convalescence [New]"],
            10: ["True Medical Miracle [New]", "Panacea Formulation [PC2 p.55]", "Master Drone Interception [New]"]
        }
    },
    {
        "name": "Scholar",
        "base": "Modified Investigator [Player Core 2 p.40]",
        "source_book": "Player Core 2 [p.40-55] / ClockworkPathfinder/Classes/Scholar.md",
        "role": "Predictive Tactical Buffer / Actuarial AC Evasion / Ballistic Calculus",
        "hp": "8 + CON mod per level (53 HP at Lv 5)",
        "key_attr": "Intelligence",
        "perception": "Expert (Master at Lv 9, Legendary at Lv 17)",
        "saves": "Fortitude: Trained (Expert at Lv 11), Reflex: Trained (Expert at Lv 7), Will: Expert (Master at Lv 5)",
        "armor": "Trained in light armor and unarmored defense. Expert at Lv 13.",
        "weapons": "Trained in simple weapons, rapiers, shortswords, canes. Expert at Lv 5.",
        "skills": "Trained in Society, Academia Lore, plus 5 + INT mod additional skills (Skill increase EVERY level).",
        "social": "Tier 2 Track (10 advancements). Base: 2 Auto + 3 Class + CHA.",
        "subclass_prompt": "Academic Specialty: [Accountant/Actuary (AC Defense)] or [Architect (Hardness)] or [Natural Philosopher (Attack)]",
        "feats": {
            1: ["Analytical Assessment (1 AP) [New]", "Actuarial Risk Assessment (+1/+2 AC) [New]", "Known Weakness [PC2 p.44]", "Combat Cartography [New]"],
            2: ["Tactical Instruction (Party Telemetry) [New]", "Encyclopedic Recall [PC2 p.44]", "Legal Retainer [New]"],
            4: ["NeitherTeck Tuning (+2 Max AP) [New]", "Applied Ballistics [New]", "Forensic Audit Matrix [New]"],
            6: ["Predictive Counter-Measure (Reaction +3 AC) [New]", "Blueprint Memory [New]", "Tactical Evade [New]"],
            8: ["NeitherTeck Advanced Calibration (+2 Max AP) [New]", "Zone & Neither Theory [New]", "Stress-Point Demolition [New]"],
            10: ["Actuarial Certainty [New]", "Civic Authority Mandate [New]", "Mass Predictive Defense Grid [New]"]
        }
    }
]

CUSTOM_FEATS_DETAIL = {
    "Soldier": [
        ("Reactive Strike (Standard)", "Level 1", "Modified (Free Feature)",
         "Trigger: A creature within your reach uses a manipulate action, move action, makes a ranged attack, or leaves a square. "
         "Make a melee Strike against the triggering creature. If your Strike is a critical hit and the trigger was a manipulate action, you disrupt that action. [PC p.138]")
    ],
    "Survivor": [
        ("Urban Infiltration Mastery", "Level 1", "New",
         "You gain a +1 circumstance bonus to Stealth checks to Hide and Sneak, Thievery checks to Pick a Lock, and Athletics checks to Climb on urban surfaces, brick, chimneys, or scaffolding."),
        ("Poison Weapon (Chemical)", "Level 4", "Modified",
         "You apply a chemical solvent, spore paste, or Neither residue to an agile/finesse weapon or ammunition as a single action. Your next successful strike deals 1d4 persistent chemical damage. [PC p.174]")
    ],
    "Pugilist": [
        ("Flurry of Blows (Standard)", "Level 1", "Unchanged",
         "Make two unarmed Strikes. If both hit the same creature, combine their damage for the purpose of resistances and weaknesses. [PC2 p.144]"),
        ("Hardened Knuckles", "Level 5", "Modified (Replaces Mystic Strikes)",
         "Conditioned bone density and leaded wraps allow your unarmed strikes to count as magic for overcoming physical resistances. [PC2 p.142]"),
        ("Metal Knuckles", "Level 9", "Modified (Replaces Metal Strikes)",
         "Devastating kinetic leverage allows your unarmed strikes to bypass hardness and count as Cold Iron and Silver. [PC2 p.142]")
    ],
    "Rake": [
        ("Confident Finisher (Standard)", "Level 1", "Unchanged",
         "Make a Strike with a finesse or agile weapon. If it hits, you deal an additional 2d6 precision damage (improves at higher levels). Even on a failure (not critical failure), you deal half precision damage. [PC2 p.180]"),
        ("Dueling Riposte", "Level 8", "Modified",
         "Trigger: A creature within reach critically fails a Strike against you while you have a dueling parry active. Strike the triggering foe. [PC2 p.184]")
    ],
    "Officer": [
        ("Officer's Reaction (Vanguard Intercept)", "Level 1", "Modified",
         "Trigger: An enemy within 15 feet hits an ally with a Strike. You reduce the damage by 2 + your level, and you or an ally may take a 5-foot step. [PC2 p.22]"),
        ("Hold the Line", "Level 2", "New",
         "When you hit with an attack of opportunity or intercept reaction, the triggering enemy's speed is reduced by 10 feet until the start of its next turn.")
    ],
    "Clockwork Engineer": [
        ("Combat Backpack Module", "Level 1", "New Innovation",
         "Your shoulder-mounted chassis grants +1 circumstance bonus to AC and 2 x Level temporary hit points each battle. As a 1-action command, your automated turret fires a 60 ft strike (2d8+3 ballistic)."),
        ("Deflective Mesh Upgrade", "Level 6", "New",
         "Increases the backpack's temp HP buffer by +2 additional temp HP per level (Total 4 x Level temp HP) each combat.")
    ],
    "Clockwork Rifleman": [
        ("Singular Neither Efficiency", "Level 1", "New",
         "You gain exceptional marksmanship with energy capacitors. All gunslinger class deeds, Slinger's Reloads, and feats function equally with Neither-tech cartridge weapons and standard firearms."),
        ("Munitions Crafting", "Level 1", "Modified",
         "Gain daily infused reagents to craft specialized cartridges, including tracer rounds, armor-piercing slugs, and Neither-dampening rounds. [G&G p.108]")
    ],
    "Scout": [
        ("Hunt Prey (Standard)", "Level 1", "Unchanged",
         "Designate a single creature within 100 feet as your prey. You gain a +2 circumstance bonus to Perception to Seek your prey and Survival to Track it, and ignore first range increment penalty. [PC p.156]"),
        ("Hunter's Edge (Flurry / Precision / Outwit)", "Level 1", "Modified",
         "Flurry: Reduces MAP to -3/-6 (-2/-4 with agile). Precision: Deals +1d8 precision damage on your first hit each round. [PC p.153]")
    ],
    "Noble": [
        ("Aristocratic Retainer (Meatshield Wall)", "Level 1", "New",
         "You command household retainers who intercept blows. When you take damage, you can redirect 50% of the damage to your bodyguard retainer's hit pool."),
        ("Bodyguard Reaction Intercept", "Level 2", "New",
         "Trigger: You are targeted with an attack. Your bodyguard steps into the line of fire, granting you +2 circumstance bonus to AC against the triggering attack.")
    ],
    "Merchant": [
        ("Hired Muscle (Mercenary Retainer)", "Level 1", "New",
         "You retain bonded mercenary guards paid via guild counting-house funds. Retainers absorb 50% of incoming damage to protect your investment."),
        ("Material Requisition (+20% Gear Fund)", "Level 2", "New",
         "You receive wholesale commercial discounts. You gain +20% bonus funds for starting and downtime equipment and consumables.")
    ],
    "Grey Marketeer": [
        ("Jitter Shunt (Bootleg Arc Deflector)", "Level 1", "New",
         "You carry a jury-rigged capacitor shunt on your belt. When an incoming shock or electrical effect hits you, spend 1 reaction to reduce damage by 10."),
        ("Contraband Cache", "Level 1", "New",
         "Once per day, access a hidden urban dead-drop to pull a required mundane tool, lockpick, or consumable without purchasing it.")
    ],
    "Chirurgeon": [
        ("Clockwork Triage Drone", "Level 1", "New",
         "Reaction: When an ally within 30 feet takes damage, deploy a drone to intercept, reducing the incoming damage by 8 points (up to 6 times per battle)."),
        ("Active Convalescence", "Level 1", "New",
         "During camp rest with No Strenuous Activity and Environmental Shift <= 2.0, heal 1d6 per INT modifier for Critical wounds (daily) and Mortal wounds (weekly). [AISummary/20_Healing.md]"),
        ("Field Triage", "Level 1", "Modified",
         "Two Actions: Heal an adjacent wounded ally for 2d6 + 4 hit points (usable 3 times per combat).")
    ],
    "Scholar": [
        ("Analytical Assessment", "Level 1", "New (Investigator Variant)",
         "Spend 1 AP to evaluate a foe within 60 ft and roll a d20. You may substitute this d20 for an attack roll using your Intelligence modifier."),
        ("Actuarial Risk Assessment", "Level 1", "New",
         "Party Telemetry: Spend 2 AP to broadcast evasive trajectory coordinates, granting all allies within 30 ft a +1 circumstance bonus to AC (+2 in High Radiant) and saves."),
        ("Predictive Counter-Measure", "Level 6", "New",
         "Reaction: When you or an ally within 30 ft is attacked, spend 2 AP (self) or 3 AP (ally) to grant an instantaneous +3 circumstance bonus to AC.")
    ]
}

def generate_build_progression_file(is_bw=False):
    doc = docx.Document()
    for s in doc.sections:
        s.top_margin = Inches(0.5); s.bottom_margin = Inches(0.5)
        s.left_margin = Inches(0.5); s.right_margin = Inches(0.5)

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_title = p_title.add_run("CLOCKWORK CITIES PATHFINDER\nCLASS BUILD PROGRESSION WORKBOOK (LEVELS 1–10)")
    r_title.font.name = "Arial"; r_title.font.size = Pt(17); r_title.font.bold = True
    r_title.font.color.rgb = RGBColor(0, 0, 0) if is_bw else RGBColor(30, 45, 70)
    
    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    sub_text = "Minimal-Ink Printable Edition (B&W)" if is_bw else "Master Fill-In Sheets for Rapid Character Creation & Leveling"
    r_sub = p_sub.add_run(f"{sub_text}\n13 Core Classes | Formatted for Print & Google Docs")
    r_sub.font.italic = True; r_sub.font.size = Pt(10.0); r_sub.font.color.rgb = RGBColor(80, 80, 80) if is_bw else RGBColor(90, 90, 90)

    doc.add_paragraph().paragraph_format.space_after = Pt(6)
    t_idx = doc.add_table(rows=1, cols=3)
    t_idx.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr = t_idx.rows[0].cells
    hdr[0].text = "Class Name"; hdr[1].text = "Base Chassis & Source Book"; hdr[2].text = "Key Attribute & Hit Points"
    for c in hdr:
        set_cell_background(c, "2C3E50", is_bw)
        for p in c.paragraphs:
            p.runs[0].font.bold = True
            p.runs[0].font.color.rgb = RGBColor(0, 0, 0) if is_bw else RGBColor(255, 255, 255)
            p.runs[0].font.size = Pt(8.5)

    for cdata in CLASSES_DATA:
        row = t_idx.add_row().cells
        row[0].text = cdata["name"]
        row[1].text = f"{cdata['base'].split('[')[0].strip()} ({cdata['source_book']})"
        row[2].text = f"{cdata['key_attr']} | {cdata['hp'].split('per')[0].strip()}"
        for c in row:
            for p in c.paragraphs:
                p.runs[0].font.size = Pt(8.0)

    # Set footer for TOC
    setup_section_footer(doc.sections[0], "Master Index", is_bw)

    for idx, cdata in enumerate(CLASSES_DATA):
        sec = doc.add_section()
        sec.top_margin = Inches(0.5); sec.bottom_margin = Inches(0.5)
        sec.left_margin = Inches(0.5); sec.right_margin = Inches(0.5)
        setup_section_footer(sec, cdata["name"], is_bw)

        p_cname = doc.add_paragraph()
        r_cn = p_cname.add_run(f"CLASS BUILD PROGRESSION: {cdata['name'].upper()}")
        r_cn.font.name = "Arial Black"; r_cn.font.size = Pt(14)
        r_cn.font.color.rgb = RGBColor(0, 0, 0) if is_bw else RGBColor(35, 55, 85)
        
        p_info = doc.add_paragraph()
        p_info.paragraph_format.space_after = Pt(4)
        r_inf = p_info.add_run(f"Base: {cdata['base']} | Source: {cdata['source_book']}\nKey Attribute: {cdata['key_attr']} | Hit Points: {cdata['hp']}")
        r_inf.font.size = Pt(8.5); r_inf.font.bold = True

        t_stats = doc.add_table(rows=3, cols=2)
        t_stats.alignment = WD_TABLE_ALIGNMENT.CENTER
        stat_rows = [
            ("Initial Proficiencies:", f"Perception: {cdata['perception']}\nSaves: {cdata['saves']}\nArmor: {cdata['armor']}\nWeapons: {cdata['weapons']}"),
            ("Class Skills & Social:", f"Trained Skills: {cdata['skills']}\nSocial Advancement: {cdata['social']}"),
            ("Character & Subclass:", f"Character Name: _______________________ Player: __________________ Level: [____]\n{cdata['subclass_prompt']}: __________________________________________")
        ]
        for r_i, (lbl, val) in enumerate(stat_rows):
            c_lbl, c_val = t_stats.rows[r_i].cells
            c_lbl.width = Inches(2.0); c_val.width = Inches(5.5)
            c_lbl.text = lbl; c_val.text = val
            set_cell_background(c_lbl, "EAECEE", is_bw)
            set_cell_margins(c_lbl, 30, 30, 45, 45); set_cell_margins(c_val, 30, 30, 45, 45)
            c_lbl.paragraphs[0].runs[0].font.bold = True; c_lbl.paragraphs[0].runs[0].font.size = Pt(8.0)
            c_val.paragraphs[0].runs[0].font.size = Pt(8.0)

        doc.add_paragraph().paragraph_format.space_after = Pt(4)

        t_prog = doc.add_table(rows=11, cols=3)
        t_prog.alignment = WD_TABLE_ALIGNMENT.CENTER
        p_hdrs = t_prog.rows[0].cells
        p_hdrs[0].width = Inches(0.8); p_hdrs[1].width = Inches(2.2); p_hdrs[2].width = Inches(4.5)
        p_hdrs[0].text = "Level"; p_hdrs[1].text = "Standard Advancements"; p_hdrs[2].text = "Your Specific Selections & Build Notes"
        for c in p_hdrs:
            set_cell_background(c, "34495E", is_bw)
            for p in c.paragraphs:
                p.runs[0].font.bold = True
                p.runs[0].font.color.rgb = RGBColor(0, 0, 0) if is_bw else RGBColor(255, 255, 255)
                p.runs[0].font.size = Pt(8.0)

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
            row[0].width = Inches(0.8); row[1].width = Inches(2.2); row[2].width = Inches(4.5)
            row[0].text = lvl; row[1].text = std; row[2].text = fill
            set_cell_margins(row[0], 20, 20, 30, 30); set_cell_margins(row[1], 20, 20, 30, 30); set_cell_margins(row[2], 20, 20, 30, 30)
            row[0].paragraphs[0].runs[0].font.bold = True; row[0].paragraphs[0].runs[0].font.size = Pt(8.0)
            row[1].paragraphs[0].runs[0].font.size = Pt(7.5); row[2].paragraphs[0].runs[0].font.size = Pt(7.5)
            if not is_bw and i % 2 == 1:
                set_cell_background(row[0], "F8F9F9", is_bw); set_cell_background(row[1], "F8F9F9", is_bw); set_cell_background(row[2], "F8F9F9", is_bw)

        pass

    fname = "bw_Clockwork_Class_Build_Progression_Lv1-10.docx" if is_bw else "Clockwork_Class_Build_Progression_Lv1-10.docx"
    out_p = Path(f"ClockworkPathfinder/Classes/buildassist/{fname}")
    doc.save(out_p)
    print("Saved:", out_p)

def generate_feats_menu_file(is_bw=False):
    doc = docx.Document()
    for s in doc.sections:
        s.top_margin = Inches(0.5); s.bottom_margin = Inches(0.5)
        s.left_margin = Inches(0.5); s.right_margin = Inches(0.5)

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_title = p_title.add_run("CLOCKWORK CITIES PATHFINDER\nCURATED CLASS FEATS MENU & RULES REFERENCE (LEVELS 1–10)")
    r_title.font.name = "Arial"; r_title.font.size = Pt(17); r_title.font.bold = True
    r_title.font.color.rgb = RGBColor(0, 0, 0) if is_bw else RGBColor(30, 45, 70)
    
    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    sub_text = "Minimal-Ink Printable Edition (B&W)" if is_bw else "Curated Class Feat Options + Full Mechanical Text for All Modified & Setting Feats"
    r_sub = p_sub.add_run(f"{sub_text}\nIncludes Direct Rulebook Citations | 13 Core Classes")
    r_sub.font.italic = True; r_sub.font.size = Pt(10.0); r_sub.font.color.rgb = RGBColor(80, 80, 80) if is_bw else RGBColor(90, 90, 90)

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    t_idx = doc.add_table(rows=1, cols=3)
    t_idx.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr = t_idx.rows[0].cells
    hdr[0].text = "Class Name"; hdr[1].text = "Source Book / Base Chassis"; hdr[2].text = "Modified / New Feats Detailed"
    for c in hdr:
        set_cell_background(c, "2C3E50", is_bw)
        for p in c.paragraphs:
            p.runs[0].font.bold = True
            p.runs[0].font.color.rgb = RGBColor(0, 0, 0) if is_bw else RGBColor(255, 255, 255)
            p.runs[0].font.size = Pt(8.5)

    for cdata in CLASSES_DATA:
        row = t_idx.add_row().cells
        row[0].text = cdata["name"]
        row[1].text = f"{cdata['source_book']}"
        num_custom = len(CUSTOM_FEATS_DETAIL.get(cdata["name"], []))
        row[2].text = f"{num_custom} Custom/Modified Feats Detailed"
        for c in row:
            for p in c.paragraphs:
                p.runs[0].font.size = Pt(8.0)

    # Set footer for TOC
    setup_section_footer(doc.sections[0], "Master Index", is_bw)

    for idx, cdata in enumerate(CLASSES_DATA):
        sec = doc.add_section()
        sec.top_margin = Inches(0.5); sec.bottom_margin = Inches(0.5)
        sec.left_margin = Inches(0.5); sec.right_margin = Inches(0.5)
        setup_section_footer(sec, cdata["name"], is_bw)

        cname = cdata["name"]
        p_hdr = doc.add_paragraph()
        r_h = p_hdr.add_run(f"{cname.upper()} — CLASS FEATS MENU & RULES REFERENCE")
        r_h.font.name = "Arial Black"; r_h.font.size = Pt(13)
        r_h.font.color.rgb = RGBColor(0, 0, 0) if is_bw else RGBColor(35, 55, 85)
        
        p_sub2 = doc.add_paragraph()
        p_sub2.paragraph_format.space_after = Pt(3)
        r_s2 = p_sub2.add_run(f"Part 1: Curated Feat Selection Menu [Source Book: {cdata['source_book']}]")
        r_s2.font.bold = True; r_s2.font.size = Pt(9.0)

        t_feats = doc.add_table(rows=7, cols=2)
        t_feats.alignment = WD_TABLE_ALIGNMENT.CENTER
        f_hdrs = t_feats.rows[0].cells
        f_hdrs[0].width = Inches(1.3); f_hdrs[1].width = Inches(6.2)
        f_hdrs[0].text = "Level Gained"; f_hdrs[1].text = "Available Class Feats (with Source Book Citations)"
        for c in f_hdrs:
            set_cell_background(c, "2C3E50", is_bw)
            for p in c.paragraphs:
                p.runs[0].font.bold = True
                p.runs[0].font.color.rgb = RGBColor(0, 0, 0) if is_bw else RGBColor(255, 255, 255)
                p.runs[0].font.size = Pt(8.5)

        for f_idx, lvl in enumerate([1, 2, 4, 6, 8, 10]):
            row = t_feats.rows[f_idx+1].cells
            row[0].width = Inches(1.3); row[1].width = Inches(6.2)
            row[0].text = f"Level {lvl} Feats"
            feat_list = cdata["feats"].get(lvl, ["See Class Document"])
            row[1].text = " • " + "\n • ".join(feat_list)
            set_cell_margins(row[0], 20, 20, 35, 35); set_cell_margins(row[1], 20, 20, 35, 35)
            row[0].paragraphs[0].runs[0].font.bold = True; row[0].paragraphs[0].runs[0].font.size = Pt(8.0)
            row[1].paragraphs[0].runs[0].font.size = Pt(8.0)
            if not is_bw and f_idx % 2 == 1:
                set_cell_background(row[0], "F4F6F6", is_bw); set_cell_background(row[1], "F4F6F6", is_bw)

        doc.add_paragraph().paragraph_format.space_after = Pt(4)

        custom_feats = CUSTOM_FEATS_DETAIL.get(cname, [])
        if custom_feats:
            p_det_hdr = doc.add_paragraph()
            p_det_hdr.paragraph_format.space_after = Pt(2)
            r_dh = p_det_hdr.add_run(f"Part 2: Full Rules Text for Modified & Setting-Created Feats ({cname})")
            r_dh.font.bold = True; r_dh.font.size = Pt(9.0)
            r_dh.font.color.rgb = RGBColor(0, 0, 0) if is_bw else RGBColor(35, 55, 85)

            t_custom = doc.add_table(rows=len(custom_feats) + 1, cols=3)
            t_custom.alignment = WD_TABLE_ALIGNMENT.CENTER
            c_hdrs = t_custom.rows[0].cells
            c_hdrs[0].width = Inches(2.2); c_hdrs[1].width = Inches(1.1); c_hdrs[2].width = Inches(4.2)
            c_hdrs[0].text = "Feat Name"; c_hdrs[1].text = "Status / Lvl"; c_hdrs[2].text = "Exact Rules Text & Mechanical Effects"
            for c in c_hdrs:
                set_cell_background(c, "34495E", is_bw)
                for p in c.paragraphs:
                    p.runs[0].font.bold = True
                    p.runs[0].font.color.rgb = RGBColor(0, 0, 0) if is_bw else RGBColor(255, 255, 255)
                    p.runs[0].font.size = Pt(8.0)

            for cf_idx, (fname, flvl, fstatus, fdesc) in enumerate(custom_feats):
                crow = t_custom.rows[cf_idx + 1].cells
                crow[0].width = Inches(2.2); crow[1].width = Inches(1.1); crow[2].width = Inches(4.2)
                crow[0].text = fname
                crow[1].text = f"{flvl}\n[{fstatus}]"
                crow[2].text = fdesc
                set_cell_margins(crow[0], 20, 20, 30, 30); set_cell_margins(crow[1], 20, 20, 30, 30); set_cell_margins(crow[2], 20, 20, 30, 30)
                crow[0].paragraphs[0].runs[0].font.bold = True; crow[0].paragraphs[0].runs[0].font.size = Pt(8.0)
                crow[1].paragraphs[0].runs[0].font.size = Pt(7.5)
                crow[2].paragraphs[0].runs[0].font.size = Pt(7.5)
                if not is_bw and cf_idx % 2 == 1:
                    set_cell_background(crow[0], "F8F9F9", is_bw); set_cell_background(crow[1], "F8F9F9", is_bw); set_cell_background(crow[2], "F8F9F9", is_bw)

        pass

    fname = "bw_Clockwork_Class_Feats_Menu_Lv1-10.docx" if is_bw else "Clockwork_Class_Feats_Menu_Lv1-10.docx"
    out_f = Path(f"ClockworkPathfinder/Classes/buildassist/{fname}")
    doc.save(out_f)
    print("Saved:", out_f)

def main():
    parser = argparse.ArgumentParser(description="Generate Build Assist Progression and Feat Menu DOCX files.")
    parser.add_argument("-bw", "--bw", action="store_true", help="Generate minimal-ink black-and-white versions (bw_*)")
    args = parser.parse_args()

    is_bw = args.bw
    print(f"Generating workbooks (B&W Minimal Ink = {is_bw})...")
    generate_build_progression_file(is_bw=is_bw)
    generate_feats_menu_file(is_bw=is_bw)
    print("Done!")

if __name__ == "__main__":
    main()
