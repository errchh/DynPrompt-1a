# DynPrompt-1a

Dynamic Prompt Assistant - Single Agent  

## Key Features

``Automate repetitive tasks using gen AI.``

``$0 subscription fee. 100% data privacy.``

## About the Project

This project demonstrates my understanding of prompt engineering and coding in Python using gen AI. 

It is a tool for automating repeatitive tasks -- minimising time spend on non-value adding processes, increasing work efficiency. 

This is a project after my completion of the ``AI Python course`` and the ``Prompt Engineering with Llama course`` from ``deeplearning.ai``. 

## Technical Details

- Python version: 3.11
- Libraries used: ollama-python
- Dependencies required: pandas 

## Installation and Usage

Download and install Ollama from ``https://ollama.com/download`` 

In Terminal: 

```
pip install ollama 
ollama pull llama3.1:latest 
```

```
pip install pandas 
```

### Prep data.csv

``prompt_var`` is the content of your task. 

Paste each of them in the ``prompt_var`` column in separate rows. 

### Set your prompt 

Edit your prompt under ``Base prompt`` section in ``app.py``. Use prompt engineering techniques for desired results. 

Example use cases: 

- Text extractor for email
    ```
    prompt = f"""
        Given is an email from contains product code and corresponding remarks. Identify the product code and remarks within the original text. 
        
        Provide the product code and remark only in csv format, ready to save. Exclude the "```csv" declaration, don't add spaces after the comma, include column headers.

        Format:
        product_code, remark
        product_code_1, remark_1
        ...
        
        Email:
        """
    ```

- Customer review text classifier 
    ```
    prompt = f"""
        Respond with "Positve" or "Negative": 
        the comment is a product reivew, describing an user experience. 

        Comment:
        """
    ```

Resources of prompt engineering: 

- deeplearning.ai Prompt Engineering for Llama course 
- Microsoft / Meta prompt engineering docs 
- SCRIBE method 

### Run app.py

```
cd DynPrompt-1a
python app.py
```

### Results in responses.csv 

``responses.csv`` is saved in the same folder. Open in Excel. 

## Challenges and Limitations

The responses are largely depend on the LLM in use, and prompt engineering techniques. 

Prompt engineering techniques can be refined with resources mentioned above. 

What LLM model could be used depends on your hardware. The better the LLM model, the higher RAM and VRAM requirements. 

In this script in particular, I am using ``Llama 3.1 8B`` on MacBook M3 Pro ``18GB RAM``. You may run into errors if your VRAM is insufficient. 

Check in terminal to see if Ollama is running correctly. Or edit the script for a smaller LLM accordingly. 

```
ollama run llama3.1:latest
```

## Future Plans and Ideas

I am interested in:

- Langflow -- a low-code tool for multi-agent workflow allows more complex tasks 

- n8n -- an automation workflow tool which works across different apps 

## Feedback and Contributions

If you have any feedback or suggestions for improvement, or if you know any good tutorials on Langflow and n8n, please let me know! Let's connect. 

## License and Attribution

This project is licensed under the MIT License. I would like to thank the open source community and the instructors from deeplearning.ai. 
