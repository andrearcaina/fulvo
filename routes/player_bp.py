from flask import Blueprint
from controllers.player_controller import index

player_bp = Blueprint("player_bp", __name__)

player_bp.route("/", methods=["GET"])(index)