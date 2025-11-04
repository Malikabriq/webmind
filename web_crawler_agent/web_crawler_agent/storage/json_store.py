import json, os
from config.paths import DOC_PATH

def save(docs, append=True):
    existing = []
    if append and os.path.exists(DOC_PATH):
        try:
            existing = json.load(open(DOC_PATH, "r", encoding="utf-8"))
        except:
            pass

    for d in docs:
        existing.append({"page_content": d.page_content, "metadata": d.metadata})

    json.dump(existing, open(DOC_PATH, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    return len(existing)

def load():
    if not os.path.exists(DOC_PATH):
        return []
    return json.load(open(DOC_PATH, "r", encoding="utf-8"))
