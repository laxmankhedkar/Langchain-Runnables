# Lambda runnable function for HuggingFace API

# import langchain modules
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompt_values import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda    

# import dotenv to load environment variables
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()

# Create a function to count the number of words in a given text
def word_count(text):
    return len(text.split())


# create a prompt 
prompt = PromptTemplate(
    template = 'Write a joke on {topic}',
    input_variables = ['topic']
)

# create a HuggingFaceEndpoint instance for the Mistral-7B-Instruct-v0.2 model
model = HuggingFaceEndpoint(
    repo_id = "mistralai/Mistral-7B-Instruct-v0.2",
    task = "text-generation",
    max_new_tokens = 100,
    temperature = 0.7
)


# create a ChatHuggingFace instance using the HuggingFaceEndpoint
chat_model = ChatHuggingFace(llm=model)

# create a StrOutputParser instance to parse the output of the model
parser = StrOutputParser()

# creating joke generation chain 
joke_gen_chain = RunnableSequence(    
    prompt,
    chat_model,
    parser
)

# creating parallel chain to run joke generation and word count in parallel
parallel_chain = RunnableParallel(
    {'joke': RunnablePassthrough(), 
     'word_count': RunnableLambda(word_count)}
)

# creating final chain to run joke generation and parallel chain in sequence
final_chain = RunnableSequence(
    joke_gen_chain, 
    parallel_chain
)

# invoke the final chain with the input topic and store the result
result = final_chain.invoke({'topic': 'programming'})

print(result)

