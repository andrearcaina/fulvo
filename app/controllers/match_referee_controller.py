from flask import jsonify, g
from app.models.match_referee import Match_Referee as MR

def list_all_mr():
    mr = g.db.query(MR).all()
    
    if not mr:
        return jsonify({"error": "That record is not found"}), 404
    
    mr_resp = [m.to_dict() for m in mr]

    return jsonify(mr_resp), 200

# get a record by match ID
def list_mr_by_id(match_id):
    mr = g.db.query(MR).filter(MR.match_id == match_id).first()
    
    if not mr:
        return jsonify({"error": "That record is not found"}), 404
    
    mr_resp = mr.to_dict()

    return jsonify(mr_resp), 200
