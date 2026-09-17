import os 
from dotenv import load_dotenv

# Hugging Face imports
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint 

# Langchain imports 
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import StrOutputParser

# Langchain Runnables imports
from langchain_core.runnables import RunnableSequence


# load environment variables from .env file
load_dotenv()


# Prompt 1
prompt1 = PromptTemplate(
    template = 'Write a joke about {topic}',
    input_variables = ['topic']
)


# Hugging Face Model 
llm = HuggingFaceEndpoint(
    repo_id = "mistralai/Mistral-7B-Instruct-v0.2",
    task = "text-generation",
    max_new_tokens = 100,
    temperature = 0.7
)


model = ChatHuggingFace(llm=llm)


# Output Parser 
parser = StrOutputParser()

# Prompt 2
prompt2 = PromptTemplate(
    template = 'Explain the following joke - {text}',
    input_variables = ['text']
)

# Runnable Sequence 
chain = RunnableSequence(
    prompt1,
    model,
    parser,
    prompt2,
    model,
    parser
)


# Invoke the chain with a topic
result = chain.invoke({'topic':'AI'})
print(result)
