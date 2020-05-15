# ISSaldikov@mephi.ru (c) IVAN SALDIKOV
# http://saldikov.com
# Исходинки для книги
# "Простой Python: современный стиль программирования", Билл Любанович
# Глава 9
# Распутываем Всемирную паутину

# Стандартные вэб-библиотеки
import urllib.request as ur
#url = 'https://quotes.rest/qod?language=en'
url = 'https://google.com'
#req = ur.Request(url)  # можно если что указывать юрл и передавать хедер вместе с ним:
#req.add_header("x-rapidapi-key", "be4765af9amshb55d78aa4a590f5p1a83d5jsn699f795801bc")
conn = ur.urlopen(url)
print(conn)
data = conn.read()
print('Чтение данных:', data)
print('Статус ответа: ',conn.status)
print('Тип возвращаемого результата из заголовка ответа:', conn.getheader('Content-Type'))
print('Все заголовки, переданные вместе с ответом:')
for key, value in conn.getheaders():
    print(key, value)


# Библиотека requests: http://docs.python-requests.org/
import requests
# Предыдущий пример на основе requests
resp = requests.get(url)
print(resp)
print('Response:', resp.text)


# Простейший вэб-сервер:
#python -m http.server


# Фреймворк (сервер) под названием Bottle (http://bottlepy.org/docs/dev)
from bottle import route, run
@route('/')
def home():
    return "It isn't fancy, but it's my home page"
#run(hos='localhost', port=9999)

from bottle import route, run, static_file
@route('/new')
def main_new():
    return static_file('home.html', root='./templates')
#run(hos='localhost', port=9998)
@route('/echo/<thing>') # передаем параметр
def echo(thing):
    return "Say hello to my good friend: %s" % thing
#run(hos='localhost', port=9997, debug=True, reloader=True)




# Flask
from flask import Flask
app = Flask(__name__, static_folder='./templates', static_url_path='')
@app.route('/')
def home2():
    return app.send_static_file('home.html')
@app.route('/echo/<thing>')
def echo2(thing):
    return "Say hello to my very good friend: %s" % thing
#app.run(port=9996, debug=True)

from flask import render_template
app2 = Flask(__name__, template_folder='./templates')
@app2.route('/echo3/<thing>')
def echo3(thing):
    return render_template('flask.html', thing=thing)
#app2.run(port=9995, debug=True)


app3 = Flask(__name__, template_folder='./templates')
@app3.route('/echo4/<thing>/<place>')
def echo4(thing, place):
    return render_template('flask2.html', thing=thing, place=place)
#app3.run(port=9994, debug=True)


# Передача параметров через командную ?key1=val1&key2=val2...:
from flask import request
app4 = Flask(__name__, template_folder='./templates')
@app4.route('/echo5/')
def echo5():
    thing = request.args.get('thing')
    place = request.args.get('place')
    return render_template('flask2.html', thing=thing, place=place)
#app4.run(port=9993, debug=True)

# Передача параметров через dict и kwargs:
app5 = Flask(__name__, template_folder='./templates')
@app5.route('/echo6/')
def echo6():
    params= {}
    params['thing'] = request.args.get('thing')
    params['place'] = request.args.get('place')
    return render_template('flask2.html', **params)
app5.run(port=9993, debug=True)




