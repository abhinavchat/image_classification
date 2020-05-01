from image_classification import app

@app.shell_context_processor
def flask_shell():
    return {'app': app}