from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
import torch

def answer_question(docs, query):
    context = "\n\n".join(d["page_content"] for d in docs)[:7000]

    tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")
    model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")
    qa = pipeline("text2text-generation", model=model, tokenizer=tokenizer)

    prompt = f"Use only the context below.\n\nContext:\n{context}\n\nQuestion: {query}\n\nIf not in context reply: ❌ Not found."
    return qa(prompt)[0]["generated_text"]
