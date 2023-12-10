from flask import render_template
from app.routes import bp
from flask_login import current_user
from sqlalchemy import desc, asc

@bp.route('/')
@bp.route('/home', strict_slashes=False)
def home():
    from app.models.product import Product
    #query products from highest to lowest cost
    products = Product.query.order_by(desc(Product.cost)).all()
    length = len(products)
    print(length)
    return render_template('home.html', products=products, length=length)
