from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False  # hot fix for minikube, it's adding trailing slash


@app.route('/hello')
def hello_world():
    return 'hello world'


@app.route('/health')
def health_check():
    return 'ok'
