from app.routes import bp
from flask import render_template, request, flash
from werkzeug.utils import secure_filename
import os
from app import db
from flask_login import login_required


@bp.route('/admin/edit_product/<product_id>', methods=['POST', 'GET'])
@login_required
def edit_product(product_id):
    from app.models.product import Product
    product = Product.query.get(product_id)
    if request.method == 'POST':
        product.name = request.form['product_name']
        product.description = request.form['description']
        product.cost = float(request.form['cost'])
        cover = request.files['cover']
        photo1 = request.files['photo1']
        photo2 = request.files['photo2']
        photo3 = request.files['photo3']


        upload_folder = os.path.join(os.getcwd(), "app/static/images/uploads")


        if cover.filename:
            cover_filename = secure_filename(cover.filename)
            cover.save(os.path.join(upload_folder, cover_filename))
            product.cover = f"static/images/uploads/{cover_filename}"
        else:
            cover = product.cover

        if photo1.filename:
            photo1_filename = secure_filename(photo1.filename)
            photo1.save(os.path.join(upload_folder, photo1_filename))
            product.photo1 = f"static/images/uploads/{photo1_filename}"
        else:
            photo1 = product.photo1

        if photo2.filename:
            photo2_filename = secure_filename(photo2.filename)
            photo2.save(os.path.join(upload_folder, photo2_filename))
            product.photo2 = f"static/images/uploads/{photo2_filename}"
        else:
            photo2 = product.photo2
        
        if photo3.filename:
            photo3_filename = secure_filename(photo3.filename)
            photo3.save(os.path.join(upload_folder, photo3_filename))
            product.photo3 = f"static/images/uploads/{photo3_filename}"
        else:
            photo3 = product.photo3

        db.session.commit()
        flash('Product is upadated Successfully!', 'success')

        

    return render_template('admin/edit_product.html', product=product)


