import sqlalchemy
from sqlalchemy import orm
from werkzeug.security import generate_password_hash, check_password_hash

from ..db_session import SqlAlchemyBase


class User_data(SqlAlchemyBase):
    __tablename__ = 'Users_data'

    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("Users.id"), primary_key=True, unique=True,
                                index=True)

    login = sqlalchemy.Column(sqlalchemy.String, nullable=False, index=True, unique=True)
    password = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    email = sqlalchemy.Column(sqlalchemy.String, nullable=False, index=True, unique=True)
    phone_number = sqlalchemy.Column(sqlalchemy.String, nullable=False, index=True, unique=True)

    user = orm.relationship("User", back_populates="data")

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

