from app.database import db

class Match_Stats(db.Model):
    __tablename__ = "match_stats"

    match_id = db.Column(db.Integer, db.ForeignKey("house_league.match_id"), nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey("players.player_id"), nullable=False)
    goals = db.Column(db.Integer)
    assists = db.Column(db.Integer)
    minutes_played = db.Column(db.Integer)
    yellow_cards = db.Column(db.Integer)
    red_cards = db.Column(db.Integer)
    attempted_goals = db.Column(db.Integer)

    __table_args__ = (
        db.PrimaryKeyConstraint("match_id", "player_id"),
    )

    def __init__(self, goals, assists, minutes_played, yellow_cards, red_cards, attempted_goals):
        self.goals = goals
        self.assists = assists
        self.minutes_played = minutes_played
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards
        self.attempted_goals = attempted_goals
    
    def to_dict(self):
        return {
            "match_id": self.match_id,
            "player_id": self.player_id,
            "goals": self.goals,
            "assists": self.assists,
            "minutes_played": self.minutes_played,
            "yellow_cards": self.yellow_cards,
            "red_cards": self.red_cards,
            "attempted_goals": self.attempted_goals
        }