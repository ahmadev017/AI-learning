from memory_retriever import MemoryRetriever

retriever = MemoryRetriever()

results = retriever.search_memories(
    query="What language do I like?",
    user_id="ahmad"
)

print(results)