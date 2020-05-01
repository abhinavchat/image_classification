from flask import Flask
from flask_bootstrap import Bootstrap
from config import create_config
import os

app = Flask(__name__)
app.config.from_object(create_config[os.getenv('ENVIRONMENT') or 'dev'])
bootstrap = Bootstrap(app)

from image_classification import routes