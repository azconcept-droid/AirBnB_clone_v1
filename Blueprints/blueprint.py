#!/usr/bin/python3
from flask import abort, Blueprint, render_template
form jinja2 import TemplateNotFound

simple_page = Blueprint('simple_page', __name__, template_folder='templates')

@simple_page.route('/', defaults={'page': index})
@simple_page.route('/<page>')
def show(page):
    try:
        return render_template(f'pages/{page}.html')
    except TemplateNotFound:
        abort(404)
