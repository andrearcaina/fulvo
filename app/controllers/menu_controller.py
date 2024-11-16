from flask import jsonify
from app.database import db
from sqlalchemy import text

def execute_sql_script(file_path):
    try:
        with open(file_path, "r") as f:
            sql_script = f.read()
        
        with db.engine.connect() as connection:
            trans = connection.begin()
            
            try:
                for statement in sql_script.split(";"):
                    if statement.strip():
                        connection.execute(text(statement))
                trans.commit()
                return jsonify({"message": f"{file_path.split("/")[-1]} executed successfully"}), 200
            except Exception as e:
                trans.rollback()                
                return jsonify({"error": str(e)}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def drop_db():
    return execute_sql_script("app/db/drop.sql")

def create_db():
    return execute_sql_script("app/db/create.sql")

def populate_db():
    return execute_sql_script("app/db/populate.sql")