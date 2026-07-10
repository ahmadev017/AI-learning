from llm import LLM

llm = LLM()

response = llm.chat(
    question="What do I like?",
    memories=[
        "I like Python.",
        "I play badminton.",
        "I enjoy coffee."
    ]
)

print(response)