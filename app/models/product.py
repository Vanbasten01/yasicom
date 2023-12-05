from app import db

class Product(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    cost = db.Column(db.DECIMAL(10, 2), nullable=False)
    cover = db.Column(db.String(255), nullable=False)
    photo1 = db.Column(db.String(255), nullable=False)
    photo2= db.Column(db.String(255), nullable=False)
    photo3= db.Column(db.String(255), nullable=False)
    flag = db.Column(db.String(28), default="YES", nullable=False)
    def __repr__(self):
        return f"Product {self.name}"
