from flask import Blueprint
from server.controllers.referee_controller import list_all_rs

referee_bp = Blueprint("referee_bp", __name__)

referee_bp.route("/read", methods=["GET"])(list_all_rs)