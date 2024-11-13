from flask import Blueprint
from server.controllers.match_stats_controller import list_all_ms

ms_bp = Blueprint("ms_bp", __name__)

ms_bp.route("/read", methods=["GET"])(list_all_ms)