import sqlalchemy
from sqlalchemy import orm
from ..db_session import SqlAlchemyBase


class User_courses_type(SqlAlchemyBase):
    __tablename__ = 'User_courses_type'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True, unique=True)

    type = sqlalchemy.Column(sqlalchemy.String, nullable=False, unique=True)
