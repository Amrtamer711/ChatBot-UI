from flask import Flask, render_template, request, jsonify
import torch
# from transformers import AutoModelForCausalLM, AutoTokenizer


app = Flask(__name__)

@app.route("/")
def getIndex():
    return render_template("index.html")

@app.route("/get", methods = ["GET", "POST"])
def chatBotReply():
    text = request.form["message"]
    input = text
    return "this is my answer"

def getReply():
    return 0

if __name__ == "__main__":
    app.run(debug=True)