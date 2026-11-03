"""
Generator for Unified Markdown Editions of Build Assist:
1. ClockworkPathfinder/Classes/buildassist/Clockwork_Class_Build_Progression_Lv1-10.md
2. ClockworkPathfinder/Classes/buildassist/Clockwork_Class_Feats_Menu_Lv1-10.md
"""

from datetime import datetime
from pathlib import Path
import sys

BUILD_DIR = Path("ClockworkPathfinder/Classes/buildassist/generator")
sys.path.append(str(BUILD_DIR))

from generate_split_workbooks import CLASSES_DATA, CUSTOM_FEATS_DETAIL

OUT_DIR = Path("ClockworkPathfinder/Classes/buildassist")
date_str = datetime.now().strftime("%m/%d/%y")

def generate_progression_markdown():
    lines = [
        "# Clockwork Cities Pathfinder — Class Build Progression (Levels 1–10)",
        f"*Master Character Creation & Leveling Sheets | Date Created: {date_str}*",
        "",
        "## Quick Index",
        "",
        "| Class Name | Base Chassis & Source Book | Key Attribute & Hit Points |",
        "| :--- | :--- | :--- |"
    ]
    for c in CLASSES_DATA:
        lines.append(f"| **[{c['name']}](#{c['name'].lower().replace(' ', '-')})** | {c['base']} ({c['source_book']}) | {c['key_attr']} / {c['hp'].split('per')[0].strip()} |")
    
    lines.append("\n---\n")

    for c in CLASSES_DATA:
        cname = c["name"]
        lines.extend([
            f"## {cname}",
            f"- **Base Chassis:** {c['base']} ({c['source_book']})",
            f"- **Squad Role:** {c['role']}",
            f"- **Key Attribute:** {c['key_attr']} | **Hit Points:** {c['hp']}",
            f"- **Perception:** {c['perception']} | **Saving Throws:** {c['saves']}",
            f"- **Armor:** {c['armor']} | **Weapons:** {c['weapons']}",
            f"- **Skills:** {c['skills']}",
            f"- **Social Advancement:** {c['social']}",
            "",
            f"**Character Name:** _______________________ **Player:** __________________ **Level:** [____]  ",
            f"**{c['subclass_prompt']}:** __________________________________________",
            "",
            "### Progression Table (Levels 1–10)",
            "",
            "| Level | Standard Advancements | Specific Selections & Build Notes |",
            "|:---:|---|---|",
            "| **1** | Subclass, 1st Class Feat, Initial Skills | **Subclass:** ____________________<br>**Feat:** ____________________<br>**Starting Rig:** ____________________ |",
            "| **2** | Class Feat, Skill Feat, Social Advancement | **Class Feat:** ____________________<br>**Skill Feat:** ____________________<br>**Social Adv:** ____________________ |",
            "| **3** | General Feat, Skill Increase, Class Feature | **General Feat:** ____________________<br>**Skill Inc:** ____________________<br>**Feature:** ____________________ |",
            "| **4** | Class Feat, Skill Feat, Social Advancement | **Class Feat:** ____________________<br>**Skill Feat:** ____________________<br>**Social Adv:** ____________________ |",
            "| **5** | 4 Ability Boosts, Skill Increase, Tier 2 Tech/Strike | **Boosts:** `[ ]STR [ ]DEX [ ]CON [ ]INT [ ]WIS [ ]CHA`<br>**Skill Inc:** ____________________<br>**Tech/Strike:** ____________________ |",
            "| **6** | Class Feat, Skill Feat, Social Advancement | **Class Feat:** ____________________<br>**Skill Feat:** ____________________<br>**Social Adv:** ____________________ |",
            "| **7** | General Feat, Skill Increase, Class Feature | **General Feat:** ____________________<br>**Skill Inc:** ____________________<br>**Feature:** ____________________ |",
            "| **8** | Class Feat, Skill Feat, Social Advancement | **Class Feat:** ____________________<br>**Skill Feat:** ____________________<br>**Social Adv:** ____________________ |",
            "| **9** | Ancestry Feat, Skill Increase, Class Feature | **Ancestry Feat:** ____________________<br>**Skill Inc:** ____________________<br>**Feature:** ____________________ |",
            "| **10** | 4 Ability Boosts, Class Feat, Skill Feat, Social Adv. | **Boosts:** `[ ]STR [ ]DEX [ ]CON [ ]INT [ ]WIS [ ]CHA`<br>**Class Feat:** ____________________<br>**Skill Feat:** ____________________ |",
            "",
            f"*Clockwork Cities Pathfinder | {cname} | Date: {date_str}*",
            "\n---\n"
        ])
    
    out_p = OUT_DIR / "Clockwork_Class_Build_Progression_Lv1-10.md"
    out_p.write_text("\n".join(lines), encoding="utf-8")
    print(f"Generated Markdown: {out_p}")

def generate_feats_menu_markdown():
    lines = [
        "# Clockwork Cities Pathfinder — Curated Class Feats Menu & Rules Reference (Levels 1–10)",
        f"*Curated Setting-Legal Options & Rules Text | Date Created: {date_str}*",
        "",
        "## Quick Index",
        "",
        "| Class Name | Source Book / Base Chassis | Modified / Custom Feats Detailed |",
        "| :--- | :--- | :--- |"
    ]
    for c in CLASSES_DATA:
        num_cust = len(CUSTOM_FEATS_DETAIL.get(c['name'], []))
        lines.append(f"| **[{c['name']}](#{c['name'].lower().replace(' ', '-')})** | {c['source_book']} | {num_cust} Custom/Modified Feats |")

    lines.append("\n---\n")

    for c in CLASSES_DATA:
        cname = c["name"]
        lines.extend([
            f"## {cname}",
            f"### Part 1: Curated Feat Selection Menu [Source: {c['source_book']}]",
            "",
            "| Level Gained | Available Class Feats (with Source Book Citations) |",
            "|:---:|---|",
        ])
        for lvl in [1, 2, 4, 6, 8, 10]:
            flist = c["feats"].get(lvl, ["See Class Document"])
            flist_str = "<br>• " + "<br>• ".join(flist)
            lines.append(f"| **Level {lvl}** | {flist_str} |")
        
        custom_feats = CUSTOM_FEATS_DETAIL.get(cname, [])
        if custom_feats:
            lines.extend([
                "",
                f"### Part 2: Full Rules Text for Modified & Setting-Created Feats ({cname})",
                "",
                "| Feat Name | Status / Level | Exact Rules Text & Mechanical Effects |",
                "| :--- | :---: | :--- |"
            ])
            for fname, flvl, fstat, fdesc in custom_feats:
                lines.append(f"| **{fname}** | {flvl}<br>`[{fstat}]` | {fdesc} |")
        
        lines.extend([
            "",
            f"*Clockwork Cities Pathfinder | {cname} Feat Reference | Date: {date_str}*",
            "\n---\n"
        ])

    out_p = OUT_DIR / "Clockwork_Class_Feats_Menu_Lv1-10.md"
    out_p.write_text("\n".join(lines), encoding="utf-8")
    print(f"Generated Markdown: {out_p}")

if __name__ == "__main__":
    generate_progression_markdown()
    generate_feats_menu_markdown()

