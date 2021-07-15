from sqlalchemy.orm import relationship
from webapp.db import db


class Playlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    comment = db.Column(db.Text(), nullable=True)
    author_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id', ondelete='CASCADE'),
        index=True
    )
    is_public = db.Column(db.Boolean, default=False)
    author = relationship('User', backref='playlists')

    def __repr__(self):
        return '<Playlist name={} id={}>'.format(self.name, self.id)
