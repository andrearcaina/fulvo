from flask import Blueprint
from server.controllers.house_league_controller import list_all_hl 

hl_bp = Blueprint("hl_bp", __name__)

hl_bp.route("/read", methods=["GET"])(list_all_hl)