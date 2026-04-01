import json

# 1. JSON Data Load karna
try:
    with open('progress.json', 'r') as f:
        data = json.load(f)
except Exception as e:
    print(f"Error loading JSON: {e}")
    exit(1)

# 2. Table Header
table_content = "| Topic | Progress | Status | Concepts Covered |\n"
table_content += "| :--- | :--- | :--- | :--- |\n"

for topic, info in data.items():
    # Ensure progress is an integer
    p = int(info['progress'])
    
    # Alternative stable progress bar service (geps.dev)
    # Ye zyada stable hai aur GitHub par jaldi load hoti hai
    bar_url = f"https://geps.dev/progress/{p}"
    bar_img = f"![{p}%]({bar_url})"
    
    table_content += f"| **{topic}** | {bar_img} | {info['status']} | {info['concepts']} |\n"

# 3. README Read karna
try:
    with open('README.md', 'r', encoding='utf-8') as f:
        readme = f.read()
except Exception as e:
    print(f"Error reading README: {e}")
    exit(1)

start_marker = ""
end_marker = ""

if start_marker not in readme or end_marker not in readme:
    print("Error: Markers not found in README.md")
    exit(1)

# 4. Content Replace karna
parts_before = readme.split(start_marker)
parts_after = parts_before[1].split(end_marker)

new_readme = parts_before[0] + start_marker + "\n" + table_content + "\n" + end_marker + parts_after[1]

# 5. File Save karna
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(new_readme)

print("Success! README updated with stable images. 🚀")
