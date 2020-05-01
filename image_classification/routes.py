from image_classification import app

@app.route('/')
def index():
    return 'Hello World'