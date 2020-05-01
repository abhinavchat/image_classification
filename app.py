from image_classification import app, db
from image_classification.models import User
from image_classification import login

@login.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()


@app.shell_context_processor
def flask_shell():
    return {'app': app, 'db': db, 'User': User}