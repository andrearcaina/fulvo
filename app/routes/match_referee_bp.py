from flask import Blueprint
from app.controllers import (
    list_all_mr,
    list_mr_by_id,
    create_mr,
    update_mr,
    delete_mr,
)

mr_bp = Blueprint("mr_bp", __name__)

mr_bp.route("/read", methods=["GET"])(list_all_mr)
mr_bp.route("/read/<int:match_id>", methods=["GET"])(list_mr_by_id)
mr_bp.route("/create", methods=["POST"])(create_mr)
mr_bp.route("/update/<int:match_id>", methods=["PUT"])(update_mr)
mr_bp.route("/delete/<int:match_id>", methods=["DELETE"])(delete_mr)