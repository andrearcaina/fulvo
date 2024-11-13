from flask import Blueprint
from server.controllers.team_controller import list_all_ts

team_bp = Blueprint("team_bp", __name__)

team_bp.route("/read", methods=["GET"])(list_all_ts)