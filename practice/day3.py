from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)

messages = [{
    "role": "system",
    "content":"You are an ai assistant and give short polite reply over any question."
}
]

while True:
    user_input=input("You :")
    if user_input.lower() == "quit":
        break
    messages.append({
        "role":"user",
        "content":user_input
    })

    response=client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages
    )

    reply= response.choices[0].message.content

    messages.append(
        {
            "role":"assistant",
           "content":reply
        }
    )

    print(f'\nAI:{reply}\n')