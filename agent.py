from crewai import Agent
from langchain_huggingface import HuggingFaceEndpoint
from crewai_tools import (
    SerperDevTool,
    WebsiteSearchTool
)
from dotenv import load_dotenv
import os
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"]="gpt-4-0125-preview"

search_tool = SerperDevTool()
web_rag_tool = WebsiteSearchTool()


researcher = Agent(
    role='Academic Content Researcher',
    goal='Provide relevant academic content and book suggestions for {topic} based on the user query.',
    verbose=False,
    memory=True, 
    backstory=(
        "A skilled researcher specializing in finding academic content for students."
    ),
    tools=[search_tool,web_rag_tool],
    allow_delegation=True
)

writer = Agent(
    role='Academic Content Writer',
    goal='Summarize and create engaging content for {topic} based on student queries.',
    verbose=False,
    memory=True, 
    backstory=(
        "A skilled writer who creates academic summaries and book recommendations."
    ),
    tools=[search_tool,web_rag_tool],
    allow_delegation=False
)