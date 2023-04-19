import sqlite3


def start_session(dbname: str) -> None:
    """Запуск сессии базы данных"""
    global db, cur
    db = sqlite3.connect(f"../database/{dbname}")
    cur = db.cursor()


def close_session() -> None:
    """Закрытие сессии базы данных"""
    db.close()


def check_user_when_logging_in(login: str, password: str) -> bool:
    """Проверяет зарегистрирован ли пользователь в системе"""
    is_exists = cur.execute(f'''SELECT login, password
                FROM User_data
                WHERE (login = "{login}") AND (password = "{password}")''').fetchall()

    if (is_exists[0] == login) and (password[1] == password):
        return True

    return False
