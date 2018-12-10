from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, ValidationError



# Login / Register Form
class LoginForm(FlaskForm):
    # Fields
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('submit')


    def validate_username(self, username):
        if len(username.data) < 4:
            raise ValidationError('username must be longer than 4 characters')

    def validate_password(self, password):
        if len(password.data) < 4:
            raise ValidationError('password must be longer than 4 characters')






# Answer / Questions Form
class AnswerForm(FlaskForm):
    # Answer may be left empty
    answer = StringField('answer')
    submit = SubmitField('submit')
