import sqlalchemy
from sqlalchemy import orm
from ..db_session import SqlAlchemyBase


class Teacher_category(SqlAlchemyBase):
    __tablename__ = 'Teacher_category'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True, index=True)

    category = sqlalchemy.Column(sqlalchemy.String, nullable=False, unique=True)
