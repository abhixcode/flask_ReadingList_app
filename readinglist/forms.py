from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User
from flask_login import login_user, current_user


class ListForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    bookname = StringField('Bookname', validators=[DataRequired()])
    #author = StringField('Author', validators=[DataRequired()])
    #search = SubmitField('search')
    submit = SubmitField('Add')