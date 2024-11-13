from flask import Blueprint
from app.controllers.user_controller import list_all_us

user_bp = Blueprint("user_bp", __name__)

user_bp.route("/read", methods=["GET"])(list_all_us)