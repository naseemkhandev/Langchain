# from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()
# os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
# Langsmith tracing configuration
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Prompt template
prompt = ChatPromptTemplate.from_messages(
   [
      ("system", "You are a helpful assistant. Answer the user's questions in a concise manner."),
      ("user", "Question: {question}"),
   ]
)

# Streamlit app configuration
st.title("LangSmith Chatbot")
input_question = st.text_input("Ask a question:")

# Google Generative AI model configuration
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_question:
    with st.spinner("Generating response..."):
        try:
            response = chain.invoke({"question": input_question})
            st.write(response)
        except Exception as e:
            st.error(f"An error occurred: {e}")