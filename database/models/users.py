import sqlalchemy
from datetime import datetime
from sqlalchemy import orm
from ..db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'Users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True, unique=True, index=True)

    surname = sqlalchemy.Column(sqlalchemy.String, nullable=False, index=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False, index=True)
    patronymic = sqlalchemy.Column(sqlalchemy.String, nullable=True, default="doesn't have")

    date = sqlalchemy.Column(sqlalchemy.Date, nullable=False)
    registration_date = sqlalchemy.Column(sqlalchemy.DateTime, nullable=False, default=datetime.now)

    education = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("Education.id"), nullable=False)
    edu_name = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    place_of_work = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    position_at_work = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    teacher_category = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("Teacher_category.id"),
                                         nullable=False)
    speciality = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    type = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("User_type.id"), nullable=False)

    data = orm.relationship("User_data", back_populates="user")

    user_courses = orm.relationship("User_courses_class", back_populates="user")

    # email = sqlalchemy.Column(sqlalchemy.String,
    #                           index=True, unique=True, nullable=True)
    # hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    # created_date = sqlalchemy.Column(sqlalchemy.DateTime,
    #                                  default="222")
