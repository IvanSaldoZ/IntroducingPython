# Процессы
import os
print(os.getpid())  # ID текущего процесса
print(os.getcwd())  # текущая рабочая папка
# print(os.getuid())  # ID текущего пользователя, ONLY for LINUX
# print(os.getgid())  # ID группы, ONLY for LINUX

import subprocess
# Выполнить команду
ret = subprocess.getoutput("dir")  # Команда выполнится и будед ждать завершение процесса
print(ret)

# Анализируем резльтат вывода:
ret = subprocess.getoutput('date -u | wc')
print(ret)

# Список команд и аргументов:
#ret = subprocess.check_output(['date', '-u'])
#print(ret)

# Получаем статус ответа, возвращаем кортеж (код_статуса, результат_работы):
# 0 = успешное выполнение программы
ret = subprocess.getstatusoutput('dir')
print(ret)

# Получаем только код статуса:
# Не работает на винде
#ret = subprocess.call('dir')
#print(ret)
#ret = subprocess.call(['date', '-u'])


