from openai import OpenAI
import chromadb
from sentence_transformers import SentenceTransformer
import os
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)

embedder = SentenceTransformer("all-MiniLM-L6-v2")

db = chromadb.PersistentClient(path="./rag_db")

collection = db.get_or_create_collection("documents")

def ingest(texts):
    embeddings = embedder.encode(texts).tolist()

    collection.add(
        documents=texts,
        embeddings=embeddings,
        ids=[f"chunk_{i}" for i in range(len(texts))]
    )

    print(f"Ingested {len(texts)} chunks")

    def retrieve(query, n=3):
     q_embed = embedder.encode([query]).tolist()
     results = collection.query(
        query_embeddings=q_embed,
        n_results=n
    )
     return results["documents"][0]
    
    def generate(query, context_chunks):
     context = "\n\n".join(context_chunks)

     response = llm.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": f"""
Answer using ONLY this context:

{context}

If the answer isn't in the context,
say "I don't have that information."
"""
            },
            {
                "role": "user",
                "content": query
            }
        ]
    )

     return response.choices[0].message.content
    
    def ask(query):
     chunks = retrieve(query)
     return generate(query, chunks)