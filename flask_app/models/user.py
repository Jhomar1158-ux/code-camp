from flask_app.config.mysqlconnection import connectToMySQL
import re 

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

from flask import flash

class User:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        # REVISAR VIDEO 
        self.image=data["image"]


    @classmethod
    def save(cls, formulario):
        #formulario = {
        #     "first_name": "Elena",
        #     "last_name": "De Troya",
        #     "email": "elena@cd.com",
        #     "password": "91289128snkndsaajdyasdl"
        # }
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)"
        nuevoId = connectToMySQL('esquema_code_camp').query_db(query, formulario)
        return nuevoId
    
    @staticmethod
    def valida_usuario(formulario):
        # formulario = {
        #     "first_name": "Emilio",
        #     "last_name": "Navejas",
        #     "email": "emilio@codingdojo.com",
        #     "password": "12345"
        # }

        es_valido = True

        #Validar que mi nombre sea mayor a 2 caracteres
        if len(formulario['first_name']) < 2:
            flash('Nombre debe de tener al menos 2 caracteres', 'registro')
            es_valido = False
        #Validar que mi apellido sea mayor a 2 caracteres
        if len(formulario['last_name']) < 2:
            flash('Apellido debe de tener al menos 2 caracteres', 'registro')
            es_valido = False
        #Valido email con expresiones regulares #abc123@21msn.com ->NO te aceptaría a.com
        if not EMAIL_REGEX.match(formulario['email']):
            flash('E-mail inválido', 'registro')
            es_valido = False
        if len(formulario['password']) < 8:
            flash('Contraseña debe tener al menos 8 caracteres', 'registro')
            es_valido = False
        if formulario['password'] != formulario['password_confirm']:
            flash('Contraseñas no coinciden', 'registro')
            es_valido = False
        
        #Consulta si ya existe ese correo
        query = "SELECT id FROM users WHERE email = %(email)s"
        results = connectToMySQL('esquema_code_camp').query_db(query, formulario)
        #results = [
        #     {"first_name": "Cynthia", "last_name":"Castillo"}
        # ]
        if len(results) >= 1:
            flash('E-mail registrado previamente', 'registro')
            es_valido = False

        return es_valido

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        result = connectToMySQL('esquema_code_camp').query_db(query, data)
        if len(result) < 1:
            return False
        else :
            usr = result[0]
            #usr = {"id": "1", "first_name": "Elena", "last_name": "De Troya", "email": "elena@cd".......}
            user = cls(usr)
            return user
    
    @classmethod
    def get_by_email(cls, data):
        # data = {
        #     "email": "cynthia@codingdojo.com",
        #     "password": "1234"
        # }
        query = "SELECT * FROM users WHERE email = %(email)s"
        result = connectToMySQL('esquema_code_camp').query_db(query, data)
        if len(result) < 1:
            return False
        else :
            usr = result[0]
            #usr = {"id": "1", "first_name": "Elena", "last_name": "De Troya", "email": "elena@cd".......}
            user = cls(usr)
            return user
