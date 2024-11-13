from flask import jsonify, g
from app.models.player import Player as PS

def list_all_ps():
    players = g.db.query(PS).all()
    
    if not players:
        return jsonify({"error": "That record is not found"}), 404

    ps_resp = [player.to_dict() for player in players]

    return jsonify(ps_resp), 200

def list_ps_by_id(player_id):
    player = g.db.query(PS).filter(PS.player_id == player_id).first()
    
    if not player:
        return jsonify({"error": "That record is not found"}), 404
    
    ps_resp = player.to_dict()

    return jsonify(ps_resp), 200