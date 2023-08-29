from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import user

class Show :
    def __init__(self,data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.title = data['title']
        self.network = data['network']
        self.release_date = data['release_date']
        self.description = data['description']
        self.poster = user.User.get_by_id({'id':self.user_id}).first_name
        
    @classmethod
    def get_all(cls):
        query = """
        SELECT * FROM shows;
        """
        results = connectToMySQL(DATABASE).query_db(query)
        show = []
        for row in results:
            show.append(cls(row))
        return show

    @classmethod
    def add_show(cls, data):
        query = """
        INSERT INTO shows (user_id, title, network,release_date,description) 
        VALUES (%(user_id)s,%(title)s,%(network)s,%(release_date)s,%(description)s);
        """
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @staticmethod
    def validate(data):
        is_valid = True
        if len(data['title'])< 2:
            flash("Tile must be at least 3", "show")
            is_valid = False
        if len(data['network'])< 10:
            flash("Network too short", "show")
            is_valid = False
        if len(data['description'])< 10:
            flash("Description too short", "show")
            is_valid = False
        if data["release_date"] == "":
            flash("Release date is required", "show")
            is_valid = False
        return is_valid
    
    @classmethod
    def delete(cls, data):
        query = """
        delete from shows where id=%(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def edit_show(cls, data):
        query = """
        UPDATE shows SET title = %(title)s, network = %(network)s, release_date= %(release_date)s , description = %(description)s
        WHERE id = %(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def get_by_id(cls, data):
        query = """
        SELECT * FROM shows WHERE id = %(id)s;
        """
        result = connectToMySQL(DATABASE).query_db(query,data)
        print(result)
        return cls(result[0])
    