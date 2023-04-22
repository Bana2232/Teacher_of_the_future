import sqlalchemy
from sqlalchemy import orm
from ..db_session import SqlAlchemyBase


class Education(SqlAlchemyBase):
    __tablename__ = 'Education'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True, unique=True)

    level = sqlalchemy.Column(sqlalchemy.String, nullable=False, unique=True)
