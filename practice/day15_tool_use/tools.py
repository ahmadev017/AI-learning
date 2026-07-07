

def calculate(expression: str):
    """
    Evaluates a mathematical expression.
    """
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Calculation Error: {e}"


def get_weather(city: str):
    """
    Returns fake weather information for demonstration purposes.
    """

    weather_data = {
        "lahore": "Sunny, 35°C",
        "karachi": "Cloudy, 31°C",
        "islamabad": "Rainy, 28°C",
        "rahim yar khan": "Hot, 41°C"
    }

    return weather_data.get(
        city.lower(),
        f"No weather data available for {city}."
    )    


def search_knowledge_base(query: str):
    """
    Searches a simple knowledge base for predefined topics.
    """

    knowledge_base = {
        "rag": "RAG (Retrieval-Augmented Generation) combines retrieval with LLM generation to answer questions using external knowledge.",
        "llm": "A Large Language Model predicts the next token and generates human-like text.",
        "langchain": "LangChain is a framework for building LLM-powered applications using chains, tools, agents, and memory.",
        "embedding": "Embeddings convert text into numerical vectors so semantic similarity can be measured."
    }

    return knowledge_base.get(
        query.lower(),
        f"No information found for '{query}'."
    )