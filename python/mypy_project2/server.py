from flask_app import app

from flask_app.controllers import table_controller
from flask_app.controllers import meal_controller
from flask_app.controllers import category_controller
from flask_app.controllers import admin_controller
from flask_app.controllers import menu_controller, order_controller

if __name__ == '__main__':
    app.run(debug=True)