from mem0 import Memory
from dotenv import load_dotenv

load_dotenv()

memory = Memory()

USER_ID = "ahmad"

while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        break

    # Retrieve relevant memories
    results = memory.search(
        user_input,
        user_id=USER_ID
    )

    print("\nRetrieved Memories:")

    if len(results["results"]) == 0:
        print("No memories found.")

    else:
        for item in results["results"]:
            print("-", item["memory"])

    # Simulate assistant reply
    assistant_reply = input("\nAssistant Reply: ")

    # Store conversation
    messages = [
        {
            "role": "user",
            "content": user_input
        },
        {
            "role": "assistant",
            "content": assistant_reply
        }
    ]

    memory.add(
        messages,
        user_id=USER_ID
    )