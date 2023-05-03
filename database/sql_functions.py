import sqlite3
from hashlib import sha3_256
from uuid import uuid4


def hash_password(password: str):
    salt = uuid4().hex
    return sha3_256(salt.encode("utf-8") + password.encode()).hexdigest() + ":" + salt


def check_password(old: str, new: str):
    password, salt = old.split(":")

    return password == sha3_256(salt.encode("utf-8") + new.encode("utf-8")).hexdigest()
