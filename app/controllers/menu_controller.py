from flask import jsonify
from app.database import db
from sqlalchemy import text

def execute_sql_script(file_path):
    try:
        with open(file_path, "r") as f:
            sql_script = f.read()
        
        results = []
        with db.engine.connect() as connection:
            trans = connection.begin()
            try:
                for statement in sql_script.split(";"):
                    if statement.strip():
                        result = connection.execute(text(statement.strip()))
                        if result.returns_rows:
                            rows = result.fetchall()
                            results.append([dict(row._mapping) for row in rows])
                trans.commit()                
                return jsonify({"message": f"{file_path.split('/')[-1]} executed successfully", "results": results}), 200
            except Exception as e:
                trans.rollback()
                return jsonify({"error": str(e)}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def drop_db():
    return execute_sql_script("app/database/drop.sql")

def create_db():
    return execute_sql_script("app/database/create.sql")

def populate_db():
    return execute_sql_script("app/database/populate.sql")

def queries_db():
    return execute_sql_script("app/database/queries.sql")