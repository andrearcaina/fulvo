from flask import g
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    db.init_app(app)

    @app.before_request
    def before_request():
        g.db = db.session

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        if hasattr(g, "db"):
            g.db.close()

__all__ = ["db", "init_db"]