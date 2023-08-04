from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE_NAME

class Book :

    def __init__(self, data_dict):
        self.id = data_dict["id"]
        self.title = data_dict["tittle"]
        self.author_id = data_dict["author_id"]
        self.pages = data_dict["pages"]
        self.release_year = data_dict["release_year"]
        self.created_at = data_dict["created_at"]
        self.updated_at = data_dict["updated_at"]

    @classmethod
    def get_all(cls):
        query = """ SELECT * FROM books;"""
        results = connectToMySQL(DATABASE_NAME).query_db(query)
        all_books = []
        for row in results:
            all_books.append(cls(row))
        return all_books
    
    @classmethod
    def create_book(cls,data_dict):
        query = """
                    INSERT INTO books (author_id, tittle, pages, release_year)
                    VALUES (%(author_id)s, %(tittle)s,  %(pages)s, %(release_year)s);
                """
        result = connectToMySQL(DATABASE_NAME).query_db(query, data_dict)
        return result