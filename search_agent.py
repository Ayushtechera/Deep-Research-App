from agents import Agent, ModelSettings, function_tool
from ddgs import DDGS
from dotenv import load_dotenv
import os

load_dotenv(override=True)
MODEL_NAME = os.getenv("DEFAULT_MODEL_NAME", "gemini-2.5-flash")

INSTRUCTIONS = """
You are a research assistant. Given a search term, you search the web for that term and
produce a concise summary of the results. The summary must be 2-3 paragraphs and less than 300 words.
Capture the main points and be succinct. Reply only with the summary.
"""

@function_tool
def web_search(query: str) -> str:
    """Search the web and return the top results.

    Args:
        query: The search term
    """
    results = DDGS().text(query, max_results=5)
    return "\n\n".join(f"{r['title']}\n{r['body']}\n{r['href']}" for r in results)

search_agent = Agent(
    name="Search Agent",
    instructions=INSTRUCTIONS,
    tools=[web_search],
    model=MODEL_NAME,
    model_settings=ModelSettings(tool_choice="required"),
)