from app.database import db

class Match_Referee(db.Model):
    __tablename__ = "match_referee"

    match_id = db.Column(db.Integer, db.ForeignKey("house_league.match_id"), nullable=False)
    referee_id = db.Column(db.Integer, db.ForeignKey("referees.referee_id"), nullable=False)
    
    __table_args__ = (
        db.PrimaryKeyConstraint("match_id", "referee_id"),
    )

    def __init__(self, match_id, referee_id):
        self.match_id = match_id
        self.referee_id = referee_id
    
    def to_dict(self):
        return {
            "match_id": self.match_id,
            "referee_id": self.referee_id
        }
    