from flask import jsonify, g
from models.user import User

def listAllUsers():
    users = g.db.query(User).all()
    users_list = [user.to_dict() for user in users]

    return jsonify(users_list)
