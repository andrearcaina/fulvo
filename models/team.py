from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
import bcrypt

Base = declarative_base()

class User(Base):
    __tablename__ = "team"

    team_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    team_name = Column(String(100), nullable=False)
    skill_level = Column(String(100), nullable=False)

    def __init__(self, team_name, skill_level):
        self.team_name = team_name
        self.skill_level = skill_level