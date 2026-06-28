# Day 10 Notes: RAG from Scratch
## Overview
Built a complete RAG pipeline manually: chunk -> embed -> store -> retrieve -> generate.
## Key Concepts
- Ingestion prepares knowledge before users ask questions.
- Retrieval finds relevant chunks using embeddings and vector similarity.
- Generation uses only retrieved context.
- ask() orchestrates the pipeline.
## Why We Need It
LLMs lack private/current knowledge; RAG augments prompts with retrieved context.
## How It Works
Document -> Chunk -> Embed -> ChromaDB -> Query Embed -> Retrieve -> Prompt Augmentation -> LLM.
## Advantages
Fresh knowledge, private knowledge, reduced hallucinations.
## Limitations
Quality depends on chunking, embeddings and retrieval.
## Interview Questions
- What is ingestion?
- Why chunk?
- Why use same embedding model for docs and queries?
- What happens if the LLM is removed?
## Key Takeaways
Retriever searches; LLM reasons and writes.
