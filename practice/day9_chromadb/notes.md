# Day 9 - ChromaDB & Vector Databases

# Overview

Today I learned about **ChromaDB**, an open-source vector database used to store and search embeddings efficiently. Unlike traditional databases that search using exact keywords, ChromaDB performs **semantic search**, meaning it retrieves documents based on their meaning rather than exact text.

Today was the first step toward building **Retrieval-Augmented Generation (RAG)** systems.

---

# What is a Vector Database?

A vector database is a database designed to store **embeddings (vectors)** and retrieve the most semantically similar vectors when given a query.

Instead of searching words, it searches **meaning**.

Example:

Document:

"I am learning AI Engineering."

Query:

"Who is studying artificial intelligence?"

Even though none of the words exactly match, a vector database understands they have similar meanings.

---

# What is ChromaDB?

ChromaDB is an open-source vector database that allows us to:

- Store embeddings
- Store original documents
- Store metadata
- Perform semantic similarity search
- Build local RAG applications

Unlike SQL or MongoDB, ChromaDB is optimized for searching vectors instead of plain text.

---

# Why Do We Need ChromaDB?

Suppose we have one million documents.

Traditional databases search like this:

Question:

"What is RAG?"

SQL searches for the exact words "RAG".

If a document contains:

"Retrieval Augmented Generation"

SQL may not find it because the words are different.

A vector database converts both the document and the question into embeddings and compares their meanings.

---

# Traditional Database vs Vector Database

## Traditional Database

Searches:

- Exact text
- IDs
- Keywords
- Numbers

Example:

```sql
SELECT *
FROM documents
WHERE title = 'Python'
```

---

## Vector Database

Searches:

- Semantic meaning
- Similar ideas
- Context

Example:

Question:

"Which project uses React and Node?"

It can retrieve:

"Doctor appointment booking application built using React, Express, MongoDB and Node.js."

even if the exact words don't match.

---

# How ChromaDB Works

```
Documents
      │
      ▼
Embedding Model
      │
      ▼
Embedding Vectors
      │
      ▼
Store in ChromaDB
      │
      ▼
User Question
      │
      ▼
Question Embedding
      │
      ▼
Cosine Similarity Search
      │
      ▼
Most Similar Documents
```

---

# Why Do We Store Documents Along With Their Embeddings?

This was one of the biggest concepts I learned today.

Embeddings look like this:

```
[0.12, -0.43, 0.88, ...]
```

Humans cannot understand these numbers.

When ChromaDB finds the closest embedding, it returns the **original document** so that a human or an LLM can read it.

Without storing the original document, we would only get numbers back.

---

# Why Not Store Only Documents?

Searching millions of text documents is slow and depends on keyword matching.

Embeddings make searching much faster because ChromaDB compares vectors instead of comparing every word.

The document is stored only so it can be returned after retrieval.

---

# ChromaDB is Like a Library

Think of ChromaDB as a librarian.

Library Books

↓

Documents

Library Index

↓

Embeddings

Librarian

↓

ChromaDB

Reader

↓

LLM or User

The librarian does not answer questions.

The librarian only finds the correct books.

---

# Retrieval is NOT Answering

One important lesson today:

ChromaDB retrieves documents.

It does NOT answer questions.

Example:

Question:

"When did Ahmad build his doctor appointment project?"

Document:

"Ahmad built a doctor appointment booking application."

The document never mentions the year.

Therefore ChromaDB correctly retrieves the document but cannot answer "when."

Answer generation is the job of an LLM.

---

# RAG Pipeline

```
Question
     │
     ▼
Embedding Model
     │
     ▼
ChromaDB
     │
     ▼
Relevant Documents
     │
     ▼
Large Language Model
     │
     ▼
Final Answer
```

Today I built only the retrieval part.

The LLM generation part will come later.

---

# PersistentClient

```
client = chromadb.PersistentClient(path="./chroma_db")
```

PersistentClient saves the database on disk.

This means the data remains even after the program stops.

If we use:

```
client = chromadb.Client()
```

everything disappears after the program ends.

---

# Collection

A collection in ChromaDB is similar to:

- Table in SQL
- Collection in MongoDB

Example:

```
collection = client.get_or_create_collection("knowledge_base")
```

---

# Important Functions

## Create Persistent Client

```python
client = chromadb.PersistentClient(path="./chroma_db")
```

Creates a local database stored on disk.

---

## Create Collection

```python
client.get_or_create_collection()
```

Creates a collection if it doesn't already exist.

---

## Add Documents

```python
collection.add()
```

Stores:

- IDs
- Documents
- Embeddings
- Metadata

---

## Query

```python
collection.query()
```

Finds the most semantically similar documents.

---

## Get Documents

```python
collection.get()
```

Returns stored data.

---

## Peek

```python
collection.peek()
```

Shows the first few stored documents.

---

## Count

```python
collection.count()
```

Returns the number of stored documents.

---

## Delete Collection

```python
client.delete_collection()
```

Deletes an existing collection.

---

# Folder Structure

```
day9_chromadb/

│── app.py
│── notes.md
│── chroma_db/
```

The `chroma_db` folder contains the stored vector database.

---

# Real-World Applications

Vector databases are used in:

- ChatGPT Memory
- AI Assistants
- RAG Systems
- Semantic Search
- Customer Support Bots
- Enterprise Search
- Document Retrieval
- Code Search
- Recommendation Systems

---

# Advantages

- Very fast semantic search
- Finds similar meaning instead of exact words
- Stores millions of embeddings efficiently
- Easy integration with LLMs
- Foundation of RAG systems

---

# Limitations

- Cannot answer questions by itself
- Needs an embedding model
- Quality depends on the embedding model
- Retrieved documents may still need an LLM to generate a final answer

---

# Key Takeaways

- ChromaDB is a vector database.
- It stores embeddings, documents, IDs and metadata.
- Semantic search is different from keyword search.
- Embeddings help retrieve meaning instead of exact text.
- ChromaDB retrieves documents but does not generate answers.
- A complete RAG system combines ChromaDB with an LLM.
- PersistentClient saves data permanently on disk.
- Collections are similar to SQL tables or MongoDB collections.

---

# Interview Questions

### What is ChromaDB?

A vector database used to store embeddings and perform semantic similarity search.

---

### Why do we need a vector database?

Because keyword search cannot understand meaning, while vector databases search using semantic similarity.

---

### Why do we store both documents and embeddings?

Embeddings are used for retrieval, while the original documents are returned so humans or LLMs can read them.

---

### What is semantic search?

Searching based on meaning rather than exact keywords.

---

### Can ChromaDB answer questions?

No.

It only retrieves the most relevant documents.

An LLM is needed to generate the final answer.

---

### What is the difference between SQL and ChromaDB?

SQL searches structured data using exact matches.

ChromaDB searches embeddings using semantic similarity.

---

### What is a Collection?

A collection is a group of documents inside ChromaDB, similar to a table in SQL or a collection in MongoDB.

---

### What is PersistentClient?

PersistentClient stores the database on disk so that the data remains after the application is closed.

---

# Today's Win 🎉

Today I learned how vector databases work internally and how semantic search retrieves documents based on meaning instead of exact text. I also understood that retrieval and answer generation are two different steps, forming the foundation of Retrieval-Augmented Generation (RAG).