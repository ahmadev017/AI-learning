from langchain.agents import create_agent
from langchain_groq import ChatGroq
from langchain_community.tools import TavilySearchResults
from config import GROQ_API_KEY

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=GROQ_API_KEY,
)

tools = [
    TavilySearchResults(max_results=3)
]

agent = create_agent(
    model=llm,
    tools=tools,
)