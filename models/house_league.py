from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class House_League(Base):
    __tablename__ = "house_league"

    match_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    match_date = Column(Date, nullable=False)
    skill_level = Column(String(20), nullable=False)
    ht_id = Column(Integer, ForeignKey("teams.team_id"), nullable=False)
    at_id = Column(Integer, ForeignKey("teams.team_id"), nullable=False)
    ht_score = Column(Integer, nullable=False)
    at_score = Column(Integer, nullable=False)

    def __init__(self, match_date, skill_level, ht_id, at_id, ht_score, at_score):
        self.match_date = match_date
        self.skill_level = skill_level
        self.ht_id = ht_id
        self.at_id = at_id
        self.ht_score = ht_score
        self.at_score = at_score
        self.validate_teams()

    def validate_teams(self):
        if self.ht_id == self.at_id:
            raise ValueError("Home team ID and away team ID cannot be the same")