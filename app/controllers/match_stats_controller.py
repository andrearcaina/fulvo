from flask import jsonify, g, request
from app.models import (
    Match_Stats as MS,
    House_League as HL,
    Player as PS
)

def list_all_ms():
    ms = g.db.query(MS).all()
    
    if not ms:
        return jsonify({"error": "That record is not found"}), 404

    ms_resp = [m.to_dict() for m in ms]

    return jsonify(ms_resp), 200

# get a record by match ID
def list_ms_by_id(match_id):
    ms = g.db.query(MS).filter(MS.match_id == match_id)
    
    if not ms:
        return jsonify({"error": "That record is not found"}), 404

    ms_resp = [m.to_dict() for m in ms]

    return jsonify(ms_resp), 200

def create_ms():
    data = request.get_json()

    if g.db.query(MS).filter(MS.player_id == data.get("player_id")).first() and g.db.query(MS).filter(MS.match_id == data.get("match_id")).first():
        return jsonify({"error": "That player ID already exists in that match ID"}), 400

    if not g.db.query(MS).filter(HL.match_id == data.get("match_id")).first() and not g.db.query(MS).filter(PS.player_id == data.get("player_id")).first():
        return jsonify({"error": "That match ID and player ID do not exist"}), 404

    if not g.db.query(MS).filter(HL.match_id == data.get("match_id")).first():
        return jsonify({"error": "That match ID does not exist"}), 404

    if not g.db.query(MS).filter(PS.player_id == data.get("player_id")).first():
        return jsonify({"error": "That player ID does not exist"}), 404

    new_ms = MS(**data)
    g.db.add(new_ms)
    g.db.commit()

    return jsonify(new_ms.to_dict()), 201
    
def update_ms(match_id):
    data = request.get_json()
    ms = g.db.query(MS).filter(MS.match_id == match_id).first()

    if not ms:
        return jsonify({"error": "That record is not found"}), 404
    
    for key, value in data.items():
        setattr(ms, key, value)

    g.db.commit()

    return jsonify(ms.to_dict()), 200

def delete_ms(match_id, player_id):
    ms = g.db.query(MS).filter(MS.match_id == match_id, MS.player_id == player_id).first()

    if not ms:
        return jsonify({"error": "That record is not found"}), 404
    
    g.db.delete(ms)
    g.db.commit()

    return jsonify({"message": "Record deleted successfully"}), 200