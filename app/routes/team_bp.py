from flask import Blueprint
from app.controllers import (
    list_all_ts, list_ts_by_id
)

team_bp = Blueprint("team_bp", __name__)

team_bp.route("/read", methods=["GET"])(list_all_ts)
team_bp.route("/read/<int:team_id>", methods=["GET"])(list_ts_by_id)