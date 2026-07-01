📄 Day12_notes.md
Day 12 – PDF Chatbot (Full Stack RAG)
Overview

Built a complete AI-powered PDF chatbot where users can upload any PDF and ask questions about its content.

The application consists of:

React Frontend
FastAPI Backend
LangChain
Chroma Vector Database
HuggingFace Embeddings
Groq LLM
Key Concepts Learned
FastAPI
Creating REST APIs
POST endpoints
File uploads
Request validation using Pydantic
CORS configuration
PDF Processing
Reading PDFs using PyPDFLoader
Extracting text page by page
Text Splitting

Used:

RecursiveCharacterTextSplitter

Configuration:

Chunk Size = 500
Chunk Overlap = 50

Purpose:

Improve retrieval accuracy
Stay within LLM context limits
Embeddings

Model:

all-MiniLM-L6-v2

Purpose:

Convert every chunk into a semantic vector.

Vector Database

Used:

Chroma

Responsibilities:

Store embeddings
Perform similarity search
Return relevant chunks
RetrievalQA

Connected:

Question
↓

Retriever
↓

Relevant Chunks
↓

Groq LLM
↓

Final Answer

This is the core of the RAG pipeline.

FastAPI Service Architecture

Separated responsibilities into:

main.py
↓

Routes

↓

PDFChatService

↓

Business Logic

Similar to the Controller-Service architecture in Express.js.

Backend Flow
React

↓

POST /upload

↓

FastAPI

↓

Save PDF temporarily

↓

PyPDFLoader

↓

Split into chunks

↓

Embedding Model

↓

Chroma

↓

Retriever

↓

Groq LLM

↓

RetrievalQA Ready

Question Flow

User

↓

POST /ask

↓

Retriever

↓

Top Relevant Chunks

↓

Groq

↓

Answer

↓

Frontend
Problems Solved Today
LangChain v1 import changes
langchain_classic
langchain_text_splitters
Pydantic Settings validation
Environment variable configuration
Windows Chroma file locking (WinError 32)
In-memory Chroma implementation
FastAPI debugging
Real-world Engineering Lesson

Most AI development time is spent on:

debugging
dependency compatibility
architecture

—not writing prompts.

Applications

This architecture can be adapted for:

Resume Chatbots
Legal Document QA
Company Knowledge Bases
Medical PDFs
Research Paper Assistants
Internal Documentation Search
Key Takeaways
FastAPI feels very similar to Express.js.
Embeddings and LLMs are separate models with different roles.
RAG is an orchestration of multiple components rather than a single model.
Separating API routes from business logic leads to cleaner, maintainable code.
Debugging library and environment issues is a normal part of AI engineering