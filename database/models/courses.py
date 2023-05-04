import sqlalchemy
from sqlalchemy import orm
from ..db_session import SqlAlchemyBase


class Course(SqlAlchemyBase):
    __tablename__ = 'Courses'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True, index=True, unique=True)

    name = sqlalchemy.Column(sqlalchemy.String, nullable=False, index=True)
    description = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    photo = sqlalchemy.Column(sqlalchemy.String, default="doesn't have")

    owner_id = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey("Users.id"), nullable=False)
    subject = sqlalchemy.Column(sqlalchemy.Date, nullable=False)

    start_time = sqlalchemy.Column(sqlalchemy.DateTime, default="infinitive")
    end_time = sqlalchemy.Column(sqlalchemy.DateTime, default="infinitive")

    is_active = sqlalchemy.Column(sqlalchemy.Boolean, default=True)
    owner = orm.relationship("User", back_populates="user_owner")
