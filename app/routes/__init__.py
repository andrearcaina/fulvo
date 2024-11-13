from .player_bp import player_bp
from .user_bp import user_bp
from .referee_bp import referee_bp
from .team_bp import team_bp
from .match_stats_bp import ms_bp
from .match_referee_bp import mr_bp
from .house_league_bp import hl_bp

def register_blueprints(app):
    app.register_blueprint(player_bp, url_prefix="/player")
    app.register_blueprint(user_bp, url_prefix="/user")
    app.register_blueprint(referee_bp, url_prefix="/referee")
    app.register_blueprint(team_bp, url_prefix="/team")
    app.register_blueprint(ms_bp, url_prefix="/match-stats")
    app.register_blueprint(mr_bp, url_prefix="/match-referees")
    app.register_blueprint(hl_bp, url_prefix="/house-league")

__all__ = ["register_blueprints"]