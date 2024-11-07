from flask import Blueprint
from controllers.referee_controller import index

referee_bp = Blueprint("referee_bp", __name__)

referee_bp.route("/", methods=["GET"])(index)