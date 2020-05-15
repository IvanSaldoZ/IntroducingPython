# ISSaldikov@mephi.ru (c) IVAN SALDIKOV
# http://saldikov.com
# Исходинки для книги
# "Простой Python: современный стиль программирования", Билл Любанович
# Глава 5
# Py Boxes: модули, пакеты и программы

import sys
print('Input arguments: ', sys.argv)

for place in sys.path:
    print(place)

# Значения по умолчанию для словаря
periodic_table = {'Hydrogen': 1, 'Helium': 2}
print(periodic_table)
carbon = periodic_table.setdefault('Carbon', 12)
print(periodic_table)
helium = periodic_table.setdefault('Helium', 977)
print(helium)

# Создание значение по умолчанию для словаря
from collections import defaultdict
periodic_table = defaultdict(int)
periodic_table['Hydrogen'] = 1
print(periodic_table['Lead'])


def no_idea():
    return 'Huh?'

bestiary = defaultdict(no_idea)
bestiary['A'] = 'Abominable Snowman'
bestiary['B'] = 'Basilisk'
print(bestiary['C'])
bestiary2 = defaultdict(lambda: 'What?')
print(bestiary2['E'])


# Можно подсчитывать количество элементов
food_counter = defaultdict(int)
for food in ['spam','spam','spam','eggs']:
    food_counter[food] += 1

for food, count in food_counter.items():
    print(food, count)
print(type(food_counter))


from collections import Counter
breakfast_counter = Counter(food_counter)
breakfast_counter.most_common()
print(breakfast_counter)
lunch = ['eggs', 'eggs', 'bacon']
lunch_counter = Counter(lunch)
print(lunch_counter)
print(breakfast_counter + lunch_counter)
print(breakfast_counter - lunch_counter)
print(lunch_counter - breakfast_counter )
print(breakfast_counter & lunch_counter)
print(lunch_counter | breakfast_counter )



# Ищем является ли слово полиндромом (одинаково читается в с обеих сторон)
def palindrome(word):
    from collections import deque
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True

print(palindrome('a'))
print(palindrome('racecar'))
print(palindrome(''))
print(palindrome('radar'))
print(palindrome('halibut'))



#itertools
import itertools  # Итерируемся по значениям объектов, которые переданы внутрь функци модуля itertools
for item in itertools.chain([1,2], ['a', 'b']):
    print(item)  # Выведет все значения и ему все равно, что передано
for item in itertools.accumulate([1,2,3,4]):
    print(item)
def multiply(a,b):
    return a*b
for item in itertools.accumulate([1,2,3,4], multiply):
    print(item)


#Pretty print
from pprint import pprint
from collections import OrderedDict
quotes = OrderedDict([
    ('Moe', 'A wise guy, huh?'),
    ('Larry', 'Ow!'),
    ('Curly', 'Nyuk nyuk!'),
])
print(quotes)
pprint(quotes)


# Управжениния
plain = {"a": 1, "b": 2, "c": 3}
print(plain)
fancy = OrderedDict(plain)
print(fancy)
dict_of_lists = defaultdict(list)
dict_of_lists['a'].append('something for a')
print(dict_of_lists['a'])