from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class Add_clip(FlaskForm):
    clip_name = StringField(
        'Название клипа',
        validators=[DataRequired()],
        render_kw={"class": "form-control"}
    )
    link = StringField(
        'Ссылка',
        validators=[DataRequired()],
        render_kw={"class": "form-control"}
    )
    playlist_id = StringField(
        'Плейлист',
        validators=[DataRequired()],
        render_kw={"class": "form-control"}
    )
    submit = SubmitField(
        'Создать',
        render_kw={"class": "btn btn-primary"}
    )