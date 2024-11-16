from flask import Blueprint
from app.controllers import (
    drop_db,
    create_db,
    populate_db
)

menu_bp = Blueprint("menu_bp", __name__)

menu_bp.route("/drop", methods=["POST"])(drop_db)
menu_bp.route("/create", methods=["POST"])(create_db)
menu_bp.route("/populate", methods=["POST"])(populate_db)