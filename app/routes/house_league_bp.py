from flask import Blueprint
from app.controllers import (
    list_all_hl,
    list_hl_by_id,
    create_hl,
    update_hl,
    delete_hl
) 

hl_bp = Blueprint("hl_bp", __name__)

hl_bp.route("/read", methods=["GET"])(list_all_hl)
hl_bp.route("/read/<int:match_id>", methods=["GET"])(list_hl_by_id)
hl_bp.route("/create", methods=["POST"])(create_hl)
hl_bp.route("/update", methods=["PUT"])(update_hl)
hl_bp.route("/delete/<int:match_id>", methods=["DELETE"])(delete_hl)
