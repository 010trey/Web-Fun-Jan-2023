from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import car
class User:

    def __init__(self, data_dict):
        self.id = data_dict['id']
        self.name = data_dict['name']
        self.age = data_dict['age']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']
        # self.my_cars =[]
        self.my_cars = car.Car.get_user_cars({'user_id':self.id})

    # CRUD Queries ==> Classmethods
    #================ CREATE USER ======================>

    @classmethod
    def create(cls, data_dict):
        query = """INSERT INTO users (name, age) 
                VALUES (%(name)s, %(age)s);"""
        #! This Query will return ID of the New Created user            
        return connectToMySQL(DATABASE).query_db(query, data_dict)
    
    # ==========================SELECT ALL USERS==================
    @classmethod
    def get_all(cls):
        query = """SELECT * FROM users;"""
        results = connectToMySQL(DATABASE).query_db(query)
        # ! this query will return list that contains all users data stored in dict
        # ! results = [{},{},{}]
        all_users = []
        for row in results:
            user = cls(row)
            all_users.append(user)
        # ! all_users : list of objects : list of instances of the class User : every instance = user
        return all_users
    #=================== SELECT ONE USER BY ID ===================>
    @classmethod
    def get_by_id(cls, data_dict):
        query= """SELECT * FROM users
                    WHERE id= %(id)s;"""
        result = connectToMySQL(DATABASE).query_db(query, data_dict)
        #! if id exist => list that contains the data of that user with the specific ID 
        #! [{'id':1, 'name':'John Wick', 'created_at': exp , 'updated_at': exp}]
        #! if id not exist =>  () empty 
        if result:
            return cls(result[0])
        return False
    
    #=================== SELECT ONE USER BY ID With his cars ===================>
    @classmethod
    def get_by_id_with_cars(cls, data_dict):
        query= """SELECT * FROM users 
                    LEFT JOIN cars 
                    ON users.id = cars.user_id 
                    WHERE users.id = %(id)s;"""
        results = connectToMySQL(DATABASE).query_db(query, data_dict)
        # ! results = [{user_1_data + car_1_data}, {user_1_data + car_2_data}] user_1 has 2 cars
        # !results = [{user_3_data + car_3_data}] user_3 has 1 car
        # ! results = [{user_2_data }] user_2 has no cars
        if results:
            this_user = cls(results[0])
            for row in results:
                car_data = {
                    'id':row['cars.id'],
                    'user_id':row['user_id'],
                    'model':row['model'],
                    'make':row['make'],
                    'year':row['year'],
                    'color':row['color'],
                    'created_at':row['cars.created_at'],
                    'updated_at':row['cars.updated_at'],
                }
                this_user.my_cars.append(Car(car_data))
            return this_user
        return False

    
    
    