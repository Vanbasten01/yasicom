from app.routes import bp
from flask import render_template, request, redirect, url_for

@bp.route('/checkout', methods=['POST', 'GET'])
def checkout():
    product_id = request.args.get('product_id', type=int)
    quantity = request.args.get('quantity', type=int)
    from app.models.product import Product
    product = Product.query.get_or_404(product_id)


    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        adress = request.form['address']
        city = request.form['city']
        postcode = request.form['postcode']
        country = request.form['country']
        phone_number = request.form['phone']
        email = request.form['email']
        quantity = quantity
        total_cost = product.cost * quantity

        from app.models.order import Order

        order = Order(first_name=first_name, last_name=last_name, adress=adress, city=city, postcode=postcode, country=country, phone_number=phone_number, email=email, product_name=product.name, product_cost=product.cost, quantity=quantity, total_cost=total_cost)

        from app import db

        db.session.add(order)
        db.session.commit()

        return redirect(url_for('routes.success'))



    return render_template('checkout.html', product=product, quantity=quantity)
