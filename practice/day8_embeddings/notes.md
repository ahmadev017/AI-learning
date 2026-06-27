# Day 8 - Embeddings & Cosine Similarity

## What I Learned

- Embeddings convert text into numerical vectors that capture semantic meaning.
- Similar sentences have embeddings that are close together in vector space.
- Different sentences have embeddings that are farther apart.
- Embeddings represent meaning, not exact words.
- Cosine similarity measures how similar two embedding vectors are.
- Cosine similarity ranges from -1 to 1.
- A value closer to 1 means the vectors are more semantically similar.
- Sentence Transformers can generate embeddings using pretrained models.
- The `all-MiniLM-L6-v2` model produces 384-dimensional embeddings.
- Embedding models understand semantic similarity but are not perfect.
- Embeddings do not truly "understand" language—they learn statistical patterns from training data.
- Polysemy (e.g., "Apple" the company vs. "apple" the fruit) can still confuse embedding models.
- Opposite sentences (e.g., "I love cats" vs. "I hate cats") may still have high similarity because they discuss the same topic.
- Embeddings are widely used in semantic search, RAG, recommendation systems, clustering, and document retrieval.

## Python Functions Used

- `SentenceTransformer()` → Loads a pretrained embedding model.
- `model.encode()` → Converts text into embedding vectors.
- `np.dot()` → Computes the dot product.
- `np.linalg.norm()` → Computes vector magnitude.
- Cosine similarity = Dot Product / (Magnitude A × Magnitude B)

## Key Takeaways

- Embeddings capture meaning instead of exact keywords.
- Cosine similarity compares semantic closeness between vectors.
- Embeddings are the foundation of vector databases and RAG systems.
- ChromaDB stores embeddings so they can be searched efficiently.

## Interview One-Liners

**What is an embedding?**
A numerical vector representation of text that captures its semantic meaning.

**Why use embeddings?**
To compare and search text based on meaning rather than exact keywords.

**What is cosine similarity?**
A metric that measures the semantic similarity between two embedding vectors.

**Why not compare raw text directly?**
Because embeddings allow semantic matching even when different words express similar meanings.