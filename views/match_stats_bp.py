from flask import Blueprint
from controllers.match_stats_controller import listAllMS

ms_bp = Blueprint("ms_bp", __name__)

ms_bp.route("/read", methods=["GET"])(listAllMS)