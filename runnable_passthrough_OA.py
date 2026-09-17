# Runnable Passthrough Example with OpenAI and LangChain

# langchain import statements
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough
from dotenv import load_dotenv


load_dotenv()

prompt1 = PromptTemplate(
    template = 'Write a joke on {topic}',
    input_variables = ['topic']
)

model = ChatOpenAI()

parser = StrOutputParser()

prompt2 = PromptTemplate(
    template = 'Explain the following joke on  {text} ',
    input_variables = ['text']
)

joke_generator_chain = RunnableSequence(
    prompt1,    
    model,
    parser
)

paralle_chain = RunnableParallel(
    {'joke': RunnablePassthrough(), 
     'explanation': RunnableSequence(prompt2, model, parser)}
)

final_chain = joke_generator_chain | paralle_chain

print(final_chain.invoke({'topic': 'programming'}))
