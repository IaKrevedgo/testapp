# Включения и генераторы

print(ord('s'))                                                                                 # вывожит код для элемента

res = []
for x in 'Iakrevedgo':
    res.append(ord(x))                                                                          # в пустой список ложим коды элементов
print(res)

res = list(map(ord,'Iakrevedgo is rule'))                                                       # то же с помощью List
print(res)
res = [ord(x) for x in 'Iakrevedgo']                                                            # то же с помощью спискового включения
print(res)
print([x**2 for x in range(4)])                                                                 # каждый шаг цикла выводит по значению в список
print(list(map((lambda x: x ** 2), range(4))))                                                  # то же, только с помощью lambda

print([x for x in range(5) if x % 2 == 0])                                                      # списковое включение с циклом и условием
print(list(filter((lambda x: x%2 == 0), range(5))))                                             # то же выражение, только с помощью Lambda

res =[]                                                                                         # то же с помощь цикла
for x in range(5):
    if x % 2 == 0:
        res.append(x)
        
print([x ** 2 for x in range(10) if x % 2 == 0])                                                # квадарты числе с пропуском нечетных

res = [x + y for x in [0, 1, 2] for y in [100, 200, 300]]                                       # два цикла в выражениии
print(res)

res = []
for x in [0, 1, 3]:                                                                             # то же выражение только двумя циклами
    for y in [100, 200, 300]:
        res.append(x + y)                                                                       # добавить элемент в список res
print(res)        

print([x + y for x in 'IAK' for y in 'iak'])                                                    # можно использовать со строками

print([x + y + z for x in 'spam'if x in 'sm'                                                    # три цикла в выражении для трех элементов
                for y in 'SPAM' if y in ('P', 'A')
                for z in '123' if z > '1'])
print([(x, y) for x in range(5) if x % 2 == 0 for y in range(5) if y % 2 == 0])

M = [[1,2,3],
     [4,5,6],
     [7,8,9]]
N = [[2,2,2],
     [3,3,3],
     [4,4,4],]
print(M[1])                                                                                     # обращение к матрице
print(M[1][2])                                                                                  # обращение к элементу матрицы (эдементы и столбцы начнаются с 0)

print([row[1] for row in M])                                                                    # обращение ко второму столбцу
print([M[row][1] for row in (0, 1, 2)])                                                         # использование смещений

print([M[i][i] for i in range(len(M))])                                                         # выводит диагональ матрицы
print([M[i][len(M) -1-i] for i in range(len(M))])                                               # обратная диагональ

L = [[1,2,3],[4,5,6]]
for i in range(len(L)):
    for j in range(len(L[i])):                                                                  # обновление на месте
        L[i][j] += 10
print(L)

print(open('myfile.py').readlines())                                                            # читаем весь файл построчно
print([line.rstrip() for line in open('myfile.py').readlines()])                                # читаем весь файл построчно и убираем символы \n
print(list(map((lambda line: line.rstrip()), open('myfile.py'))))                               # то же самое, только с map и lambda

listoftuple = [('bob', '35','mgr'),('den','30','pgr')]
print([age for (name, age, job) in listoftuple])                                                # циклом разбиваем на элементы списка и выводим age
print(list(map((lambda row: row[1]), listoftuple)))                                             # тоже самое с map и row



# ГЕНЕРАТОРЫ ФУНКЦИИ И ВЫРАЖЕНИЯ
def gensquares(N):
    for i in range(N):
        yield i ** 2                                                                            # позже возобносвить здесь
        
for i in gensquares(5):                                                                         # возобновление выполнение функции
    print(i, end = ' : ')                                                                       
    
x = gensquares(5)

print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

def buildsquares(n):
    res = []
    for i in range(n): res.append(i ** 2)
    return res
for x in buildsquares(5): print(x, end = ' : ')                                                 # вывод квадратов с помощью функции

for x in [n**2 for n in range(5)]:                                                              # то же самое с помощью спискового включения и без фцункции
    print(x, end = ' : ')

def ups(line):                                                                                  # генератор подстрок
    for sub in line.split(','):
        yield sub.upper()

tuple(ups('aaa,bbb,ccc'))                                                                       # все контексты

{i: s for (i, s) in enumerate (ups('aaa,bbb,ccc'))}

print('\n')
def gen():                                                                                      # созддаем йункцию с использованием генератора
    for i in range(10):
        X = yield i
    print(X)
G = gen()                                                                                       # присваиваем функцию переменной
print(next(G))                                                                                  # сначала должен запускаться next

print(G.send(77))                                                                               # продвигается вперед и отправляет значение генератору yield
print(G.send(88))

print(next(G))



# генераторные выражения
print([x ** 2 for x in range(10)])                                                              # в квадратных скобках строит список
print((x ** 2 for x in range(10)))                                                              # в круглых скобка создает генераторное выражение

print(list(x**2 for x in range(10)))                                                            # при помещении в list выдет уже список

G = (x **2 for x in range(10))                                                                  # присваиваем генераторное выражение пресменной
print(next(G))                                                                                  # теперь G можно итерировать
print(next(G))  
print(next(G))  
print(next(G))  

for num in (x **2 for x in range(10)):                                                          # цикл, который сразу эмилирует выхов next(x)
    print('%s , %s' % (num, num / 2.0))

print(''. join(x.upper() for x in 'aaa,bbb,ccc'.split(',')))                                    # объеденяем и выводим в верхнем регистре

a, b, c = (x + '\n' for x in 'aaa, bbb,ccc'.split(','))
print(a, c)

print(sum(x**2 for x in range(4)))                                                              # сумма значений генераторного выражения
print(sorted(x ** 2 for x in range(4)))                                                         # вывод отсортировнного списка генератора                                                         
print(sorted((x ** 2 for x in range(4)), reverse=True))                                         # вывод отсортированного списка с реверсом значений

print(list(map(abs, (-1,-2,-3,4))))                                                             # отображает функцию на кортеж
print(list(abs(x) for x in (-1,-2,-3,5)))                                                       # генераторное выражение
print(list(map(lambda x: x*2, (1,2,3,4))))                                                      # с помощью lambda
print(list(x*2 for x in (1,2,3,4)))                                                             # самое простое с помощью генератора

import math
print(list(map(math.sqrt, (x**2 for x in range(4)))))                                           # ывложенные комбинации квадратный корень из авыражения 2 степени

print(list(abs(x)*2 for x in (-1, -2, -3, -4)))                                                 # генераторы без вложения
print(list(math.sqrt(x ** 2)for x in range(4)))                                                 # без map

line = 'aa bbb c'
print(''.join(x for x in line.split() if len(x) > 1))                                           # условия в генераторах. Объеденить и вывести строки длина которых больше 1('с' не подходит)
print(''.join(filter (lambda x: len(x)> 1, line.split())))                                      # тоже самое только с Lambda

res = ''
for x in line.split():                                                                          # почти тоже самое только с циклом. Писаныны больше, но читабельнеее
    if len(x) > 1:
        res += x.upper()
print(res)


#генераторные функциии и выражения
G = (c *4 for c in 'SPAM')                                                                      # генераторное выражение в круглых скобках
print(list(G))                                                                                  # выводим результат с помощью list

def timefour(S):                                                                                # генераторная функция
    for c in S:                                                                                 # больше писанины, но больше функционала
        yield c * 4
G = timefour('SPAM')
print(list(G))       

G = (c *4 for c in 'SPAM')                                                                      # используем выражение
I = iter(G)                                                                                     # итерация вручную
print(next(I))  
print(next(I))  

G = timefour('spam')                                                                            # используем функцию
I = iter(G)                                                                                     # итерациия вручную
print(next(I))
print(next(I))

print('\n')
G = (c*4 for c in 'SPAM')
I1 = iter(G)                                                                                    # создаем первый генератор
print(next(I1))
print(next(I1))
I2 = iter(G)                                                                                    # второй генератор остается в той же позиции, что и первый
print(next(I2))
I3 = iter(G)
print(next(I3))                                                                                 # все генераторы будут израсходованны и чтобы начать заново нужно создать новый генератор

I3 = (c*4 for c in 'spam')
print(next(I3))

def timefour1(S):
    for c in S:
        yield c * 4
G = timefour1('spam')                                                                           # генераторная функция таким же образом
iter(G) is G
I1, I2 = iter(G), iter(G)                                                                       # запускаем новые генераторы
print(next(I1))
print(next(I1))
print(next(I2))                                                                                 # использует тот же самый генератор

L = [1,2,3,4]
I1, I2 = iter(L), iter(L)
print(next(I1))
print(next(I1))
print(next(I2))                                                                                 # со списками работает по другому. Каждый список отдельная итерация

del L[2:]                                                                                       # изменения отражаются в итераторах
#  print(next(I1))                                                                              # тут выдаст ошибку так как список закончился


def both(N):                                                                                    # функция использует 2 генератора
    for i in range(N): yield i
    for i in (x**2 for x in range(N)): yield i
    
print(list(both(5)))

def both1(N):                                                                                   # те же тапки, тольько с использованием yield from
    yield from range(N)
    yield from (x**2 for x in range(N))

print(list(both1(5)))

print(' : '.join(str(i) for i in both1(5)))                                                     # используем генераторную функцию



D = {'a':1, 'b':2, 'c':3}
x = iter(D)
print(next(x))
print(next(x))

for key in D:
    print(key, D[key])
    
for line in open('inter2.py'):
    print(line, end = '')


import os

for (root, subs, files) in os.walk('.'):                                                        # генератор инструмента
    for name in files:
        if name.startswith('test'):                                                             # проходит по всем каталогам и подкаталогам начиная с текущего и выдает все файлы, наинающиеся на test
            print(root, name)

def f(a, b, c): print('%s, %s and %s' %(a, b, c))
f(0, 1, 2)            
f(*range(3))                                                                                    # дает тот же результат 0, 1 and 2
f(*(i for i in range(3)))                                                                       # тот же результат, но с распаковкой


L, S = [1,2,3],'spam'
for i in range(len(S)):                                                                         # цикл по перемешиванию последовательности строк
    S = S[1:]+ S[:1]
    print(S, end = ' ')
for i in range(len(L)):                                                                         # цикл по перемешиванию последовательности чисел
    L = L[1:]+L[:1]
    print(L, end = ' ')
    
for i in range(len(S)):                                                                         # тот же самый эффект
    X = S[i:] + S[:i]
    print(X, end = ' ')
    
def scramble(seq):                                                                              # вместо циклов делаем функцию, которая будет работать с любым оъектом
    res = []
    for i in range(len(seq)):
        res.append(seq[i:]+seq[:i])
    return res
print(scramble('IaKrevedgo'))

def scramble1(seq):                                                                             # то же самое только со списковым включением. от себя добавил сразу print
    return print([seq[i:]+seq[:i] for i in range(len(seq))])
scramble1('fire')

for x in scramble((1,2,3)):                                                                     # тут используем первую функцию
    print(x, end = '')


def scramble2(seq):                                                                             # генераторная функция
    for i in range(len(seq)):
        seq = seq[1:]+seq[:1]
        yield seq
print(list(scramble2('spam')))

def scramble3(seq):                                                                             #          
    for i in range(len(seq)):
        yield seq[i:]+seq[:i]
print(list(scramble3('spam')))
print(list(scramble3((1,2,3))))                                                                 # подходит любой тип данных

print(S)
G = (S[i:]+S[:i] for i in range(len(S)))                                                        # то же самое, только генераторным выражением
print(list(G))

F = lambda seq: (seq[i:] + seq[:i] for i in range(len(seq)))                                    # то же самое, с помощью lambda
print(list(F(S)))

#тут мы созддали файл sramble.py и туда запихали функции генератора описанные выше

from scrambler import scramblef                                                                 # импортируем функцию генератора из стороннеого модуля
from inter2 import intersect, union                                                             # импортируем функцию из модуля описанного в 18 главе

def tester(func, items, trace=True):
    for args in scramble(items):                                                                # использовать генератор (или scramble(items))
        if trace: print(args)
        print(sorted(func(*args)))

tester(intersect,('abbaa','bbbcdbaa','cccsdda'))

from permute import permute1, permute2                                                          # импортируем функции из еще одного модуля созданоого по этой главе

print(list(scramble('abc')))                                                                    # простое перемешивание
print(list(permute1('abc')))
print(list(permute2('abc')))

for x in permute2('abc'): print(x)                                                              # выводит 6 итераций


import math
print(math.factorial(10))
seq = list(range(10))
p1 = permute1(seq)
p2 = permute2(seq)
print(next(p2))
print(next(p2))
#p2 = list(permute2(seq))
#print(p2)                                                                                      # генерирует огромный сипсок перестоновок около 10 сек



import random
print(math.factorial(20))
seq = list(range(20))
random.shuffle(seq)                                                                             # перетасовывает последовательность
p = permute2(seq)
print(next(p))
print(next(p))

random.shuffle(seq)
p = permute2(seq)
print(next(p))
print(next(p))
