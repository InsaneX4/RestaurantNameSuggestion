from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import Runnable
import os
from sk_key import openapi_key

# Set the OpenAI API key
os.environ['OPENAI_API_KEY'] = openapi_key

# Initialize the OpenAI model
llm = OpenAI(temperature=0.6)

def name_and_menu_generator(selected_cuisine):
    # Define prompt for restaurant name
    prompt_template_name = PromptTemplate(
        input_variables=["cuisine"],
        template="I want to open a restaurant for {cuisine} food. Suggest a fancy name for this."
    )

    # Define prompt for menu items
    prompt_template_items = PromptTemplate(
        input_variables=["restaurant_name"],
        template="Suggest me some menu items for {restaurant_name}. Return it as a comma-separated string."
    )

    # Chain the prompts and LLM using piping (| operator)
    chain = (
        prompt_template_name | llm |  # Step 1: Generate restaurant name
        prompt_template_items | llm   # Step 2: Generate menu items based on restaurant name
    )

    # Invoke the chain using the input cuisine
    response = chain.invoke({'cuisine': selected_cuisine})

    return response

# Execute the function with "Indian" cuisine
if __name__ == "__main__":
    print(name_and_menu_generator("Indian"))
