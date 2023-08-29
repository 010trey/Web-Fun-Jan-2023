from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB

class Order:
    def __init__(self,data):
        self.id = data['id']
        self.table_id = data['table_id']
        self.meal_id = data['meal_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # @classmethod
    # def create_order(cls,data):
    #     query = "INSERT INTO orders (table_id) VALUES (%(table_id)s)"
    #     return connectToMySQL(DB).query_db(query, data)

    @classmethod
    def create_order(cls, data):
        query = "INSERT INTO orders (meal_id, table_id) VALUES (%(meal_id)s, %(table_id)s)"
        return connectToMySQL(DB).query_db(query, data)
    
    @classmethod
    def verify_orders(cls, data):
        query = "SELECT * FROM orders WHERE table_id = %(table_id)s"
        result = connectToMySQL(DB).query_db(query, data)
        # print ("+"*50,result)
        if len(result) < 1:
            return False
        return True
    
    @classmethod
    def delete_order(cls, data):
        query = """ DELETE FROM orders WHERE table_id = %(table_id)s AND meal_id = %(meal_id)s
                    ORDER BY id ASC LIMIT 1
                """
        return connectToMySQL(DB).query_db(query, data)