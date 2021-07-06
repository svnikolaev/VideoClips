# template of config.py
# need to fill and remove .templati in filename
from datetime import timedelta
import os

basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.abspath(os.path.join(basedir, '..', 'webapp.db'))

SQLALCHEMY_DATABASE_URI = "sqlite:///" + db_path

SECRET_KEY = "supersecret"

REMEMBER_COOKIE_DURATION = timedelta(days=5)

SQLALCHEMY_TRACK_MODIFICATIONS = False
