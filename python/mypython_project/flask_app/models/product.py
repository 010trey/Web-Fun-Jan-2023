from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import user
from flask_app.models import product 


class Product:
    def __init__(self,data):
        self.id = data['id']
        # self.user_id = data['user_id']
        self.name = data['name']
        self.description = data['description']
        self.price = data['price']
        self.stockquantity = data['stockquantity']
        self.image = data['image']
        # self.poster = user.User.get_by_id({'id':self.user_id}).user_name 
        
    
    @classmethod
    def get_all(cls):
        query = """
        SELECT * FROM products;
        """
        results = connectToMySQL(DATABASE).query_db(query)
        products= []
        for row in results:
            products.append(cls(row))
        return products 
    
    @classmethod
    def add_product(cls, data):
        query = """
        INSERT INTO products (name, description, price, stockquantity, image) 
        VALUES (%(name)s,%(description)s,%(price)s,%(stockquantity)s,%(image)s);
        """
    
        result = connectToMySQL(DATABASE).query_db(query, data)
        print('****QUERY RESULT',result)
        return result
    
    @staticmethod
    def validate(data):
        is_valid = True
        if len(data['name'])< 2:
            flash("Name must be at least 3", "name")
            is_valid = False
        if len(data['description'])< 10:
            flash("description too short", "description")
            is_valid = False
        # if len(data['price'])< 10:
        #     flash("price too short", "price")
        #     is_valid = False
        # if len(data['stockquantity'])< 10:
        #     flash("stockquantity too short", "stockquantity")
        #     is_valid = False
        return is_valid
    
    @classmethod
    def delete(cls, data):
        query = """
        delete from products where id=%(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @classmethod
    def edit_products(cls, data):
        query = """
        UPDATE products SET name = %(name)s, description = %(description)s, price = %(price)s , stockquantity = %(stockquantity)s)s
        WHERE id = %(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query, data)
    
    
    @classmethod
    def get_by_user(cls, data):
        query = """
        SELECT * FROM products WHERE user_id = %(user_id)s;
        """
        result = connectToMySQL(DATABASE).query_db(query,data)
        products= []
        for row in result:
            products.append(cls(row))
        return products
    
# @app.route('/products/create' ,methods=['POST'])
# def create_product():
#     print(request.form)
#     if 'user_id' not in session:
#         return redirect('/') 
#     if product.validate(request.form):
#         data = {
#             **request.form,
#             'user_id':session['user_id']
#         }
#     product.add_products(data)
#     return redirect('/')

