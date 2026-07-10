from memory_store import MemoryStore

store = MemoryStore()

store.save_memory(
    memory="I am learning AI Engineering.",
    user_id="ahmad",
    memory_type="education"
)

store.save_memory(
    memory="I like Python.",
    user_id="ahmad",
    memory_type="preference"
)

store.save_memory(
    memory="I play badminton.",
    user_id="ahmad",
    memory_type="hobby"
)