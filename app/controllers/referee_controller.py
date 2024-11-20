from flask import jsonify, g, request
from app.models import (
    User as US,
    Referee as RS,
    Match_Referee as MR,    
)

def list_all_rs():
    referees = g.db.query(RS).all()

    if not referees:
        return jsonify({"error": "That record is not found"}), 404

    return jsonify([referee.to_dict() for referee in referees]), 200

def list_rs_by_id(referee_id):
    referee = g.db.query(RS).filter(RS.referee_id == referee_id).first()

    if not referee:
        return jsonify({"error": "That record is not found"}), 404

    return jsonify(referee.to_dict()), 200

def update_rs(referee_id):
    data = request.get_json()
    referee = g.db.query(RS).filter(RS.referee_id == referee_id).first()

    # if trying to update the referee_id column
    if data.get("referee_id"):
        return jsonify({"error": "You cannot update the referee_id"}), 400

    if not referee:
        return jsonify({"error": "That record is not found"}), 404

    for key, value in data.items():
        setattr(referee, key, value)

    g.db.commit()

    return jsonify(referee.to_dict()), 200

def delete_rs(referee_id):
    referee = g.db.query(RS).filter(RS.referee_id == referee_id).first()

    if not referee:
        return jsonify({"error": "That record is not found"}), 404

    match_referee = g.db.query(MR).filter(MR.referee_id == referee_id).first()
    if match_referee:
        g.db.delete(match_referee)

    user = g.db.query(US).filter(US.user_id == referee_id).first()
    if user:
        g.db.delete(user)

    g.db.delete(referee)
    g.db.commit()

    return jsonify({"message": "Record deleted successfully"}), 200