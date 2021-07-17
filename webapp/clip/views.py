from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user

from webapp.db import db
from webapp.clip.forms import Add_clip
from webapp.clip.models import Clip
from webapp.playlist.models import Playlist


blueprint = Blueprint('clip', __name__)


@blueprint.route('/')
def index():
    title = "Video Clips"
    return render_template('clip/index.html',
                           title=title)


@blueprint.route('/add_clip')
def add_clip():
    title = "Добавить клип"
    if current_user.is_authenticated:
        pl_form = Add_clip()
        return render_template('clip/add_clip.html', title=title, form=pl_form)

@blueprint.route('/prosses_add_clip', methods=['POST'])
def prosses_add_clip():
    if current_user.is_authenticated:
        form = Add_clip()
        new_clip = Clip(name=form.clip_name.data, link=form.link.data,
                        author_id=current_user.id, playlist_id=form.playlist_id.data
                                )
        db.session.add(new_clip)
        db.session.commit()
        flash('Клип добавлен')
        return redirect(url_for('playlist.all_playlist'))
    flash('Страница доступна только авторизованным пользователям')
    return redirect(url_for('user.login'))   