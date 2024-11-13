from flask import jsonify, g
from app.models.user import User

def list_all_us():
    users = g.db.query(User).all()
    users_list = [user.to_dict() for user in users]

    return jsonify(users_list)
