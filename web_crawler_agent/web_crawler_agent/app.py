import streamlit as st, asyncio, zipfile, io, os
from crawler.crawl_service import crawl_site, process_page
from storage.json_store import save, load
from qa.agent import answer_question
from config.paths import MD_DIR, DOC_PATH

st.set_page_config(page_title="Modular Web → Local Agent", layout="wide")
st.title("🧱 Modular Web Crawler + Local QA Agent")

tab1, tab2 = st.tabs(["🕷️ Crawl & Store", "🤖 Ask Agent"])

# --- Tab 1 ---
with tab1:
    url = st.text_input("URL to crawl:")
    mode = st.radio("Mode:", ["Single Page", "Website"])
    if st.button("Crawl"):
        max_pages = 1 if mode=="Single Page" else 5
        data = asyncio.run(crawl_site(url, max_pages))
        docs = [process_page(p) for p in (data.pages if hasattr(data,"pages") else [data])]
        total = save(docs, append=True)
        st.success(f"Saved! Total docs: {total}")

    if os.path.exists(DOC_PATH):
        st.download_button("⬇ Download JSON", open(DOC_PATH,"rb"),"stored_docs.json","application/json")

    if len(os.listdir(MD_DIR))>0:
        buf = io.BytesIO()
        with zipfile.ZipFile(buf,"w") as z:
            for f in os.listdir(MD_DIR): z.write(os.path.join(MD_DIR,f),f)
        buf.seek(0)
        st.download_button("⬇ Download Markdown ZIP", buf, "markdown.zip", "application/zip")

# --- Tab 2 ---
with tab2:
    docs = load()
    q = st.text_input("Ask:")
    if st.button("Answer") and docs:
        st.success(answer_question(docs, q))
