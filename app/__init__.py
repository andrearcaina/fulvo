from flask import Flask, g
from app.config import Config
from app.database import db, init_db
from app.routes import register_blueprints
from app.views import register_views

def init_app():
    app = Flask(__name__)

    # load the configuration from the Config class in config.py into the app
    app.config.from_object(Config)
    app.json.sort_keys = app.config["JSON_SORT_KEYS"]

    # initialize the database with the app and register the blueprints (routes) of the app
    try:
        init_db(app)
        register_blueprints(app)
        register_views(app)
    except Exception as e:
        print(f"An error occurred: {e}")

    @app.before_request
    def before_request():
        g.db = db.session

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        if hasattr(g, "db"):
            g.db.close()

    return app