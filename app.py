from flask import Flask

print(dir(Flask))

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world'