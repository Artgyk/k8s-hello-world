from flask import Flask, request

app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return 'hello world'


@app.route('/health')
def health_check():
    return 'ok'
