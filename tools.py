from dotenv import load_dotenv
from langchain_tavily import TavilySearch

load_dotenv()

# Create Tavily search tool
tavily = TavilySearch(max_results=5)


def search_web(question: str):
    """
    Search the web using Tavily.
    """

    result = tavily.invoke(question)

    return result