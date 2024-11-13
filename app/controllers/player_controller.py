from flask import jsonify, g
from app.models.player import Player

def list_all_ps():
    players = g.db.query(Player).all()
    player_list = [player.to_dict() for player in players]

    return jsonify(player_list)
