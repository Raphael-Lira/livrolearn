from livrolearn import database, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(id_usuario):
    return User.query.get(int(id_usuario))


class User(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, unique=True, nullable=False)
    password = database.Column(database.String, nullable=False)
