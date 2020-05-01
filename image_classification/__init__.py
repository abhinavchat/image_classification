from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
bootstrap = Bootstrap()
login = LoginManager()

def create_app(app_config):
    app = Flask(__name__)
    app.config.from_object(app_config)
    db.init_app(app)
    migrate.init_app(app, db)
    bootstrap.init_app(app)
    login.init_app(app)
    login.login_view = '/login'
    from image_classification.auth import auth
    app.register_blueprint(auth)

    from image_classification.main import main
    app.register_blueprint(main)

    return app


from image_classification import models