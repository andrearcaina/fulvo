from flask import jsonify, g
from app.models import User as US

def list_all_us():
    users = g.db.query(US).all()
    
    if not users:
        return jsonify({"error": "That record is not found"}), 404
    
    us_resp = [user.to_dict() for user in users]

    return jsonify(us_resp), 200

def list_us_by_id(user_id):
    user = g.db.query(US).filter(US.user_id == user_id).first()
    
    if not user:
        return jsonify({"error": "That record is not found"}), 404
    
    us_resp = user.to_dict()

    return jsonify(us_resp), 200