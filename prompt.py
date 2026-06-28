import streamlit as st
from langchain_community.llms import Ollama


st.title("Static Prompting Chatbot")

input_text = st.text_input("Enter your query : ")
model = Ollama(model= 'gemma3')
reponse = model.invoke(input_text)


if st.button("Answer"):
    st.write(reponse)