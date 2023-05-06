from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, FieldList
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    repeat_password = PasswordField('Повторите пароль', validators=[DataRequired()])

    submit = SubmitField('Войти')
