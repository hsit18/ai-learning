from langchain_app.models.hf_api import get_model
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser


# Define the model
model = get_model({"repo_id": "google/gemma-2-2b-it"})

parser = JsonOutputParser()

template = PromptTemplate(
    template='Give me 5 facts about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({'topic':'black hole'})

print(result)

