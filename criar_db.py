from livrolearn import database, app
from livrolearn.models import User


with app.app_context():
    database.create_all()