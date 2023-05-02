from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
def func():
    return render_template('index.html')


@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/urok')
def urok():
    return render_template('course_page.html')


@app.route('/sign_up')
def sign_up():
    return render_template("sign_in_page.html")


@app.route('/courses', )
def courses():
    return render_template("projects.html")


@app.route('/phys')
def phys():
    param = {}
    param['main_title'] = 'Физика'
    param['first_title'] = 'Первый курс'
    param['second_title'] = 'Второй курс'
    param['third_title'] = 'Третий курс'
    param[
        'firstimg'] = 'https://trafaret-decor.ru/sites/default/files/2022-12/%D0%A4%D0%B8%D0%B7%D0%B8%D0%BA%D0%B0%20%D1%84%D0%BE%D0%BD%20%D0%B4%D0%BB%D1%8F%20%D0%BF%D1%80%D0%B5%D0%B7%D0%B5%D0%BD%D1%82%D0%B0%D1%86%D0%B8%D0%B8%20%2865%29.jpg'
    param[
        'secondimg'] = 'https://studentu24.ru/uploads/rs/articletitleimage/256/%D1%84%D0%B8%D0%B7%D0%B8%D0%BA%D0%B0.jpg'
    param[
        'thirdimg'] = 'https://gamerwall.pro/uploads/posts/2022-03/1648053390_13-gamerwall-pro-p-elektricheskii-tok-fon-krasivie-14.jpg'
    param['bgheadgrad'] = '-webkit-linear-gradient(45deg, rgb(100, 203, 243), rgb(84, 94, 239));'
    param['main_title_color'] = '#5f5e59'
    param['main_title_opacity'] = '1'
    return render_template("lessons/lesson-page.html", **param)


@app.route('/math', methods=['POST', 'GET'])
def math():
    param = {}
    param['main_title'] = 'Математика'
    param['first_title'] = 'Первый курс'
    param['second_title'] = 'Второй курс'
    param['third_title'] = 'Третий курс'
    param['bgheadgrad'] = 'linear-gradient(45deg, #37ecba, #72afd3);'
    param['main_title_color'] = '#636363'
    param['main_title_opacity'] = '1'
    return render_template("lessons/lesson-page.html", **param)


@app.route('/bio', methods=['POST', 'GET'])
def bio():
    param = {}
    param['main_title'] = 'Биология'
    param['first_title'] = 'Первый курс'
    param['second_title'] = 'Второй курс'
    param['third_title'] = 'Третий курс'
    param[
        'firstimg'] = 'https://www.sostav.ru/articles/rus/2010/03.12/news/images/1agrotest3.jpg'
    param[
        'secondimg'] = 'https://catherineasquithgallery.com/uploads/posts/2021-02/1613697482_37-p-fon-dlya-prezentatsii-po-biologii-39.jpg'
    param['thirdimg'] = 'https://klike.net/uploads/posts/2022-08/1661961079_j-58.jpg'

    param['bgheadgrad'] = '-webkit-linear-gradient(45deg, rgb(82, 181, 30), rgb(207, 222, 100))'
    param['main_title_color'] = '#e6e6e6'
    return render_template("lessons/lesson-page.html", **param)


@app.route('/chem', methods=['POST', 'GET'])
def chem():
    param = {}
    param['main_title'] = 'Химия'
    param['first_title'] = 'Первый курс'
    param['second_title'] = 'Второй курс'
    param['third_title'] = 'Третий курс'
    param['bgheadgrad'] = '-webkit-linear-gradient(45deg, rgb(224, 100, 252) 38%, rgb(83, 221, 244));'
    param['main_title_color'] = '#f5f8ad'
    param['main_title_opacity'] = '0.8'
    param[
        'firstimg'] = 'https://en.termodizayn.com/img/uploads/kullanimalanlari/85870b2e98716e5623287d812289c514.jpg'
    param[
        'secondimg'] = 'https://cdn.futura-sciences.com/buildsv6/images/wide1920/b/b/5/bb5ab61f3e_50151085_quiz-chimie-bac-mg-fotolia.jpg'
    param['thirdimg'] = 'https://phonoteka.org/uploads/posts/2022-02/1645015868_28-phonoteka-org-p-fon-po-khimii-29.jpg'
    return render_template("lessons/lesson-page.html", **param)


@app.route('/geo', methods=['POST', 'GET'])
def geo():
    param = {}
    param['main_title'] = 'География'
    param['first_title'] = 'Первый курс'
    param['second_title'] = 'Второй курс'
    param['third_title'] = 'Третий курс'
    param[
        'firstimg'] = 'https://sportishka.com/uploads/posts/2022-04/1650716759_24-sportishka-com-p-geografiya-krasivo-foto-30.jpg'
    param[
        'secondimg'] = 'https://sportishka.com/uploads/posts/2022-04/1650716725_58-sportishka-com-p-geografiya-krasivo-foto-68.jpg'
    param['thirdimg'] = 'https://gobigo.ru/wp-content/uploads/2021/09/545454llages.jpg'

    param['bgheadgrad'] = '-webkit-linear-gradient(45deg, rgb(226, 181, 25), rgb(222, 161, 27))'
    param['main_title_color'] = '#a65209'
    return render_template("lessons/lesson-page.html", **param)


@app.route('/info', methods=['POST', 'GET'])
def info():
    param = {}
    param['main_title'] = 'Информатика'
    param['first_title'] = 'Первый курс'
    param['second_title'] = 'Второй курс'
    param['third_title'] = 'Третий курс'
    return render_template("lessons/lesson-page.html", **param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
