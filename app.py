from flask import Flask, g, render_template
from config import Config
from database import db, init_db
from views.blueprints import register_blueprints, render_views

app = Flask(__name__)

# load the configuration from the Config class in config.py into the app
app.config.from_object(Config)
app.json.sort_keys = False # set json to not sort keys

# initialize the database with the app and register the blueprints (routes) of the app
try:
    init_db(app)
    register_blueprints(app)
    render_views(app)
except Exception as e:
    print(f"An error occurred: {e}")

@app.before_request
def before_request():
    g.db = db.session

@app.teardown_appcontext
def shutdown_session(exception=None):
    if hasattr(g, "db"):
        g.db.close()

if __name__ == "__main__":
    app.run(debug=True)