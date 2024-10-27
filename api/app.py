from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()

os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")

app = FastAPI(
    title="Langchain server",
    version="1.0",
    description="A simple API Server"
)

model=ChatOpenAI()

llm1=Ollama(model="llama3")
llm2=Ollama(model="mistral")

prompt1=ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")
prompt2=ChatPromptTemplate.from_template("Write me a poem about {topic} for a child")
prompt3=ChatPromptTemplate.from_template("Write me a paragraph about {topic} for newspaper")

add_routes(
    app,
    prompt1|llm1,
    path="/essay"
)

add_routes(
    app,
    prompt2|llm2,
    path="/poem"
)

add_routes(
    app,
    prompt3|model,
    path="/paragraph"
)

if __name__=="__main__":
    uvicorn.run(app,host="0.0.0.0",port=8000)