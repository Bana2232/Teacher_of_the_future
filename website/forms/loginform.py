from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, FieldList, BooleanField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')

    submit = SubmitField('Войти')
