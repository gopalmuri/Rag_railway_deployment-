import os
import fitz
import re
import json
import time
import datetime
import spacy
from typing import List, Dict, Any
from groq import Groq

# Constants
pdf_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "uploaded_pdfs")
os.makedirs(pdf_dir, exist_ok=True)

# In-memory storage for text content
document_store = {} # {filename: [{page_no: int, text: str}]}

# Lightweight NLP
try:
    nlp = spacy.load("en_core_web_sm", disable=["ner", "parser"])
except:
    nlp = None

def clean_text(text):
    text = re.sub(r'[^\x00-\x7F]+', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def extract_text_per_page(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        page_texts = []
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text = page.get_text("text")
            cleaned = clean_text(text)
            if cleaned.strip():
                page_texts.append({
                    "page_no": page_num + 1,
                    "text": cleaned
                })
        doc.close()
        return page_texts
    except Exception as e:
        print(f"[ERROR] PDF Extraction failed: {e}")
        return []

def analyze_pdf(file_path):
    try:
        doc = fitz.open(file_path)
        num_pages = len(doc)
        total_words = 0
        for page in doc:
            text = page.get_text()
            total_words += len(text.split())
        doc.close()
        return num_pages, total_words
    except:
        return 0, 0

def process_pdf(file_path, filename, conversation_id=None):
    """Store text in memory only. No vectorization = super fast."""
    print(f"[PDF] Processing: {filename}")
    page_texts = extract_text_per_page(file_path)
    document_store[filename] = page_texts
    return True

def get_answer(query, conversation_id=None, pdf_context=None, **kwargs):
    """Simple contextual search. No vector database needed."""
    context_text = ""
    
    # Reload files if store is empty (e.g. after server restart)
    if not document_store and os.path.exists(pdf_dir):
        for f in os.listdir(pdf_dir):
            if f.endswith('.pdf'):
                process_pdf(os.path.join(pdf_dir, f), f)

    if pdf_context and pdf_context in document_store:
        pages = document_store[pdf_context]
        # Grab first 4000 chars roughly
        context_text = "\n".join([p['text'] for p in pages])[:8000]
    else:
        # Grab snippet from all documents
        for filename, pages in document_store.items():
            context_text += f"\n[Document: {filename}]\n"
            content = "\n".join([p['text'] for p in pages])
            context_text += content[:2000] # Take first 2k chars from each
            if len(context_text) > 10000: break

    if not context_text:
        return {
            "answer": "I don't see any uploaded documents. Please upload a PDF first.",
            "citations": [],
            "has_relevant_info": False
        }

    # Query Groq
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        return {"answer": "Error: GROQ_API_KEY is missing in Railway Variables.", "citations": []}
    
    client = Groq(api_key=api_key)
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are a helpful assistant. Use the provided context to answer the user's question accurately. If the answer isn't in the context, say you don't know based on the documents."},
                {"role": "user", "content": f"Context:\n{context_text}\n\nQuestion: {query}"}
            ],
            temperature=0.5
        )
        answer = response.choices[0].message.content.strip()
    except Exception as e:
        answer = f"API Error: {str(e)}"

    return {
        "answer": answer,
        "citations": [{"source_pdf": pdf_context or "Uploaded Documents", "page_numbers": [1]}],
        "follow_up_questions": ["What else is in this file?", "Can you summarize it?"],
        "has_relevant_info": True
    }

# Mocked classes to keep views.py happy
class MockCollection:
    def count(self): return len(document_store)
    def get(self, **kwargs): return {"documents": [], "embeddings": [], "metadatas": []}
    def add(self, **kwargs): pass

class MockChroma:
    def get_collection(self, name): return MockCollection()
    def create_collection(self, name): return MockCollection()

chroma_client = MockChroma()
collection_name = "mock_rag"
in_memory_chunks = {}
in_memory_embeddings = {}
in_memory_metadata = []