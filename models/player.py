from database import db
from models.user import User

class Player(User):
    __tablename__ = "players"

    player_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey("team.team_id"))
    position = db.Column(db.String(50), nullable=False)
    skill_level = db.Column(db.String(50), nullable=False)

    def __init__(self, first_name, last_name, age, team_id, role, position, skill_level):
        super().__init__(first_name, last_name, age, role)
        self.team_id = team_id
        self.position = position
        self.skill_level = skill_level
