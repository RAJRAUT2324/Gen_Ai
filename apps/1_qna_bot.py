# Project One FullWorking CHatbot Qna

import os
from dotenv import load_dotenv
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

st.set_page_config(page_title="AskBuddy Q&A Bot", page_icon="🤖", layout="centered")

st.title("🤖 AskBuddy Q&A Bot")
st.caption("Powered by Gemini 2.5 Flash & LangChain")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

query = st.chat_input("Ask me anything...")

if query:
    st.session_state.chat_history.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)

    try:
        llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
        res = llm.invoke(query)
        
        st.session_state.chat_history.append({"role": "assistant", "content": res.content})
        with st.chat_message("assistant"):
            st.markdown(res.content)
    except Exception as e:
        st.error(f"Error: {e}")