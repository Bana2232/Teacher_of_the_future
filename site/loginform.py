from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, FieldList
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    surname = StringField('Фамилия', validators=[DataRequired()], description="ФФ")
    name = StringField('Имя', validators=[DataRequired()])
    patronymic = StringField('Отчество')
    # date = DateField('Дата рождения', validators=[DataRequired()])

    education = StringField('Образование', validators=[DataRequired()])
    edu_name = StringField('Название образовательного учреждения', validators=[DataRequired()])
    work = StringField('Место работы', validators=[DataRequired()])

    position = StringField('Должность', validators=[DataRequired()])
    # category = FieldList('Ваша категория', validators=[DataRequired()])
    speciality = StringField('Специальность', validators=[DataRequired()])
    # type = FieldList('1111', validators=[DataRequired()])

    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Зарегистрироваться')
