from flask import render_template, abort, redirect, url_for
from app.routes import bp
from flask_login import login_required, current_user


@bp.route('/admin/dashboard')
@login_required
def dashboard():
    print(current_user)
    if not current_user.is_authenticated:
        return redirect(url_for('routes.login'))
    return render_template('admin/base.html')
