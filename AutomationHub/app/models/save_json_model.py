import json
from pathlib import Path
def read_json(file: Path):
    if not file.exists():
        return []
    if file.stat().st_size == 0:
        with open(file, 'w', encoding='utf-8') as f:
            json.dump([], f)
    with open(file, 'r', encoding='utf-8') as f:
        content = json.load(f)
        return content

def add_to_json(file, newcontent):
    oldcontent = read_json(file)
    content = oldcontent.append(newcontent)
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(content, f, ensure_ascii=False, indent=4)