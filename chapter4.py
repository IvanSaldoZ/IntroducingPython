# ISSaldikov@mephi.ru (c) IVAN SALDIKOV
# http://saldikov.com
# Исходинки для книги
# "Простой Python: современный стиль программирования", Билл Любанович
# Глава 4
# Корочка Python: структуры кода


# Книга ""
#zip-тест, что он возвращает

days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']

for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day, ": drink", drink,"eat", fruit,"enjoy",dessert)

print(list(zip(days, fruits, drinks, desserts)))


#------------------------------
# обычный синтаксис создания списков
number_list = []
for number in range(1,6):
    number_list.append(number)
print(number_list)


# специальный синтаксис создания списков
number_list_new = list(number-1 for number in range(1,6))
number_list_new2 = [number**2 for number in range(1,6)]
print(number_list_new)
print(number_list_new2)


# двойная проходочка
rows = range(1,4)
cols = range(1,3)
cells = [(row, col) for row in rows for col in cols]
for cell in cells:
    print(cell)


# для словаря
word = 'letter'
letters_count = {letter: word.count(letter) for letter in word}
print(letters_count)

# для множества:
a_set = {number for number in range(1, 6) if number % 3 ==1 }
print(a_set)

# для кортежа (круглые скобки вместо квадратных и фигурных) не существует такого включения for.. in..
# зато появляются генераторы, по которым можно итерироваться
list_number_generator = (number for number in range(1, 6))
print(list_number_generator)
for number in list_number_generator:
    print(number)
try_again = list(list_number_generator)
print(try_again)

def echo(str):
    '''
    Показывает строку. Введена для почитателей PHP :)
    :param str: строка для отображения
    :return: возвращает строку отображения
    '''
    print(str)

echo('test')
help(echo)


# Замыкания
def knights2(saying):
    def inner2():
        return "We are the knights who say: '%s'" % saying
    return inner2

a = knights2("Hello!")
b = knights2("Hey!")
print(type(a))
print(a)
print(a())


#lambda
stairs = ['Meou', 'Augh', 'Shhhh']
def edit_story(words, func):
    for word in words:
        print(func(word))

edit_story(stairs, lambda word: word.capitalize() + '!')

# свой генератор
def my_ranger(begin = 1, end = 10, step = 1):
    i = begin
    while i < end:
        yield i
        i += step

ranger = my_ranger(1, 5, 1)
for x in ranger:
    print(x)


# декораторы
def document_it(func): # задокументируем функцию
    def new_function(*args, **kwargs):
        print("Name of called function:",func.__name__)
        print("Позиционные аргументы:",args)
        print("Keywords arguments:",kwargs)
        result = func(*args, **kwargs)
        print("Result:",result)
        return result
    return new_function

def add_ints(a,b):
    return a + b
print(add_ints(8,5))
cooled_add_ints = document_it(add_ints)
cooled_add_ints(8,5)

@document_it
def subst_ints(a,b):
    return a - b
print(subst_ints(9,7))

def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result*result
    return new_function

@document_it
@square_it
def addints2(a,b):
    return a + b
print(addints2(4,2))


# локальные и глобальные переменные
def local_func():
    #global days
    #days = ['Friday']  # если не указать явно, то это локальная переменная
    print(globals())
    print(locals())
    days = ['Wednesday']
    print(globals())
local_func()



# упражнения
guess_me = 7
if guess_me < 7:
    print('too_low')
elif guess_me > 7:
    print('too_high')
elif guess_me == 7:
    print('just right')


guess_me = 5
start = 1
while True:
    if start < guess_me:
        print('too_low')
    elif start > guess_me:
        print('oops')
        break
    elif start == guess_me:
        print('found it!')
        break
    start += 1


for x in [3,2,1,0]:
    print(x)

new_list = [number for number in range(10) if number % 2 == 1]
print(new_list)

squares = {number: number**2 for number in range(10)}
print(squares)

# множество четных чисел:
odd = {number for number in range(10) if number % 2 == 0}
print(odd)

for x in ('Got %s' % number for number in range(10)):
    print(x)

def good():
    return ['Harry', 'Ron', 'Hermione']

def get_odds():
    for number in range(1, 10, 2):
        yield number
#print(list(get_odds()))
for count, number in enumerate(get_odds(), 1): # enumerate возвращает пару номер-значение для итерируемых объектов
    if count == 3:
        print('Third number is %s' % number)


def test(func):
    def new_function(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result
    return new_function

@test
def greetings():
    print('Greetings, Earth!')

greetings()


class OoopsException(Exception):
    pass

#raise OoopsException()

try:
    raise OoopsException()
except OoopsException:
    print("Oops exception")


title = ['Creature a Habit', 'Crewel Fate']
plots = ['A num turns into a monster', 'A haunted yarn shop']
new_dict = dict(zip(title,plots))
print(new_dict)