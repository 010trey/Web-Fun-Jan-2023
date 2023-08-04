from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models.book import Book

class Author:

    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.name = data_dict['name']
        self.nationality = data_dict['nationality']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']
        # List of all author books
        self.my_books = []

    # CRUD Queries => Classmethods

    @classmethod
    def get_all(cls):
        query = """ SELECT * FROM authors;"""

        results = connectToMySQL(DATABASE).query_db(query)
        # print("🎈"*20, results,"🎈"*20)
        all_authors = []
        for row in results :
            # print(row['name'], row['nationality'])
            # author = Author({'id':'1', 'name':'Najib Mahfouz', 
            #                  'nationality':'Egyptian', 
            #                  'created_at':'2023-07-24 15:09:25', 
            #                  'updated_at':'2023-07-24 15:09:25'})
            author = cls(row)
            all_authors.append(author)
        return all_authors

    @classmethod
    def create(cls, data_dict):
        """
        data_dict = {
        'name':"Alex",
        'nationality': "French"
        }
        """
        query = """INSERT INTO authors (name, nationality) VALUES (%(name)s, %(nationality)s);"""
        result = connectToMySQL(DATABASE).query_db(query, data_dict)
        # query = """INSERT INTO authors (name, nationality) VALUES (:"Alex", "French");"""
        return result
    
    @classmethod
    def get_one_by_id_with_books(cls, data_dict):
        query  = """SELECT * FROM authors 
                    LEFT JOIN books ON authors.id  = books.author_id 
                    WHERE authors.id = %(id)s ;"""

        results  = connectToMySQL(DATABASE).query_db(query, data_dict)
        if results:
            this_author = cls(results[0])
            for row in results :
                book_data ={
                    'id':row['books.id'],
                    'author_id':row['author_id'],
                    'tittle': row['tittle'],
                    'pages':row['pages'],
                    'release_year':row['release_year'],
                    'created_at' : row['books.created_at'],
                    'updated_at' : row['books.updated_at']
                }
                book = Book(book_data)
                this_author.my_books.append(book)
                # print(row['books.id'], row['tittle'],row['pages'],row['release_year'],row['author_id'],row['books.created_at'])
            return this_author
        # print("This Author  Have Books")
        return None