import sqlalchemy
from sqlalchemy import orm
from ..db_session import SqlAlchemyBase


class User_data(SqlAlchemyBase):
    __tablename__ = 'User_data'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey("Users.id"))

    login = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    password = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    email = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    number = sqlalchemy.Column(sqlalchemy.String, nullable=False)
