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


st.title("Topic Research")
topic = st.text_input("Enter a topic to research:", "enter your topic")

if st.button("Run Research"):
    with st.spinner("Researching..."):

        result = crew.kickoff(inputs={'topic': topic})
        st.success("Research completed!")


    st.write("### Research Output:")
    st.write(result)
