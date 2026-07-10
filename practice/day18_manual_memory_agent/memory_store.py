import uuid

import chromadb
from chromadb.utils.embedding_functions import (
    SentenceTransformerEmbeddingFunction,
)


class MemoryStore:
    def __init__(self):
        # Create (or load) a persistent ChromaDB database
        self.client = chromadb.PersistentClient(path="./chroma_db")

        # Register the embedding model
        self.embedding_function = SentenceTransformerEmbeddingFunction(
            model_name="all-MiniLM-L6-v2"
        )

        # Create (or load) the memories collection
        self.collection = self.client.get_or_create_collection(
            name="memories",
            embedding_function=self.embedding_function,
        )

    def save_memory(
        self,
        memory: str,
        user_id: str,
        memory_type: str = "general",
    ) -> None:
        """
        Save a single memory into ChromaDB.
        """

        self.collection.add(
            ids=[str(uuid.uuid4())],
            documents=[memory],
            metadatas=[
                {
                    "user_id": user_id,
                    "type": memory_type,
                }
            ],
        )

        print(f"Memory saved: {memory}")