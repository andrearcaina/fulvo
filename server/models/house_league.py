from server.database import db

class House_League(db.Model):
    __tablename__ = "house_league"

    match_id = db.Column(db.Integer, primary_key=True, index=True, autoincrement=True)
    match_date = db.Column(db.Date, nullable=False)
    skill_level = db.Column(db.String(20), nullable=False)
    ht_id = db.Column(db.Integer, db.ForeignKey("teams.team_id"), nullable=False)
    at_id = db.Column(db.Integer, db.ForeignKey("teams.team_id"), nullable=False)
    ht_score = db.Column(db.Integer, nullable=False)
    at_score = db.Column(db.Integer, nullable=False)

    def __init__(self, match_date, skill_level, ht_id, at_id, ht_score, at_score):
        self.match_date = match_date
        self.skill_level = skill_level
        self.ht_id = ht_id
        self.at_id = at_id
        self.ht_score = ht_score
        self.at_score = at_score
        self.__validate_teams()

    def __validate_teams(self):
        if self.ht_id == self.at_id:
            raise ValueError("Home team ID and away team ID cannot be the same")
        
    def to_dict(self):
        return {
            "match_id": self.match_id,
            "match_date": self.match_date.strftime("%Y-%m-%d"),
            "skill_level": self.skill_level,
            "ht_id": self.ht_id,
            "at_id": self.at_id,
            "ht_score": self.ht_score,
            "at_score": self.at_score
        }