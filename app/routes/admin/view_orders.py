from app.routes import bp
from flask import render_template, request
from flask_login import login_required
from sqlalchemy import desc, asc

@bp.route('/admin/view_orders')
@login_required
def view_orders():
    status_filter = request.args.get('status', 'all').lower()
    from app.models.order import Order
    if status_filter == 'all':
        orders = Order.query.order_by(desc(Order.order_id)).all()
    elif status_filter == 'completed':
        orders = Order.query.filter_by(status='completed').all()
    elif status_filter == 'pending':
        orders = Order.query.filter_by(status='pending').all()
    elif status_filter == 'canceled':
        orders = Order.query.filter_by(status='canceled').all()
    return render_template('admin/view_orders.html', orders=orders, selected_tab=status_filter)
