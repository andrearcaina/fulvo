from flask import Blueprint
from controllers.team_controller import index

team_bp = Blueprint("team_bp", __name__)

team_bp.route("/", methods=["GET"])(index)