from flask import jsonify, g
from server.models.house_league import House_League as HL

def list_all_hl():
    hl = g.db.query(HL).all()
    hl_list = [m.to_dict() for m in hl]

    return jsonify(hl_list)
