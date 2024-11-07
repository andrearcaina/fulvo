from sqlalchemy import Column, Integer, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Match_Referee(Base):
    __tablename__ = "match_referee"

    match_id = Column(Integer, ForeignKey("house_league.match_id"), nullable=False)
    referee_id = Column(Integer, ForeignKey("players.referee_id"), nullable=False)
    
    __table_args__ = (
        PrimaryKeyConstraint("match_id", "player_id"),
    )

    def __init__(self, match_id, referee_id):
        self.match_id = match_id
        self.referee_id = referee_id