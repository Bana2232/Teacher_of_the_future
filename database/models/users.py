import sqlalchemy
from sqlalchemy import orm
from ..db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'Users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True, index=True)

    surname = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False, index=True)
    patronymic = sqlalchemy.Column(sqlalchemy.String, nullable=True, default="doesn't have")
    date = sqlalchemy.Column(sqlalchemy.Date, nullable=False)

    education = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("Education.id"))
    edu_name = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    place_of_work = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    position_at_work = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    teacher_category = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("Teacher_category.id"))
    speciality = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    type = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("User_type.id"))

    # email = sqlalchemy.Column(sqlalchemy.String,
    #                           index=True, unique=True, nullable=True)
    # hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    # created_date = sqlalchemy.Column(sqlalchemy.DateTime,
    #                                  default="222")
