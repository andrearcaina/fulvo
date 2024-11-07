from flask import Flask, render_template
from routes.blueprints import register_blueprints

app = Flask(__name__)

if register_blueprints(app):
    print(" * Blueprints registered successfully.")
else:
    raise Exception("Failed to register blueprints.")

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)