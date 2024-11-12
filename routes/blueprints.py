from routes.player_bp import player_bp
from routes.user_bp import user_bp
from routes.referee_bp import referee_bp
from routes.team_bp import team_bp
from routes.match_stats_bp import ms_bp
from routes.match_referee_bp import mr_bp
from routes.house_league_bp import hl_bp

def register_blueprints(app):
    app.register_blueprint(player_bp, url_prefix="/player")
    app.register_blueprint(user_bp, url_prefix="/user")
    app.register_blueprint(referee_bp, url_prefix="/referee")
    app.register_blueprint(team_bp, url_prefix="/team")
    app.register_blueprint(ms_bp, url_prefix="/match-stats")
    app.register_blueprint(mr_bp, url_prefix="/match-referees")
    app.register_blueprint(hl_bp, url_prefix="/house-league")