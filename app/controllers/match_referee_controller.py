from flask import jsonify, g, request
from app.models import (
    Match_Referee as MR,
    House_League as HL,
    Referee as RS,                   
)

def list_all_mr():
    mr = g.db.query(MR).all()
    
    if not mr:
        return jsonify({"error": "That record is not found"}), 404
    
    mr_resp = [m.to_dict() for m in mr]

    return jsonify(mr_resp), 200

# get a record by match ID
def list_mr_by_id(match_id):
    mr = g.db.query(MR).filter(MR.match_id == match_id).first()
    
    if not mr:
        return jsonify({"error": "That record is not found"}), 404
    
    mr_resp = mr.to_dict()

    return jsonify(mr_resp), 200

def create_mr():
    data = request.get_json()

    #need to make sure that the match_id does not already exist in the MR table
    #if g.db.query(MR).filter(MR.match_id == data.get("match_id")).first():
    #   return jsonify({"error": "That Match ID already exists"}), 404
    
    #make sure that match_id exists in the house league table
    if not g.db.query(HL).filter(HL.match_id == data.get("match_id")).first():
        return jsonify({"error": "Match ID does not exist in House League Table"}), 404

    #make sure that the referee_id exists in the referee table
    if not g.db.query(RS).filter(RS.referee_id == data.get("referee_id")).first():
        return jsonify({"error": "Referee ID does not exist in the Referee Table"}), 404
    
    new_MR = MR(**data)
    g.db.add(new_MR)
    g.db.commit()

    return jsonify(new_MR.to_dict()), 201

def update_mr(match_id):
    data = request.get_json()
    match_referee = g.db.query(MR).filter(MR.match_id == match_id).first()
    if not match_referee:
        return jsonify({"error": "That record is not found"}), 404
    
    for key, value in data.items():
        setattr(match_referee, key, value)
    
    g.db.commit()
    
    return jsonify(match_referee.to_dict()), 200

def delete_mr(match_id):
    referee = g.db.query(MR).filter(MR.match_id == match_id).first()

    if not referee:
        return jsonify({"error": "That record is not found"}), 404
    
    g.db.delete(referee)
    g.db.commit()

    return jsonify({"message": "Record deleted successfully"}), 200