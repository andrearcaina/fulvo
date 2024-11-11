from database import db
from models.user import User

class Referee(User):
    __tablename__ = "referees"

    referee_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    experience_level = db.Column(db.String(50))

    def __init__(self, first_name, last_name, age, role, experience_level):
        super().__init__(first_name, last_name, age, role)
        self.experience_level = experience_level