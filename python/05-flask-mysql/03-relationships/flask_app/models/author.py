from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE_NAME

class Author:

    def __init__(self, data_dict) :
        self.id = data_dict["id"]
        self.name = data_dict["name"]
        self.nationality = data_dict["nationality"]
        self.created_at = data_dict["created_at"]
        self.updated_at = data_dict["updated_at"]

    @classmethod
    def get_all(cls):
        query = """ SELECT * FROM authors;"""
        results = connectToMySQL(DATABASE_NAME).query_db(query)
        all_authors = []
        for row in results:
            all_authors.append(cls(row))
        return all_authors
    
    @classmethod
    def create_author(cls,data_dict):
        query = """
                    INSERT INTO authors (name, nationality)
                    VALUES (%(name)s, %(nationality)s);
                """
        result = connectToMySQL(DATABASE_NAME).query_db(query, data_dict)
        return result