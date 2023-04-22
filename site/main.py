from flask import Flask, request, render_template
from database.sql_functions import start_session, close_session, check_user_when_logging_in
from login_for_site.loginform import LoginForm
from config import SECRET_KEY

app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY


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
            return render_template("personal_account.html")

        return "Всё давай, салам алейкум"


@app.route("/log_in", methods=["GET", "POST"])
def log_in():
    form = LoginForm()

    if form.validate_on_submit():
        return "Success"

    return render_template("registration.html", title="Регистрация", form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
