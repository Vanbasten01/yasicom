from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
#from app.routes import bp
from flask_migrate import Migrate
from dotenv import load_dotenv
from flask_login import LoginManager
import os

load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'routes.login'


db = SQLAlchemy(app)
from app.routes import bp as routes_bp
app.register_blueprint(routes_bp)
migrate = Migrate(app, db)

#login_manager = LoginManager()
#login_manager.init_app(app)
#login_manager.login_view = 'routes.login'

from app.models.product import Product
from app.models.admin import Admin
from app.models.order import Order

@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(int(user_id))

if __name__ == "__main__":
    app.run(debug=True)
