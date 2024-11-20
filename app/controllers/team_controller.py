from flask import jsonify, g, request
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

def create_ts():
    data = request.get_json()

    if g.db.query(TS).filter(TS.team_id == data.get("team_id")).first():
        return jsonify({"error": "That team ID already exists"}), 404

    if g.db.query(TS).filter(TS.team_name == data.get("team_name")).first():
        return jsonify({"error": "That team name already exists"}), 404

    print(data)

    new_team = TS(**data)
    g.db.add(new_team)
    g.db.commit()

    return jsonify(new_team.to_dict()), 201

def update_ts(team_id):
    data = request.get_json()
    team = g.db.query(TS).filter(TS.team_id == team_id).first()

    if not team: #make sure that the team is found in the database so we can change it
        return jsonify({"error": "That record is not found"}), 404
    
    for key, value in data.items():
        setattr(team, key, value)
    
    g.db.commit()

    return jsonify({"message": "Updated record successfully"}), 200

def delete_ts(team_id):
    team = g.db.query(TS).filter(TS.team_id == team_id).first()

    if not team:
        return jsonify({"error": "That record is not found"}), 404

    g.db.delete(team)
    g.db.commit()
    
    return jsonify({"message": "Record deleted successfully"}), 200
