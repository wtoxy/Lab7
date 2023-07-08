from flask import Flask
from flask_migrate import Migrate
from app.auth import auth
from flask_login import LoginManager
from app.db import db
from app.views import bp
from app.templates.config import Config
from app.models import Employee, Position, Division, Job, User

app = Flask(__name__)
app.debug = True
app.config.from_object(Config)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:1029@localhost:5432/lab7"

db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


migrate = Migrate(app, db)
app.register_blueprint(bp)
app.register_blueprint(auth)
