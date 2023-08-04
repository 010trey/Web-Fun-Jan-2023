from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class Book:

    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.author_id = data_dict['author_id']
        self.tittle = data_dict['tittle']
        self.pages = data_dict['pages']
        self.release_year = data_dict['release_year']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']

    
    # CRUD Queries => Classmethods

    @classmethod
    def get_all(cls):
        query = """ SELECT * FROM books;"""
        results = connectToMySQL(DATABASE).query_db(query)
        all_books = []
        for row in results :
            # author = Author({'id':'1', 'name':'Najib Mahfouz', 
            #                  'nationality':'Egyptian', 
            #                  'created_at':'2023-07-24 15:09:25', 
            #                  'updated_at':'2023-07-24 15:09:25'})
            book = cls(row)
            all_books.append(book)
        return all_books

    @classmethod
    def create(cls, data_dict):
        query = """INSERT INTO books (author_id,tittle, pages, release_year) 
                    VALUES (%(author_id)s, %(tittle)s, %(pages)s, %(release_year)s);"""
        return connectToMySQL(DATABASE).query_db(query, data_dict)