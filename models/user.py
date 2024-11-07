from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)
    email_address = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    role = Column(String(50), nullable=False)

    def __init__(self, first_name, last_name, age, email_address, password, date_of_birth, role):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email_address = email_address
        self.password = password
        self.date_of_birth = date_of_birth
        self.role = role