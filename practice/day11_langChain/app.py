from dotenv import load_dotenv
import os

from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_core.prompts import ChatPromptTemplate

from langchain_classic.chains.combine_documents import (
    create_stuff_documents_chain,
)
from langchain_classic.chains import (
    create_retrieval_chain,
)

# ---------------------------------------
# Load Environment Variables
# ---------------------------------------

load_dotenv()

# ---------------------------------------
# Initialize LLM
# ---------------------------------------

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)

# ---------------------------------------
# Embedding Model
# ---------------------------------------

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# ---------------------------------------
# Load Text File
# ---------------------------------------

loader = TextLoader("sample.txt")

documents = loader.load()

print("=" * 50)
print("DOCUMENTS LOADED")
print("=" * 50)

print(f"Total Documents: {len(documents)}")

print(documents[0].metadata)

print(documents[0].page_content)

# ---------------------------------------
# Split Documents
# ---------------------------------------

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20
)

chunks = splitter.split_documents(documents)

print("\n" + "=" * 50)
print("DOCUMENT CHUNKS")
print("=" * 50)

print(f"Total Chunks: {len(chunks)}")

for i, chunk in enumerate(chunks, start=1):
    print(f"\nChunk {i}")
    print(chunk.page_content)

# ---------------------------------------
# Store in Chroma
# ---------------------------------------

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./chroma_db"
)

# ---------------------------------------
# Retriever
# ---------------------------------------

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)

# Debug retrieved chunks

print("\n" + "=" * 50)
print("RETRIEVED DOCUMENTS")
print("=" * 50)

retrieved_docs = retriever.invoke("What has Ahmad built?")

for i, doc in enumerate(retrieved_docs, start=1):
    print(f"\nRetrieved Document {i}")
    print(doc.page_content)

# ---------------------------------------
# Prompt
# ---------------------------------------

prompt = ChatPromptTemplate.from_template(
    """
Answer the question using ONLY the provided context.

Context:
{context}

Question:
{input}
"""
)

# ---------------------------------------
# Document Chain
# ---------------------------------------

document_chain = create_stuff_documents_chain(
    llm,
    prompt
)

# ---------------------------------------
# Retrieval Chain
# ---------------------------------------

retrieval_chain = create_retrieval_chain(
    retriever,
    document_chain
)

# ---------------------------------------
# Ask Question
# ---------------------------------------

response = retrieval_chain.invoke(
    {
        "input": "What has Ahmad built?"
    }
)

# ---------------------------------------
# Print Result
# ---------------------------------------

print("\n" + "=" * 50)
print("FULL RESPONSE")
print("=" * 50)

print(response)

print("\n" + "=" * 50)
print("FINAL ANSWER")
print("=" * 50)

print(response["answer"])