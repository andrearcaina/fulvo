from flask import jsonify, g, request
from app.models import (
    User as US, 
    Player as PS, 
    Referee as RS,
    Team as TS,
)
from datetime import datetime

def list_all_us():
    users = g.db.query(US).all()
    
    if not users:
        return jsonify({"error": "That record is not found"}), 404
    
    return jsonify([user.to_dict() for user in users]), 200

def list_us_by_id(user_id):
    user = g.db.query(US).filter(US.user_id == user_id).first()
    
    if not user:
        return jsonify({"error": "That record is not found"}), 404
    
    return jsonify(user.to_dict()), 200
    
def create_us():
    data = request.get_json()
    
    if g.db.query(US).filter(US.user_id == data.get("user_id")).first():
        return jsonify({"error": "That user ID already exists"}), 400

    if data.get("date_of_birth"):
        data["date_of_birth"] = datetime.strptime(data["date_of_birth"], "%Y-%m-%d")

    if data.get("role") == "player":
        # check if the team_id exists (basically check if the team exists in the table)
        if not g.db.query(TS).filter(TS.team_id == data.get("team_id")).first():
            return jsonify({"error": "That team is not found"}), 404

        player_data = {
            "player_id": data.get("user_id"),
            "team_id": data.get("team_id"),
            "skill_level": data.get("skill_level"),
            "position": data.get("position")
        }
        
        data.pop("team_id")
        data.pop("skill_level")
        data.pop("position")
        
        print(data)
        print(player_data)

        new_user = US(**data)
        g.db.add(new_user)
        g.db.commit()

        new_player = PS(**player_data)
        g.db.add(new_player)
    elif data.get("role") == "referee":
        referee_data = {
            "referee_id": data.get("user_id"),
            "experience_level": data.get("experience_level")
        }
        data.pop("experience_level")
        new_user = US(**data)
        g.db.add(new_user)
        g.db.commit()

        new_referee = RS(**referee_data)
        g.db.add(new_referee)
    
    g.db.commit()
    
    return jsonify(new_user.to_dict()), 201

def update_us(user_id):
    data = request.get_json()
    user = g.db.query(US).filter(US.user_id == user_id).first()
    
    if not user:
        return jsonify({"error": "That record is not found"}), 404
    
    for key, value in data.items():
        setattr(user, key, value)
    
    g.db.commit()
    
    return jsonify(user.to_dict()), 200

def delete_us(user_id):
    user = g.db.query(US).filter(US.user_id == user_id).first()

    if not user:
        return jsonify({"error": "That record is not found"}), 404
    
    # if a user is a player, delete the player record
    player = g.db.query(PS).filter(PS.player_id == user_id).first()
    if player:
        g.db.delete(player)

    # if a user is a referee, delete the referee record
    referee = g.db.query(RS).filter(RS.referee_id == user_id).first()
    if referee:
        g.db.delete(referee)

    # then, delete the user record
    g.db.delete(user)
    g.db.commit()

    return jsonify({"message": "Record deleted successfully"}), 200