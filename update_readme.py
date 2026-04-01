import json

# JSON data read karna
with open('progress.json', 'r') as f:
    data = json.load(f)

# Table header
table_content = "| Topic | Progress | Status | Concepts Covered |\n"
table_content += "| :--- | :--- | :--- | :--- |\n"

for topic, info in data.items():
    p = info['progress']
    # Progress bar image logic
    bar = f"![{p}%](https://progress-bar.dev/{p}/)"
    table_content += f"| **{topic}** | {bar} | {info['status']} | {info['concepts']} |\n"

# README update logic
with open('README.md', 'r') as f:
    readme = f.read()

start_marker = ""
end_marker = ""

# Markers ke beech ka content replace karna
new_readme = readme.split(start_marker)[0] + start_marker + "\n" + table_content + "\n" + end_marker + readme.split(end_marker)[1]

with open('README.md', 'w') as f:
    f.write(new_readme)
