import streamlit as st
import requests

def get_gemini_response(input_text):
   response = requests.post("http://localhost:8000/essay/invoke", json={'input': {'topic': input_text}})
   return response.json()['output']['content']

def get_ollama_response(input_text):
   response = requests.post("http://localhost:8000/poem/invoke", json={'input': {'topic': input_text}})
   return response.json()['output']['content']

st.title('Langchain Demo With LLAMA2 API')
input_text1=st.text_input("Write an essay on")
input_text2=st.text_input("Write a poem on")

if input_text1:
   st.write("Google Gemini Response")
   st.write(get_gemini_response(input_text1))

if input_text2:
   st.write("OLLAMA Response")
   st.write(get_ollama_response(input_text2))