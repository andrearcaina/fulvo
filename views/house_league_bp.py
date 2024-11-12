from flask import Blueprint
from controllers.house_league_controller import listAllHL

hl_bp = Blueprint("hl_bp", __name__)

hl_bp.route("/read", methods=["GET"])(listAllHL)