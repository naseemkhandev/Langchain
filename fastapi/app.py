from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
from langserve import add_routes
from dotenv import load_dotenv
import uvicorn
import os

load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

app = FastAPI(
   title="LangChain Google Generative AI Chatbot & Ollama Chatbot",
   description="A FastAPI application that serves LangChain Google Generative AI and Ollama chatbots.",
   version="0.1.0",
)

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
ollama_model = ChatOllama(model="llama2")

prompt1 = ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words.")
prompt2 = ChatPromptTemplate.from_template("Write me an poem about {topic} with 100 words.")

add_routes(app, prompt1 | model, path="/essay")
add_routes(app, prompt2 | ollama_model, path="/poem")

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)