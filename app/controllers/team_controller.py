from flask import jsonify, g
from app.models import Team as TS

def list_all_ts():
    teams = g.db.query(TS).all()

    if not teams:
        return jsonify({"error": "That record is not found"}), 404

    ts_resp = [team.to_dict() for team in teams]

    return jsonify(ts_resp), 200

def list_ts_by_id(team_id):
    team = g.db.query(TS).filter(TS.team_id == team_id).first()

    if not team:
        return jsonify({"error": "That record is not found"}), 404

    ts_resp = team.to_dict()

    return jsonify(ts_resp), 200