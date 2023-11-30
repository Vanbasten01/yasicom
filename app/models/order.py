from app import db
from datetime import datetime

class Order(db.Model):
    order_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=False)
    adress = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(64), nullable=False)
    postcode = db.Column(db.String(28), nullable=False)
    country = db.Column(db.String(64), nullable=False)
    phone_number = db.Column(db.String(28), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    product_name = db.Column(db.String(64), nullable=False)
    product_cost = db.Column(db.DECIMAL(10, 2), nullable=False)
    quantity = db.Column(db.String(28), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    total_cost = db.Column(db.DECIMAL(10, 2), nullable=False)
    status = db.Column(db.String(28), default="pending", nullable=False)

    def __repr__(self):
        return f"Order {self.order}"
