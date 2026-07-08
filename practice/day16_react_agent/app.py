from agent import agent
from langchain.agents import create_agent
print(type(create_agent))
while True:

    question = input("You: ")

    if question.lower() == "exit":
        break

    response = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": question
                }
            ]
        }
    )

    print()
    print(response["messages"][-1].content)
    print()