from flask import jsonify, g
from models.match_referee import Match_Referee as MR

def listAllMR():
    mr = g.db.query(MR).all()
    mr_list = [r.to_dict() for r in mr]

    return jsonify(mr_list)
