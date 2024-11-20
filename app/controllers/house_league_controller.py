from flask import jsonify, g, request
from app.models import (
    House_League as HL,
    Team as TS
)

from datetime import datetime

# get all records
def list_all_hl():
    hl = g.db.query(HL).all()

    if not hl:
        return jsonify({"error": "House League Table is not found"}), 404

    return jsonify([m.to_dict() for m in hl]), 200

# get a record by match ID
def list_hl_by_id(match_id):
    hl = g.db.query(HL).filter(HL.match_id == match_id).first()
    
    if not hl:
        return jsonify({"error": "That record is not found"}), 404
    
    return jsonify(hl.to_dict()), 200


def create_hl():
    data = request.get_json()
    if g.db.query(HL).filter(HL.match_id == data.get("match_id")).first(): #checks to see if the match is already in the database
        return jsonify({"error": "Match ID Already Exists"}), 404
    
    #make sure that the home team ID exists in the teams table
    if not g.db.query(TS).filter(TS.team_id == data.get("ht_id")).first():
        return jsonify({"error": "Home Team does not exist"}), 404
    
    #make sure that the home team ID exists in the teams table
    if not g.db.query(TS).filter(TS.team_id == data.get("at_id")).first():
        return jsonify({"error": "Away Team does not exist"}), 404


    if data.get("match_date"): #makes sure that the data format is good
        data["match_date"] = datetime.strptime(data["match_date"], "%Y-%m-%d")
    
    new_entry = HL(**data)
    g.db.add(new_entry)
    g.db.commit()

    return jsonify(new_entry.to_dict()), 201

def update_hl(match_id):
    data = request.get_json()
    house_league = g.db.query(HL).filter(HL.match_id == match_id).first()

    if not house_league: #make sure that the team is found in the database so we can change it
        return jsonify({"error": "That record is not found"}), 404
    
    for key, value in data.items():
        setattr(house_league, key, value)
    
    g.db.commit()

    return jsonify({"message": "Updated record successfully"}), 200

def delete_hl(match_id):
    house_league = g.db.query(HL).filter(HL.match_id == match_id).first() # finds the entry of the match id

    if not house_league: # checks to see if the record is found
        return jsonify({"error": "That record is not found"}), 404
    
    g.db.delete(house_league)
    g.db.commit()

    return jsonify({"message": "Record deleted successfully"}), 200