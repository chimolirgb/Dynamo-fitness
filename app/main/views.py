
from . import main
from flask import render_template,redirect, url_for,abort,flash,request
from flask_login import login_required, current_user

# from ..email import mail_message


@main.route('/')
def index():

   return render_template('index.html' )