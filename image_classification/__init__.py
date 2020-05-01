from flask import Flask

app = Flask(__name__)

from image_classification import routes