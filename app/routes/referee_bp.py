from flask import Blueprint
from app.controllers import (
    list_all_rs,
    list_rs_by_id
)

referee_bp = Blueprint("referee_bp", __name__)

referee_bp.route("/read", methods=["GET"])(list_all_rs)
referee_bp.route("/read/<int:referee_id>", methods=["GET"])(list_rs_by_id)