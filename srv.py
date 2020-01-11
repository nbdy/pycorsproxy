#!/usr/bin/python3

from sanic import Sanic, response
from argparse import ArgumentParser
import requests

ap = ArgumentParser()
ap.add_argument("--host", type=str, help="host to run on", default="0.0.0.0")
ap.add_argument("--port", type=int, help="port to run on", default=8080)
ap.add_argument("--only-from", type=str, help="only from domain")
args = ap.parse_args()

app = Sanic(__name__)


@app.route("/")
async def root(req):
    return response.text("https://github.com/smthnspcl/pycorsproxy")


@app.route("/proxy/<path:path>")
async def proxy(req, path):  # todo validate it is a url
    r = response.html(requests.get(path).content.decode("utf-8"))  # todo post/etc requests?
    r.headers.add('Access-Control-Allow-Origin', "*")
    return r


if __name__ == '__main__':
    app.run(args.host, args.port)
