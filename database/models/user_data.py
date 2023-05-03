import sqlalchemy
from sqlalchemy import orm
from ..db_session import SqlAlchemyBase


class User_data(SqlAlchemyBase):
    __tablename__ = 'Users_data'

    # id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, unique=True)

    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("Users.id"), primary_key=True, unique=True,
                                index=True)

    login = sqlalchemy.Column(sqlalchemy.String, nullable=False, index=True)
    password = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    email = sqlalchemy.Column(sqlalchemy.String, nullable=False, index=True)
    number = sqlalchemy.Column(sqlalchemy.String, nullable=False, index=True)

    user = orm.relationship("User", back_populates="data")
