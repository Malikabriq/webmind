import os, markdownify
from config.paths import MD_DIR
from crawl4ai import AsyncWebCrawler
from langchain.schema import Document

async def crawl_site(url, max_pages):
    async with AsyncWebCrawler() as crawler:
        return await crawler.arun(url=url, max_pages=max_pages, markdown=True)

def process_page(page):
    md_text = getattr(page, "markdown", None)
    if not md_text:
        md_text = markdownify.markdownify(getattr(page, "content", "") or "")

    clean_lines = []
    for line in md_text.splitlines():
        line = line.strip()
        if line and not any(x in line.lower() for x in ["cookie", "advert", "accept"]):
            clean_lines.append(line)

    cleaned = "\n".join(clean_lines)

    filename = os.path.join(MD_DIR, f"page_{len(os.listdir(MD_DIR)) + 1}.md")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(cleaned)

    return Document(page_content=cleaned, metadata={"source": getattr(page, "url", "")})
