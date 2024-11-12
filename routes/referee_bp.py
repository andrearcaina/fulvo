from flask import Blueprint
from controllers.referee_controller import listAllReferees

referee_bp = Blueprint("referee_bp", __name__)

referee_bp.route("/read", methods=["GET"])(listAllReferees)