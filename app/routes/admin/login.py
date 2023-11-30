from flask import render_template, request, url_for, redirect, flash
from app.routes import bp
from flask_login import login_user, login_required, current_user, logout_user

@bp.route('/admin/login', methods=['POST', 'GET'])
def login():
    from app.models.admin import Admin
    existing_admin = Admin.query.first()
    if existing_admin:
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']
            if existing_admin.check_pwd(password) and existing_admin.email == email:
                login_user(existing_admin)
                return redirect(url_for('routes.dashboard'))
            else:
                flash('Invalid Email or Password', 'danger')
        return render_template('admin/login.html')
    
    elif request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        admin = Admin(email=email)
        admin.set_pwd(password)

        from app import db

        db.session.add(admin)
        db.session.commit()
        login_user(admin)
        return redirect(url_for('routes.dashboard'))
    return render_template('admin/login.html')




@bp.route('/admin/logout')
@login_required
def logout():
    flash('Have a Nice Day Admin', 'success')
    logout_user()
    print(current_user)
    return redirect(url_for('routes.login'))
