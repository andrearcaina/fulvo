from database import db

class User(db.Model):
    __tablename__ = "team"

    team_id = db.Column(db.Integer, primary_key=True, index=True, autoincrement=True)
    team_name = db.Column(db.String(100), nullable=False)
    skill_level = db.Column(db.String(100), nullable=False)

    def __init__(self, team_name, skill_level):
        self.team_name = team_name
        self.skill_level = skill_level