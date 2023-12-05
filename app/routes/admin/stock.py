from app.routes import bp
from flask import render_template, request, redirect, url_for


@bp.route('/admin/stock/<product_id>', methods=['GET', 'POST'])
def stock(product_id):
    from app.models.product import Product
    product = Product.query.get_or_404(product_id)
    if request.method == 'POST':
        new_flag = request.form['new_flag']
        product.flag = new_flag
        from app import db
        db.session.commit()
        return redirect(url_for('routes.edit_products'))
    return render_template('admin/stock.html', product=product)

