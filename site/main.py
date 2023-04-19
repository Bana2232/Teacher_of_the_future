from flask import Flask, request, render_template, redirect
from database.sql_functions import start_session, close_session, check_user_when_logging_in

app = Flask(__name__)


@app.route('/')
def func():
    return "Главное меню"


@app.route('/index', methods=['POST', 'GET'])
def index():
    if request.method == "GET":
        return render_template("sign_in_page.html")

    elif request.method == "POST":
        start_session("main_database.db")
        check = check_user_when_logging_in(request.form.get("login"), request.form.get("password"))

        close_session()

        if check:
            return "Добро пожаловать"

        return "Всё, давай, салам алейкум"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
