# langchain import statements

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint 
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough

from dotenv import load_dotenv

load_dotenv()


# passthrought = RunnablePassthrough()

# print(passthrought.invoke("Hello World!"))





prompt1 = PromptTemplate(
    template = 'Write a joke on {topic}',
    input_variables = ['topic']
)

llm = HuggingFaceEndpoint(
    repo_id = "mistralai/Mistral-7B-Instruct-v0.2",
    task = "text-generation",
    max_new_tokens = 100,
    temperature = 0.7
)
model = ChatHuggingFace(llm=llm)

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






