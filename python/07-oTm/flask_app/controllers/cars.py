from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.car import Car

@app.route('/cars')
def cars(): 
    all_cars = Car.get_all()
    return render_template("cars.html", cars = all_cars)