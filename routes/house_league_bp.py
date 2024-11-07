from flask import Blueprint
from controllers.house_league_controller import index

hl_bp = Blueprint("hl_bp", __name__)

hl_bp.route("/", methods=["GET"])(index)