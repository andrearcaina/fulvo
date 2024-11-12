from flask import Blueprint
from controllers.match_referee_controller import listAllMR

mr_bp = Blueprint("mr_bp", __name__)

mr_bp.route("/read", methods=["GET"])(listAllMR)