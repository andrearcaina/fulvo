from flask import Blueprint
from app.controllers import (
    list_all_ms, 
    list_ms_by_id
)

ms_bp = Blueprint("ms_bp", __name__)

ms_bp.route("/read", methods=["GET"])(list_all_ms)
ms_bp.route("/read/<int:match_id>", methods=["GET"])(list_ms_by_id)