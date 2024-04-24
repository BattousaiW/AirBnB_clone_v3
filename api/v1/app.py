#!/usr/bin/python3
"""Flask api for airbnb clone project """


from flask import Flask
from models import storage
from api.v1.views import app_views
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


if __name__ == "__main__":
    app.run(host=host, port=port,
            threaded=True)
