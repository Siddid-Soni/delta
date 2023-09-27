from flask import Flask
from flask import request

app = Flask(__name__)

n=0

@app.route("/")
def hello_world():
    global n
    if request:
        n+=1
    return {
        "response" : "Hello World!",
        "times-responded" : n
    }