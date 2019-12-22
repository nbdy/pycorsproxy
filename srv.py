from flask import Flask, Response
from argparse import ArgumentParser
import requests

app = Flask(__name__)

ap = ArgumentParser()
ap.add_argument("-h", "--host", type=str, help="host to run on")
ap.add_argument("-p", "--port", type=int, help="port to run on")
args = ap.parse_args()  # todo only from certain hosts


@app.route("/")
def root():
    return Response("cors proxy")  # todo actual info site and how to use this thing


@app.route("/proxy/<path:path>")
def proxy(path):  # todo validate it is a url
    r = Response(requests.get(path))  # todo post/etc requests?
    r.headers['Access-Control-Allow-Origin'] = "*"
    return r


if __name__ == '__main__':
    app.run(args.host, args.port, threaded=True)
