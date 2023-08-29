from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB
from flask import flash

from flask_app.models import category_model

class Meal:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.price = data['price']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.category_id = data['category_id']
        self.category = category_model.Category.get_category_by_id({'id': self.category_id}).name
        self.image = data['image']


    @classmethod
    def get_all_meals(cls):
        query= """
                SELECT * FROM meals;
                """
        result =  connectToMySQL(DB).query_db(query)
        all_meals = []
        for meal in result:
            all_meals.append(cls(meal))
        return all_meals
    

    @classmethod
    def delete_meal(cls, data):
        query = "DELETE FROM meals WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query, data)
    

    @classmethod
    def add_meal(cls, data):
        query = """
                INSERT INTO meals (name,image,description,category_id,price)
                VALUES (%(name)s,%(image)s,%(description)s,%(category_id)s,%(price)s)
                """
        return connectToMySQL(DB).query_db(query, data)
    

    @classmethod
    def update_meal(cls, data):
        query = """
                UPDATE meals SET
                name = %(name)s,
                image = %(image)s,
                description = %(description)s,
                category_id = %(category_id)s,
                price = %(price)s
                WHERE id = %(id)s
                """
        return connectToMySQL(DB).query_db(query, data)
    

    @classmethod
    def get_meal_by_id(cls, data):
        query = "SELECT * FROM meals WHERE id = %(id)s"
        result = connectToMySQL(DB).query_db(query, data)
        print(f"meal by id: {result}")
        if len(result)<1:
            return False
        return cls(result[0])
    

    @classmethod
    def get_ordered_meals(cls, data):
        query = """
            SELECT * FROM meals 
            JOIN orders ON meals.id = orders.meal_id 
            WHERE orders.table_id = %(table_id)s;
        """ 
        result =  connectToMySQL(DB).query_db(query,data)
        ordered_meals = []
        for meal in result:
            ordered_meals.append(cls(meal))
        return ordered_meals
    

    @staticmethod
    def validate_meal(data):
        is_valid = True
        if len(data['name'])<3:
            is_valid = False
            flash("Invalid name, must be at least 3 characters!", "name")
        if len(data['description'])<8:
            is_valid = False
            flash("Description must be at least 8 characters!", "description")
        if data['price']=="":
            is_valid = False
            flash("You should put a price", "price")
        if data['category_id']=="":
            is_valid = False
            flash("You should pick a category", "category")
        # if data['image']=="":
        #     is_valid = False
        #     flash("You should pick an image", "image")
        return is_valid