from flask import jsonify, g
from models.referee import Referee

def listAllReferees():
    referees = g.db.query(Referee).all()
    referees_list = [referee.to_dict() for referee in referees]

    return jsonify(referees_list)
