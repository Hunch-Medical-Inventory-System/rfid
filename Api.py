from flask import Flask
app = Flask(__name__)


@app.route(rule='/', methods=['GET'])
def hello_world():
    return 'Hello World'


@app.route(rule='/test', methods=['POST'])
def test():
    return 'Hello World'


if __name__ == '__main__':
    app.run()
