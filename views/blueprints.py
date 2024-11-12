from flask import render_template
from views.player_bp import player_bp
from views.user_bp import user_bp
from views.referee_bp import referee_bp
from views.team_bp import team_bp
from views.match_stats_bp import ms_bp
from views.match_referee_bp import mr_bp
from views.house_league_bp import hl_bp

def register_blueprints(app):
    app.register_blueprint(player_bp, url_prefix="/player")
    app.register_blueprint(user_bp, url_prefix="/user")
    app.register_blueprint(referee_bp, url_prefix="/referee")
    app.register_blueprint(team_bp, url_prefix="/team")
    app.register_blueprint(ms_bp, url_prefix="/match-stats")
    app.register_blueprint(mr_bp, url_prefix="/match-referees")
    app.register_blueprint(hl_bp, url_prefix="/house-league")

def render_views(app):
    @app.route("/")
    def index():
        return render_template("pages/index.html")

    @app.route("/user_table")
    def user_table():
        return render_template("pages/users.html")

    @app.route("/player_table")
    def player_table():
        return render_template("pages/players.html")

    @app.route("/referee_table")
    def referee_table():
        return render_template("pages/referee.html")

    @app.route("/team_table")
    def team_table():
        return render_template("pages/team.html")

    @app.route("/match_stats_table")
    def match_stats_table():
        return render_template("pages/match_stats.html")

    @app.route("/match_referee_table")
    def match_referee_table():
        return render_template("pages/match_referee.html")

    @app.route("/house_league_table")
    def house_league_table():
        return render_template("pages/house_league.html")