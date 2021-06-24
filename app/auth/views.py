from werkzeug.wrappers import UserAgentMixin
from app.forms import ContactForm
# from .forms import contactForms
from flask import render_template,redirect,url_for, flash,request
from flask_login import login_user,login_required,logout_user
from . import auth 
 
@auth.route('/contact', methods=["GET", "POST"])
def contact():
    form = ContactForm()

    if form.validate_on_submit():

        user = UserAgentMixin.query.filter_by(email=form.email.data).first()

        if user is not None and user.verify_password(form.password.data):

            form (user, form.remember.data)

            if user.is_admin:
                return redirect(url_for('main.admin_dashboard'))
            else:
                return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or password')

    title = "Dynamo-fitness contact"

    return render_template('auth/contact.html', contact_form=form, title=title)
