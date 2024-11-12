from flask import Blueprint
from controllers.player_controller import listAllPlayers

player_bp = Blueprint("player_bp", __name__)

player_bp.route("/read", methods=["GET"])(listAllPlayers)