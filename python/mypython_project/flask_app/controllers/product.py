from pathlib import Path
from flask_app import app
import os
from flask import request ,render_template, session, redirect, flash
from flask_app.models.user import User
from flask_app.models.product import Product
from werkzeug.utils import secure_filename
UPLOAD_FOLDER = "/Users/mac/Desktop/mypython_project/flask_app/static/project_image"
from flask import Flask, render_template
import uuid

# display route
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_name = request.form['user_name']
        password = request.form['password']
        user_name.append({'username': user_name, 'password': password})
        return redirect(('login'))
    return render_template('register.html')

@app.route('/products/new')
def new_products():
    if 'user_id' in session:
        return render_template("new_products.html")
    return redirect('/my_store') 

@app.route('/products/create' ,methods=['POST'])
def create_products():
    print(request.form)
    if(Product.validate(request.form)):
        file = request.files['image']
        filename = secure_filename(file.filename)
        #print()
        # file.save(os.path.join(UPLOAD_FOLDER, file.filename))
        unique_filename = 'image' + str(uuid.uuid4())
        file_path = Path(UPLOAD_FOLDER) / unique_filename
        os.makedirs(file_path.parent, exist_ok=True)
        file.save(file_path)
        data = {
            **request.form,
            'image': unique_filename
        }
        Product.add_product(data)
        return redirect('/my_store')
    return redirect('/products/new')

@app.route('/products/<product_id>/destroy/')
def delete_products(product_id):
    if 'user_id' in session:
        Product.delete({'id':product_id})
    return redirect('/products')

@app.route('/products/<int:product_id>/edit', methods=['post'])
def edit_products(product_id):
    if 'user_id' in session:
        one_product=Product.edit_products({'id':product_id})
        return render_template("edit_products.html", product=one_products)
    return redirect('/')

@app.route('/products/update' ,methods=['POST'])
def update_product():
    if(Product.validate(request.form)):
        Product.edit_products(request.form)
        return redirect('/products')
    return redirect('/products/'+str(request.form['id'])+'/edit')

@app.route('/products/<int:products_id>')
def one_products(product_id):
    if 'user_id' in session:
        user = User.get_by_id({'id':session['user_id']})
        one_products=Product.get_by_id({'id':product_id})
        print(one_products)
        return render_template('one_products.html',product=one_products,user=user)
    return redirect('/')     

@app.route('/my_store')
def my_store():
    products = Product.get_all()
    return render_template('products.html', products=products)


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

# UPLOAD_FOLDER = '/'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['DATABASE'] = 'image_database.db'

# # ... (rest of the code remains the same) ...

# @app.route('/delete/<int:image_id>', methods=['POST'])
# def delete_image(image_id):
#     # Fetch the filename from the database
#     db = ()
#     cursor = db.execute('SELECT filename FROM images WHERE id = ?', (image_id,))
#     image = cursor.fetchone()
    
#     if image:
#         filename = image[0]
        
#         # Remove the image file from the filesystem
#         file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#         if os.path.exists(file_path):
#             os.remove(file_path)
        
#         # Delete the image entry from the database
#         db.execute('DELETE FROM images WHERE id = ?', (image_id,))
#         db.commit()
        
#         return redirect(('home'))  # Redirect to the home page

#     return 'Image not found'




