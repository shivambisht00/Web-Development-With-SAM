import json
import os

def update_readme():
    # 1. Load your progress data
    try:
        with open('progress.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Error: progress.json not found.")
        return

    # 2. Generate the dynamic table
    table_content = "| Topic | Progress | Status | Concepts Covered |\n"
    table_content += "| :--- | :--- | :--- | :--- |\n"

    for topic, info in data.items():
        p = info['progress']
        # Using a cleaner progress bar style
        bar = f"![{p}%](https://progress-bar.dev/{p}/?scale=100&title=Progress&width=120)"
        table_content += f"| **{topic}** | {bar} | {info['status']} | {info['concepts']} |\n"

    # 3. Read the current README
    with open('README.md', 'r', encoding='utf-8') as f:
        readme = f.read()

    # Define professional markers
    start_marker = ""
    end_marker = ""

    if start_marker not in readme or end_marker not in readme:
        print("Error: Markers not found in README.md")
        return

    # 4. Replace content between markers
    before_part = readme.split(start_marker)[0]
    after_part = readme.split(end_marker)[1]
    
    new_readme = f"{before_part}{start_marker}\n{table_content}\n{end_marker}{after_part}"

    # 5. Write back to README
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(new_readme)
    
    print("Success: README.md has been uploaded 🚀")

if __name__ == "__main__":
    update_readme()
