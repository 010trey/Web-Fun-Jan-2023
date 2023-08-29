from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import author
class Quote:

    def __init__(self, data_dict) :
        self.id = data_dict['id']
        self.content = data_dict['content']
        self.author_id = data_dict['author_id']
        self.type = data_dict['type']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']
        self.author = ""
        # self.author = author.Author.get_by_id({'id':self.author_id})

    #  CRUD = All Queries will be classmethods

    @classmethod
    def get_all(cls):
        query =  """SELECT * FROM quotes JOIN authors ON authors.id = quotes.author_id ;"""
        results = connectToMySQL(DATABASE).query_db(query)
        # print("**********************",results,"**********************")
        quotes = []
        for row in results:
            quote =  cls(row)
            quote.author = row['name']
            # quote =  Quote(row)
            quotes.append(quote)
        # print("-"*10,quotes,"-"*10)
        return quotes
    @classmethod
    def get_author_quotes(cls, data):
        query =  """SELECT * FROM quotes WHERE author_id = %(author_id)s;"""
        results = connectToMySQL(DATABASE).query_db(query, data)
        # print("**********************",results,"**********************")
        quotes = []
        for row in results:
            quote =  cls(row)
            quotes.append(quote)
        return quotes
    @classmethod
    def create(cls, data_dict):
        query = """INSERT INTO quotes (content, type, author_id) 
        VALUES (%(content)s, %(type)s,%(author_id)s);"""
        # ! This query will return the id of the new created object
        return connectToMySQL(DATABASE).query_db(query, data_dict)
    
    @classmethod
    def get_by_id(cls, data_dict):
        query =  """SELECT * FROM quotes WHERE id = %(id)s;"""
        result = connectToMySQL(DATABASE).query_db(query, data_dict)
        # print("**********************",result,"**********************")
        return cls(result[0])
    
    @classmethod
    def update(cls, data):
        query = """UPDATE quotes SET content=%(content)s , type=%(type)s, author_id=%(author_id)s WHERE id =%(id)s;"""
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def destroy(cls, data):
        query = """DELETE FROM quotes WHERE id=%(id)s;"""
        return connectToMySQL(DATABASE).query_db(query, data)