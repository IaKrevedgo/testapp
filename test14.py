import os


#Цикл фор работает с разными типами данных
for x in [1, 2, 3, 4]:
    print(x**2, end = ' ')
for x in (1, 2, 3, 4):
    print(x**3, end = ' ')
for x in 'spam':
    print(x * 2, end = ' ')    
    
print('\n')
print(open('script2.py').read())                            # открываем весь файл целиком для чтения
f = open('script2.py')
print(f.readline())                                         # открываем файл построчно
print(f.readline())                                         # открывается следуюязая строка файла для чтения

print('\n')
f = open('script2.py')
print(f.__next__())                                         # тоже самое с использованием метода __next__
print(f.__next__())
print(f.__next__())
print(f.__next__())
#print(f.__next__())                                        # этой строки нет, поэтому программа останавливает

for line in open('script2.py'):                             # читаем по одной строке из файла и выводим в верхнем регистре
    print(line.upper(), end = ' ')

print('\n')    
f = open('script2.py')    
while True:                                                 # тоже самое тока с циклом while
    line = f.readline()                                     # читаем строку
    if not line:                                            # если строки закончились то выходим из цикла
        break
    print(line.upper(), end = '')                           # отображаем все в верхнем регистре убирая в конце строки \n

print('\n')     
f = open('script2.py')
print(f.__next__())
print(f.__next__())

print('\n')                                                 # то же что и выше, но с использованием универсального методоа next
f = open('script2.py')
print(next(f))
print(next(f))

L= [1, 2, 3]
I = iter(L)                                                 # получение объекта итератора из итерируемого объекта
print(next(I))                                              # вывод первого элемента итерации
print(next(I))                                              # вывод следующего элемента итерации

f = open('script2.py')
print(iter(f) is f)                                         # файлы являются итераторами по умолчанию
print(iter(f) is f.__iter__())

L = [1, 2, 3]                                               # списки не являются
print(iter(L) is L)                                         # выдет фалсе

L = [1, 2, 3]                                               # итерация вручную с помощью цикла    
for X in L:
    print(X ** 2, end = ' ')
    
I = iter(L)
while True:
    try:                                                    # пытаемся выполнить с использованием исключений
        X = next(I) 
    except StopIteration:                                   # если прилетело исключение выходим из цикла а не рубим программу
        print('Список закончился')
        break
    print(X ** 22, end = ' ')



D = {'a': 1, 'b': 2, 'c': 3}                                # по циклу вытаскиваем ключи и значенияиз словаря
for key in D.keys():
    print(key, D[key])

I = iter(D)                                                 # словарь является итерируемым объектом
print(next(I))                                              # вытаскиваем ключи с помощью iter и next
print(next(I))

P = os.popen('dir')
print(P.__next__())                                         # next(P) не работает так как объект нужно еще итерировать как показано ниже

P = os.popen('dir')
I = iter(P)
print(next(I))
print(next(I))

R = range(5)
print(R)

I = iter(R)
print(next(I))                                              # вывод первого элемента из генератора
print(next(I))                                              # вывод второго элемента из генератора

E = enumerate('IaKrevedgo')
I = iter(E)
print(next(I))                                              # выводит номер и 1 элемент
print(next(I))                                              # выводит номер и второй элемент

# СПИСКОВЫЕ ВЛОЖЕНИЯ
L = [1, 2, 3, 4, 5]
for i in range(len(L)):
    L[i] += 10
print(L)
L = [x + 10 for x in L]                                     # тотже цикл только сразу в переменной и меньше по размеру
print(L)

res = []        
for x in L:                                                 # еще один вариант цикла
    res.append((x + 10))
print(res)

f = open('script2.py')                                      # отркывает файл и выводит содержимое в списко но с символом новой строки \n
lines = f.readlines()
print(lines)

lines = [line.rstrip() for line in lines]                   # код убирает символ новой строки из всего файла
print(lines)

lines2 = [line.rstrip() for line in open('script2.py')]     # те же тапки, только одновремнно с открытием файла минимальный код
print(lines2)


print([line.upper() for line in open('script2.py')])        # разом читаем построчно файл и выводим его содержимое в верхнем регистре!
print([line.rstrip().upper() for line in open('script2.py')])   # то же самое, но еще сразу убирает сисмволы новой строки 
print([line.split() for line in open('script2.py')])        # разделяет строки на элементы
print([line.replace(' ', '!') for line in open('script2.py')])  # заменем пробелы на восклицательный знак
print([('sys' in line, line[:5]) for line in open('script2.py')])   # ищет sys  построчно в файле

lines = [line.rstrip() for line in open('script2.py') if line[0] == 'p']
print(lines)
print([line.rstrip() for line in open('script2.py') if line.rstrip()[-1].isdigit()])

fname = 'c:\\code\\testapp\\log.txt'

# print(len(open(fname)).readlines())                       # чото не работает
print(len([line for line in open(fname) if line.rstrip() != '']))
print([x + y for x in 'ABCD' for y in '123'])               # вложенные циклы в циклах


uppers = [line.upper() for line in open('script2.py')]
print(uppers)

print(list(map(str.upper, open('script2.py'))))             # то же, что и выше

print('\n')
print(sorted(open('script2.py')))                           # сортирует и выводит
print(list(zip(open('script2.py'), open('script2.py'))))    # выводится с помощью List
print(list(enumerate(open('script2.py'))))                  # выводится с помощью list
print(list(filter(bool, open('script2.py'))))
import functools, operator
functools.reduce(operator.add, open('script2.py'))          # вызов с помощью импорта

a, b, c, d = open('script2.py')                             # можно даже переменным присваивать строки из файла, причем без символа \n
print(a, c)

a, *b = open('script2.py')
print(a, b)

print('y = 2\n' in open('script2.py'))                      # проверка на совпадение в файле тут FALSE
print('x = 2\n' in open('script2.py'))                      # проверка на совпадение в файле тут TRUE

L =[11, 22, 33, 44] 
L[1:3] = open('script2.py')                                 # вместо второго и третьего элемента присваем содержимое файла
print(L)

L = [11]
L.extend(open('script2.py'))                                # Добавляем к списку содержимое файла
print(L)

print(set(open('script2.py')))                              # создаем множество
print({line for line in open('script2.py')})                # создаем множество с помощью вложения
print({ix: line for ix, line in enumerate(open('script2.py'))}) # создаем словаь с ключами и значениями строками из файла

print(max([3,5,67,8,7,345,23,4324,235,5,25,25,252,1,6]))    # максимальное значение в списке
print(min([3,5,67,8,7,345,23,4324,235,5,25,25,252,1,6]))    # минимальное значение в списке

print(max(open('script2.py')), min(open('script2.py')))     # строка с максимальным строковы значением и минимальным (первая и последняя строки)

def f(a, b, c, d): print(a, b, c, d, sep = '$')             # добавялем разделитель $
print(f(1,2,3,4))

print(f(*[1,2,3,4]))
print(f(*open('script2.py')))


R = range(10)                                               
print(R)                                                    # возвращает диапазон указаный в range
I = iter(R)
print(next(I))                                              # возвращает значение
print(next(I))

print(list(range(10)))                                      # возвращает список, если надо

M = map(abs, (-1, 0 ,1))                                    # в абсолюте от -1 до 1
print(M)                                                    # возвращает обхект а не список
print(next(M))
print(next(M))
print(next(M))                                              # возвращает значение
'''print(next(M))                                              # четвертого значения нет поэтому тут исключение '''
for x in M:                                                 # список М пуст, так как все значения уже выведены.
    print(x)                                                # поэтому выводит пустоту

M = map(abs, (-1, 0 ,1))                                    # генерируем еще разок
for x in M:
    print(x)                                                # в этот раз выводит все 3 значения
    
Z = zip((1, 2, 3), (10, 20, 30))
print(list(Z))                                              # выводит запакованный список
for pair in Z:
    print(pair)                                             # список пуст после одного прохода

Z = zip((1, 2, 3), (10, 20, 30))                            # объявляем второй раз
for pair in Z:
    print(pair) 

Z = zip((1, 2, 3), (10, 20, 30))                            # объявляем второй раз
print(next(Z))                                              # ручная итерация

R = range(3)
I1 = iter(R)
print(next(I1))
print(next(I1))
I2 = iter(R)                                                # при присвоении второй переменной итератора он считается с 1 элемента
print(next(I2))
print(next(I2))
print(next(I1))

Z = zip((1, 2, 3), (10, 11, 12))
I1 = iter(Z)                                                # обратная ситуация
I2 = iter(Z)                                                # обе переменной к одному итератору
print(next(I1))                                             # при увеличении итерации увеличивается сразу в обоих переменных
print(next(I1))
print(next(I2))

D = dict(a=1, b=2, c=3)
print(D)
K = D.keys()                                                # выделяем ключи из словаря
print(K)
I = iter(K)                                                 # итерируем
print(next(I))
print(next(I))

for k in D.keys():                                          # выводим все ключи. ЫВ цикле все итерации делаются автоматически
    print(k, end = ' ')

K = D.keys()
print(list(K))                                              # всегда можно создать список ключей
V = D.values()                                              # и список значений
print(list(V))  
print(list(D.items()))                                      # вывести список элементов

for (k, v) in D.items():
    print(k, v, end = ' ')                                  # выводим только значения ключей и значений без самого словаря

print('\n')
I = iter(D)                                                 # итерируем словарь
print(next(I))                                              # автоматом итерируется по ключам
print(next(I))                                              # автоматом итерируется по ключам

for key in D:
    print(key, end= ' ')                                    # проход по всем ключам
    
print('\n')
for k in sorted(D):
    print(k, D[k], end = ' ')                               # вывод ключей с сортировкой

    
