import chromadb
from chromadb.utils.embedding_functions import (
    SentenceTransformerEmbeddingFunction,
)


class MemoryRetriever:
    def __init__(self):
        # Connect to the same persistent ChromaDB
        self.client = chromadb.PersistentClient(path="./chroma_db")

        # Register the same embedding model used during storage
        self.embedding_function = SentenceTransformerEmbeddingFunction(
            model_name="all-MiniLM-L6-v2"
        )

        # Load the same collection
        self.collection = self.client.get_or_create_collection(
            name="memories",
            embedding_function=self.embedding_function,
        )

    def search_memories(
        self,
        query: str,
        user_id: str,
        n_results: int = 3,
    ) -> list[str]:
        """
        Search for the most relevant memories of a user.
        """

        results = self.collection.query(
            query_texts=[query],
            n_results=n_results,
            where={"user_id": user_id},
        )

        documents = results.get("documents", [])

        if not documents:
            return []

        return documents[0]