from flask import render_template, url_for, redirect, request, flash
from livrolearn import app, bcrypt, database
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from livrolearn.models import User
from livrolearn.forms import Cadastro, LoginForm

@app.route('/')
@login_required
def homepage():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    cadastro_form = Cadastro()

    if request.method == 'POST':
        if 'login' in request.form and login_form.validate_on_submit():
            print('xx')
            email = login_form.email.data
            password = login_form.password.data
            user = User.query.filter_by(email=login_form.email.data).first()
            if user and bcrypt.check_password_hash(user.password, login_form.password.data):
                login_user(user)
                return redirect(url_for('homepage'))  # Redireciona para a homepage
            else:
                flash('Login ou senha incorretos', 'danger')
        elif 'signup' in request.form and cadastro_form.validate_on_submit():
            print('xxx')
            username = cadastro_form.username.data
            email = cadastro_form.email.data
            password = cadastro_form.password.data
            confirm_password = cadastro_form.password_confirmation.data
            if password == confirm_password:
                hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
                new_user = User(username=username, email=email, password=hashed_password)
                database.session.add(new_user)
                database.session.commit()
                flash('Sua conta foi criada! Agora você pode fazer login.', 'success')
                login_user(new_user, remember=True)
                return redirect(url_for('homepage'))
            else:
                flash('As senhas não coincidem', 'danger')

    return render_template('login.html', login_form=login_form, cadastro_form=cadastro_form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
