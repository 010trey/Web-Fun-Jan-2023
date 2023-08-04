from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import user

class Car:

    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.user_id = data_dict['user_id']
        self.model = data_dict['model']
        self.make = data_dict['make']
        self.year = data_dict['year']
        self.color = data_dict['color']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']
        self.owner = ""

    # CRUD Queries ==> Classmethods
    #================ CREATE CAR ======================>

    @classmethod
    def create(cls, data_dict):
        query = """INSERT INTO cars (user_id,model, make,year,color) 
                VALUES (%(user_id)s, %(model)s,%(make)s,%(year)s,%(color)s);"""
        #! This Query will return ID of the New Created car            
        return connectToMySQL(DATABASE).query_db(query, data_dict)
    
    # ==========================SELECT ALL CARS==================
    @classmethod
    def get_all(cls):
        query = """SELECT * FROM cars JOIN users on cars.user_id = users.id;"""
        results = connectToMySQL(DATABASE).query_db(query)
        # ! this query will return list that contains all users data stored in dict
        # ! results = [{},{},{}]
        all_cars = []
        for row in results:
            car = cls(row)
            car.owner = row['name']
            all_cars.append(car)
        # ! all_cars : list of objects : list of instances of the class Car : every instance = car
        return all_cars
    
    #=================== SELECT ONE CAR BY ID ===================>
    @classmethod
    def get_by_id(cls, data_dict):
        query= """SELECT * FROM cars
                    WHERE id= %(id)s;"""
        result = connectToMySQL(DATABASE).query_db(query, data_dict)
        if result:
            return cls(result[0])
        return False
    
    #=================== SELECT all USER CARS ===================>
    @classmethod
    def get_user_cars(cls, data_dict):
        query= """SELECT * FROM cars
                    WHERE user_id= %(user_id)s;"""
        results = connectToMySQL(DATABASE).query_db(query, data_dict)
        if results:
            cars = []
            for row in results:
                cars.append(cls(row))
            return cars 
        return []
    
    
    