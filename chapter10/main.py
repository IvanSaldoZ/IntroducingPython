import os
import stat
if os.path.exists('oops.txt'):
    os.chmod('oops.txt', stat.S_IRUSR + stat.S_IWUSR)
    #os.chmod('oops.txt', 0o600)  # Права на чтение и запись юзером


# Создаем файл с помощью функции open()
fout = open('oops.txt', 'wt')
print('Oops, I created a file', file=fout)
fout.close()

import os
# Проверяем существование файла
print(os.path.exists('oops.txt'))
print(os.path.exists('./oops.txt'))
print(os.path.exists('waffles'))
print(os.path.exists('.'))
print(os.path.exists('..'))
print('----------')

# Проверяем тип с помощью функции isfile()
name = 'oops.txt'
print(os.path.isfile(name))
print(os.path.isdir(name))
print(os.path.isdir('.'))
print(os.path.isdir('..'))
print('----------')

# Проверяем, задан ли абсолютный путь до файла
print(os.path.isabs(name))
print(os.path.isabs('/big/fake/name'))
print(os.path.isabs('big/fake/name/without/leading/slash'))
print('----------')

# Копируем файл
import shutil
shutil.copy('oops.txt', 'ohno.txt')
shutil.move('ohno.txt', 'new_file.txt')
# Переименовываем:
import os
if os.path.isfile('renamed_file.txt'):
    os.remove('renamed_file.txt')
os.rename('new_file.txt', 'renamed_file.txt')

print('----------')
# Далее идут команды только для UNIX-систем

# Создаем ссылки с помощью link() или symlink()
if os.path.isfile('yikes.txt'):
    os.remove('yikes.txt')
os.link('oops.txt', 'yikes.txt')
print(os.path.isfile('yikes.txt'))
print(os.path.islink('yikes.txt'))
# Если ссылка, то мы это узнаем:
print(os.path.realpath('yikes.txt'))


#os.symlink('oops.txt','jeepers.txt')
#print(os.path.islink('jeepers.txt'))
os.chmod('oops.txt', 0o600)

# Меняем владельца файла (uid) или идентификатор группы (gid)
uid = 5
gid = 22
#os.chown('oops.txt', uid, gid)

# Получаем абсолютный путь до файла:
print(os.path.abspath('oops.txt'))

# Удаляем файл с помощью функции remove
os.remove('oops.txt')
print(os.path.exists('oops.txt'))


print('----------')
# Создаем каталог с помощью функции mkdir:
if not os.path.exists('poems'):
    os.mkdir('poems')
print(os.path.exists('poems'))
# Удаляем каталог:
#os.rmdir('poems')
#print(os.path.exists('poems'))
#if not os.path.exists('poems'):
#    os.mkdir('poems')
# Отображаем содержимое каталога:
print('Содержимое каталога poems:',os.listdir('poems'))
if not os.path.exists('poems/mcintyre'):
    os.mkdir('poems/mcintyre')
print(os.listdir('poems'))
fout = open('poems/mcintyre/the_good_main', 'wt')
fout.write("""

THIS IS A TEXT!!!

ANOTHER ONE

""")
fout.close()
print(os.listdir('poems/mcintyre'))


# Меняем каталоги:
os.chdir('poems')
print(os.listdir('.'))


# Функция glob для поиска файлов по маске:
# Получим все файлы и каталоги, имена которых начинаются с буквы m
import glob
print('glob func, starts with m:', glob.glob('m*'))
# Как насчет файлов и каталогов с именами, состоящими из двух символов?
print('glob func, couple symbols:', glob.glob('??'))
# Слово из восьми символов, начинающееся с m и заканчивающееся на e?
print('glob func, eight symbols starts with m and end with e:', glob.glob('m??????e'))
# Что-то, что начинается с букв k,l, или m и заканчивающееся на букву e
print('glob func, eight symbols starts with or k,l,m and end with e:', glob.glob('[klm]*e'))