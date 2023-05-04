import sqlalchemy
from sqlalchemy import orm
from ..db_session import SqlAlchemyBase


class User_courses_class(SqlAlchemyBase):
    __tablename__ = 'User_courses'

    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("Users.id"), primary_key=True, index=True)

    course_id = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey("Courses.id"))
    type = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("User_courses_type.id"), nullable=False)

    user = orm.relationship("User", back_populates="user_courses")
