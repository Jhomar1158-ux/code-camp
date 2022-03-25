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
        self.owner_id=data["owner_id"]

        # OBTUVE UN ERROR DE KEY Y LO COMENTÉ PARA SOLUCIONARLO
        # Atributo creado con el fin de ver los nombres de una tech
        self.tech_name=data["tech_name"]

    @classmethod
    def save(cls, data):
        query = "INSERT INTO rooms (name, level, technologie_id, owner_id) VALUES (%(name)s, %(level)s, %(technologie_id)s , %(owner_id)s);"
        nuevoId = connectToMySQL('esquema_code_camp').query_db(query, data)
        return nuevoId

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM rooms LEFT JOIN technologies ON rooms.technologie_id=technologies.id ORDER BY rooms.created_at DESC"
        results = connectToMySQL('esquema_code_camp').query_db(query)
        rooms = []
        for i in results:
            rooms.append(cls(i))
        return rooms

    @classmethod
    def get_all_rooms_by_text(cls,data):

        # main_search_tech=data["main_search_tech"]+"%"

        # query = """SELECT * FROM rooms LEFT JOIN technologies ON rooms.technologie_id=technologies.id  WHERE technologies.tech_name LIKE %s ORDER BY rooms.created_at DESC """
        # connectToMySQL('esquema_code_camp').execute(query,[main_search_tech])
        # results= connectToMySQL('esquema_code_camp').fetchall()
        # data2={
        #     "main_search_tech":data["main_search_tech"]+"%"
        # }

        query = """SELECT * FROM rooms LEFT JOIN technologies ON rooms.technologie_id=technologies.id  
                WHERE technologies.tech_name LIKE '"""+data["main_search_tech"]+"%"+"""' 
                ORDER BY rooms.created_at DESC """

        results= connectToMySQL('esquema_code_camp').query_db(query)

        rooms = []
        for i in results:
            rooms.append(cls(i))
        print("/"*10)
        print(rooms)
        print("/"*10)
        return rooms

    @staticmethod
    def valida_room(formulario):
        es_valido = True

        if len(formulario['name']) < 3:
            flash("El nombre del room debe tener al menos 3 caracteres", "room")
            es_valido = False
        
        return es_valido

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM rooms LEFT JOIN technologies ON rooms.technologie_id=technologies.id WHERE rooms.id = %(id)s"
        result = connectToMySQL('esquema_code_camp').query_db(query, data)
        print("*"*10)
        print(result)
        print("*"*10)
        room = cls(result[0])
        return room

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM rooms WHERE id = %(id)s"
        return connectToMySQL('esquema_code_camp').query_db(query, data)

    @classmethod
    def update(cls, data):
        query = "UPDATE rooms SET name = %(name)s, level = %(level)s, technologie_id = %(technologie_id)s, owner_id = %(owner_id)s WHERE (id = %(id)s);"
        result = connectToMySQL('esquema_code_camp').query_db(query, data)
        return result
