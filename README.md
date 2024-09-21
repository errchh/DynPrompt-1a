# DynPrompt-1a

Dynamic Prompt Assistant - Single Agent  

## Key Features

``Automate repeatitive tasks using gen AI.``

``$0 subscription fee. 100% data privacy.``

## About the Project

This project demonstrate my understanding of prompt engineering of gen AI and coding in Python using gen AI. 

It is a tool for automating repeatitive tasks -- minimising time spend non-value adding processes, increasing work efficiency. 

This is a project after my completion of the ``AI Python course`` and the ``Prompt Engineering with Llama course`` from ``deeplearning.ai``. 

## Technical Details

* Python version: 3.11
* Libraries used: ollama-python
* Dependencies required: pandas 

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

Resources of prompt engineering: 

- deeplearning.ai Prompt Engineering for llama course 
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

The responses is largely depends on the LLM in use, and prompt engineering techniques. 

Prompt engineering techniques can be refined with resources mentioned above. 

The LLM model could be used depends on your hardware. The better the model, the higher RAM and VRAM requirements. 

In this script in particular, I am using ``Llama 3.1 8B`` on MacBook M3 Pro ``18GB RAM``. You may run into errors if your VRAM is insufficient. 

Check in terminal to see if Ollama is running correctly. Or edit the script for a smaller LLM accordingly. 

```
ollama run llama3.1:latest
```

## Future Plans and Ideas

I am interested in:

* Langflow -- a low-code tool for multi-agent workflow allows more complex tasks 

* n8n -- an automation workflow tool which works across differnt apps 

## Feedback and Contributions

If you have any feedback or suggestions for improvement, please let me know! 

## License and Attribution

This project is licensed under the MIT License. I would like to thank the instructors from deeplearning.ai. 