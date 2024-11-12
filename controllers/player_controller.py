from flask import jsonify, g
from models.player import Player

def listAllPlayers():
    players = g.db.query(Player).all()
    player_list = [player.to_dict() for player in players]

    return jsonify(player_list)
