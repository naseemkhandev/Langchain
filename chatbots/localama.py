from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama

import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

# Prompt template
prompt = ChatPromptTemplate.from_messages(
   [
      ("system", "You are a helpful assistant. Answer the user's questions in a concise manner."),
      ("user", "Question: {question}"),
   ]
)

# Streamlit app configuration
st.set_page_config(page_title="Ollama Chatbot", page_icon=":robot_face:")
st.title("Ollama Chatbot")
input_question = st.text_input("Ask a question:")

# Ollama model configuration
llm = ChatOllama(model="llama2", temperature=0)
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_question:
    with st.spinner("Generating response..."):
        try:
            response = chain.invoke({"question": input_question})
            st.write(response)
        except Exception as e:
            st.error(f"An error occurred: {e}")