import os
from flask import render_template, request, flash
from app.routes import bp
from werkzeug.utils import secure_filename
from flask_login import login_required, current_user


@bp.route('/admin/add_product', methods=['GET', 'POST'])
@login_required
def add_product():
    if request.method == 'POST':
        from app.models.product import Product
        product_name = request.form['product_name']
        description = request.form['description']
        cost = float(request.form['cost'])

        cover_photo = request.files['cover']
        photo1 = request.files['photo1']
        photo2 = request.files['photo2']
        photo3 = request.files['photo3']

        upload_folder = f"app/static/images/uploads"

        cover_filename = secure_filename(cover_photo.filename)
        photo1_filename = secure_filename(photo1.filename)
        photo2_filename = secure_filename(photo2.filename)
        photo3_filename = secure_filename(photo3.filename)

        cover_photo.save(os.path.join(upload_folder, cover_filename))
        photo1.save(os.path.join(upload_folder, photo1_filename))
        photo2.save(os.path.join(upload_folder, photo2_filename))
        photo3.save(os.path.join(upload_folder, photo3_filename))

        cover_path = f"static/images/uploads/{cover_filename}"
        photo1_path = f"static/images/uploads/{photo1_filename}"
        photo2_path = f"static/images/uploads/{photo2_filename}"
        photo3_path = f"static/images/uploads/{photo3_filename}"

        new_product = Product(name=product_name, description=description, cost=cost, cover=cover_path, photo1=photo1_path, photo2=photo2_path, photo3=photo3_path)

        from app import db
        db.session.add(new_product)
        db.session.commit()
        flash('Product added successfully!', 'success')


    return render_template('admin/add_product.html')
