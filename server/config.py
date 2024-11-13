from dotenv import load_dotenv
import os

load_dotenv()

class Config:    
    USER = os.environ.get("ORACLE_USER")
    PASSWORD = os.environ.get("ORACLE_PASS")
    HOST = os.environ.get("ORACLE_HOST")
    PORT = os.environ.get("ORACLE_PORT")
    SID = os.environ.get("ORACLE_SID")

    DATABASE_URL = f"oracle+oracledb://{USER}:{PASSWORD}@{HOST}:{PORT}/?service_name={SID}"

    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False