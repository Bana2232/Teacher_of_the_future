from werkzeug.security import check_password_hash

from database.models.user_data import User_data
from database.models.users import User

from hashlib import sha3_256
from uuid import uuid4

from . import db_session
from website.forms.registerform import ReqisterForm


def check_password(old: str, new: str):
    password, salt = old.split(":")

    return password == sha3_256(salt.encode("utf-8") + new.encode("utf-8")).hexdigest()


def add_user(form: ReqisterForm) -> None:
    """Добавляет пользователя в базу данных"""
    user = User()
    user_data = User_data()
    db_sess = db_session.create_session()

    user.name = form.name.data.capitalize()
    user.surname = form.surname.data.capitalize()

    if form.patronymic.data is not None:
        user.patronymic = form.patronymic.data.capitalize()

    user.date = form.date.data
    user.education = form.education.data
    user.edu_name = form.edu_name.data

    if form.work.data is not None:
        user.place_of_work = form.work.data

    if form.position.data is not None:
        user.position_at_work = form.position.data

    user.teacher_category = 3

    user.speciality = form.speciality.data.capitalize()
    user.type = 2

    db_sess.add(user)
    db_sess.commit()

    user_data.user_id = user.id

    user_data.login = form.login.data
    user_data.set_password(form.password.data)
    user_data.email = form.email.data
    user_data.phone_number = form.phone_number.data

    db_sess.add(user_data)
    db_sess.commit()


def check_user(email: str, password: str) -> bool:
    """Проверяет данные пользователя при входе"""

    db_sess = db_session.create_session()

    user_data = db_sess.query(User_data).filter(User_data.email == email).first()

    user = db_sess.query(User).filter(User.id == user_data.user_id)

    for i in user:
        print(i)

    return check_password_hash(user_data.password, password)
