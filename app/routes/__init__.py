from flask import Blueprint, Flask

bp = Blueprint('routes', __name__)

from app.routes.home import home
from app.routes.contacts import contact
from app.routes.about import about
from app.routes.product import productid
from app.routes.products import products
from app.routes.order import checkout
from app.routes.success import success
from app.routes.admin.login import login
from app.routes.admin.login import logout
from app.routes.admin.dashboard import dashboard
from app.routes.admin.add_product import add_product
from app.routes.admin.edit_products import edit_products
from app.routes.admin.edit_product import edit_product
from app.routes.admin.delete_product import delete_product
from app.routes.admin.view_orders import view_orders
from app.routes.admin.view_order import view_order
from app.routes.admin.stock import stock
