from flask import render_template
from app.routes import bp

@bp.route('/contacts', strict_slashes=False)
def contact():
    return render_template('contact.html')
