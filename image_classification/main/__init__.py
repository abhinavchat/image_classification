from flask import Blueprint

main = Blueprint('main', __name__)

from image_classification.main import routes