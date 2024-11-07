from sqlalchemy import Column, Integer, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Match_Stats(Base):
    __tablename__ = "house_league"

    match_id = Column(Integer, ForeignKey("house_league.match_id"), nullable=False)
    player_id = Column(Integer, ForeignKey("players.player_id"), nullable=False)
    goals = Column(Integer)
    assists = Column(Integer)
    minutes_played = Column(Integer)
    yellow_cards = Column(Integer)
    red_cards = Column(Integer)
    attempted_goals = Column(Integer)

    __table_args__ = (
        PrimaryKeyConstraint("match_id", "player_id"),
    )

    def __init__(self, match_id, player_id, goals, assists, minutes_played, yellow_cards, red_cards, attempted_goals):
        self.match_id = match_id
        self.player_id = player_id
        self.goals = goals
        self.assists = assists
        self.minutes_played = minutes_played
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards
        self.attempted_goals = attempted_goals