from flask import jsonify, g
from models.team import Team

def listAllTeams():
    teams = g.db.query(Team).all()
    teams_list = [team.to_dict() for team in teams]

    return jsonify(teams_list)
