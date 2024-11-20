from flask import Blueprint
from app.controllers import (
    list_all_ms, 
    list_ms_by_id,
    create_ms,
    update_ms,
    delete_ms
)

ms_bp = Blueprint("ms_bp", __name__)

ms_bp.route("/read", methods=["GET"])(list_all_ms)
ms_bp.route("/read/<int:match_id>", methods=["GET"])(list_ms_by_id)
ms_bp.route("/create/", methods=["POST"])(create_ms)
ms_bp.route("/update/<int:match_id>", methods=["PUT"])(update_ms)
ms_bp.route("/delete/<int:match_id>", methods=["DELETE"])(delete_ms)