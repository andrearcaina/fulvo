from flask import Blueprint
from controllers.match_stats_controller import index

ms_bp = Blueprint("ms_bp", __name__)

ms_bp.route("/", methods=["GET"])(index)