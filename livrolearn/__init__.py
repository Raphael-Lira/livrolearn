from flask import Flask


app = Flask(__name__)
#app.config['SECRET_KEY'] = '664529d5f8ba707b7da4e4e0c58a7703'


from livrolearn import routes 