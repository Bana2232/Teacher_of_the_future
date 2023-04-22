import sqlite3
from hashlib import sha3_256
from uuid import uuid4


def start_session(dbname: str) -> None:
    """Запуск сессии базы данных"""
    global db, cur
    db = sqlite3.connect(f"../database/{dbname}")
    cur = db.cursor()


def close_session() -> None:
    """Закрытие сессии базы данных"""
    db.close()


def hash_password(password: str):
    salt = uuid4().hex
    return sha3_256(salt.encode("utf-8") + password.encode()).hexdigest() + ":" + salt


def check_password(old: str, new: str):
    password, salt = old.split(":")

    return password == sha3_256(salt.encode("utf-8") + new.encode("utf-8")).hexdigest()


def check_user_when_logging_in(login: str, password: str) -> bool:
    """Проверяет зарегистрирован ли пользователь в системе. Возвращает булевое значение"""

    is_exists = cur.execute(f'''SELECT login, password
                FROM User_data
                WHERE (login = "{login}") AND (password = "{password}")''').fetchall()

    if not is_exists:
        return False

    return True


def register_user(surname: str, name: str, date: str, education: str, edu_name: str, work: str, position: str,
                  category: str, speciality: str, type: str) -> bool:
    """Регистрирует пользователя в системе и возвращает True в случае успеха, иначе - False"""
    ...
