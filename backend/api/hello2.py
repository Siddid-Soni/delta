from flask import Flask
from flask import request

app = Flask(__name__)

n=0

@app.route("/")
def hello_world():
    global n
    if request:
        n+=1
    return f"<p>Hello World! You have requested this endpoint {n} times!</p>"