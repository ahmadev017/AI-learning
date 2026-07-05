# AI Engineering Interview Questions

---

# Embeddings

### What is an embedding?

### Why do we need embeddings?

### How are embeddings generated?

### Why don't we compare raw text directly?

### What is cosine similarity?

### Why is cosine similarity preferred over Euclidean distance?

### Why can opposite sentences still have high cosine similarity?

### What is semantic similarity?

### What are embeddings used for?

---

# ChromaDB

### What is ChromaDB?

### What is a vector database?

### Why not use PostgreSQL or MongoDB for semantic search?

### Why do we store documents together with embeddings?

### Why not store only embeddings?

### What is a Collection?

### What is PersistentClient?

### What is semantic search?

### What is retrieval?

### Does ChromaDB answer questions?

### Explain the RAG pipeline.

### Difference between retrieval and generation.

---

# Transformers

### What is Attention?

### Why was Attention invented?

### Explain Query, Key and Value.

### Why do we calculate Q × Kᵀ?

### Why do we divide by √dₖ?

### Why is Softmax applied?

### Why do attention weights sum to one?

### Are attention weights applied to Queries, Keys or Values?

### What is Multi-Head Attention?

### Why is Multi-Head better than Single-Head?

### Why do we need a Feed Forward Network after Attention?

### Why do Transformers use Residual Connections?

### Why is Layer Normalization needed?

### What happens if residual connections are removed?

---

# GPT Generation

### Why does GPT generate one token at a time?

### What are logits?

### Why apply Softmax after logits?

### What happens after one token is generated?

### Difference between Temperature, Top-k and Top-p?

---

# Practice Questions

* Explain embeddings to a 10-year-old.
* Explain semantic search using a library analogy.
* Explain why RAG is better than storing knowledge inside an LLM.
* Explain how ChromaDB retrieves documents.
* Draw the Transformer architecture from memory.
* Explain the complete GPT inference pipeline.


# Day 10 Interview Questions
1. Explain RAG from scratch.
2. Why chunk documents?
3. Why store both text and embeddings?
4. What remains if the LLM is removed?
5. Why doesn't the LLM know the whole vector DB?

# Day 11 (langChain)

Beginner
What is LangChain?
Why was LangChain created?
What is a Document?
What is metadata?
Why is chunking necessary?
Why do we use chunk overlap?
Intermediate
Explain the difference between from_texts() and from_documents().
Explain the role of a Retriever.
What does create_stuff_documents_chain() do?
Why does LangChain still require embeddings?
Advanced
Explain the complete execution flow when calling retrieval_chain.invoke().
Why did increasing k from 2 to 3 improve retrieval in your project?
How would you separate ingestion and querying in a production RAG system?

# Day 12 (Pdf App)

What problem does Retrieval-Augmented Generation (RAG) solve?
Why do we split documents into chunks before embedding?
What is the difference between an embedding model and an LLM?
Why is a vector database required in a RAG system?
Why does FastAPI use Pydantic?
Why was the uploaded PDF saved temporarily before processing?
What caused the Windows WinError 32 when uploading a second PDF, and how was it resolved?
Explain the complete request flow from uploading a PDF to generating an answer.

# Day 13

What is Docker?
Why was Docker created?
Image vs Container.
Explain the Docker lifecycle.
What is a Dockerfile?
Why are environment variables important?
What happens during docker build?
What happens during docker run?
Why is Docker popular for AI applications?
How did we deploy our PDF Chatbot?

