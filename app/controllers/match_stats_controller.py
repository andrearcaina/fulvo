from flask import jsonify, g
from app.models.match_stats import Match_Stats as MS

def list_all_ms():
    ms = g.db.query(MS).all()
    ms_list = [m.to_dict() for m in ms]

    return jsonify(ms_list)
