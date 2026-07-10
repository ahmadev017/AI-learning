# AI Engineering Glossary

> A growing dictionary of AI Engineering concepts. Updated after every learning day.

---

# Attention

A mechanism in Transformers that allows each token to decide which other tokens are most important when understanding context.

**Example**

"The cat sat on the mat because **it** was tired."

Here, "it" attends to "cat".

---

# Attention Score

A raw similarity score calculated between a Query and every Key before Softmax is applied.

Higher score = More relevant token.

---

# Attention Weights

Probabilities obtained after applying Softmax to attention scores.

They determine how much importance each Value receives.

Properties:

* Between 0 and 1
* Always sum to 1

---

# Cosine Similarity

A mathematical measure used to determine how similar two vectors are.

Formula:

Cosine Similarity = (A · B) / (||A|| × ||B||)

Range:

-1 → Completely opposite

0 → Unrelated

1 → Identical direction

---

# Embedding

A dense numerical vector that represents the semantic meaning of text.

Example:

"I love AI"

↓

[0.18, -0.42, 0.73, ...]

Embeddings are the foundation of semantic search and RAG.

---

# Feed Forward Network (FFN)

A small neural network applied independently to every token after attention.

Purpose:

* Learn richer features
* Add nonlinear transformations
* Increase model capacity

---

# Key (K)

Represents the information each token offers to other tokens.

Queries compare themselves with Keys.

---

# Layer Normalization

Normalizes activations inside a Transformer layer.

Benefits:

* Stable training
* Faster convergence
* Prevents exploding values

---

# Logits

Raw prediction scores produced by GPT before Softmax converts them into probabilities.

---

# Multi-Head Attention

Uses multiple attention heads in parallel.

Each head learns different relationships within the sentence.

---

# PersistentClient

A ChromaDB client that stores the database permanently on disk.

Data remains even after restarting the application.

---

# Query (Q)

Represents what a token is looking for.

Every Query compares itself with all Keys.

---

# RAG (Retrieval-Augmented Generation)

An AI architecture that combines:

Retriever (Vector Database)

*

Large Language Model

Retriever finds relevant documents.

LLM generates the final answer.

---

# Residual Connection

Adds the input of a layer to its output.

Benefits:

* Better gradient flow
* Easier optimization
* Enables very deep Transformers

---

# Semantic Search

Searching by meaning instead of exact keywords.

Example:

Question:

"Who studies AI?"

Can retrieve:

"Ahmad is learning Artificial Intelligence."

---

# Softmax

Converts logits or attention scores into probabilities.

Properties:

* Outputs between 0 and 1
* Probabilities sum to 1

---

# Temperature

Controls randomness during text generation.

Low Temperature:

More deterministic.

High Temperature:

More creative.

---

# Top-k Sampling

Chooses the next token only from the top k most probable tokens.

---

# Top-p Sampling (Nucleus Sampling)

Chooses the smallest set of tokens whose cumulative probability reaches p.

Produces more natural text than fixed Top-k.

---

# Transformer

A neural network architecture built around the Attention mechanism.

Foundation of GPT, BERT, Claude, Gemini and modern LLMs.

---

# Value (V)

Contains the actual information passed forward after attention weights are applied.

---

# Vector

A list of numerical values representing information.

Example:

[0.12, -0.31, 0.74]

---

# Vector Database

A database optimized for storing and searching embeddings.

Examples:

* ChromaDB
* Pinecone
* Weaviate
* Milvus

---

# ChromaDB

An open-source vector database used for storing embeddings and performing semantic search.

---

# Collection

A group of documents inside ChromaDB.

Equivalent to:

* SQL Table
* MongoDB Collection

---

# Retrieval

The process of finding relevant documents.

Performed by a vector database.

---

# Generation

The process of producing the final answer.

Performed by an LLM.


# Day 10
- RAG
- Ingestion
- Retrieval
- Prompt Augmentation
- Orchestration
- Context Window
- Semantic Search


# Day 11 (langChain)
| Term                           | Definition                                                      |
| ------------------------------ | --------------------------------------------------------------- |
| LangChain                      | Framework for orchestrating LLM applications.                   |
| Document                       | Standard LangChain object containing page content and metadata. |
| TextLoader                     | Reads text files and converts them into Document objects.       |
| RecursiveCharacterTextSplitter | Splits large documents into overlapping chunks.                 |
| Chunk Overlap                  | Shared text between consecutive chunks to preserve context.     |
| Retriever                      | Retrieves the most relevant documents from a vector store.      |
| ChatPromptTemplate             | Template for constructing prompts with variables.               |
| Stuff Documents Chain          | Combines retrieved documents into a single prompt.              |
| Retrieval Chain                | Complete pipeline combining retrieval and LLM generation.       |
| `invoke()`                     | Executes a LangChain runnable or chain.                         |


# Day 12 (PDF App)

| Term                          | Meaning                                                                                               |
| ----------------------------- | ----------------------------------------------------------------------------------------------------- |
| FastAPI                       | High-performance Python framework for building APIs.                                                  |
| UploadFile                    | FastAPI type for handling uploaded files.                                                             |
| Pydantic                      | Library for data validation and request parsing.                                                      |
| PyPDFLoader                   | LangChain loader for extracting text from PDF files.                                                  |
| RetrievalQA                   | LangChain chain that combines retrieval with an LLM to answer questions.                              |
| Chroma                        | Vector database used for storing and searching embeddings.                                            |
| CORS                          | Browser security mechanism controlling cross-origin requests.                                         |
| SentenceTransformerEmbeddings | Embedding wrapper using sentence-transformer models (deprecated in favor of `langchain_huggingface`). |


# Day 13 (containerised and deployed)

AI_Glossary.md Updates
Docker
A platform for packaging applications and their dependencies into portable containers.
Docker Image
A read-only blueprint containing everything required to run an application.
Docker Container
A running instance of a Docker image.
Dockerfile
A script containing instructions to build a Docker image.
Containerization
The process of packaging software with all dependencies into isolated containers.
Render
A cloud platform used to deploy backend applications.
Vercel
A cloud platform optimized for deploying frontend applications.
Environment Variables
Configuration values stored outside the source code, commonly used for secrets such as API keys

# Day 17 (langraph)

State
StateGraph
Node
Edge
Conditional Edge
Router
START
END
TypedDict
Shared State
Workflow Orchestration
Graph Compilation
State Transition

# Day 18 (mem0)

Long-Term Memory:
Persistent storage that survives application restarts and allows an AI system to remember users across sessions.
Short-Term Memory:
Temporary conversational context available only during the current interaction.
Episodic Memory:
Memory that stores events or experiences.
Semantic Memory:
Memory that stores facts and knowledge.
Metadata Filtering:
Restricting vector search results using metadata such as user_id.
Memory Management Framework:
A framework (such as Mem0) that automates memory extraction, updating, storage, and retrieval.