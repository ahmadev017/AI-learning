import chromadb

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(
    path="./chroma_db"
)
client.delete_collection("my_knowledge_base")

collection = client.create_collection("my_knowledge_base")
collection = client.get_or_create_collection("my_knowledge_base")

documents = [

"""
Ahmad is currently learning AI Engineering.
He studies embeddings, vector databases, RAG, LangChain and LLM applications.
""",

"""
Ahmad built a doctor appointment booking web application using React, Express, MongoDB and Node.js.
The application has authentication, doctor panel, admin panel and appointment booking.
"""

]

embeddings = model.encode(documents).tolist()

collection.add(
    documents=documents,
    embeddings=embeddings,
    ids=[f"doc_{i}" for i in range(len(documents))]
)

query = "when ahmad built his doctor appointment booking app project"

query_embedding = model.encode([query]).tolist()

results = collection.query(
    query_embeddings=query_embedding,
    n_results=5
)
print(results)

print(results["documents"])


##visualizing chromadb
print("Collections:")
print(client.list_collections())

print("\nNumber of documents:")
print(collection.count())

print("\nFirst document:")
print(collection.peek())

print("\nEverything:")
print(
    collection.get(
        include=["documents", "embeddings"]
    )
)