from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class Admin(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)

    def __repr__(self):
        return f"<Admin {self.email}>"

    def set_pwd(self, pwd):
        self.password_hash = generate_password_hash(pwd, method='sha256')

    def check_pwd(self, pwd):
        return check_password_hash(self.password_hash, pwd)
