from database import db

class Referee(db.Model):
    __tablename__ = "referees"

    referee_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), primary_key=True)
    experience_level = db.Column(db.String(50), nullable=False)

    def __init__(self, user_id, experience_level):
        self.referee_id = user_id
        self.experience_level = experience_level

    def to_dict(self):
        return {
            "referee_id": self.referee_id,
            "experience_level": self.experience_level
        }