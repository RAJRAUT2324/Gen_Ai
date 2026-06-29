
# This is Google search agent who can search on google and give result 

import os
from dotenv import load_dotenv
load_dotenv()

from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver

llm=ChatGroq(model="openai/gpt-oss-20b")
search=GoogleSerperAPIWrapper()

agent=create_agent(
    model=llm,
    tools=[search.run],
    system_prompt="You are aagent who can search any question on google",
    checkpointer=MemorySaver()
)

while True:
    query=input("User:")
    if query.lower()=="quit":
        print("Good Bye !")
        break
    else:
        response=agent.invoke({"messages":[{"role":"user","content":query}]},
                              {"configurable": {"thread_id": "Raj"}})
        print("AI:",response["messages"][-1].content)
        