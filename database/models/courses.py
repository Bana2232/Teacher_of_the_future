import sqlalchemy
from sqlalchemy import orm
from ..db_session import SqlAlchemyBase


class Courses(SqlAlchemyBase):
    __tablename__ = 'Courses'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True, index=True)

    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    description = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    owner = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey("Users.id"))
    subject = sqlalchemy.Column(sqlalchemy.Date, nullable=False)

    start_time = sqlalchemy.Column(sqlalchemy.DateTime, default="infinitive")
    end_time = sqlalchemy.Column(sqlalchemy.DateTime, default="infinitive")
