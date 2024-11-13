from flask import jsonify, g
from app.models import Referee as RS

def list_all_rs():
    referees = g.db.query(RS).all()

    if not referees:
        return jsonify({"error": "That record is not found"}), 404

    rs_resp = [referee.to_dict() for referee in referees]

    return jsonify(rs_resp), 200

def list_rs_by_id(referee_id):
    referee = g.db.query(RS).filter(RS.referee_id == referee_id).first()

    if not referee:
        return jsonify({"error": "That record is not found"}), 404

    rs_resp = referee.to_dict()

    return jsonify(rs_resp), 200