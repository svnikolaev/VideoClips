from sqlalchemy.orm import relationship
from webapp.db import db


class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id', ondelete='CASCADE'),
        index=True
    )
    playlist_id = db.Column(
        db.Integer,
        db.ForeignKey('playlist.id', ondelete='CASCADE'),
        index=True
    )
    user = relationship('User', backref='favorites')
    playlist = relationship('Playlist', backref='favorites')

    def __repr__(self):
        return '<Favorite id={}>'.format(self.id)
