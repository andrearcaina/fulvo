from flask import jsonify, g, request
from app.models import (
    User as US,
    Player as PS,
    Match_Stats as MS,
    Team as TS,
)

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

def update_ps(player_id):
    data = request.get_json()
    player = g.db.query(PS).filter(PS.player_id == player_id).first()
    
    if not player:
        return jsonify({"error": "That record is not found"}), 404
    
    for key, value in data.items():
        setattr(player, key, value)
    
    g.db.commit()
    
    return jsonify(player.to_dict()), 200

def delete_ps(player_id):
    player = g.db.query(PS).filter(PS.player_id == player_id).first()
    
    if not player:
        return jsonify({"error": "That record is not found"}), 404
    
    # if a player is deleted, the player's associated records in the MatchStats table are also deleted
    stat = g.db.query(MS).filter(MS.player_id == player_id).first()
    if stat:
        g.db.delete(stat)
    
    # if a player is deleted, delete the user record
    user = g.db.query(US).filter(US.user_id == player.user_id).first()
    if user:
        g.db.delete(user)

    g.db.delete(player)
    g.db.commit()
    
    return jsonify({"message": "Record deleted successfully"}), 200