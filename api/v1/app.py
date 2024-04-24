#!/usr/bin/python3
"""Flask api for airbnb clone project """


from flask import Flask
from models import storage
from api.v1.views import app_views
from flask import jsonify, request
import os


app = Flask(__name__)

host = os.environ.get(
        'HBNB_API_HOST',
        '0.0.0.0')
port = int(os.environ.get(
        'HBNB_API_PORT',
        5000))

app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


@app.errorhandler(404)
def error_404(exception):
    obj = {
        "error": "Not found"
    }
    response = jsonify(obj)
    response.status_code = 404
    return response


if __name__ == "__main__":
    app.run(host=host, port=port,
            threaded=True)
