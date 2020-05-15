# ISSaldikov@mephi.ru (c) IVAN SALDIKOV
# http://saldikov.com
# Исходинки для книги
# "Простой Python: современный стиль программирования", Билл Любанович
# Глава 6
# Ой-ой-ой: объекты и классы

# Создание класса
class Person():
    def __init__(self, name):
        self.name = name

hunter = Person('Elmer Fudd')
print('The mighty hunter: ', hunter.name)


# Наследование
class Car():
    def exclaim(self):
        return "I'am a Car!"

class Yugo(Car):
    def exclaim(self):
        return "I'am a Yugo!"
    def need_a_push(self):
        return "A little help here?"

give_me_a_car = Car()
give_me_a_yugo = Yugo()

print(give_me_a_car.exclaim())
print(give_me_a_yugo.exclaim())
print(give_me_a_yugo.need_a_push())


class MDPerson(Person):
    def __init__(self, name):
        self.name = "Doctor " + name

class JDPerson(Person):
    def __init__(self, name):
        self.name = name + ". Esquire"

person = Person('Fudd')
doctor = MDPerson('Fudd')
lawyer = JDPerson('Fudd')
print(person.name)
print(doctor.name)
print(lawyer.name)

class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email

bob = EmailPerson('Bob Frapples', 'bob@frapples.com')

print(bob.name)
print(bob.email)


# self - это объект класса, который передается как параметр метода. Например, можно сделать так:
car = Car()
print(Car.exclaim(car))


# свойства атрибута name для класса утки
class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    # геттер
    def get_name(self):
        print ('inside the getter')  # каждый раз будет вызываться этот код при получении имени
        return self.hidden_name
    # сеттер
    def set_name(self, input_name):
        print ('inside the setter') # каждый раз будет вызываться этот код при задании имени
        self.hidden_name = input_name

    # это атрибут класса, который также является свойством
    name = property(get_name, set_name)



fowl = Duck('Howard')
print(fowl.name)
fowl.name = 'Daffy'

# То же самое, но с помощью декораторов:
class Duck2():
    def __init__(self, input_name):
        self.hidden_name = input_name
    @property
    def name(self):
        print('inside the getter 2')
        return self.hidden_name
    @name.setter
    def name(self, input_name):
        print('inside the setter 2')
        self.hidden_name = input_name

fowl = Duck2('Howard')
print(fowl.name)
fowl.name = 'Daffy'

class Circle():
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return 2 * self.radius

c = Circle(5)
print(c.radius)
print(c.diameter)
c.radius = 7
print(c.radius)
print(c.diameter)
#will not work:
# c.diameter = 20



# То же самое, но с помощью декораторов:
class Duck3():
    def __init__(self, input_name):
        self.__name = input_name
    @property
    def name(self):
        print('inside the getter 3')
        return self.__name
    @name.setter
    def name(self, input_name):
        print('inside the setter 3')
        self._name = input_name

fowl = Duck3('Howard')
print(fowl.name)
fowl.name = 'Daffy'
#print(fowl.__name)

print('Real:'+fowl._Duck3__name)

class A():
    count = 0
    def __init__(self):
        A.count += 1
    def exclaim(self):
        return "I'm an A!"
    @classmethod
    def kids(cls):
        return "A has "+str(cls.count)+" little objects."

easy_a = A()
breezy_a= A()
wheezy_a = A()
print(A.kids())



# Утиная типизация - полиморфизм в Python
class Quote():
    def __init__(self, person, words):
        self.person = person
        self.words = words
    def who(self):
        return self.person
    def says(self):
        return self.words + '.'

class QuestionQuote(Quote):
    def says(self):
        return self.words + '?'

class ExclamationQuote(Quote):
    def says(self):
        return self.words + '!'

hunter = Quote('Elmer Fudd', "I'm hunting wabbits")
print(hunter.who(), 'says: ', hunter.says())
hunter1 = QuestionQuote('Bugs Bunny', "Whats up, doc")
print(hunter1.who(), 'says: ', hunter1.says())
hunter2 = ExclamationQuote('Duffy Duck', "Its rabbit season")
print(hunter2.who(), 'says: ', hunter2.says())

class BabbingBrook():
    def who(self):
        return "Brook"
    def says(self):
        return 'Bable'

brook = BabbingBrook()

def who_says(obj):
    print(obj.who(), 'says', obj.says())

who_says(hunter)
who_says(hunter1)
who_says(hunter2)
who_says(brook)


class Word():
    def __init__(self, text):
        self.text = text

    def equals(self, word2):
        return self.text.lower() == word2.text.lower()

    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()

    def __str__(self):
        return self.text

    def __repr__(self):
        return 'Word("'+self.text+'")'

first = Word('ha')
second = Word('HA')
third = Word('eh')

print(first.equals(second))
print(first.equals(third))

# а дальше проверка идет с помощью магического метода __eq__
print(first == second)
print(first == third)


print(Word('HAAA'))
print(first)


# Композиция классов
class Bill():
    def __init__(self, description):
        self.description = description

class Tail():
    def __init__(self, length):
        self.length = length

class Duck():
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail
    def about(self):
        print('This duck has a ', self.bill.description, 'bill and a ',
              self.tail.length, 'tail')

tail = Tail('long')
bill = Bill('wide orange')
duck = Duck(bill, tail)

print(duck.about())


# именнованные кортежи
from collections import namedtuple
Duck = namedtuple('Duck', 'bill tail')
duck = Duck('wide orange', 'long')
print(duck)
print(duck.bill)
print(duck.tail)

# именнованный кортеж можно сделать на основе словаря:
parts = {'bill': 'wide orange', 'tail': 'long'}
duck2 = Duck(**parts)
print(duck2)

duck3 = duck2._replace(tail='magniicent', bill = 'crushing')
print(duck3)

duck_dict = {'bill': 'wide orange', 'tail': 'long'}
print(duck_dict)
duck_dict['color'] = 'green'
print(duck_dict)


# Купил новую клаву
class Test():

    def __init__(self, name):
        self.name = name
        print("Cool!", name)

    def __str__(self):
        return self.name




# Упражнения
class Thing():
    pass
print(Thing)
example = Thing()
print(example)

class Thing2():
    letters = 'abc'
print(Thing2.letters)

class Thing3():
    def __init__(self):
        self.letters = 'xyz'

class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def __str__(self):
        return 'name=%s, symbol=%s, number=%s' % (self.name, self.symbol, self.number)

        

hydrogen = Element('Hydrogen', 'H', 1)
print(hydrogen)
hydrogen_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
hydrogen = Element(**hydrogen_dict)
print(hydrogen.name)


# Версия с закрытыми атрибутами
class Element():
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    @property
    def name(self):
        return self.__name
    @property
    def symbol(self):
        return self.__symbol
    @property
    def number(self):
        return self.__number


hydrogen = Element('Hydrogen', 'H', 1)
print(hydrogen.name)
print(hydrogen.symbol)
print(hydrogen.number)

# Задание 9
# Класс животное
class Animal:
    def eats(self):
        pass

class Bear(Animal):
    def eats(self):
        return "berries"

class Rabbit(Animal):
    def eats(self):
        return "clover"

class Octothorpe(Animal):
    def eats(self):
        return "campers"

bear = Bear()
rabbit = Rabbit()
octothrpe = Octothorpe()

print(bear.eats())
print(rabbit.eats())
print(octothrpe.eats())


# 10-е задание
class Laser:
    def does(self):
        return "disintegrate"

class Claw:
    def does(self):
        return "crush"

class SmartPhone:
    def does(self):
        return "ring"

class Robot:
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smart_phone = SmartPhone()

    def does(self):
        return ('laser does %s, claw does %s, smart_phone does %s...' % (self.laser.does(), self.claw.does(), self.smart_phone.does()))

laser = Laser
claw = Claw
smart_phone = SmartPhone
robot = Robot()
print(robot.does())