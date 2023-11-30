from app.routes import bp
from flask import render_template


@bp.route('/products/<product_id>', methods=['GET', 'POST'])
def productid(product_id):
    from app.models.product import Product
    product = Product.query.get_or_404(product_id)
    return render_template('productid.html', product=product)
