from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class Add_playlist(FlaskForm):
    pl_name = StringField(
        'Название плейлиста',
        validators=[DataRequired()],
        render_kw={"class": "form-control"}
    )
    comment = StringField(
        'Описание',
        validators=[DataRequired()],
        render_kw={"class": "form-control"}
    )
    submit = SubmitField(
        'Создать',
        render_kw={"class": "btn btn-primary"}
    )
