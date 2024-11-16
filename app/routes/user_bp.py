from flask import Blueprint
from app.controllers import (
    list_all_us, 
    list_us_by_id, 
    create_us, 
    update_us, 
    delete_us
)

user_bp = Blueprint("user_bp", __name__)

user_bp.route("/read", methods=["GET"])(list_all_us)
user_bp.route("/read/<int:user_id>", methods=["GET"])(list_us_by_id)
user_bp.route("/create", methods=["POST"])(create_us)
user_bp.route("/update/<int:user_id>", methods=["PUT"])(update_us)
user_bp.route("/delete/<int:user_id>", methods=["DELETE"])(delete_us)