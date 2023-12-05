from app.routes import bp
from flask import request, render_template, flash, redirect, url_for
from flask_login import login_required


@bp.route('/admin/delete_product/<product_id>', methods=['POST'])
def delete_product(product_id):
    from app import db
    from app.models.product import Product
    if request.method == 'POST':
        product = Product.query.get_or_404(product_id)
        db.session.delete(product)
        db.session.commit()
        flash('Product has been deleted successfully!', 'success')
        redirect(url_for('routes.edit_products'))
        return redirect(url_for('routes.edit_products'))
    return render_template('admin/edit_products.html')


