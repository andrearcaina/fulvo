from dotenv import load_dotenv
import os

load_dotenv()

class Config:    
    # database configuration
    USER = os.environ.get("ORACLE_USER")
    PASSWORD = os.environ.get("ORACLE_PASS")
    HOST = os.environ.get("ORACLE_HOST")
    PORT = os.environ.get("ORACLE_PORT")
    SID = os.environ.get("ORACLE_SID")

    SQLALCHEMY_DATABASE_URI = f"oracle+oracledb://{USER}:{PASSWORD}@{HOST}:{PORT}/?service_name={SID}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # app configuration
    JSON_SORT_KEYS = False
