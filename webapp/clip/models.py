from sqlalchemy.orm import relationship
from webapp.db import db


class Clip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(128), index=True,
                     unique=True, nullable=False)
    name = db.Column(db.String(128), nullable=False)
    author_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id', ondelete='CASCADE'),
        index=True
    )
    playlist_id = db.Column(
        db.Integer,
        db.ForeignKey('playlist.id', ondelete='CASCADE'),
        index=True
    )
    author = relationship('User', backref='clips')
    playlist = relationship('Playlist', backref='clips')

    def __repr__(self):
        return '<Clip name={} id={}>'.format(self.name, self.id)
