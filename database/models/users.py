import sqlalchemy

from datetime import datetime
from sqlalchemy import orm
from flask_login import UserMixin

from ..db_session import SqlAlchemyBase


class User(SqlAlchemyBase, UserMixin):
    __tablename__ = 'Users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True, unique=True, index=True)

    surname = sqlalchemy.Column(sqlalchemy.String, nullable=False, index=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False, index=True)
    patronymic = sqlalchemy.Column(sqlalchemy.String, nullable=True, default="doesn't have")

    date = sqlalchemy.Column(sqlalchemy.Date, nullable=True)
    registration_date = sqlalchemy.Column(sqlalchemy.DateTime, nullable=True, default=datetime.now)

    education = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("Education.id"), nullable=True)
    edu_name = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    place_of_work = sqlalchemy.Column(sqlalchemy.String, default="doesn't work")
    position_at_work = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    teacher_category = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("Teacher_category.id"),
                                         nullable=True)
    speciality = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    type = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("User_type.id"), nullable=True)

    data = orm.relationship("User_data", back_populates="user")

    user_courses = orm.relationship("User_courses_class", back_populates="user")

    user_owner = orm.relationship("Course", back_populates="owner")
