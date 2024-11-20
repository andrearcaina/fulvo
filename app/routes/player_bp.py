from flask import Blueprint
from app.controllers import (
    list_all_ps,
    list_ps_by_id,
    update_ps,
    delete_ps
)

player_bp = Blueprint("player_bp", __name__)

player_bp.route("/read", methods=["GET"])(list_all_ps)
player_bp.route("/read/<int:player_id>", methods=["GET"])(list_ps_by_id)
player_bp.route("/update/<int:player_id>", methods=["PUT"])(update_ps)
player_bp.route("/delete/<int:player_id>/<int:team_id>", methods=["DELETE"])(delete_ps)