from flask import render_template, url_for, redirect, request, session
from livrolearn import app

@app.route('/')
def homepage():
    return render_template('index.html')