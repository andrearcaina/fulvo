from flask import Blueprint
from app.controllers import (
    list_all_rs,
    list_rs_by_id,
    update_rs,
    delete_rs
)

referee_bp = Blueprint("referee_bp", __name__)

referee_bp.route("/read", methods=["GET"])(list_all_rs)
referee_bp.route("/read/<int:referee_id>", methods=["GET"])(list_rs_by_id)
referee_bp.route("/update/<int:referee_id>", methods=["PUT"])(update_rs)
referee_bp.route("/delete/<int:referee_id>", methods=["DELETE"])(delete_rs)