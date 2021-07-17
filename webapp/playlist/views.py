from webapp.clip.models import Clip
from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user
import flask_login

from webapp.db import db
from webapp.playlist.forms import Add_playlist
from webapp.playlist.models import Playlist


blueprint = Blueprint('playlist', __name__, url_prefix='/playlist')


@blueprint.route('/user_<user_id>/playlist_<pl_id>')
def current_playlist(user_id, pl_id):
    title = "Плейлист {}".format(pl_id)
    clip_list = Clip.query.filter_by(author_id=user_id, playlist_id=pl_id).all()
    print (clip_list)
    return render_template('playlist/playlist.html', title=title, clip_list=clip_list)


@blueprint.route('/my_playlists')
def all_playlist():
    title = "Мои плейлисты"
    if current_user.is_authenticated:
        pl_list = Playlist.query.filter_by(author_id=current_user.id).all()
        clip_list = Clip.query.filter_by(author_id=current_user.id).all()
        return render_template('playlist/my_playlists.html', title=title, pl_list=pl_list, clip_list=clip_list)
    flash('Страница доступна только авторизованным пользователям')
    return redirect(url_for('user.login'))

@blueprint.route('/add_playlist')
def add_playlist():
    title = "Добавить плейлист"
    if current_user.is_authenticated:
        pl_form=Add_playlist()
        return render_template('playlist/add_playlist.html', title=title, form=pl_form)


@blueprint.route('/prosses_add_playlist', methods=['POST'])
def prosses_add_playlist():
    if current_user.is_authenticated:
        form = Add_playlist()
        new_playlist = Playlist(name=form.pl_name.data, comment=form.comment.data,
                                author_id=current_user.id
                                )
        db.session.add(new_playlist)
        db.session.commit()
        flash('Плейлист добавлен')
        return redirect(url_for('playlist.all_playlist'))
    flash('Страница доступна только авторизованным пользователям')
    return redirect(url_for('user.login'))   
