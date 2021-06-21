
from . import main
from flask import render_template,url_for
from .. import db,photos

# from ..email import mail_message


@main.route('/')
def index():

   return render_template('index.html' )