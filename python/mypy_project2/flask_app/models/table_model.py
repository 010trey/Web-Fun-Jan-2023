from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB

from flask_app.models import meal_model

class Table:
    def __init__(self, data):
        self.id = data['id']
        self.status = data['status'] or 0
        self.stage = data['stage'] or 0
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.meals = []

    @classmethod
    def get_all_tables(cls):
        query= """
                SELECT * FROM tables;
                """
        result =  connectToMySQL(DB).query_db(query)
        all_tables = []
        for table in result:
            all_tables.append(cls(table))
        return all_tables
    
    @classmethod
    def add_table(cls, data):
        query = """
                INSERT INTO tables (id)
                VALUES (%(id)s)
                """
        return connectToMySQL(DB).query_db(query, data)
    
    @classmethod
    def delete_table(cls, data):
        query = "DELETE FROM tables WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query, data)
    
    @classmethod
    def update_table_status(cls, data):
        query = """
                UPDATE tables SET
                status = %(status)s
                WHERE id = %(id)s
                """
        return connectToMySQL(DB).query_db(query, data)

    @classmethod
    def get_meals_with_table_id(cls, data):
        query = """
                SELECT * FROM tables
                LEFT JOIN orders ON tables.id = orders.table_id
                LEFT JOIN meals ON meals.id=orders.meal_id
                WHERE tables.id =  %(id)s;
                """
        result =  connectToMySQL(DB).query_db(query, data)
        table = cls(result[0])
        for row in result:
            data = {
                **row,
                'id': row['meals.id'],
                'created_at': row['meals.created_at'],
                'updated_at': row['meals.updated_at']
            }
            print(f"hhhhhhhhhhhhhhhhhhhhh{data}")
            table.meals.append(meal_model.Meal(data))

        print(result)
        return table
    
    @classmethod
    def update_table_stage(cls, data):
        query = """
                UPDATE tables SET
                stage = %(stage)s
                WHERE id = %(id)s;
                """
        return connectToMySQL(DB).query_db(query, data)
    
    @classmethod
    def get_orders(cls):
        query = """
                SELECT * FROM tables
                JOIN orders ON tables.id = orders.table_id
                JOIN meals ON meals.id = orders.meal_id
                """
        result =  connectToMySQL(DB).query_db(query)
        for table in result:
            tables = cls(table)
        #orders = cls(result[0])
        for row in result:
            data = {
                **row,
                'id': row['meals.id'],
                'created_at': row['meals.created_at'],
                'updated_at': row['meals.updated_at']
            }
            # print(f"hhhhhhhhhhhhhhhhhhhhh{data}")
            tables.meals.append(meal_model.Meal(data))           

        print(result)
        return tables