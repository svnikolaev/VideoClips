from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from webapp.db import db
from webapp.user.models import User
from webapp.clip.views import blueprint as clip_blueprint
from webapp.user.views import blueprint as user_blueprint
from webapp.playlist.views import blueprint as playlist_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    Migrate(app, db, render_as_batch=True)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'

    app.register_blueprint(clip_blueprint)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(playlist_blueprint)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    return app
