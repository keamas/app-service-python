from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World! this is AppService 2 - West Europe"
