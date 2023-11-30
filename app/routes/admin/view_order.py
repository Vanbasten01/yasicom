from app.routes import bp
from flask import render_template, request, redirect, url_for
from flask_login import login_required


@bp.route('/admin/view_order/<order_id>', methods=['POST', 'GET'])
@login_required
def view_order(order_id):
    from app.models.order import Order
    order = Order.query.get_or_404(order_id)
    if request.method == 'POST':
        new_status = request.form['new_status']
        order.status = new_status
        from app import db
        db.session.commit()
        return redirect(url_for('routes.view_orders'))
    return render_template('admin/view_order.html', order=order)
