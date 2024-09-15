import re
import streamlit as st
from crewai import Crew
from agent import researcher, writer
from task import research, write

crew = Crew(
    agents=[researcher, writer],
    tasks=[research, write],
    verbose=False,
    planning=True
)

def extract_sources(text):
    source_pattern = re.compile(r"(Sources?:\s*.*(?:\n-.*)*)", re.IGNORECASE)
    sources_match = source_pattern.search(text)
    if sources_match:
        sources = sources_match.group(1).strip()
        return sources
    return "No sources found."

st.title("Academic Topic Research and Writing")

topic = st.text_input("Enter a topic to research:", "enter your topic")

if st.button("Run Research"):
    if topic.strip():  
        with st.spinner("Researching..."):
            try:
                result = crew.kickoff(inputs={'topic': topic})
                research_output = result.tasks_output[0].raw
                writing_output = result.tasks_output[1].raw
                if research_output:
                    st.success("Research completed!")
                    st.write("### Research Output:")
                    st.write(research_output)
                else:
                    st.warning("No research content was generated.")
                if writing_output:
                    st.write("### Writing Output:")
                    st.write(writing_output)
                    sources = extract_sources(writing_output)
                    st.write("### Sources of Information:")
                    st.write(sources)

            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a valid topic before running the research.")
