from database import db

class User(db.Model):
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email_address = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    role = db.Column(db.String(50), nullable=False)

    def __init__(self, first_name, last_name, age, email_address, password, date_of_birth, role):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email_address = email_address
        self.password = password
        self.date_of_birth = date_of_birth
        self.role = role

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "email_address": self.email_address,
            "password": self.password,
            "date_of_birth": self.date_of_birth.strftime("%Y-%m-%d"),
            "role": self.role
        }