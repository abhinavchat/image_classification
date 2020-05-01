from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from config import create_config
import os

app = Flask(__name__)
app.config.from_object(create_config[os.getenv('ENVIRONMENT') or 'dev'])
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bootstrap = Bootstrap(app)
login = LoginManager(app)
login.login_view = '/login'

from image_classification import routes