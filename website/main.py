import flask_login
from flask import Flask, request, render_template, redirect
from flask_login import LoginManager, login_required, logout_user, login_user

from database import db_session
from database.db_session import global_init
from database.models.users import User
from database.sql_functions import add_user, log_in_user

from website.forms.registerform import ReqisterForm
from website.forms.loginform import LoginForm
from website.forms.personal_account_form import Personal_account_form

from config import SECRET_KEY

app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route("/")
@login_required
def main_menu():
    return f"Здравствуйте, {flask_login.current_user.name} {flask_login.current_user.patronymic}"
    # return render_template("index.html")


@app.route('/')
def func():
    return render_template("index.html")


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/sign_in', methods=['POST', 'GET'])
def sign_in():
    form = LoginForm()

    if form.validate_on_submit():
        if log_in_user(form.email.data, form.password.data, form):
            return redirect("/")

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
