"""
Automated Git Conventional Changelog Generator
Scans commit messages and aggregates categorized releases.
"""

import subprocess
import re

def generate_changelog() -> str:
    res = subprocess.run(["git", "log", "--oneline", "-n", "30"], capture_output=True, text=True)
    commits = res.stdout.strip().split("\n")
    
    categories = {
        "Features": [],
        "Fixes": [],
        "Refactoring": [],
        "Chore": []
    }
    
    for c in commits:
        if not c: continue
        parts = c.split(" ", 1)
        if len(parts) < 2: continue
        msg = parts[1]
        
        if msg.startswith("feat"): categories["Features"].append(msg)
        elif msg.startswith("fix"): categories["Fixes"].append(msg)
        elif msg.startswith("refactor"): categories["Refactoring"].append(msg)
        else: categories["Chore"].append(msg)

    md = "# Changelog\n\n"
    for cat, items in categories.items():
        if items:
            md += f"### {cat}\n"
            for it in items:
                md += f"- {it}\n"
            md += "\n"
    return md

if __name__ == "__main__":
    print(generate_changelog())
