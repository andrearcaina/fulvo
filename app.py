from flask import Flask, render_template
from routes.player_bp import player_bp

app = Flask(__name__)

app.register_blueprint(player_bp, url_prefix="/player")

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)