import json
import re

with open("progress.json", "r") as f:
    data = json.load(f)

def make_bar(p):
    if p == 0:
        color = "lightgrey"
    elif p < 50:
        color = "orange"
    elif p < 100:
        color = "yellow"
    else:
        color = "brightgreen"
    label = f"{p}%25"
    return f"![{p}%](https://img.shields.io/badge/Progress-{label}-{color}?style=flat-square)"

rows = []
for topic, info in data.items():
    bar = make_bar(info["progress"])
    rows.append(f"| **{topic}** | {bar} | {info['status']} | {info['concepts']} |")

table = """| Topic | Progress | Status | Concepts Covered |
| :--- | :--- | :--- | :--- |
""" + "\n".join(rows)

new_section = f"<!-- PROGRESS:START -->\n{table}\n<!-- PROGRESS:END -->"

with open("README.md", "r") as f:
    content = f.read()

updated = re.sub(
    r"<!-- PROGRESS:START -->.*?<!-- PROGRESS:END -->",
    new_section,
    content,
    flags=re.DOTALL
)

with open("README.md", "w") as f:
    f.write(updated)

print("README updated!")
