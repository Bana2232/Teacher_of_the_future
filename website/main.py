from flask import Flask, request, render_template, redirect
from flask_login import LoginManager

from database.db_session import global_init
from database.sql_functions import add_user, check_user

from website.forms.registerform import ReqisterForm
from website.forms.loginform import LoginForm
from website.forms.personal_account_form import Personal_account_form

from config import SECRET_KEY

app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY


# login_manager = LoginManager()
# login_manager.init_app(app)


@app.route('/')
def func():
    return render_template("index.html")


@app.route('/main_menu')
def func():
    return render_template("index.html")


@app.route('/sign_in', methods=['POST', 'GET'])
def sign_in():
    form = LoginForm()

    if form.validate_on_submit():
        if check_user(form.email.data, form.password.data):
            return redirect("/main_menu")

        return "Ты кого обмануть пытался?"

    return render_template("sign_in.html", form=form)


@app.route("/sign_up", methods=["GET", "POST"])
def log_in():
    form = ReqisterForm()

    if form.validate_on_submit():
        add_user(form)

        return redirect("/")

    return render_template("sign_up.html", form=form)


if __name__ == '__main__':
    global_init("../database/main_database.db")
    # db_sess = db_session.create_session()

    app.run(port=8080, host='127.0.0.1')
