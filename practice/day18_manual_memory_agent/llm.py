from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()


class LLM:

    def __init__(self):
        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )

    def chat(
        self,
        question: str,
        memories: list[str]
    ) -> str:

        memory_context = "\n".join(memories)

        prompt = f"""
You are a helpful AI assistant.

Relevant memories:
{memory_context}

User Question:
{question}

Answer naturally using the memories if they are relevant.
"""

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response.choices[0].message.content