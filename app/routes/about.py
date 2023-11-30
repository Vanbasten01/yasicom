from flask import render_template
from app.routes import bp

@bp.route('/about', strict_slashes=False)
def about():
    return render_template('about.html')
