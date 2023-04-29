from database.models.user_type import User_type
from database.models.education import Education
from database.models.teacher_category import Teacher_category

from database.db_session import create_session

is_started = False


def start_init() -> None:
    """Добавляет константные строки в базу данных"""
    global is_started, user_type, education, category

    if is_started:
        raise Exception("Стартовая инициализация уже была осуществлена")

    else:
        user_type = User_type()
        education = Education()
        category = Teacher_category()

        db_sess = create_session()

        user_type.type = "Teacher"
        education.level = "Secondary"
        category.category = "None"

        db_sess.add(user_type)
        db_sess.add(education)
        db_sess.add(category)

        db_sess.commit()

        user_type.type = "Student"
        education.level = "Higher"
        category.category = "First"

        db_sess.add(user_type)
        db_sess.add(education)
        db_sess.add(category)

        db_sess.commit()

        category.category = "Higher"

        db_sess.add(category)
        db_sess.commit()

        is_started = True
