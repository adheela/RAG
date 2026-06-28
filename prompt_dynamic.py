import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate , load_prompt
from dotenv import load_dotenv

load_dotenv()


st.title("RGC Prompt Template Chatbot")

role = st.selectbox('Select your Role :',['AI Engineer','Data Scientists', 'Data Engineer','Data Analyst'])
goal = st.text_input("What Goal you have in your mind : ")
context = st.text_area('Tell me about your experience')

template = load_prompt('promptT.json')
#template = PromptTemplate(template="""Your are a senoir{AI_Role} working in a company. You always have a {AI_Goal} in your mind and you have {AI_Context}""",input_variables=['role','goal','context'])

prompt = template.invoke({'AI_Role' : role ,'AI_Goal' : goal, 'AI_Context' : context})
model = ChatOpenAI(model= 'gpt-3.5-turbo')


response = model.invoke(prompt)

if st.button("Answer"):
    st.write(response.content)