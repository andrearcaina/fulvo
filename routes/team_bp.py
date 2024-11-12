from flask import Blueprint
from controllers.team_controller import listAllTeams

team_bp = Blueprint("team_bp", __name__)

team_bp.route("/read", methods=["GET"])(listAllTeams)