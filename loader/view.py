import logging
from json import JSONDecodeError

from flask import Blueprint, render_template, request

from functions import add_post
from loader.utils import save_picture

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


@loader_blueprint.route("/post")
def page_post_form():
    return render_template('post_form.html')


@loader_blueprint.route("/post", methods=["POST"])
def page_post_upload():
    picture = request.files.get('picture')
    content = request.form.get('content')

    if not picture or not content:
        return 'Error'

    if picture.filename.split('.')[-1] not in ['jpeg', 'png']:
        logging.info('File is not a picture')
        return 'Not valid file'
    try:
        picture_path: str = '/' + save_picture(picture)
    except FileNotFoundError:
        logging.error('File not found')
        return 'File not exists'
    except JSONDecodeError:
        return 'Invalid JSON'
    post: dict = add_post({'pic': picture_path, 'content': content})
    return render_template('post_uploaded.html', post=post)
