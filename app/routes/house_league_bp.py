from flask import Blueprint
from app.controllers import (
    list_all_hl,
    list_hl_by_id,
    create_house_league,
    delete_house_league,
    update_house_league
) 

hl_bp = Blueprint("hl_bp", __name__)

hl_bp.route("/read", methods=["GET"])(list_all_hl)
hl_bp.route("/read/<int:match_id>", methods=["GET"])(list_hl_by_id)
hl_bp.route("/create", methods=["POST"])(create_house_league)
hl_bp.route("/delete/<int:match_id>", methods=["DELETE"])(delete_house_league)
hl_bp.route("/update/<int:match_id>", methods=["PUT"])(update_house_league)