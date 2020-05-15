# Даты-календарь
import calendar
print(calendar.isleap(2000))  # Високосный ли год


# Модуль datetime
import datetime
print(datetime.date)  # Для годов, месяцев и дней
print(datetime.time)  # для часов, минут, секунд и долей секунды
print(datetime.datetime)  # Для работы с датой и временем одновременно
print(datetime.timedelta)  # дли интервалов даты и/или времени
from datetime import date
halloween = date(2014, 10, 31)
print('halloween=', halloween)
print(halloween.day)
print(halloween.month)
print(halloween.year)
print(halloween.isoformat())  # В Python3 это по умолчанию
now = date.today() # Сегодняшняя дата:
print(now)
from datetime import timedelta # timedelta
one_day = timedelta(days=1)  # Формируем дельту
tomorrow = now + one_day
print('Завтрашняя дата', tomorrow)
print(now + 14*one_day)
yesterday = now - one_day
print('Вчерашняя дата:', yesterday)
# Максимальное-минимальное значение:
print('Минимальное значение:', date.min)
print('Максимальное значение:', date.max)

from datetime import time
noon = time(12, 0, 0)  # Полдень
print('Полдень:', noon)
print(noon.hour)
print(noon.minute)
print(noon.second)
print(noon.microsecond)
from datetime import datetime
some_day = datetime(2020,1,2,3,4,5,6)
print('Какой-то день:', some_day)
now = datetime.now()
print('Сейчас:', now)
print('Сейчас (ISO-формат):', now.isoformat())
print('Текущий год:',now.year)
print('Текущий месяц:',now.month)
print('Текущий день:',now.day)
print('Текущий час:',now.hour)
print('Текущая минута:',now.minute)
print('Текущая секунда:',now.second)
print('Текущая микросекнда:',now.microsecond)
# Объединение date и time в datetime
from datetime import datetime, time, date
noon = time(12)
this_day = date.today()
noon_today = datetime.combine(this_day, noon)
print('Сегодня в полдень: ', noon_today)
# Разделение datetim на date и time
print('Разделение date():', noon_today.date())
print('Разделение time():', noon_today.time())
print('----------------------------')


# Модуль time (но это не тот модуль из модуля datetime):
# ПУТАНИЦА ;)
# time работает с временем epoch - количеством секунд от полуночи 1 января 1970го года
import time
now = time.time()  # Текущее время epoch
print('Текущее время epoch:',now)
# преобразуем строку epoch в строку нормального времени (gmtime() и localtim())
# лучше использовать всегда UTC, потому что это абсолютное время
print(time.ctime(now))
print('Текущее время с учетом моего часового пояса (структура struct_time): ', time.localtime())
print('Текущее время UTC (структура struct_time): ', time.gmtime())
# конвертируем обратно в epoch (mktime):
tm = time.localtime(now)
print(time.mktime(tm))

# Преобразование epoch в строку по формату
import time
fmt_usa = "It's %A, %B %d, %Y, local time %I:%M:%S %p"
fmt_rus = "It's %A, %d.%m.%Y, local time %H:%M:%S"
t = time.localtime()
print("Структура:", t)
print("По формату:", time.strftime(fmt_rus, t))

import time
fmt = "%Y-%m-%d"
#print(time.strptime("2020 01 29", fmt))  # ERROR, потому что пробелы вместо дефисов
print(time.strptime("2020-01-29", fmt))  # OK!
#print(time.strptime("2020-13-29", fmt))  # OK, но лучше так не делать, ничего не выведится

# Изменение локалей для отображения дня недели и месяца
import locale
from datetime import date
halloween = date(2014, 10, 31)
for lang_country in ['en_us', 'fr_fr', 'de_de', 'es_es', 'is_is', 'ru_ru']:
    locale.setlocale(locale.LC_TIME, lang_country)
    print(halloween.strftime('%A, %B %d'))


# Получаем все локали:
import locale
names = locale.locale_alias.keys()
# работает с setlocale только те коды, где два символа кода языка и два символа страны
good_names = [name for name in names if len(name) == 5 and name[2] == '_']
print(good_names)
# все локали Германии:
de = [name for name in good_names if name.startswith('de')]
print(de)