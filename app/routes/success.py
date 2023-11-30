from app.routes import bp
from flask import render_template

@bp.route('/success')
def success():
    return render_template('success.html')
