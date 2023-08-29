from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import quote

class Author:
    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.name = data_dict['name']
        self.country = data_dict['country']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']
        # -------------IMPORT QUOTE MODEL************
        self.my_quotes = quote.Quote.get_author_quotes({'author_id':self.id})
        # ---------------------------------------------------------

        # * USING JOIN/LEFT JOIN  + METHOD get_by_id_with_quotes()
        # self.my_quotes = []
        # ****************************

    # CRUD QUERIES  = classmethods

    # ===============GET ALL============
    @classmethod
    def get_all(cls):
        query = """SELECT * FROM authors;"""
        results = connectToMySQL(DATABASE).query_db(query)
        all_authors = []
        for row in results:
            all_authors.append(cls(row))
        return all_authors
    
    # ===================GET ONE BY ID==============
    @classmethod
    def get_by_id(cls, data_dict):
        query = """SELECT * FROM authors 
                    WHERE authors.id=%(id)s;"""
        result = connectToMySQL(DATABASE).query_db(query, data_dict)
        print("⛔"*10, result,"⛔"*10)
        return cls(result[0])
    
    # ===================GET ONE BY ID WITH QUOTES==============
    @classmethod
    def get_by_id_with_quotes(cls, data_dict):
        query = """SELECT * FROM authors 
                    LEFT JOIN quotes 
                    ON authors.id  = quotes.author_id
                    WHERE authors.id=%(id)s;"""
        result = connectToMySQL(DATABASE).query_db(query, data_dict)
        print("⛔"*10, result,"⛔"*10)
        this_author = cls(result[0])
        for row in result:
            one_quote_data = {
                'id':row['quotes.id'],
                'author_id':row['author_id'],
                'content':row['content'],
                'type':row['type'],
                'created_at':row['quotes.created_at'],
                'updated_at':row['quotes.updated_at'],
            }
            print("🎈🎈🎈🎈",one_quote_data,"🎈🎈🎈🎈")
            if one_quote_data['id']:
                quote = quote.Quote(one_quote_data)
                this_author.my_quotes.append(quote)
        return this_author
    
    # ================CREATE================
    @classmethod
    def  create(cls,data):
        query = """INSERT INTO authors (name, country) VALUES (%(name)s,%(country)s);"""
        return connectToMySQL(DATABASE).query_db(query,data)