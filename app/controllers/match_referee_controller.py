from flask import jsonify, g
from app.models.match_referee import Match_Referee as MR

def list_all_mr():
    mr = g.db.query(MR).all()
    mr_list = [r.to_dict() for r in mr]

    return jsonify(mr_list)
