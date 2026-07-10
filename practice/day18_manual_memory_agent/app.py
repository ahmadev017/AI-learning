from memory_store import MemoryStore
from memory_retriever import MemoryRetriever
from llm import LLM


memory_store = MemoryStore()
memory_retriever = MemoryRetriever()
llm = LLM()


USER_ID = "ahmad"


while True:

    question = input("\nYou: ")

    if question.lower() == "exit":
        break

    memories = memory_retriever.search_memories(
        query=question,
        user_id=USER_ID,
    )

    response = llm.chat(
        question=question,
        memories=memories,
    )

    print(f"\nAssistant: {response}")

    should_save = input(
        "\nSave this as memory? (y/n): "
    )

    if should_save.lower() == "y":

        memory = input(
            "Enter memory: "
        )

        memory_store.save_memory(
            memory=memory,
            user_id=USER_ID,
        )