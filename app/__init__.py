from flask import Flask, g
from app.config import Config
from app.database import init_db
from app.routes import handle_routes
from app.views import serve_views

def init_app():
    app = Flask(__name__)

    # load the configuration from the Config class in config.py into the app
    app.config.from_object(Config)
    app.json.sort_keys = app.config["JSON_SORT_KEYS"]

    # initialize the database with the app and register the blueprints (routes) of the app
    try:
        init_db(app)
        handle_routes(app)
        serve_views(app)
    except Exception as e:
        print(f"An error occurred: {e}")

    return app