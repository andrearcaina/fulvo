from sqlalchemy import Column, Integer, String, ForeignKey
from models.user import User
import bcrypt

class Player(User):
    __tablename__ = "players"

    player_id = Column(Integer, ForeignKey("users.user_id"), index=True, autoincrement=True)
    team_id = Column(Integer, ForeignKey("team.team_id"), nullable=False)
    position = Column(String(50), nullable=False)
    skill_level = Column(String(50), nullable=False)

    def __init__(self, first_name, last_name, age, team_id, role, position, skill_level):
        super().__init__(first_name, last_name, age, role)
        self.team_id = team_id
        self.position = position
        self.skill_level = skill_level
