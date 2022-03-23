from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Techonology:
    def __init__(self, data):
        self.id = data["id"]
        self.tech_name = data["tech_name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all(cls):
        query="SELECT * FROM technologies"
        result= connectToMySQL('esquema_code_camp').query_db(query)
        tech_arr=[]
        for i in result:
            tech_arr.append(cls(i))
        return tech_arr