from flask import jsonify, g
from app.models.referee import Referee

def list_all_rs():
    referees = g.db.query(Referee).all()
    referees_list = [referee.to_dict() for referee in referees]

    return jsonify(referees_list)
