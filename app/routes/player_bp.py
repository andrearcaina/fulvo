from flask import Blueprint
from app.controllers.player_controller import (
    list_all_ps,
    list_ps_by_id
)

player_bp = Blueprint("player_bp", __name__)

player_bp.route("/read", methods=["GET"])(list_all_ps)
player_bp.route("/read/<int:player_id>", methods=["GET"])(list_ps_by_id)