# Runnable Parallel Example with Hugging Face Model

# import langchain 
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import StrOutputParser

# import langchain runnables
from langchain_core.runnables import RunnableSequence, RunnableParallel 

# load environment variables from .env file
from dotenv import load_dotenv 

load_dotenv()

# Create Prompt 1
prompt1 = PromptTemplate(
    template = 'Generate a tweet about {topic}',
    input_variables = ['topic']
)

# Create Prompt 2
prompt2 = PromptTemplate(
    template = 'Generate a Linkedin post about {topic}',
    input_variables = ['topic']
)

# Create Hugging Face LLM 
llm = HuggingFaceEndpoint(
    repo_id = "mistralai/Mistral-7B-Instruct-v0.2",
    task = "text-generation",
    max_new_tokens = 100,
    temperature = 0.7
)


# Convert Hugging Face LLM into Chat Model 
model = ChatHuggingFace(llm=llm)



# Create Output Parser 
parser = StrOutputParser()


# Create Tweet Chain 
tweet_chain = RunnableSequence(
    prompt1,
    model,
    parser
)


# Create Linkedin Chain
linkedin_chain = RunnableSequence(
    prompt2,
    model,
    parser
)


# Create a parallel runnable that runs both sequences in parallel
parallel_chain = RunnableParallel({
    'tweet': tweet_chain,
    'linkedin': linkedin_chain
})


# Invoke the parallel chain with a topic
result = parallel_chain.invoke({'topic':'AI'})  

# Print the result of the tweet
print(result['tweet'])


# Print the result of the linkedin post
print(result['linkedin'])
