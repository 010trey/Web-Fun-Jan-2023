from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import user
from flask_app.models import band

class Band:
    def __init__(self,data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.band_name = data['band_name']
        self.music_genre = data['music_genre']
        self.homecity = data['homecity']
        self.poster = user.User.get_by_id({'id':self.user_id}).first_name
        
    @classmethod
    def get_all(cls):
        query = """
        SELECT * FROM bands;
        """
        results = connectToMySQL(DATABASE).query_db(query)
        bands = []
        for row in results:
            bands.append(cls(row))
        return bands

    @classmethod
    def add_bands(cls, data):
        query = """
        INSERT INTO bands (user_id, band_name, music_genre,homecity) 
        VALUES (%(user_id)s,%(band_name)s,%(music_genre)s,%(homecity)s);
        """
    
        result = connectToMySQL(DATABASE).query_db(query, data)
        print(result)
        return result
    
    
    @staticmethod
    def validate(data):
        is_valid = True
        if len(data['band_name'])< 2:
            flash("Band Name must be at least 3", "bands")
            is_valid = False
        if len(data['music_genre'])< 10:
            flash("music too short", "bands")
            is_valid = False
        if len(data['homecity'])< 10:
            flash("homecity too short", "bands")
            is_valid = False
        return is_valid
    
    @classmethod
    def delete(cls, data):
        query = """
        delete from bands where id=%(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def edit_bands(cls, data):
        query = """
        UPDATE bands SET band_name = %(band_name)s, music_genre = %(music_genre)s, homecity= %(homecity)s ,)s
        WHERE id = %(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def get_by_user(cls, data):
        query = """
        SELECT * FROM bands WHERE user_id = %(user_id)s;
        """
        result = connectToMySQL(DATABASE).query_db(query,data)
        bands = []
        for row in result:
            bands.append(cls(row))
        return bands
