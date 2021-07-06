from flask import Blueprint, render_template
from webapp.user.forms import LoginForm

blueprint = Blueprint('user', __name__, url_prefix='/users')


@blueprint.route('/login')
def login():
    title = "Авторизация"
    login_form = LoginForm()
    return render_template(
        'user/login.html',
        title=title,
        form=login_form
    )
