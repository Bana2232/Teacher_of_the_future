from flask import Flask, request, render_template, redirect

app = Flask(__name__)


@app.route('/')
def func():
    return "Главное меню"


@app.route('/index', methods=['POST', 'GET'])
def index():
    print(request.method)
    if request.method == "GET":
        return render_template("sign_in_page.html")

    elif request.method == "POST":
        print(request.form.get("login"))
        print(request.form.get("password"))

        return "Данные отправлены"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
