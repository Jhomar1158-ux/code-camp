from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Group:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.maximum_people=data["maximum_people"]
        self.level=data["level"]
        self.technology=data["technology"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

