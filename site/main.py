from flask import Flask, request, render_template, redirect
from database.sql_functions import start_session, close_session, check_user_when_logging_in

app = Flask(__name__)
app.config["SECRET_KEY"] = "104479aad65a9c7479ef411a75c58d4fe2cb2d3bd5653e9171f2ec4e996d9fce"


@app.route('/')
def func():
    return "Главное меню"


@app.route('/sign_in', methods=['POST', 'GET'])
def sign_in():
    if request.method == "GET":
        return render_template("sign_in_page.html")

    elif request.method == "POST":
        start_session("main_database.db")
        check = check_user_when_logging_in(request.form.get("login"), request.form.get("password"))

        close_session()

        if check:
            return "Добро пожаловать"

        return "Всё, давай, салам алейкум"


@app.route("/log_in")
def log_in():
    if request.method == "GET":
        return render_template("registration.html")

    elif request.method == "POST":
        pass


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
