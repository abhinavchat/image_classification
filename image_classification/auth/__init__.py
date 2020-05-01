from flask import Blueprint

auth = Blueprint('auth', __name__)

from image_classification.auth import routes