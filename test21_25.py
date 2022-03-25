# оценка производительности функций
import time
from timer0 import timer

print(timer(pow,2,1000), end = ' сек\n')                                                        # время, затраченное на вызов pow(2, 1000) 1000 раз
print(timer(str.upper,'IaKrevedgo'), end = ' сек\n')                                            # время, затраченное на вызов 'IaKrevedgo'.upper 1000 раз

print('\n')
import timer                                                                                    # импортируем созданый для урока модуль
print(timer.total(1000, pow,2,1000)[0])                                                         # похоже на предыдущие результаты
print(timer.total(1000000, str.upper,'IaKrevedgo'))                                             # возвращает время и результат последнего вызова в верхнем регистре

print(timer.bestof(1000000, str.upper,'IaKrevedgo'))                                            # увеличил количество вызовов до 1000000 хоть видать что там что-то считается
print(timer.bestof(1000, pow, 2, 10000)[0])

print(timer.bestof(500, timer.total, 1000, str.upper, 'IaKrevedgo'))
print(timer.bestoftotal(500, 1000, str.upper, 'Put in'))


print(min(timer.total(10000, str.upper, 'Evergreen') for i in range(50)))




# Глава 22-23 МОДУЛИ
import sys
print(sys.path)

# 23
import module1                                                                                  # получать модуль как единое целое(один или больше)
module1.printer('Hackameda')                                                                    # уточняяем, чтобы получить имя

from module1 import printer                                                                     # импортируем конкретную функцию
printer('ZZZERRRRGGG')                                                                          # вызываем функцию с ее именем как в импортируемомм модуле

from module1 import *                                                                           # импортирует все имена и модуля. также будет работать printer('txt')


import simple                                                                                   # вызывает модуль и выполняет код файла
print(simple.spam)
simple.spam = 2
import simple                                                                                   # повторно модуль уже не загружается. код модуля повторно не выполняется
print(simple.spam)

print(list(name for name in module1.__dict__ if not name.startswith('__')))                     # моно вызвать все пространство имен с помощью ключей словаря


import changer
changer.printer()
changer.message = 'Qwerty'
changer.printer()
from imp import reload                                                                          # пишет что модуль imp будет удален в версии Python 3.12
reload(changer)
changer.printer()


# 24 глаАВА - ПАКЕТЫ МОДУЛЕЙ
import dir1.dir2.mod                                                                            # импортируем и сразу запускаем модуль mod.
import dir1.dir2.mod

from imp import reload 
reload (dir1)
reload(dir1.dir2)
dir1.dir2.mod

# 25 сокрытие данных в модулях
from unders import *                                                                            # испортируем все переменные из файла модуля Unders.py
print(a,c)                                                                                      # выводим значения переменных из файла модуля

import unders                                                                                   # имполртируем весь модуль и испольняем
print(unders._b)                                                                                # обращаемся к конктреной переменной конкретного модуля

from alls import *
print(a, _c)                                                                                    # выводит а и с
#print(b)                                                                                       # не выведет, так как в alls.py в параметре __all__ не указан

#from imp import reload                                                                         # пишет что модуль imp будет удален в версии Python 3.12
#reload(alls)
#print(a, b, _c, _d)
import tester
tester.tester()

import mins
import sys
print(sys.path)
sys.path.append('C:\\VM')                                                                       # добавляем новый путь для поиска модулей на текущуу сессию
print(sys.path)                                                                                 #