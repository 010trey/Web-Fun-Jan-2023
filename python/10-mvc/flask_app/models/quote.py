from flask_app.config.mysqlconnection import connectToMySQL

class Quote:

    def __init__(self, data_dict) :
        self.id = data_dict['id']
        self.content = data_dict['content']
        self.author = data_dict['author']
        self.type = data_dict['type']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']

    #  CRUD = All Queries will be classmethods

    @classmethod
    def get_all(cls):
        query =  """SELECT * FROM quotes;"""
        results = connectToMySQL("flask_mysql_db").query_db(query)
        # print("**********************",results,"**********************")
        quotes = []
        for row in results:
            quote =  cls(row)
            # quote =  Quote(row)
            quotes.append(quote)
        # print("-"*10,quotes,"-"*10)
        return quotes
    @classmethod
    def create(cls, data_dict):
        query = """INSERT INTO quotes (content, type, author) 
        VALUES (%(content)s, %(type)s,%(author)s);"""
        # ! This query will return the id of the new created object
        return connectToMySQL("flask_mysql_db").query_db(query, data_dict)
    
    @classmethod
    def get_by_id(cls, data_dict):
        query =  """SELECT * FROM quotes WHERE id = %(id)s;"""
        result = connectToMySQL("flask_mysql_db").query_db(query, data_dict)
        # print("**********************",result,"**********************")
        return cls(result[0])
    
    @classmethod
    def update(cls, data):
        query = """UPDATE quotes SET content=%(content)s , type=%(type)s, author=%(author)s WHERE id =%(id)s;"""
        return connectToMySQL("flask_mysql_db").query_db(query, data)
    
    @classmethod
    def destroy(cls, data):
        query = """DELETE FROM quotes WHERE id=%(id)s;"""
        return connectToMySQL("flask_mysql_db").query_db(query, data)