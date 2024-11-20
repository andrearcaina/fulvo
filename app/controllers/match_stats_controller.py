from flask import jsonify, g
from app.models import Match_Stats as MS

def list_all_ms():
    ms = g.db.query(MS).all()
    
    if not ms:
        return jsonify({"error": "That record is not found"}), 404

    ms_resp = [m.to_dict() for m in ms]

    return jsonify(ms_resp), 200

# get a record by match ID
def list_ms_by_id(match_id):
    ms = g.db.query(MS).filter(MS.match_id == match_id).first()
    
    if not ms:
        return jsonify({"error": "That record is not found"}), 404
    
    ms_resp = ms.to_dict()

    return jsonify(ms_resp), 200

def create_ms():
    pass

def update_ms(match_id):
    pass

def delete_ms(match_id):
    pass