
from flask.helpers import flash
from flask.wrappers import Request
from werkzeug.utils import redirect
from werkzeug.wrappers import UserAgentMixin
# from app.forms import ContactForm
from . import main
from flask import render_template,redirect, url_for,abort,flash,request
from flask_login import login_required, current_user
from ..models import User,Blog,Comment,Subscribe
from .. import db,photos
from .forms import BlogForm,CommentsForm,UpdateProfile,SubscriptionForm
import markdown2 

from ..email import mail_message


@main.route('/',methods=['POST','GET'])
def index():
    subscribeform = SubscriptionForm()
    if subscribeform.validate_on_submit():
        email = subscribeform.email.data
        sub=Subscribe(email=email)
        sub.save_email()
        db.session.add(sub)
        db.session.commit()

        mail_message("Thank You for Subscribing","/thank_you",sub.email,sub=sub)

    return render_template('index.html',subscribeform=subscribeform)

# @main.route('/contact', methods=["GET", "POST"])
# def contact():
#     form = ContactForm()

#     if form.validate_on_submit():

#         user = UserAgentMixin.query.filter_by(email=form.email.data).first()

#         if user is not None and user.verify_password(form.password.data):

#             form (user, form.remember.data)

#             if user.is_admin:
#                 return redirect(url_for('main.admin_dashboard'))
#             else:
#                 return redirect(Request.args.get('next') or url_for('main.index'))

#         flash('Invalid username or password')

#     title = "Dynamo-fitness contact"

#     return render_template('auth/contact.html', contact_form=form, title=title)
  


@main.route('/nutrition')
def nutrition():

   return render_template('nutrition.html')

@main.route('/workouts')
def workouts():

   return render_template('workouts.html')


@main.route('/about')
def about():

   return render_template('about.html')

@main.route('/services')
def services():

   return render_template('services.html')

@main.route('/blogs')
def blog():
    # user = User.query.filter_by(username = uname).first()

    all_blogs=Blog.query.order_by(Blog.posted).all()

    return render_template("blogs.html", blogs=all_blogs)



@main.route('/blogs/create_blog',methods=['POST','GET'])
@login_required
def create():

    form = BlogForm()
    
   
    if form.validate_on_submit():
        title = form.title.data
        blog= form.blog.data
        author = form.author.data
        
        new_blog = Blog(title=title,blog=blog, author=author)
        new_blog.save_blog()
        db.session.add(new_blog)
        db.session.commit()
     
        return redirect(url_for('main.blog'))
      
    
    
    return render_template("create_blog.html", blog_form=form)


@main.route('/comments/<int:id>',methods=['POST','GET'])
@login_required
def comments(id):
    blog = Blog.query.get(id)
    commentform = CommentsForm()
    
    if commentform.validate_on_submit():
        comment= commentform.comment.data
        new_comment=Comment(comment=comment)
        new_comment.save_comment()
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('main.comments',id = id))
    
         
    
    
    comment = Comment.query.filter_by(id=id).all()
    format_blog = markdown2.markdown(blog.blog,extras=["code-friendly", "fenced-code-blocks"])
    return  render_template("comments.html", blog=blog, format_blog=format_blog , commentform=commentform, comments=comment)
   

@main.route('/deleteblog/<int:id>', methods=['GET', 'POST'])
@login_required
def deleteBlog(id):
    blog = Blog.query.get_or_404(id)
    db.session.delete(blog)
    db.session.commit()
    return redirect(url_for('main.blog'))

    return render_template('blogs.html')




@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)


@main.route('/user/<uname>/update/pic',methods= ['POST','GET'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

