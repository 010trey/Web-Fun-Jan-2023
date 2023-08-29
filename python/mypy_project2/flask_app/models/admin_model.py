from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Admin:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
    
    @classmethod
    def register(cls, data):
        query = """
                INSERT INTO admin (first_name, last_name, email, password) 
                VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)
                """
        return connectToMySQL(DB).query_db(query, data)
    
    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM admin WHERE email = %(email)s"
        result= connectToMySQL(DB).query_db(query,data)
        #print(cls(result[0]))
        if len(result)<1:
            return False
        return cls(result[0])
    
    # @classmethod
    # def get_by_id(cls, data):
    #     query = "SELECT * FROM admin WHERE id = %(id)s"
    #     result= connectToMySQL(DB).query_db(query,data)
    #     #print(cls(result[0]))
    #     if len(result)<1:
    #         return False
    #     return cls(result[0])
    
    @staticmethod
    def validate_user(data):
        is_valid = True
        if len(data['first_name'])<2:
            is_valid = False
            flash("Invalid first name, must be greater than 2 characters!", "first_name")
        if len(data['last_name'])<2:
            is_valid = False
            flash("Invalid last name, must be greater than 2 characters!", "last_name")
        if not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address!", "email")
            is_valid = False
        elif Admin.get_by_email({'email': data['email']}):
            is_valid = False
            flash("email address already exists!", "email")
        if len(data['password'])<4:
            is_valid = False
            flash("Invalid password, must be greater than 8 characters!", "password")
        elif data['password']!=data['confirm_password']:
            flash("Password and confirm_password must match!", "confirm_password")
            is_valid = False
        return is_valid