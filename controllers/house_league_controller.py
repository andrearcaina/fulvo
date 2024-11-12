from flask import jsonify, g
from models.house_league import House_League as HL

def listAllHL():
    hl = g.db.query(HL).all()
    hl_list = [m.to_dict() for m in hl]

    return jsonify(hl_list)
