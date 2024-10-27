from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

# Promt Template

promt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an assistant. Please response to the questions"),
        ("user", "Question:{question}")
    ]
)

# streamlit framework
st.title('Langchain demo with LLAMA3 API')
input_text = st.text_input("Search the topic you want")

# ollama llama3 llm
llm = Ollama(model="llama3")
output_parser = StrOutputParser()
chain = promt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))