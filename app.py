from flask import Flask, render_template, request, jsonify
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

device = 'cuda' if torch.cuda.is_available() else 'cpu' # setting device to be used as GPU

model_name = "distilgpt2" # specifying model

tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir="D:\HCI project") # getting tokenizer of model using model-agnostic tokenizer class
model = AutoModelForCausalLM.from_pretrained(model_name, cache_dir="D:\HCI project").to(device) # getting model using model-agnostic model class

if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token # setting tokenizer pad token
tokenizer.padding_side = 'left' # setting padding to left as decoder models run from left to right

app = Flask(__name__)

@app.route("/")
def getIndex():
    return render_template("index.html")

@app.route("/get", methods = ["GET", "POST"])
def chatBotReply():
    text = request.form["message"]
    input = text
    return getReply(input)

def getReply(text):
    prompt = str(text)
    print("Beginning generation")
    input_ids = tokenizer(prompt, padding=True, return_tensors='pt', truncation=True).to(device) # tokenizing input prompts
    attention_mask = input_ids['attention_mask'] # retrieving attention mask which is needed in batch inference
    input_ids = input_ids['input_ids'] # retrieving input token IDs to run them through model
    output = model.generate( # function to generate output completion
        input_ids[0].unsqueeze(0), # passing input prompt
        attention_mask=attention_mask[0].unsqueeze(0), # including attention mask
        max_length= int(input_ids.shape[0]) + 500,  # specifying maximum length of model generation
        pad_token_id=tokenizer.pad_token_id,
        no_repeat_ngram_size=2,  # Prevent repeating the same n-grams so will prevent the same token to be repeated n times
        eos_token_id=tokenizer.eos_token_id
      ) # generating outputs from inputs
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True) # retrieving text from tokenized outputs
    response = generated_text[len(prompt):].strip()
    return response

if __name__ == "__main__":
    app.run()
