from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB

from flask_app.models import meal_model

class Category:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.meals = []

    @classmethod
    def add_category(cls, data):
        query = "INSERT INTO categories (name) VALUES (%(name)s)"
        return connectToMySQL(DB).query_db(query, data)
    
    @classmethod
    def get_all_categories(cls):
        query= """
                SELECT * FROM categories;
                """
        result =  connectToMySQL(DB).query_db(query)
        all_categories = []
        for cat in result:
            all_categories.append(cls(cat))
        return all_categories
    
    @classmethod
    def get_category_by_id(cls, data):
        query= """
                SELECT * FROM categories
                WHERE id = %(id)s
                """
        result =  connectToMySQL(DB).query_db(query, data)
        print(result)
        return cls(result[0])
    
    @classmethod
    def get_category_with_meals(cls, data):
        query = """
                SELECT * FROM categories
                LEFT JOIN meals ON categories.id = meals.category_id
                WHERE categories.id = %(id)s
                """
        result = connectToMySQL(DB).query_db(query, data)
        category = cls(result[0])
        for row in result:
            data = {
                'id': row['meals.id'],
                'name': row['meals.name'],
                'description': row['description'],
                'created_at': row['meals.created_at'],
                'updated_at': row['meals.updated_at'],
                'category_id': row['category_id'],
                'price': row['price'],
                'image': row['image']
                }
            category.meals.append(meal_model.Meal(data))

        return category


    # @classmethod
    # def get_categories_with_meals(cls):
    #     query= """
    #             SELECT * FROM categories
    #             LEFT JOIN meals ON categories.id = meals.category_id
    #             """
    #     result =  connectToMySQL(DB).query_db(query)
    #     print(result)
    #     # all_categories = []
    #     # for cat in result:
    #     #     all_categories.append(cls(cat))
    #     # for row in result:
    #     #     meal = {
    #     #         'id': row['meals.id'],
    #     #         'name': row['meals.name'],
    #     #         'description': row['description'],
    #     #         'created_at': row['meals.created_at'],
    #     #         'updated_at': row['meals.updated_at'],
    #     #         'category_id': row['category_id'],
    #     #         'price': row['price']
    #     #     }
    #     #     all_categories.
    #         #cls.meals.append(meal_model.Meal(meal))
        
    #     return "ok"

