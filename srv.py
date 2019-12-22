from flask import Flask, Response
import requests

app = Flask(__name__)


@app.route("/")
def root():
    return Response("cors proxy")


@app.route("/proxy/<path:path>")
def proxy(path):  # todo validate it is a url
    data = requests.get(path)
    r = Response(data.content)
    r.headers['Access-Control-Allow-Origin'] = "*"
    return r


if __name__ == '__main__':
    app.run("0.0.0.0", 8043, threaded=True)
