from flask import Flask, render_template, redirect, url_for, flash, session, request


app = Flask(__name__)


# ... (other configurations and database setup)

# Configure Flask-Login
login_manager = (app)
login_manager.login_view = 'login'

# Load user function for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return load_user.ser.query.get(int(user_id))

# ... (other routes)

# User registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Retrieve user registration data from the form
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        # ... (additional fields)

        # Create a new user object
        new_user = new_user(username=username, email=email, password=password, role='customer')
        
        # Save the user to the database
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

# User login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    if request.method == 'POST':
        # Retrieve user login data from the form
        email = request.form['email']
        password = request.form['password']

        # Find the user by email
        user = user.query.filter_by(email=email).first()

        # Check if user exists and the password is correct
        if user and user.password == password:
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login failed. Please check your email and password.', 'danger')

    return render_template('login.html')

# User logout route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully.', 'success')
    return redirect(url_for('home'))


# Home Page
@app.route('/')
def home():
    return render_template('home.html')

# Product Listing Page
@app.route('/products')
def products():
    # Here, you would retrieve the product data from the database
    # and pass it to the template for rendering
    products_data = [
        {"name": "Product 1", "price": 100},
        {"name": "Product 2", "price": 200},
        # Add more products here
    ]
    return render_template('products.html', products=products_data)

# Shopping Cart Page
@app.route('/cart')
def cart():
    # Here, you would retrieve the user's cart data from the database
    # and pass it to the template for rendering
    cart_data = [
        {"product": "Product 1", "quantity": 2, "subtotal": 200},
        # Add more cart items here
    ]
    return render_template('cart.html', cart=cart_data)

# User Registration Page
@app.route('/register')
def register():
    return render_template('register.html')


# Configure MySQL database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://username:password@localhost/online_shop_db'  # Replace with your MySQL credentials and database name
db = SQLAlchemy(app)



@app.route('/protected')
@login_required
def protected_route():
    return "This is a protected route. Only authenticated users can access it."




# Add product to cart route
@app.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    # Retrieve the selected product from the database
    product = products.query.get(product_id)

    # Initialize the cart if it doesn't exist in the session
    if 'cart' not in session:
        session['cart'] = []

    # Add the product to the cart
    session['cart'].append({
        'product_id': product.id,
        'product_name': product.name,
        'product_price': product.price
    })

    return redirect(url_for('products'))



# Remove product from cart route
@app.route('/remove_from_cart/<int:product_id>', methods=['POST'])
def remove_from_cart(product_id):
    # Retrieve cart data from the session
    cart = session.get('cart', [])

    # Remove the specified product from the cart
    cart = [item for item in cart if item['product_id'] != product_id]

    # Update the cart data in the session
    session['cart'] = cart

    return redirect(url_for('cart'))


# Create order route
@app.route('/create_order', methods=['POST'])
@login_required
def create_order():
    # Retrieve cart data from the session
    cart = session.get('cart', [])

    # Calculate the total amount of the order
    total_amount = sum(item['product_price'] * item['quantity'] for item in cart)

    # Create a new order
    order = Order(
        user_id=current_user.id,
        total_amount=total_amount,
        order_status='pending'
    )
    db.session.add(order)
    db.session.commit()

    # Add items to the order
    for item in cart:
        order_item = OrderItem(
            order_id=order.id,
            product_id=item['product_id'],
            quantity=item['quantity'],
            subtotal=item['product_price'] * item['quantity']
        )
        db.session.add(order_item)

    # Clear the cart
    session['cart'] = []
    db.session.commit()

    flash('Order placed successfully!', 'success')
    return redirect(url_for('orders'))

# Create order route
@app.route('/create_order', methods=['POST'])
@login_required
def create_order():
    # Retrieve cart data from the session
    cart = session.get('cart', [])

    # Calculate the total amount of the order
    total_amount = sum(item['product_price'] * item['quantity'] for item in cart)

    # Create a new order
    order = Order(
        user_id=current_user.id,
        total_amount=total_amount,
        order_status='pending'
    )
    db.session.add(order)
    db.session.commit()

    # Add items to the order
    for item in cart:
        order_item = OrderItem(
            order_id=order.id,
            product_id=item['product_id'],
            quantity=item['quantity'],
            subtotal=item['product_price'] * item['quantity']
        )
        db.session.add(order_item)

    # Clear the cart
    session['cart'] = []
    db.session.commit()

    flash('Order placed successfully!', 'success')
    return redirect(url_for('orders'))

# View orders route
@app.route('/orders')
@login_required
def orders():
    # Retrieve orders for the current user
    user_orders = Order.query.filter_by(user_id=current_user.id).all()
    return render_template('orders.html', orders=user_orders)

# Query products with a given name
product_name = "Product 1"
products = Product.query.filter_by(name=product_name).all()


def test_user_registration(client):
    response = client.post('/register', data={'username': 'testuser', 'email': 'test@example.com', 'password': 'password'})
    assert response.status_code == 200
    # Assert other conditions

def test_user_login(client):
    response = client.post('/login', data={'email': 'test@example.com', 'password': 'password'})
    assert response.status_code == 200
    # Assert other conditions

if __name__ == '__main__':
    app.run(debug=True)

