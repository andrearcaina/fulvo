from flask import jsonify, g
from app.models.house_league import House_League as HL

# get all records
def list_all_hl():
    hl = g.db.query(HL).all()

    if not hl:
        return jsonify({"error": "House League Table is not found"}), 404

    hl_resp = [m.to_dict() for m in hl]

    return jsonify(hl_resp), 200

# get a record by match ID
def list_hl_by_id(match_id):
    hl = g.db.query(HL).filter(HL.match_id == match_id).first()
    
    if not hl:
        return jsonify({"error": "That record is not found"}), 404
    
    hl_resp = hl.to_dict()

    return jsonify(hl_resp), 200
