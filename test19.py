# РАСШИРЕННЫЕ ВОМОЖНОСТИ ФУНКЦИЙ

def mysum(L):
    print(L)                                                                        # можно опустить. Добавлен, чтобы видеть ка квсе происходит в функции
    if not L:
        return 0
    else:
        return L[0] + mysum(L[1:])                                                  # на каждом уровне функция вызывает сама себя пока не кочится L
    
print(mysum([1, 2, 3, 4, 5, 6]), mysum(range(100)))                                 # сумму можно элементами, можно ренджем список дать

def mysum2(L):                                                                      # то же, с помощью вложения
    print(L)
    return 0 if not L else L[0] + mysum2(L[1:])

print(mysum2([1,2,3,4,5,6,7,8,9]))                                                  # нужно указывать обязательно список

def mysum3(L):
    print(L)
    return L[0] if len(L) == 1 else L[0] + mysum3(L[1:])                            # в таком виде можно подсовывать любые типы данных,кроме пустых списков

print(mysum3([1,2,3,4,5,7]))
print(mysum3(['spam','Iakrevedgo','bugagag']))                                      # собирает символы вместе
print(mysum3(('s','p','a','m')))                                                    # собирает слово вместе

def mysum4(L):                                                                      # косвенная рекурсия
    if not L: return 0
    return noempty(L)                                                               # вызов функции noempty которая вызывает mysum4

def noempty(L):
    return L[0] + mysum4(L[1:])

print(mysum4([1.1,1.2,1.3,3,5]))



# рекрсия в цикле
L = [1, 2, 3, 4, 5]
sum = 0
while L:                                                                            # рекурсия в цикле
    sum += L[0]
    L = L[1:]
    
print(sum)

L = [1, 2, 3, 4, 5]
sum = 0
for x in L: sum += x                                                                # то же самое, только меньше писанины
print(sum)


# атрибуты и аннотации
def echo(message):                                                                  # имя эхо присваивается объект функций
    print(message)

echo('Iakrevedgo')                                                                  # выхов объекта через первоначальное имя

x = echo                                                                            # х также ссылается на функцию
x('Farwater')                                                                       # вызов объекта функции через добавление ()

def indirect(func, arg):
    func(arg)                                                                       # вызов переданного объекта петм добавления ()
indirect(echo, '!!Вызов функции из другой функции!!')                               # передача функции другой функции

kortec = [(echo, 'spam!'), (echo,'sdddfURCH')]                                      # объект помещен в кортеж
for (func, arg) in kortec:                                                          # распаковываем с помощью цикла
    func(arg)                                                                       # и выполняем как функцию и аргумент
    

def make(label):
    def echo(message):
        print(label + ':' + message)
    return echo

F = make('Iakrevedgo')                                                              # label в объемлющей области видимости предсохраняется
F('Glory')                                                                          # вызываем функции, возаращенной make
F('Urlich')

def func(a):
    b = 'spam'
    return b * a
print(func(8))

func.count = 0                                                                      # создаем произвольный атрибут, например таймер
func.count += 1
print(func.count)

func.handles = 'Button - press'
print(func.handles)
print(dir(func))                                                                    # новые атрибуты добавляются в конец списка

def f(): pass
print(dir(f))

def fuc(a, b, c):
    return a + b + c
print(fuc(1, 2, 3))

def fuc2(a:'spam', b:(1, 10), c:float) -> int:                                      # тут помимо аргументов еще прописаны аннотации
    return a + b + c
print(fuc2 (1, 2, 3))

print(fuc2.__annotations__)                                                         # чтобы посмотреть аннотации

def fuc3(a: 'IaKrevedgo' , b, c:float):
    return a + b + c

for arg in fuc3.__annotations__:                                                    # выводит аргумент и аннотацию к нему
    print(arg, '=>', fuc3.__annotations__[arg])


def fuc4(a:'IaKrevedgo', b=7, c:float=3):                                           # можно использовать и аннотации и стандартные значения
    return a + b + c
print(fuc4.__annotations__)   



# Анонимные функции: выражения lambda
def fuc5(x , y, z): return x + y + z
print(fuc5(2, 3, 4))

x = (lambda a = 'fff', b = 'aqwer', c='aqert': a + b + c)                           # присваиваем функцию переменой х. Можно присваивать станартные пе
print(x())                                                                          # исполнение со стандартными значениями
print(x(1, 2, 3))                                                                   # с новыми аргументами

def knights():
    title = 'sir'
    action = (lambda x: title + ' ' + x)                                             # title из области вдиимости объемлющео def
    
    return action

act = knights()
msg = act('robin')                                                                  # robin перадется аргументу x
print(msg)

L = [lambda x: x ** 2,
     lambda x: x ** 3,
     lambda x: x ** 4]                                                              # внутристрочное определнние функции. спсок из трех вызываемых функций

for f in L:
    print(f(2))

print(L[0](3))

key = 'got'
print({'already': (lambda: 2*2),
 'got': (lambda: 2*4),
 'one': (lambda: 2*3)}[key]())                                                      # выводит 8



def f1(): return 2 + 2                                                              # тоже выражение только с использованием def
def f2(): return 2 * 4
def f3(): return 2 ** 6

key = 'one'
print({'already': (lambda: 2*2),
 'got': (lambda: 2*4),
 'one': (lambda: 2*3)}[key]())

lower = (lambda x, y: x if x < y else y)                                            # lambda c условиями
print(lower('bb', 'aa'))

import sys

showfall = lambda x: list(map(sys.stdout.write, x))                                 # должен применятся список
t = showfall(['\nspamy\n','toast\n','eggs\n'])

showfall = lambda x: [sys.stdout.write(line) for line in x]                         # lambda с использованием цикла
t = showfall(['\nBrings\n','more\n','ideas\n'])

snowfall = lambda x: [print(line, end = ' ') for line in x]                         # то же самое тока с принтом
t = snowfall(['\nBrings','me','fire'])

showfall = lambda x: print(*x, sep = ' ', end = ' ')                                # то же самое
t= showfall(['\nKolya', 'Send', 'a', 'letter'])


# вложенное lambda
def action(x):                                                                                    
    return (lambda y: x + y)                                                        # создание и возвращение функции, запоминание x
act = action(99)                                                                    # аргумент х
print(act(78))                                                                      # аргумент у

action = (lambda x: (lambda y: x + y))                                              # то же с одной лямбда
act = action(99)
print(act(3))
x = (lambda x: (lambda y: x + y))(99)(3)                                            # то же сразу с присваиванием в переменную
print(x)




# зачатки графики
# ДЕЛАЕМ КНОПОЧКУ
'''
#import sys                                                                         # вызывалось ранее поэтому комментим
from tkinter import Button, mainloop
X = Button(                                                                         # по нажатию пишет текст в консоль
    text = ' Нажми меня ',
    command = (lambda:sys.stdout.write('IaKrevedgo\n')))
X.pack()
mainloop()                                                                          # в консольном режиме может быть необязательным
'''

counters = [1, 2, 3, 4, 5, 6]
updated = []
for x in counters:                                                                  # применить операцию ко всем элементам списка или таблицы
    updated.append(x * 11)
print(updated)



def inc(x):                                                                         # то же самое, только с функцией
    return x * 12

uplist = list(map(inc, counters))                                                   # создает список используюя функцию и значения
print(uplist)                                                     

uplist = list(map(lambda x: x + 10, counters))                                      # то же, с использованием lambda
print(uplist)

def mymap(func, seq):                                                               # функция вызывает функцию, подставляя аргументы
    res= []
    for x in seq: res.append(func(x))
    return res

print(list(map(inc,[1,2,3,4,5,6])))
print(mymap(inc, [1,2,3,4,5,6]))                                                    # то же, что и с использованием выше

print(pow(3,4))                                                                     # 3**4

print(list(map(pow, [1,2,3], [2,3,4])))                                             # 1**2, 2**3, 3**4
print([inc(x) for x in [1,2,3,4,5,6]])                                              # со списковым включением


#filter

print(list(range(-5,5)))
print(list(filter((lambda x: x > 0), range(-5,5))))                                 # filter условие, и итерируемый объект

res = []
for x in range(-5,5):                                                               # то же самое, но с использования цикла. filter быстрее и проще             
    if x > 0:
        res.append(x)
print(res)
                     
from functools import reduce

print(reduce((lambda x, y: x + y),[1, 2, 3, 4, 5]))
print(reduce((lambda x, y: x * y),[1, 2, 3, 4, 5]))                                 # вычисляет единственное значение, не вовращая список


L = [1, 2, 3, 4, 5]                                                                 # тоже, что и выше, только с помощью цикла
res=L[0]
for x in L[1:]:
    res = res + x
print(res)
    
import operator, functools

print(functools.reduce(operator.add,[2, 4, 6]))                                     # операция +б основанная на функции. сумма элементов справа








