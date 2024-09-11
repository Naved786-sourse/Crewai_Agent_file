from crewai import Task
from agent import researcher, writer,web_rag_tool,search_tool

research = Task(
    description=(
        "Identify and research academic resources on {topic}. "
        "Retrieve detailed information from reliable sources."
    ),
    expected_output='A detailed 3-paragraph report based on the {topic}.',
    tools=[search_tool,web_rag_tool],
    agent=researcher,
)

write = Task(
    description=(
        "Write an engaging summary or blog post based on researched content or book recommendations."
    ),
    expected_output='A 4-paragraph, student-friendly blog post formatted in markdown.',
    agent=writer,
    output_file='outputs/new_post.md'  
)