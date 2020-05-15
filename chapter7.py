# ISSaldikov@mephi.ru (c) IVAN SALDIKOV
# http://saldikov.com
# Исходинки для книги
# "Простой Python: современный стиль программирования", Билл Любанович
# Глава 7
# Работаем с данными профессионально

# Юникод
# \N{имя}:
# https://www.unicode.org/charts/charindex.html - charindex

# \u - и далее идут 4 16ричных кода символа из Юникод таблицы http://www.unicode.org/charts/

import unicodedata


def unicode_test(value):
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print('value="%s", name="%s", value2="%s"' %
          (value, name, value2))

unicode_test('A')
unicode_test('$')
unicode_test('\u00a2') # Символ валюты из юникод
unicode_test('\u20ac') # Ещё один символ валюты из юникод
unicode_test('\u2603') # Snowman

code_e = unicodedata.name('\u00e9')
print(code_e)
place = 'caf\u00e9'
print(place)
place2 = 'caf\N{LATIN SMALL LETTER E WITH ACUTE}'
print(place2)


snowman = '\u2603'
print(snowman)
print(len(snowman))
ds = snowman.encode('utf-8')
print(len(ds))
print(ds)
#ds = snowman.encode('ascii') # ERROR
print(snowman.encode('ascii', 'ignore'))
print(snowman.encode('ascii', 'replace'))
print(snowman.encode('ascii', 'backslashreplace'))
print(snowman.encode('ascii', 'xmlcharrefreplace'))

# декодирование - проблемы кодировок
place='caf\u00e9'
print(place)
print(type(place))
place_bytes = place.encode('utf-8')
print(place_bytes)
print(type(place_bytes))
place2 = place_bytes.decode('utf-8')
print(place2)
#place3 = place_bytes.decode('ascii')
#print(place3)
place4 = place_bytes.decode('latin-1')
print(place4)
place5 = place_bytes.decode('windows-1251')
print('place5=',place5)

# bit.ly/unicode-howto
# bit.ly/pragmatic-uni
# bit.ly/jspolsky


#ФОРМАТЫ
# Форматирование чисел
# Старый стиль форматирования чисел
print('%s' % 42) # строковой
print('%d' % 42) # десятичный
print('%x' % 42) # шестнадцатиричный
print('%o' % 42) # восьмиричный
print('%s' % 7.03) # строковой
print('%f' % 7.03) # с плавающей точкой (десятичный)
print('%e' % 7.03) # с плавающей точкой (шестнадцетиричный)
print('%g' % 7.03) # с плавающей точкой (восьмиричной)
print('%d%%' % 100) # отображаем проценты
n = 42
f = 7.03
s = 'string cheese'
print('%d %f %s' % (n, f, s))
# мин 10 символов для каждого, выравним по правому краю:
print('%10d %10f %10s' % (n, f, s))
# мин 10 символов для каждого, выравним по левому краю:
print('%-10d %-10f %-10s' % (n, f, s))
# мин 10 символов для каждого, выравним по правому краю, ограничим максимальную длину 4 символами
# (добавление 0 в недостающие позиции для целого числа, обрезка float до нужной длины, обрезка строки до нужной длины)
print('%10.4d %10.4f %10.4s' % (n, f, s))
# то же, но по левому краю
print('%.4d %.4f %.4s' % (n, f, s))
# получим длину полей из аргументов:
print('%*.*d %*.*f %*.*s' % (10,5,n,9,2,f,16,15,s))

# Новый стиль форматирования чисел
print('{} {} {}'.format(n,f,s))
print('{2} {0} {1}'.format(n,f,s))
print('{n} {f} {s}'.format(n=42,f=7.03,s='string cheese'))
d = {'n': 42, 'f': 7.03, 's': 'string cheese'}
print('{0[n]} {0[f]} {0[s]} {1}'.format(d, 'other'))
print('{2:s} {0:d} {1:f}'.format(n,f,s))
print('{n:d} {f:f} {s:s}'.format(n=42,f=7.03,s='string cheese'))
print('{2:10s} {0:10d} {1:10f}'.format(n,f,s))
# символы > делают выравнивание по правому краю более явным
print('{2:>10s} {0:>10d} {1:>10f}'.format(n,f,s))
# по левому краю
print('{2:<10s} {0:<10d} {1:<10f}'.format(n,f,s))
# выравнивание по центру
print('{2:^10s} {0:^10d} {1:^10f}'.format(n,f,s))
# форматирование строки (для digit-а не применяется)
print('{2:^10.4s} {0:^10d} {1:^10.4f}'.format(n,f,s))
# заполнить длину строки чем-то другим (восклицательным знаком)
print('{0:!^20s}'.format("BIG SALE"))
#... или ведущими нулями (вместо 10.4d)
print('{0:0>4s}'.format("42"))

# регулярные выражения
import re
source = 'Young Frankenstein'
m = re.match('You', source)
print(m)
youpattern = re.compile('You')
if m:
    print(m.group())
m = re.match('^You', source)  #якорь ^ означает то же самое - начало строки
if m:
    print(m.group())
m = re.match('Frank', source)  # матч работает только от начала строки, поэтому это не сработает:
if m:
    print(m.group())  # не выведет
m = re.search('Frank', source)
if m:
    print(m.group())  # а теперь выведет, потому что search работает по всей строке
m = re.match('.*Frank', source)
if m:
    print(m.group())  # выведет, потому что . означает любой символ, а * означает любое количество предыдущих символов
m = re.findall('n', source) # находим, сколько раз встречается n и заносим данные в лист
print(m) # выведет ['n', 'n', 'n', 'n']
print('Found', len(m), ' matches')
m = re.findall('n.', source) # Строка 'n', за которой следует любой символ
print(m) # выведет ['ng', 'nk', 'ns']
m = re.findall('n.?', source) # Строка 'n', за которой следует любой символ, ? - означает, что символ . - опционален
print(m) # выведет ['ng', 'nk', 'ns', 'n']
m = re.split('n', source)  # разбиение строки
print(m) # выведет ['You', 'g Fra', 'ke', 'stei', '']
m = re.sub('n', '?', source)  # поиск и замена в строке
print(m) # выведет You?g Fra?ke?stei?
'''
. - любой символ, кроме \n
Либое число, включая 0 - это *
Опциональное значение - это ?
\d - цифровой символ
\D - нецифровой символ
\w - буквенный или цифровой символ или знак подчеркивания
\W - любой сивол, кроме \w
\s - Пробельный символ
\S - Непробельный символ
\b - Граница слова
\B - Неграница слова
'''

import string
printable = string.printable
print(len(printable))
print(printable[0:50])
print(printable[50:])
# Какие символы в printable являются цифрами:
print(re.findall('\d', printable))
# Какие символы в printable являются буквенными или цифровыми символами или знаками подчеркивания:
print(re.findall('\w', printable))
x = 'abc'+'-/*'+'\u00ea'+'\u0115'
print(re.findall('\w', x))


# Табличка
'''
abc - буквосочетание abc
(expr) - expr
expr1 | expr2 - expr1 или expr2
. - любой символ, кроме \n
^ - начало строки источника
$ - конец строки источника
prev ? - ноль или одно включение prev
prev * - ноль или больше включений prev, максимальное количество
prev *? - ноль или больше включений prev, минимальное количество
prev + - одно или больше больше включений prev, максимальное количество
prev +? - одно или больше больше включений prev, минимальное количество
prev {m} - m последовательных включений prev
prev {m,n} - От m до n последовательных включений prev, максимальное количество
prev {m,n}? - От m до n последовательных включений prev, минимальное количество
[abc] - a, или b или с (аналогично a|b|c)
[^abc] - не(a, или b или с) (аналогично a|b|c)
prev (?= next) - prev, если за ним следует next
prev (? ! next) - prev, если за ним НЕ следует next
prev (? ! next) - prev, если за ним НЕ следует next
(?<=prev) next - next, если перед ним находится prev
(?<! prev) next - next, если перед ним НЕ находится prev
'''

source = '''I wish I may, I wish I might
... Have a dish of fish tonight.'''
# Найдем строку 'wish' во всем тексте
print(re.findall('wish',source))
# Найдем строку 'wish' или 'fish' во всем тексте
print(re.findall('wish|fish',source))
# Найдем строку 'I wish' в начале текста
print(re.findall('^I wish',source))
# Найдем строку 'fish' в конце текста
print(re.findall('fish$',source))
# Найдем строку 'fish tonight.' в конце текста
print(re.findall('fish tonight.$',source))
# Найдем строку 'fish tonight.' в конце текста, но уточним, что в конце именно точка, а не управляющий символ
print(re.findall('fish tonight\.$',source))
# Поиск w или f, за которыми следует буквенное сочетание 'ish'
print(re.findall('[wf]ish',source))
# Найдем одно или несколько сочетаний символов w, s и h:
print(re.findall('[wsh]+',source))
# Найдем сочетание ght, за которым следует любой символ, кроме буквенно или цифрового символа или занка подчеркивания
print(re.findall('ght\W',source))
# Найдем символ I, за которым следует сочетание wish
print(re.findall('I (?=wish)',source))
# Найдем сочетание wish, перед которым находится I
print(re.findall('(?<=I) wish',source))
# Но можно перепутать управляющий последовательности ругелярных выаржений и павилами для строк Python:
# Вывести любое слово, которое начинается с fish:
print(re.findall('\bfish',source)) # пусто, потому что \b говорит Python-у также "вовзрат на шаг"
# Поэтому нужно использовати чистые (raw) неформатированные строки:
print(re.findall(r'\bfish',source)) # будет работать норм


# Группировка вывода в отдельный кортеж при использовании match или search:
m = re.search(r'(. dish\b).*(\bfish)', source)
print(m.group())
print(m.groups())
# можно давать имя группам, заключая их в скобки: <>
m = re.search(r'(?P<DISH>. dish\b).*(?P<FISH>\bfish)', source)
print(m.group())
print(m.groups())
print(m.group('DISH'))
print(m.group('FISH'))

blist = [1,2,3,255]
the_bytes = bytes(blist)
print(the_bytes)
the_byte_array = bytearray(blist)
print(the_byte_array)
print(b'\x61')
print(b'\x01abc\xff')
#the_bytes[1] = 127 # нельзя - неизменяемый тип
the_byte_array[1] = 127
print(the_byte_array)
the_bytes = bytes(range(0,256))
the_byte_array = bytearray(range(0,256))
print(the_bytes)


# читаем PNG как бинарник
with open('_assets/O_Reilly_Media_logo.svg.png', 'rb') as f: # open the file in read binary mode
    data = f.read() # read the bytes from the file to a variable
message = data[0:30] #read 30 first bytes
print(message)
import struct
valid_png_header = b'\x89PNG\r\n\x1a\n'
data = message
if data[:8] == valid_png_header:
    # >LL указывает как интерпретировать байты и преобразовывать их в данные Python
    width, height = struct.unpack('>LL', data[16:24])
    print('Valid PNG, width=',width,', height=',height)
else:
    print('Not a valid PNG')
print(data[16:20])
print(data[20:24])
print('\x80')

# запаковывает числа в байтовую последовательность
print(struct.pack('>L', 154))
print(struct.pack('>L', 141))
print(struct.pack('>L', 1920))
print(struct.pack('>L', 417))
print(struct.unpack('>2L', data[16:24]))
# также можно пропустить несколько байтов, чтобы начать с определенной позиции (спецификатор x )
print(struct.unpack('>16x2L6x', data))


# то же, но с помощью пакета construct
from construct_legacy import Struct, Magic, UBInt32, Const, String
fmt = Struct('png',
             Magic(b'\x89PNG\r\n\x1a\n'),
             UBInt32('length'),
             Const(String('type', 4), b'IHDR'),
             UBInt32('width'),
             UBInt32('height'),
             )
result = fmt.parse(data)
print(result)
print(result.width, result.height)

# Преобразование байтов/строк с помощью функции binascee()
import binascii
bin16 = binascii.hexlify(valid_png_header)
print(bin16) # последовательность шестнадцатиричных значений
# в другую сторону тоже работает (теперь в виде ASCII-символов и управляющих последовательностей виде \x xx)
print(binascii.unhexlify(bin16)) # последовательность шестнадцатиричных значений


# битовые операции
a = 5 # в двоичной 0b0101
b = 1 # в двоичной 0b0001
'''
& - логическое И,  a & b, результат=1, двоичный результат=0b0001, оставляет только одинаоквые биты
| - логическое ИЛИ,  a | b, результат=5, двоичный результат=0b0101, оставляет те, где установлен хотя бы один бит
^ - исключающее ИЛИ,  a ^ b, результат=4, двоичный результат=0b0100, оставляет те, что в одном или в другом, но не в обоих
~ - инверсия битов,  ~a, результат=-6, двоичный результат зависит от размера типа int
            обращает порядок битов в одном аргументе (ну и меняет знак, потому что старший бит означает знак 1 - минус)
<< - сдвиг влево, a << 1, результат=10, 0b1010, просто свдигает влево все единички (аналогия умножению на 2)
>> - сдвиг вправо, a >> 1, результат=2, 0b0010, просто свдигает вправо все единички (аналогия делению на 2)
'''
c = a & b
print(c)
c = a | b
print(c)
c = a ^ b
print(c)
c = ~a
print(c)
c = a << 1
print(c)
c = a >> 1
print(c)
