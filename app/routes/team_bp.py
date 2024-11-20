from flask import Blueprint
from app.controllers import (
    list_all_ts, 
    list_ts_by_id, 
    create_ts, 
    update_ts,
    delete_ts
)

team_bp = Blueprint("team_bp", __name__)

team_bp.route("/read", methods=["GET"])(list_all_ts)
team_bp.route("/read/<int:team_id>", methods=["GET"])(list_ts_by_id)
team_bp.route("/create", methods=["POST"])(create_ts)
team_bp.route("/update/<int:team_id>",methods=["PUT"])(update_ts)
team_bp.route("/delete/<int:team_id>",methods=["DELETE"])(delete_ts)