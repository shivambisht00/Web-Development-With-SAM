import json
import re

with open("progress.json", "r") as f:
    data = json.load(f)

def make_bar(p):
    filled = round(p / 10)
    empty = 10 - filled
    bar = "█" * filled + "░" * empty
    return f"`{bar}` {p}%"

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
