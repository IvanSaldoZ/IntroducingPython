# ISSaldikov@mephi.ru (c) IVAN SALDIKOV
# http://saldikov.com
# Исходинки для книги
# "Простой Python: современный стиль программирования", Билл Любанович
# Глава 8
# Данные нужно куда-то сохранять
poem = '''There was a young lady named Bright.
Whose speed was far faster than light;
She set out one day
In a relative way.
And returned on the previous night.'''
print(len(poem))
relfilename = '_assets/chapter8/relativity'
fout = open(relfilename, 'wt')
#mode: r-read, w-write, x-записывать только, если ещё нет файла, a-add (дописывать существующий файл)
#mode (2й символ): t (или отсутсвует) - текстовой файл, b - бинарынй режим записи
fout.write(poem)
fout.close()
fout = open(relfilename, 'wt')
print(poem, file=fout, sep='', end='')
fout.close()
# запись частями
fout = open(relfilename, 'wt')
size=len(poem)
offset=0
chunk = 100
while True:
    if offset > size:
        break
    fout.write(poem[offset:offset+chunk])
    offset+=chunk
fout.close()
try:
    fout = open(relfilename, 'xt')  # Ошибка, файл уже существует!
    fout.write('stomp stomp stomp')
except FileExistsError:
    print('ERROR: relativity is already exists! That was a close one.')


# чтение файла
fin = open(relfilename, 'rt')
poem = fin.read()
fin.close()
print(len(poem))

# Но если файл слишком большой, то лучше его читать с помощью буфера
poem = ''
fin = open(relfilename, 'rt')
chunk = 100
while True:
    fragment = fin.read(chunk)
    if not fragment:
        break
    poem += fragment
fin.close()
print(len(poem))

# Также можно воспользоваться функцией readline, чтобы читать построчно
poem = ''
fin = open(relfilename, 'rt')
while True:
    line = fin.readline()
    if not line:
        break
    poem += line
fin.close()
print(len(poem))

# использование итератора
poem = ''
fin = open(relfilename, 'rt')
for line in fin:
    poem += line
fin.close()
print(len(poem))

# readlineS
fin = open(relfilename, 'rt')
lines = fin.readlines()
fin.close()
print(len(lines), 'lines read')
for line in lines:
    print(line, end='')
print('\n')

# БАЙТЫ
# Запись байтов в файл
bdata = bytes(range(0,256))
print(len(bdata))
bfilename = '_assets/chapter8/bfile'
fout = open(bfilename, 'wb')
print(fout.write(bdata))
fout.close()

# Записываем бинарные данные частями
fout = open(bfilename, 'wb')
size = len(bdata)
offset = 0
chunk = 100
while True:
    if offset > size:
        break
    print(fout.write(bdata[offset:offset+chunk]))
    offset += chunk
fout.close()

# Читаем бинарные данные
fin = open(bfilename, 'rb')
bdata = fin.read()
print(len(bdata))
fin.close()


# Менеджеры контекста (Context managers)
with open(relfilename, 'wt') as fout:
    print(fout.write(poem))


# Курсор путешествует по файлу (seek и tell)
fin = open(bfilename, 'rb')
print(fin.tell())
fin.seek(255)  # Переходим к последнему байту
bdata = fin.read()
print(len(bdata))
print(bdata[0])

# seek(offset, origin)
# origin = 0 (по умолчанию) - смещение от начала файла
# origin = 1 - смещение от с текущей позиции
# origin = 2 - смещение от с конца файла

import os
print(os.SEEK_SET)  # 0
print(os.SEEK_CUR)  # 1
print(os.SEEK_END)  # 2

fin = open(bfilename, 'rb')
print(fin.seek(-1, 2))
print(fin.tell())
bdata = fin.read()
print(len(bdata))
print(bdata[0])
fin = open(bfilename, 'rb')
print(fin.seek(254, 0))
print(fin.tell())
print(fin.seek(1,1))
print(fin.tell())
bdata = fin.read()
print(len(bdata))
print(bdata[0])


#CSV
import csv
villains = [['Doctor', 'No'], ['Rosa', 'Klebb'], ['Mister', 'Big'], ['Auric', 'Goldfinger'], ['Ernst', 'Blofeld'],]
csvfile = '_assets/chapter8/villains.csv'
with open(csvfile, 'wt') as fout:  # Контекстный менеджер
    csvout = csv.writer(fout)
    csvout.writerows(villains)

with open(csvfile, 'rt') as fin:
    cin = csv.reader(fin)
    villains = [row for row in cin]  # здесь используется включение списка
print(villains)


# Можно записывать результат чтения в переменную типа словаря
with open(csvfile, 'rt') as fin:
    cin = csv.DictReader(fin, fieldnames=['first', 'last'])
    villains = [row for row in cin]
print(villains)

villains = [
    {'first': 'Doctor', 'last': 'No'},
    {'first': 'Rosa', 'last': 'Klebb'},
    {'first': 'Mister', 'last': 'Big'},
    {'first': 'Auric', 'last': 'Goldfinger'},
    {'first': 'Ernst', 'last': 'Blofeld'},
]
with open(csvfile, 'wt') as fout:
    cout = csv.DictWriter(fout, ['first', 'last'])
    cout.writeheader()
    cout.writerows(villains)

with open(csvfile, 'rt') as fin:
    cin = csv.DictReader(fin)
    villains = [row for row in cin]
print(villains)


#XML
# XML Tree: http://bit.ly/elementtree
import xml.etree.ElementTree as et
xmlfile = '_assets/chapter8/menu.xml'
tree = et.ElementTree(file=xmlfile)
root = tree.getroot()
print(root.tag)
for child in root:
    print("tag:",child.tag, 'attributes:', child.attrib)
    for grandchild in child:
        print("\ttag:", grandchild.tag,'attributes:',grandchild.attrib)
print(len(root)) # количество разделов root
print(len(root[0])) # количество элементов breakfast
'''
Есть еще пара модулей для работы с xml:
1. Модуль xml.dom - представляет xml в виде DOM-дерева, но загружает сразу его в память, поэтому не подходит для больших XML-файлов
2. Модуль xml.sax - разбирает XML на ходу, поэтому хорошо подходит для больших потоков xml
'''


#JSON
menu = \
    {
        "breakfast": {
            "hours": "7-11",
            "items": {
                "buritos": "$6.00",
                "pancakes": "$4.00"
            }
        },
        "lunch": {
            "hours": "11-3",
            "items": {
                "hamburger": "$5.00"
            }
        },
        "dinner": {
            "hours": "3-10",
            "items": {
                "spaghetti": "$8.00"
            }
        }
    }
import json
menu_json = json.dumps(menu)
print(menu_json)

menu2 = json.loads(menu_json)
print(menu2)

import datetime
now = datetime.datetime.utcnow()
print(now)
# json.dumps(now) --- ОШИБКА

now_str = str(now)
print(json.dumps(now_str))
from time import mktime
now_epoch = int(mktime(now.timetuple()))
json.dumps(now_epoch)

class DTEncoder(json.JSONEncoder):
    def default(self, obj):
        # instance() проверяет тип объекта
        if isinstance(obj, datetime.datetime):
            return int(mktime(obj.timetuple()))
        # в ином случае нормальные декодер работает
        return json.JSONEncoder.default(self, obj)

print(json.dumps(now, cls=DTEncoder))
print(type(now))
print(isinstance(now, datetime.datetime))
print(type(234))
print(isinstance(234, int))
print(type('hey'))
print(isinstance('hey', str))


#YAML
import yaml
with open('_assets/chapter8/mcintyre.yaml', 'rt') as fin:
    text = fin.read()
data = yaml.load(text, Loader=yaml.FullLoader)
print(data['details'])
print(len(data['poems']))
print(data['poems'][1]['title']) #заголовок второго стихотворения

# Безопасность
# https://bitbucket.org/tiran/defusedxml
from xml.etree.ElementTree import parse #insecure
et = parse(xmlfile)
print(et)
from defusedxml.ElementTree import parse #protected
et = parse(xmlfile)
print(et)


# Конфигурационные файлы (.ini)
import configparser
cfg = configparser.ConfigParser()
cfg.read('_assets/chapter8/settings.cfg')
print(cfg['french'])
print(cfg['french']['greetings'])
print(cfg['files']['bin'])


# Другие форматы обмена данными
#Бинарные обмен
# MsgPack (http://msgpack.org)
# Protocol Buffers (https://code.google.com/p/protobuf/)
# Avro (http://avro.apache.org/docs)
# Thrift (htp://thrift.apache.org)
'''
import msgpack
res = msgpack.packb([1, 2, 3], use_bin_type=True)
print(res)
print(msgpack.unpackb(res, raw=False))
print(msgpack.unpackb(b'\x93\x01\x02\x03', use_list=False, raw=False))  # To tuple
import umsgpack
res=umsgpack.packb({u"compact": True, u"schema": 0})
print(res)
print(umsgpack.unpackb(res))
'''



#pickle
import pickle
import datetime
now1 = datetime.datetime.utcnow()
pickled = pickle.dumps(now1)
now2 = pickle.loads(pickled)
print(now1)
print(now2)

class Tiny():
    def __str__(self):
        return 'tiny'
obj1 = Tiny()
print(obj1)
print(str(obj1))
pickled = pickle.dumps(obj1)  # бинарная строка с объектом нашего класса Tiny
print(pickled)
obj2 = pickle.loads(pickled)
print(obj2)
print(str(obj2))

#HDF5 (http://www.hdfgroup.org/why_hdf)
# Модули для работы с HDF5
# h5py - http://www.h5py.org/
# PyTables - http://www.pytables.org


    #SQLite
dbname = '_assets/chapter8/enterprise.db'
import sqlite3
conn = sqlite3.connect(dbname)
curs = conn.cursor()
sql_query = '''CREATE TABLE zoo
(critter VARCHAR(20) PRIMARY KEY ,
count INT,
damages FLOAT)'''
#curs.execute(sql_query)
curs.execute('INSERT INTO zoo VALUES("duck", 5, 0.0)')
curs.execute('INSERT INTO zoo VALUES("bear", 2, 1000.0)')
# более безопасный способ добавить данные
ins = 'INSERT INTO zoo (critter, count, damages) VALUES (?, ?, ?)'
curs.execute(ins, ('weasel', 1, 2000.0))
curs.execute('SELECT * FROM zoo')
rows = curs.fetchall()
print(rows)
curs.execute('SELECT * FROM zoo ORDER BY count')
print(curs.fetchall())
# Сортировка по количеству животных
curs.execute('SELECT * FROM zoo ORDER BY count DESC')
print(curs.fetchall())
# Самое дорогое животное
curs.execute('''SELECT * FROM zoo WHERE damages= (SELECT MAX(damages) FROM zoo)''')
print(curs.fetchall())
# Закрываем курсор и соединение
curs.close()
conn.close()

# MySQL
# MySQL Connector, http://bit.ly/mysql-cpdg - mysql-connector-python, mysql.connector
# PyMySQL,  https://github.com/petehunt/PyMySQL/ - pymysql, pymysql
# oursql,  http://pythonhosted.org/oursql - oursql, oursql
# Только для 2.7 MysqlBD (http://sourceforge.net/projects/mysql-python)


# PostgreSQL
# psycopg2, http://initd.org/psycopg, psycopg2, psycopg2
# py-postgresql, http://python.projects.pgfoundry.org, py-postgresql, postgresql


# SQLAlchemy - http://www.sqlalchemy.org
# Уровень движка
import sqlalchemy as sa
conn = sa.create_engine('sqlite://')
conn.execute('''CREATE TABLE zoo
(critter VARCHAR(20) PRIMARY KEY,
count INT,
damages FLOAT
)
''')
ins = 'INSERT INTO zoo (critter, count, damages) VALUES (?, ?, ?)'
conn.execute(ins, 'duck', 10, 0.0)
conn.execute(ins, 'bear', 2, 1000.0)
conn.execute(ins, 'weasel', 1, 2000.0)
rows = conn.execute('SELECT * FROM zoo')
print(rows)
for row in rows:
    print(row)
# Язык выражений SQL
import sqlalchemy as sa
conn = sa.create_engine('sqlite://')
meta = sa.MetaData()
zoo = sa.Table('zoo', meta,
               sa.Column('critter', sa.String, primary_key=True),
               sa.Column('count', sa.Integer),
               sa.Column('damages', sa.Float),
               )
meta.create_all(conn)
conn.execute(zoo.insert(('bear', 2, 1000.0)))
conn.execute(zoo.insert(('weasel', 1, 2000.0)))
conn.execute(zoo.insert(('duck', 10, 0)))
result = conn.execute(zoo.select())
rows = result.fetchall()
print(rows)

# ORM SQLAlchemy
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

conn = sa.create_engine('sqlite:///zoo.db')
Base = declarative_base()
class Zoo(Base):
    __tablename__ = 'zoo'
    critter = sa.Column('critter', sa.String, primary_key=True)
    count = sa.Column('count', sa.Integer)
    damages = sa.Column('damages', sa.Float)
    def __init__(self, critter, count, damages):
        self.critter = critter
        self.count = count
        self.damages = damages
    def __repr__(self):
        return "<Zoo({}, {}, {})>".format(self.critter, self.count, self.damages)

Base.metadata.create_all(conn)
first = Zoo('duck', 10, 0.0)
second = Zoo('bear', 2, 1000.0)
third = Zoo('weasel', 1, 2000.0)
print(first)

# беседуем с БД
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=conn)
session = Session()
session.add(first)
session.add_all([second, third])
#session.commit()



### NO SQL Базы данных
## DBM - семейство
import dbm
from datetime import datetime
db = dbm.open('_assets/chapter8/definitions', 'c')
db['mustard'] = 'yellow'
db['time'] = str(datetime.utcnow())
db['my_name'] = 'Ivan'
print(len(db))
print(db['time'])
db.close()
db = dbm.open('_assets/chapter8/definitions', 'r')
print(db['time'])



### Memcached
# Для работы нужно либо скачать сервер Memcached, либо использовать сервер из
# поставки OpenServer
import memcache
db = memcache.Client(['127.0.0.1:11211'])
db.set('marco', 'polo')
print(db.get('marco'))
print(db.set('duck', 0))
print(db.get('duck'))
print(db.incr('duck', 2))  # увеличиваем счетчик на 2
print(db.get('duck'))


### Redis
import redis
conn = redis.Redis('localhost', 6379)
print(conn.keys('*'))
conn.set('secret', 'ni!')
conn.set('carats', 24)
conn.set('fever', '101.5')
print(conn.get('secret'))
print(conn.get('carats'))
print(conn.get('fever'))
print(conn.setnx('secret', 'will not added because it is already exists'))
print(conn.get('secret'))
# getset возвращает старое значение и устанавливает новое
print(conn.getset('secret', 'new secret'))
print(conn.get('secret'))
print(conn.getrange('secret', -5, -1))
conn.setrange('secret', 0, 'old')  # заменяем начиная с нуля на строку old
print(conn.get('secret'))
# устанавливаем сразу несколько значений:
print(conn.mset({'pie': 'cherry', 'cordial': 'sherry'}))
# получим более одного значения, используя mget
print(conn.mget(['fever', 'carats']))
print(conn.delete('fever'))
# Выполним инкремент с помощью команд incr() и inrcbyfloat() и декремент с помощью комнды dect()
print(conn.incr('carats'))
print(conn.incr('carats', 10))
print(conn.decr('carats'))
print(conn.decr('carats', 15))
print(conn.set('fever', '101.5'))
print(conn.incrbyfloat('fever'))
print(conn.incrbyfloat('fever', 0.5))
print(conn.incrbyfloat('fever', -0.5))

# Redis-списки
print(conn.lpush('zoo', 'bear'))  # Список zoo, содержащий элемент bear
print(conn.lpush('zoo', 'alligator', 'duck'))  # добавляем в начало списка более одного элемента
print(conn.lrange('zoo', 0, -1))  # Выводим список zoo в диапазоне по индексам (-1 - это последний)
print(conn.linsert('zoo', 'before', 'bear', 'beaver')) # добавляем beaver ДО bear
print(conn.linsert('zoo', 'after', 'bear', 'cassowary'))  # добавляем cassowary ПОСЛЕ bear
print(conn.lrange('zoo', 0, 26))  # Выводим список zoo в диапазоне по индексам
# Добавим элемент, указав смещение для него
conn.lset('zoo', 2, 'marmoset')
print(conn.lrange('zoo', 0, 26))  # Выводим список zoo в диапазоне по индексам
print(conn.rpush('zoo', 'yak'))  # можно добавить в конец списка
print(conn.lrange('zoo', 0, 26))  # Выводим список zoo в диапазоне по индексам
print(conn.lindex('zoo', 3))
print(conn.ltrim('zoo', 1, 1))  # обрезать все элементы, кроме указанного диапазона

# Redis - хэши
print(conn.hmset('song', {'do': 'a deer', 're': 'about a deer'}))  # установка пары полей в хэше song
print(conn.hset('song', 'mi', 'a note to follow me'))  # установка одного поля в хэше song
# получаем значение одного поля с помощью метода hget():
print(conn.hget('song', 'mi'))
# Получаем значения нескольких полей с помощью метода hmget():
print(conn.hmget('song', 're', 'do'))
# Получаем ключи всех полей хэша:
print(conn.hkeys('song'))
# Получаем значениях всех ключей поля хэша:
print(conn.hvals('song'))
# Получим количество полей хэша с помощью функции:
print(conn.hlen('song'))
# Получим ключи и их значения для хэша:
print(conn.hgetall('song'))
# Создаем поле, если его ключ не существует:
print(conn.hsetnx('song', 'fa', 'a note that rhymes with la'))

# Множества Redis:
conn.sadd('zoo_new', 'duck', 'goat', 'turkey') # Добавим одно или несколько значений множества:
print(conn.scard('zoo_new'))  # Кол-во значений множества
# Получим все значения множества:
print(conn.smembers('zoo_new'))
# Удалим значение из множества:
print(conn.srem('zoo_new', 'turkey'))
# Создадим второе множество, чтобы продемонстрировать некоторые операции:
conn.sadd('better_zoo', 'tiger','wolf','duck')
# Пересечение множества (получение общих членов):
print(conn.sinter('zoo_new', 'better_zoo'))
# ...то же, но ещё сохраняем результат в новое множество
print(conn.sinterstore('fowl_zoo', 'zoo_new', 'better_zoo'))
print(conn.smembers('fowl_zoo'))
# Выполним объединение (всех членов) множества zoo_new и better_zoo
print(conn.sunion('zoo_new', 'better_zoo'))
# и сохраняем
print(conn.sunionstore('fabulous_zoo', 'zoo_new', 'better_zoo'))
print(conn.smembers('fabulous_zoo'))
# Какие элементы присутствуют в множестве zoo_new и отсутствуют в множестве better_zoo?
print(conn.sdiff('zoo_new', 'better_zoo'))

# Redis - упорядоченные множества
import time
now = time.time()
print(now)
# Добавим первого гостя
conn.zadd('logins', {'smeagol': now})
# 5 минут спустя добавим второго гостя:
conn.zadd('logins', {'sauron': now+(5*60)})
# через два часа
conn.zadd('logins', {'bilbo': now+(2*60*60)})
# через сутки:
conn.zadd('logins', {'threebeard': now+(24*60*60)})
# Каким по счету пришел Бильбо?
print(conn.zrank('logins', 'bilbo'))
# Когда это было?
print(conn.zscore('logins', 'bilbo'))
# Посмотрим, каким по счету пришел каждый гость:
print(conn.zrange('logins', 0, -1))
# И когда:
print(conn.zrange('logins', 0, -1, withscores=True))

# Redis-биты
days = ['2020-02-25', '2020-02-26', '2020-02-27', ]  # Даты статистики посещений
big_spender = 1089 # ID пользователя big_spender = 1089
tire_kicker = 40459
late_joiner = 550212

#Удобно и быстрее использовать биты:
# В первую дату наш сайт посетило 2 человека
conn.setbit(days[0], big_spender, 1)
conn.setbit(days[0], tire_kicker, 1)
# на следующий день, первый пользователь опять зашел
conn.setbit(days[1], big_spender, 1)
# на третий день снова биг сендер посетил сайт... и ещё один новый юзер:
conn.setbit(days[2], big_spender, 1)
conn.setbit(days[2], late_joiner, 1)
# Получим счетчик ежедневных посещений за эти три дня:
for day in days:
    print(conn.bitcount(day))

# Посещал ли сайт заданный пользователь в указанный день?
print(conn.getbit(days[1], tire_kicker))
print(conn.getbit(days[1], big_spender))

# Сколько пользователей посещает сайт каждый день?
print(conn.bitop('and', 'everyday', *days))
print(conn.bitcount('everyday'))
print(conn.getbit('everyday', big_spender))

# Сколько уникальных пользователей посетили сайт за эти три дня?
print(conn.bitop('or', 'alldays', *days))
print(conn.bitcount('alldays'))

# REDIS - Кэши и истечение срока действия:
import time
key = 'test key'
conn.set(key, 'not to long')
conn.expire(key, 5) # через 5 секунд уничтожить ключ
print(conn.ttl(key))
print(conn.get(key))
#time.sleep(6)
print(conn.get(key))



# MongoDB - может обойти ограничение Redis по объему оперативной памяти (потому что работает с объемом данных,
# который могут превышать объем оперативной памяти компьютера)



# Упражениния

#1
test1 = 'This is a test of the emergency text system'
f = open('_assets/chapter8/test.txt', 'w')
f.write(test1)
f.close()

#2
f = open('_assets/chapter8/test.txt', 'r')
test2 = f.read()
f.close()
print(test2)
print(test1==test2)

#3
csv_text = '''author,book
JRR Tolkien,The Hobbit
Lynne Truss,"Eats, Shoots & Leaves"'''
csv_file_name = '_assets/chapter8/task4.csv'
with open(csv_file_name, 'w') as fin:
    fin.write(csv_text)
#4
import csv
with open(csv_file_name, 'r') as fin:
    books = csv.DictReader(fin)
    for book in books:
        print(book)

#5
csv_text = '''title,author,year
The Weirdstone of Brisingamen,Alan Graner,1960
Perdido Street Station,China Mieville,2000
Thud!,Terry Pratchett,2005
The Spellman Files,Lisa Lutz,2007
Small Gods,Terry Pratchett,1992'''
csv_file_name = '_assets/chapter8/task5.csv'
with open(csv_file_name, 'w') as fin:
    fin.write(csv_text)

#6
dbname = '_assets/chapter8/books.db'
conn = sqlite3.connect(dbname)
cursor = conn.cursor()
sql = '''CREATE TABLE books
(title TEXT,
author TEXT,
year INT)'''
#sql = 'DROP TABLE books'
#cursor.execute(sql)
#conn.commit()
#7
import csv
with open('_assets/chapter8/task5.csv', 'r') as fin:
    books1 = csv.DictReader(fin)
    for book in books1:
        ins = 'INSERT INTO books VALUES (?, ?, ?)'
        #cursor.execute(ins, (book["title"], book["author"], int(book["year"])))
        print(book["title"], ' was added successfully')
#conn.commit()

#8
# Вывод в алфавитном порядке с помощью нативного драйвера SQLite3
sql_query = 'SELECT title FROM books ORDER BY title ASC'
answer = cursor.execute(sql_query)
for book in answer.fetchall():
    print(book)

# Чтобы не учитывать в сортировке "The"
sql_query = '''SELECT title FROM books ORDER BY
CASE WHEN (title like "The %") THEN SUBSTR(title, 5) ELSE title END'''
answer = cursor.execute(sql_query)
for book in answer.fetchall():
    print(book[0])

#9
# Вывод по годам
sql_query = 'SELECT * FROM books ORDER BY year ASC'
a = cursor.execute(sql_query)
for book in a.fetchall():
    #print(book)
    print(*book, sep=', ')

#10
# Вывод в алфавитном порядке с помощью SQLAlchemy
import sqlalchemy as sa

conn = sa.create_engine('sqlite:///_assets/chapter8/books.db')
sql_query = 'SELECT title from books ORDER BY title ASC'
a = conn.execute(sql_query)
for book in a:
    print(book)

#11
# Редис, сохранить хэш
import redis
r = redis.Redis('localhost')
r.hmset('test', {'count':1, 'name':'Faster Besterterster'})
print(r.hgetall('test'))

#12
print(r.hincrby('test', 'count'))
print(r.hget('test', 'count'))