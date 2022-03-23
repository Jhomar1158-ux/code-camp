from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Room:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.level=data["level"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.technologie_id=data["technologie_id"]

        self.tech_name=data["tech_name"]

    @classmethod
    def save(cls, data):
        query = "INSERT INTO rooms (name, level, technologie_id) VALUES (%(name)s, %(level)s, %(technologie_id)s);"
        nuevoId = connectToMySQL('esquema_code_camp').query_db(query, data)
        return nuevoId

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM rooms LEFT JOIN technologies ON rooms.technologie_id=technologies.id"
        results = connectToMySQL('esquema_code_camp').query_db(query)
        rooms = []
        for i in results:
            rooms.append(cls(i))
        return rooms

    @staticmethod
    def valida_room(formulario):
        es_valido = True

        if len(formulario['name']) < 3:
            flash("El nombre del room debe tener al menos 3 caracteres", "room")
            es_valido = False
        
        return es_valido
