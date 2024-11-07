from flask import Blueprint
from controllers.match_referee_controller import index

mr_bp = Blueprint("mr_bp", __name__)

mr_bp.route("/", methods=["GET"])(index)