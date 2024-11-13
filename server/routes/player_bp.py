from flask import Blueprint
from server.controllers.player_controller import list_all_ps

player_bp = Blueprint("player_bp", __name__)

player_bp.route("/read", methods=["GET"])(list_all_ps)