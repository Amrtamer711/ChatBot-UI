# ChatBot-UI
ChatBot that allows users to communicate with LLM. It uses the Python library Flask to link an HTML file page, which uses a CSS file to design the page, with a Python script. The HTML file creates the website and the user can enter text through the text block and submit it to the ChatBot. The text is then retrieved from the HTML page to the Python script via Flask, prompted to an LLM and the output is sent back to the HTM page to be placed as a response, simulating a conversation.  
## Tutorial:

1. To execute the code, simply clone the repository, go to your preferred Python terminal and execute the code using `python app.py`

![image](https://github.com/Amrtamer711/ChatBot-UI/assets/131773782/3fe949d8-6b82-4ec9-8b9c-73df1d74aa70)

2. Go to the link provided by Flask and CTRL + Click on the link

![image](https://github.com/Amrtamer711/ChatBot-UI/assets/131773782/7a5faeb0-f10a-4fe3-9edb-b009de90884f)

3. You should then see a screen similar to this at your command prompt when you return to it:

![image](https://github.com/Amrtamer711/ChatBot-UI/assets/131773782/ae59a168-d8dd-42c2-a27d-9d181a0ff3d9)

4. At the home screen, enter text and wait for a reply (it may take a while depending on the LLM used and the type of machine it is running on):

![image](https://github.com/Amrtamer711/ChatBot-UI/assets/131773782/4a2ca167-4a87-4a63-889b-7283a494ae3e)

## Conversation Example:
![image](https://github.com/Amrtamer711/ChatBot-UI/assets/131773782/deae33d6-9083-4067-9814-9424e819fea1)

## Note 
Outputs from the conversation depend on the complexity of the LLM used. The LLM DistilGPT-2, a very small LLM, will produce pretty bad answers so it is advised to use a larger, more complex LLM on a powerful GPU. Changing the LLM is very easy by simpley changing the model_name variable in `app.py` to another HuggingFace LLM keyword.

![image](https://github.com/Amrtamer711/ChatBot-UI/assets/131773782/7816e748-365f-4257-ba5f-f3f4f54c07e5)

## Report

Project report is avaialble in [`report.docx`] (https://github.com/Amrtamer711/ChatBot-UI/blob/main/report.docx)
