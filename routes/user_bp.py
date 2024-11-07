from flask import Blueprint
from controllers.user_controller import index

user_bp = Blueprint("user_bp", __name__)

user_bp.route("/", methods=["GET"])(index)