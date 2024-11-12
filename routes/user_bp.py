from flask import Blueprint
from controllers.user_controller import listAllUsers

user_bp = Blueprint("user_bp", __name__)

user_bp.route("/read", methods=["GET"])(listAllUsers)