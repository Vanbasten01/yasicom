from app.routes import bp
from flask_login import login_required
from sqlalchemy import desc
from flask import render_template


@bp.route('/admin/edit_products')
def edit_products():
    from app.models.product import Product
    products = Product.query.order_by(desc(Product.product_id)).all()
    return render_template('admin/edit_products.html', products=products)


