from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv


load_dotenv()

messages = [
    SystemMessage(
        content="You are a helpful assistant that provides information about YouTubers."
    ),
    HumanMessage(
        content="Who is MrBeast?"
    )
]

model = ChatOpenAI(model = 'gpt-4o')

reponse = model.invoke(messages)

print(AIMessage(content=reponse.content))  