from app.database import db

class Player(db.Model):
    __tablename__ = "players"

    player_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey("teams.team_id"))
    position = db.Column(db.String(20), nullable=False)
    skill_level = db.Column(db.String(20), nullable=False, default="beginner")

    def __init__(self, team_id, position, skill_level):
        self.team_id = team_id
        self.position = position
        self.skill_level = skill_level

    def to_dict(self):
        return {
            "player_id": self.player_id,
            "team_id": self.team_id,
            "position": self.position,
            "skill_level": self.skill_level
        }