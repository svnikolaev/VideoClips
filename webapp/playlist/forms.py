from flask_wtf import FlaskForm
from wtforms import SubmitField

class Add_playlist(FlaskForm):
    submit = SubmitField(
        'Создать',
        render_kw={"class": "btn btn-primary"}
    )
