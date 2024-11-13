from flask import Blueprint
from app.controllers.match_referee_controller import list_all_mr

mr_bp = Blueprint("mr_bp", __name__)

mr_bp.route("/read", methods=["GET"])(list_all_mr)