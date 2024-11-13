from flask import Blueprint
from app.controllers import (
    list_all_hl,
    list_hl_by_id
) 

hl_bp = Blueprint("hl_bp", __name__)

hl_bp.route("/read", methods=["GET"])(list_all_hl)
hl_bp.route("/read/<int:match_id>", methods=["GET"])(list_hl_by_id)