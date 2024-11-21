from flask import Blueprint
from .player_bp import player_bp
from .user_bp import user_bp
from .referee_bp import referee_bp
from .team_bp import team_bp
from .match_stats_bp import ms_bp
from .match_referee_bp import mr_bp
from .house_league_bp import hl_bp
from .menu_bp import menu_bp

def handle_routes(app):
    api_bp = Blueprint("api", __name__, url_prefix="/api")

    api_bp.register_blueprint(player_bp, url_prefix="/player")
    api_bp.register_blueprint(user_bp, url_prefix="/user")
    api_bp.register_blueprint(referee_bp, url_prefix="/referee")
    api_bp.register_blueprint(team_bp, url_prefix="/team")
    api_bp.register_blueprint(ms_bp, url_prefix="/match-stats")
    api_bp.register_blueprint(mr_bp, url_prefix="/match-referees")
    api_bp.register_blueprint(hl_bp, url_prefix="/house-league")
    api_bp.register_blueprint(menu_bp, url_prefix="/menu")

    app.register_blueprint(api_bp)

__all__ = ["handle_routes"]