import os
import ollama
import pandas as pd 

# Set pwd same as app.py 
script_dir = os.path.dirname(__file__)
os.chdir(script_dir)

# Ollama model, error handling 
model = 'llama3.1:latest'

try:
    ollama.chat(model)
except ollama.ResponseError as e:
    print('Error:', e.error)
    if e.status_code == 404:
        ollama.pull(model)

# Read the CSV, error handling 
df = pd.read_csv('data.csv')

try:
    df = pd.read_csv('data.csv')
except FileNotFoundError:
    print("The file does not exist.")
except pd.errors.EmptyDataError:
    print("The file is empty.")
except pd.errors.ParserError:
    print("Error parsing the file. Please check the file format.")

# Column prompt_var to a list
prompt_var_list = df["prompt_var"].tolist()

##### ================================================================== #####
#                                                                            #
#     Edit your base prompt below                                            #
#     Each item in data.csv will sit in a new line under the base prompt     #
#                                                                            #
#### =================================================================== #####

# Base prompt
prompt = """
    You are a helpful assistant expert in branding. Create a brand name using the following keyword. It must be easy to pronounce and easy to remember. 
    Provide the brand name only. 
    Keyword:\n
"""

responses = []  # Create an empty list to store the responses

# Loop variable through LLM 
for item in prompt_var_list:
    response = ollama.chat(model=model, messages=[
        {
            'role': 'user',
            'content': f"""
                {prompt}
                {item}
            """,
        },
    ])
    responses.append(response['message']['content'])  # Append the response to the list
    #print(response['message']['content'])


# Save responses list as csv 
responses = pd.DataFrame(responses, columns=['responses'])  # Convert list to DataFrame
responses.to_csv('responses.csv', index=False)

