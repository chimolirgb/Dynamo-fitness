from werkzeug.wrappers import UserAgentMixin
from app.forms import ContactForm
# from .forms import contactForms
from flask import render_template,redirect,url_for, flash,request
from flask_login import login_user,login_required,logout_user
from . import auth 
 
