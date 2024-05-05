# ChatBot-UI
ChatBot that allows users to communicate with LLM. It uses the Python library Flask to link an HTML file page, which uses a CSS file to design the page, with a Python script. The HTML file creates the website and the user can enter text through the text block and submit it to the ChatBot. The text is then retrieved from the HTML page to the Python script via Flask, prompted to an LLM and the output is sent back to the HTM page to be placed as a response, simulating a conversation.

## Command prompt:
![image](https://github.com/Amrtamer711/ChatBot-UI/assets/131773782/ae59a168-d8dd-42c2-a27d-9d181a0ff3d9)

## Home Screen:
![image](https://github.com/Amrtamer711/ChatBot-UI/assets/131773782/deae33d6-9083-4067-9814-9424e819fea1)

Note: Outputs from the conversation depend on the complexity of the LLM used. The LLM DistilGPT-2, a very small LLM. Changing the LLM is very easy by simpley changing the model_name variable to another HuggingFace LLM keyword.
