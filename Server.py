# This file generates a Server using flask.
# It utilizes globalKalman.py as globalKalman to provide access to the shared global variable kalmanX and kalmanY

import flask
import globalKalman

def initServer():
    app = flask.Flask(__name__)
    @app.route('/')
    def index():
        return str(globalKalman.kalmanX)

    app.run(debug = True, host = '0.0.0.0')