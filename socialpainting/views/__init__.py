# -*- coding: utf-8 -*-
from flask import (
    Blueprint,
    render_template,
)

pages = Blueprint('pages', __name__, url_prefix='')


@pages.route('/')
def home():
    return render_template('home.html')


@pages.route('/contributions')
def catalogue():
    return render_template('catalogue.html')
