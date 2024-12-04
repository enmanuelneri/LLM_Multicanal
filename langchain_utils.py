# Este archivo contendrá las funciones relacionadas con LangChain.
from langchain_community.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

llm = OpenAI(openai_api_key=OPENAI_API_KEY)
prompt_template = PromptTemplate(
    input_variables=["question"],
    template="Responde la siguiente pregunta: {question}"
)
chain = LLMChain(llm=llm, prompt=prompt_template)

def get_response(question):
    return chain.run(question)