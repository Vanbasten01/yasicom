from flask import render_template
from app.routes import bp
from sqlalchemy import desc, asc

@bp.route('/products', strict_slashes=False)
def products():
    from app.models.product import Product
    products = Product.query.order_by(desc(Product.product_id)).all()
    length = len(products)
    return render_template('products.html', products=products, length=length)
