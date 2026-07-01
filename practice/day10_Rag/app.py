from openai import OpenAI
import chromadb
from sentence_transformers import SentenceTransformer
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Groq LLM
llm = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)

# Load embedding model
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to ChromaDB
db = chromadb.PersistentClient(path="./rag_db")
collection = db.get_or_create_collection("documents")


# ---------------------------
# INGEST
# ---------------------------
def ingest(texts):
    embeddings = embedder.encode(texts).tolist()

    collection.add(
        documents=texts,
        embeddings=embeddings,
        ids=[f"chunk_{i}" for i in range(len(texts))]
    )

    print(f"Ingested {len(texts)} chunks")


# ---------------------------
# RETRIEVE
# ---------------------------
def retrieve(query, n=3):
    q_embed = embedder.encode([query]).tolist()

    results = collection.query(
        query_embeddings=q_embed,
        n_results=n
    )

    return results["documents"][0]


# ---------------------------
# GENERATE
# ---------------------------
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


# ---------------------------
# ASK
# ---------------------------
def ask(query):
    chunks = retrieve(query)
    return generate(query, chunks)


# ---------------------------
# SAMPLE KNOWLEDGE
# ---------------------------
knowledge = [
    "Ahmad is a MERN Stack Developer with 1 year of experience.",
    "Ahmad is transitioning into AI Engineering and Agentic AI.",
    "Ahmad built a CV Analyzer using Python and Groq API in week 1.",
    "Ahmad is from Rahim Yar Khan, Pakistan.",
    "Ahmad's tech stack includes React, Node.js, MongoDB, and Express."
]

# Store knowledge
ingest(knowledge)

# Ask questions
print(ask("Where is Ahmad from?"))
print(ask("What did Ahmad build in week 1?"))
print(ask("What technologies does Ahmad know?"))