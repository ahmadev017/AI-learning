# Day 11 — LangChain

## Overview

Today I learned how to build a RAG application using LangChain. LangChain doesn't replace RAG—it simplifies it by connecting all the components together.

---

## What I Learned

* LangChain is an orchestration framework for LLM applications.
* Manual RAG and LangChain perform the same steps internally.
* LangChain reduces boilerplate code and makes applications easier to maintain.

---

## RAG Flow

Text File

↓

TextLoader

↓

Document

↓

Text Splitter

↓

Chunks

↓

Embeddings

↓

Chroma Vector Database

↓

Retriever

↓

Prompt Template

↓

LLM (ChatGroq)

↓

Answer

---

## Important Components

### ChatGroq

* Connects to the Groq LLM.

### HuggingFaceEmbeddings

* Converts text into vectors.

### Chroma

* Stores vectors and performs similarity search.

### TextLoader

* Loads text files as `Document` objects.

### RecursiveCharacterTextSplitter

* Splits large documents into overlapping chunks.

### Retriever

* Retrieves the most relevant chunks from Chroma.

### ChatPromptTemplate

* Builds the prompt sent to the LLM.

### create_stuff_documents_chain()

* Combines retrieved documents into a single prompt.

### create_retrieval_chain()

* Connects the retriever and the LLM into one pipeline.

---

## Key Functions

* `load_dotenv()` → Loads environment variables.
* `loader.load()` → Loads documents.
* `split_documents()` → Creates chunks.
* `Chroma.from_documents()` → Creates the vector database.
* `as_retriever()` → Creates a retriever.
* `invoke()` → Runs the complete RAG pipeline.

---

## Biggest Lesson

LangChain does **not** change how RAG works.

It simply automates the pipeline:

Retrieve → Build Prompt → Send to LLM → Generate Answer

---

## Real-World Uses

* PDF Chatbots
* Company Knowledge Bases
* Customer Support Bots
* AI Assistants
* Enterprise Search

---

## Interview Questions

1. What is LangChain?
2. Why do we need chunking?
3. What is a Retriever?
4. What is the difference between `from_texts()` and `from_documents()`?
5. Why is LangChain easier than manual RAG?

---

## Key Takeaways

* LangChain is a framework, not an LLM.
* RAG works the same with or without LangChain.
* Retrieval quality directly affects answer quality.
* Understanding Manual RAG makes LangChain easy to understand.
