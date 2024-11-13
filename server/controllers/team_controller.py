from flask import jsonify, g
from server.models.team import Team

def list_all_ts():
    teams = g.db.query(Team).all()
    teams_list = [team.to_dict() for team in teams]

    return jsonify(teams_list)
