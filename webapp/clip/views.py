from flask import Blueprint, render_template


blueprint = Blueprint('clip', __name__)


@blueprint.route('/')
def index():
    # title = "Video Clips"
    title = "Hello World"
    # news_list = News.query.order_by(News.published.desc()).all()
    return render_template('clip/index.html',
                           title=title)
