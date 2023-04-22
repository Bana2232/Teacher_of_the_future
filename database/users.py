import sqlalchemy
from db_session import SqlAlchemyBase


# доработать
class User(SqlAlchemyBase):
    __tablename__ = 'Users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True, index=True)

    surname = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False, index=True)
    patronymic = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    date = sqlalchemy.Column(sqlalchemy.Date, nullable=False)

    education = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    edu_name = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    place_of_work = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    position_at_work = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    teacher_category = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    speciality = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    type = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)

    # email = sqlalchemy.Column(sqlalchemy.String,
    #                           index=True, unique=True, nullable=True)
    # hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    # created_date = sqlalchemy.Column(sqlalchemy.DateTime,
    #                                  default="222")
