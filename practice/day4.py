#streaming response from AI

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)

messages = [
    {
        "role": "system",
        "content": "You are an AI assistant and give short polite replies."
    }
]

while True:
    user_input = input("You: ")

    if user_input.lower() == "quit":
        break

    messages.append({
        "role": "user",
        "content": user_input
    })

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
        stream=True
    )

    full_reply = ""

    print("AI: ", end="", flush=True)

    for chunk in response:
        content = chunk.choices[0].delta.content
        if content:
            full_reply += content
            print(content, end="", flush=True)

    print("\n")

    # append full response ONCE
    messages.append({
        "role": "assistant",
        "content": full_reply
    })


    