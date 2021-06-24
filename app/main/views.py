
from flask.helpers import flash
from flask.wrappers import Request
from werkzeug.utils import redirect
from werkzeug.wrappers import UserAgentMixin
from app.forms import ContactForm
from . import main
from flask import render_template,url_for
from .. import db,photos

# from ..email import mail_message


@main.route('/')
def index():

   return render_template('index.html' )

@main.route('/contact', methods=["GET", "POST"])
def contact():
    form = ContactForm()

    if form.validate_on_submit():

        user = UserAgentMixin.query.filter_by(email=form.email.data).first()

        if user is not None and user.verify_password(form.password.data):

            form (user, form.remember.data)

            if user.is_admin:
                return redirect(url_for('main.admin_dashboard'))
            else:
                return redirect(Request.args.get('next') or url_for('main.index'))

        flash('Invalid username or password')

    title = "Dynamo-fitness contact"

    return render_template('auth/contact.html', contact_form=form, title=title)
  