from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv


load_dotenv()

domain = input("Domain:" )
query = input("Query: " )



messages = ChatPromptTemplate.from_messages([
    ("system", "You are an expert on YouTubers and content creators."),
    ("human", "Tell me about {youtuber}.")
])

model = ChatOpenAI(model = 'gpt-4o')

prompt = messages.invoke({"youtuber": "MrBeast"})

reponse = model.invoke(prompt)

print(reponse.content)  