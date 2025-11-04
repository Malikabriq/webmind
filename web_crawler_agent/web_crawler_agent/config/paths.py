import os

BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_DIR = os.path.join(BASE_PATH, "data")

DOCS_DIR = os.path.join(DATA_DIR, "local_docs")
MD_DIR = os.path.join(DATA_DIR, "scraped_markdown")
DOC_PATH = os.path.join(DOCS_DIR, "stored_docs.json")

os.makedirs(DOCS_DIR, exist_ok=True)
os.makedirs(MD_DIR, exist_ok=True)
