import os
import sys
import myfile #импортирует модуль из той же папки
import names #импортируем модуль с именами и проект и запускает его
print('<--- Запуск программы--->') 
print(myfile.title +'\n')

print(sys.hash_info)
print ('Hello')
print(12+32434-343)
a = 3
print (a*3)
print ('test work')
from names import a, b, c, d, e, f, g, h, i, j #импортируем атрибуты из другого модуля без запуска модуля
print(a, b)

dir(names)
print(dir(names))
l=[1,2]
l.append(l)
print(l)
print('<--- Окончание программы--->') 
input('Для выхода нажмите ENTER') #чтобы окошко не исчезало сразу
