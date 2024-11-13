from flask import render_template

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