from flask import Flask, request, render_template, redirect

from database import db_session
from database.db_session import global_init
from database.models.user_data import User_data
from database.models.users import User
from database.sql_functions import add_user

from website.forms.loginform import ReqisterForm
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
        return redirect("main_menu.html")


@app.route("/log_in", methods=["GET", "POST"])
def log_in():
    form = ReqisterForm()

    if form.validate_on_submit():
        add_user(form)

        return redirect("/")

    return render_template("registration.html", form=form)


if __name__ == '__main__':
    global_init("../database/main_database.db")
    # start_init()
    # db_sess = db_session.create_session()

    app.run(port=8080, host='127.0.0.1')
