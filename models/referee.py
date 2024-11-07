from sqlalchemy import Column, Integer, String, ForeignKey
from models.user import User

class Referee(User):
    __tablename__ = "referees"

    referee_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    experience_level = Column(String(50))

    def __init__(self, first_name, last_name, age, role, experience_level):
        super().__init__(first_name, last_name, age, role)
        self.experience_level = experience_level