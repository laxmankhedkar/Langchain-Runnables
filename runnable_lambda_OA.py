# Lambda runnable function for OpenAI API

# import langchain modules
from langchain_openai import ChatOpenAI
from langchain_core.prompt_values import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda

from dotenv import load_dotenv

load_dotenv()

def word_count(text):
    return len(text.split())


prompt = PromptTemplate(
    template = 'Write a joke on {topic}',
    input_variables = ['topic']
)


model = ChatOpenAI()

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(    
    prompt,
    model,
    parser
)

parallel_chain = RunnableParallel(
    {'joke': RunnablePassthrough(), 
     'word_count': RunnableLambda(word_count)}
)


final_chain = RunnableSequence(
    joke_gen_chain, 
    parallel_chain

)


result = final_chain.invoke({'topic': 'programming'})

final_result = """{} \n word count - {}""".format(result['joke'], result['word_count'])

print(final_result)