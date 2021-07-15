from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user
from webapp.playlist.forms import Add_playlist


blueprint = Blueprint('playlist', __name__, url_prefix='/playlist')

@blueprint.route('/index')
def all_playlist():
    title = "Мои плейлисты"
    if current_user.is_authenticated:
        return render_template('playlist/index.html', title=title)
    flash('Страница доступна только авторизованным пользователям')
    return redirect(url_for('user.login'))

@blueprint.route('/add_playlist')
def add_playlist():
    title = "Добавить плейлист"
    if current_user.is_authenticated:
        pl_form=Add_playlist()
        return render_template('playlist/add_playlist.html', title=title, form=pl_form )
    flash('Страница доступна только авторизованным пользователям')
    return redirect(url_for('user.login'))

@blueprint.route('/prosses_add_playlist')
def prosses_add_playlist():
    if current_user.is_authenticated:
        return redirect(url_for('clip.index'))
    flash('Страница доступна только авторизованным пользователям')
    return redirect(url_for('user.login'))
