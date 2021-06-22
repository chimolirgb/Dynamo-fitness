from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import required,Email

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [required()])
    submit = SubmitField('Submit')
class BlogForm(FlaskForm):
    title = StringField('Blog title', validators=[required()])
    author = StringField('Author')
    blog = TextAreaField('Blog')
    submit =SubmitField('Submit')

class CommentsForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[required()])
    submit = SubmitField('Submit')