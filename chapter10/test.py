# Задания
# 1 Текущая дата и время как строка в файл today.txt
from datetime import datetime
now = datetime.now()
with open('today.txt', 'wt') as f:
    #f.write(str(now))
    # или
    print(str(now), file=f)


# 2. Читаем файл и записываем в переменную
with open('today.txt', 'rt') as f:
    today_string = f.read()
print(today_string)

# 3. Разберите дату из строки today_string
from datetime import datetime, date
fmt = '%Y-%m-%d %H:%M:%S'
# 2020-05-07 02:22:22.774588 отбрасываем после точки
today_string = today_string.split('.')[0]
get_date = datetime.strptime(today_string, fmt)
print(get_date.date())

# 4. Вывести содержание текущего каталога:
import os
print(os.listdir('.'))

# 5. Вывести содержимое родительского каталога:
import os
print(os.listdir('..'))

# 6. multiprocessing


# 7. Создайте объект date, содержащий дату вашего рождения
from datetime import date
my_birth = date(1988, 6, 5)
print(my_birth)

# 8. В какой день недели Вы родились?
print(my_birth.isoweekday())  # 7й - это Воскресенье ;)

# 9. Когда Вам будет (или уже было) 10 000 дней от роду?
from datetime import timedelta
date10000 = timedelta(days=10000) + my_birth
print(date10000)


