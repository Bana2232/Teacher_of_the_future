from database.models.user_type import User_type
from database.models.education import Education
from database.models.teacher_category import Teacher_category

from database.db_session import create_session

is_started = False


def start_init() -> None:
    """Добавляет константные строки в базу данных"""
    global is_started, user_type, education, category, db_sess

    if is_started:
        raise Exception("Стартовая инициализация уже была осуществлена")

    else:
        user_type1 = User_type()
        education1 = Education()
        category1 = Teacher_category()

        db_sess = create_session()

        user_type1.type = "Teacher"
        education1.level = "Secondary"
        category1.category = "None"

        db_sess.add(user_type1)
        db_sess.add(education1)
        db_sess.add(category1)

        user_type2 = User_type()
        education2 = Education()
        category2 = Teacher_category()

        user_type2.type = "Student"
        education2.level = "Higher"
        category2.category = "First"

        db_sess.add(user_type2)
        db_sess.add(education2)
        db_sess.add(category2)

        category3 = Teacher_category()

        category3.category = "Higher"
        db_sess.add(category3)

        db_sess.commit()

        is_started = True
