from flask import jsonify, g
from models.match_stats import Match_Stats as MS

def listAllMS():
    ms = g.db.query(MS).all()
    ms_list = [m.to_dict() for m in ms]

    return jsonify(ms_list)
