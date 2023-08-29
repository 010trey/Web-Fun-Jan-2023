from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import user

class Trip :
    def __init__(self,data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.destination = data['destination']
        self.start_date = data['start_date']
        self.end_date = data['end_date']
        self.plan = data['plan']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.poster = "s"

    @classmethod
    def get_all(cls):
        query = """
        SELECT * FROM trips;
        """
        results = connectToMySQL(DATABASE).query_db(query)
        trip = []
        for row in results:
            trip.append(cls(row))
        return trip

    @classmethod
    def add_Trip(cls, data):
        query = """
        INSERT INTO recipes (user_id, destination, start_date,end_date,plan) 
        VALUES (%(user_id)s,%(destination)s,%(start_date)s,%(end_date)s,%(plan)s);
        """
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @staticmethod
    def validate(data):
        is_valid = True
        if len(data['destination'])< 2:
            flash("Destination must be at least 3")
            is_valid = False
        if len(data['plan'])< 10:
            flash("Plan too short")
            is_valid = False
        if data["start_date"] == "":
            flash("Start Date is required")
            is_valid = False
        if data["end_date"] == "":
            flash("End Date is required")
            is_valid = False
        return is_valid
    
    @classmethod
    def delete(cls, data):
        query = """
        delete from trips where id=%(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def edit_Trip(cls, data):
        query = """
        UPDATE Trip SET destination = %(destination)s, start_date = %(start_date)s, end_date= %(end_date)s , plan = %(plan)s
        WHERE id = %(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def get_by_id(cls, data):
        query = """
        SELECT * FROM trips WHERE id = %(id)s;
        """
        result = connectToMySQL(DATABASE).query_db(query,data)
        return cls(result[0])
    