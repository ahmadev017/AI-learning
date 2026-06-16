
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)

def ask(system, user):
    r = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role":"system","content":system},
                  {"role":"user","content":user}]
    )
    return r.choices[0].message.content

print("=== Zero-shot ===")
print(ask("You are a helpful assistant.", "Is this email spam? 'Win $1000 now!'"))

print("\n=== Few-shot ===")
print(ask(
    """Classify emails as SPAM or NOT SPAM.
Examples:
'Claim your prize!' -> SPAM
'Meeting at 3pm' -> NOT SPAM
'Free iPhone winner' -> SPAM""",
    "'Your invoice is attached' -> ?"
))

print("\n=== Chain of thought ===")
print(ask(
    "Think step by step before answering.",
    "A developer earns $50/hr. Works 6hrs/day, 5 days/week. How much in a month?"
))