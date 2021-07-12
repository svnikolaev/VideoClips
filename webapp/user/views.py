from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user, login_user, logout_user
from webapp.user.forms import LoginForm
from webapp.user.models import User

blueprint = Blueprint('user', __name__, url_prefix='/users')


@blueprint.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('clip.index'))
    title = "Авторизация"
    login_form = LoginForm()
    return render_template(
        'user/login.html',
        title=title,
        form=login_form
    )

@blueprint.route('/process-login', methods=['POST'])
def process_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Вы вошли на сайт')
            return redirect(url_for('clip.index'))
    flash('Неправильное имя пользователя или пароль')
    return redirect(url_for('login'))

@blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('clip.index'))