
# Import necessary modules
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

# Create a Flask app
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=False)

# Define the Cart model
class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

# Create the database tables
db.create_all()

# Populate the database with some sample products
db.session.add(Product(name="Soccer Ball", price=20.00, category="Soccer", description="A regulation-sized soccer ball."))
db.session.add(Product(name="Basketball", price=30.00, category="Basketball", description="A regulation-sized basketball."))
db.session.add(Product(name="Swimming Goggles", price=15.00, category="Swimming", description="A pair of swimming goggles."))
db.session.commit()

# Define routes
@app.route("/")
def home():
    """
    Renders the home page.
    """
    return render_template("toy_shop.html", categories=Product.query.distinct(Product.category).all())

@app.route("/category/<category_name>")
def product_list(category_name):
    """
    Renders the category page.
    """
    return render_template("product_list.html", category_name=category_name, products=Product.query.filter_by(category=category_name).all())

@app.route("/product/<product_id>")
def product_details(product_id):
    """
    Renders the product page.
    """
    return render_template("product_details.html", product=Product.query.get(product_id))

@app.route("/add_to_cart/<product_id>")
def add_to_cart(product_id):
    """
    Adds the specified product to the cart.
    """
    cart_item = CartItem.query.filter_by(product_id=product_id).first()
    if cart_item is None:
        cart_item = CartItem(product_id=product_id, quantity=1)
        db.session.add(cart_item)
    else:
        cart_item.quantity += 1
    db.session.commit()
    return redirect(url_for("cart"))

@app.route("/cart")
def cart():
    """
    Renders the shopping cart.
    """
    return render_template("cart.html", cart_items=CartItem.query.all())

@app.route("/checkout")
def checkout():
    """
    Processes the checkout.
    """
    return render_template("checkout.html")

@app.route("/search", methods=["POST"])
def search():
    """
    Searches for products.
    """
    search_query = request.form.get("search_query")
    products = Product.query.filter(Product.name.like(f"%{search_query}%")).all()
    return render_template("toy_shop.html", products=products)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
