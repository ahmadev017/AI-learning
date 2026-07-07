import json

from groq import Groq

from config import GROQ_API_KEY
from tools import calculate, get_weather, search_knowledge_base

# Create Groq client
client = Groq(api_key=GROQ_API_KEY)

# -----------------------------
# Tool Definitions
# -----------------------------

tools = [
    {
        "type": "function",
        "function": {
            "name": "calculate",
            "description": "Perform mathematical calculations.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "The mathematical expression to evaluate."
                    }
                },
                "required": ["expression"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather for a city.",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "The city name."
                    }
                },
                "required": ["city"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "search_knowledge_base",
            "description": "Search the AI knowledge base.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The topic to search."
                    }
                },
                "required": ["query"]
            }
        }
    }
]

# -----------------------------
# Tool Registry
# -----------------------------

tool_registry = {
    "calculate": calculate,
    "get_weather": get_weather,
    "search_knowledge_base": search_knowledge_base
}

# -----------------------------
# User Input
# -----------------------------

user_input = input("You: ")

messages = [
    {
        "role": "user",
        "content": user_input
    }
]

# -----------------------------
# First LLM Call
# -----------------------------

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=messages,
    tools=tools,
    tool_choice="auto"
)

assistant_message = response.choices[0].message
print("\n========== FIRST LLM RESPONSE ==========")
print(assistant_message)
print("========================================\n")
# -----------------------------
# Check if LLM wants a tool
# -----------------------------

if assistant_message.tool_calls:

    tool_call = assistant_message.tool_calls[0]

    tool_name = tool_call.function.name

    arguments = json.loads(tool_call.function.arguments)

    function = tool_registry.get(tool_name)

    if function:

        tool_result = function(**arguments)

        messages.append(assistant_message)

        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": tool_result
        })

        final_response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages
        )

        print("\nAssistant:", final_response.choices[0].message.content)

    else:

        print("Unknown tool requested.")

else:

    print("\nAssistant:", assistant_message.content)
print("Tool Selected:", tool_name)
print("Arguments:", arguments)
print("Tool Result:", tool_result)