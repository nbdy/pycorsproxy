from flask import Flask, Response, request
from argparse import ArgumentParser
import requests

app = Flask(__name__)

ap = ArgumentParser()
ap.add_argument("-h", "--host", type=str, help="host to run on")
ap.add_argument("-p", "--port", type=int, help="port to run on")
ap.add_argument("--only-from", type=str, help="only from domain")
args = ap.parse_args()


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
