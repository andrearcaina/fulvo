from server.database import db

class Team(db.Model):
    __tablename__ = "teams"

    team_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    team_name = db.Column(db.String(20), nullable=False)
    skill_level = db.Column(db.String(20), nullable=False)

    def __init__(self, team_name, skill_level):
        self.team_name = team_name
        self.skill_level = skill_level

    def to_dict(self):
        return {
            "team_id": self.team_id,
            "team_name": self.team_name,
            "skill_level": self.skill_level
        }