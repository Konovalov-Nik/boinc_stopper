from flask import Flask
from gevent.pywsgi import WSGIServer

app = Flask(__name__)
STATE = False


@app.route("/get", methods=["GET"])
def get():
    return str(STATE)


@app.route("/set/<state>", methods=["POST"])
def _set(state=False):
    global STATE
    if state in ("True", "true", "1", "yes", "enabled"):
        STATE = True
    else:
        STATE = False

    return str(STATE)


http_server = WSGIServer(('', 5020), app)
http_server.serve_forever()
