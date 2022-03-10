# ГЛАВА 12, 13
import os

choise = 'ham'
print({'spam':1.25,
       'ham': 1.99,
       'beacon': 1.10}[choise])                 # выбор из списка( заменяет много if)

branch = {'spam':1.25,
       'ham': 1.99,
       'eggs': 0.99,
       'beacon': 1.10}
print(branch.get('spam', 'Bad choice'))         # есть в списке пишем значение 'spam'
print(branch.get('meat', 'Bad choice'))         # нет в списке, пишем 'bad choice'

choice = 'ham'
try:
    print(branch[choice])                       # если есть в списке то выдаем значение
except:
    print('Bad choice3')                        # если не тв списке пишем сообщение
        
print(2 or 3, 3 or 2)
L = [1, 0, 2, 0, 'spam', '', 'ham',[]]
print(list(filter(bool,L)))                     # получение истинных значений

X = 1
Z = 2
Y = 3

print(Y if X else Z)                            # вместо тысячи условий. Возвращает Y если X истина

x = 'spam'
while x:                                        # до тех пор пока Х не пустая
    print(x, end=' ')                           
    x = x[1:]                                   # отбрасывание первого элемента цикла
    
a = 0; b=10
while a <= b:
    print(a, end = '..')
    a += 1
    
x = 10
while x:
    x = x-1
    if x % 2 != 0: continue                     # Нечетное? тогда пропустить
    print(x, end= ' ') 

x = 10
while x:                                        # тоже самое без континиума
    x = x-1
    if x % 2 ==0:
        print(x, end = ' ')
'''        
while True:
    name = input('\nEnter name: ')
    if name == 'stop': break
    age = input('Введите возраст: ')
    print(' Hello', name, '=>', int(age)** 2)
''' 
y=3   
x = y // 2
while x > 1:
    if y % x == 0:
        print('\n', y, 'has factor', x)
        break
    x -= 1
else:                                           # условие для цикла 
    print('\n', y, 'is prime')
    
for x in ['spam','ham','eggs']:
    print(x, end=' ')
    
sum = 0
for x in [1, 2, 3, 4]:
    sum = sum + x                               # сумма всех элементов в списке
print(sum)

prod = 1
for item in [1, 2, 3, 4]:
    prod *= item                                # перемножение всех элементов в списке
print(prod)

S = 'IaKrevedgo'                            
T = ("and", "i'am", "okay")                     
Z = [(1, 2), (3, 4), (5, 6)]
for x in S:                                     # применяем цикл на строку
    print(x, end = ' ')    
for x in T:                                     # примеяем цикл на кортеж (список элементов)
    print(x, end = ' ')    
for a, b in Z:
    print(a, b)
D = {'a': 1, 'b': 2, 'c': 3}                    # вывод ключей и значений из словаря
for key in D:
    print(key, '-->', D[key])
list(D.items())
for (key, value) in D.items():                  # итерация сразу по ключам и значениям
    print(key, '-->>', value)

for both in Z:
    a, b = both                                 # итерация с присваиваением вручную
    print(a, b)    

((a, b), c) = ((1, 2), 3)
for ((a, b), c) in [((1, 2), 3), ((4 ,5), 6)]:
    print(a, b, c)
for ((a, b), c) in [((1, 2), 3), ['XY', 6]]:    # присваивание строки
    print(a, b, c)    

a, *b, c = (1, 2, 3, 4)                         # тут b = [2, 3]
for (a, *b, c) in [(1, 2, 3, 4), (5, 6, 7, 8)]: # присваивание последовательностей
    print(a, b, c)
    
items = ['aaa', 111, (4, 5), 2.01]              # набор объектов
tests = [(4, 5), 3.14]                          # ключи для поиска
for key in tests:                               # для всех ключей
    for item in items:                          # для всех элементов
        if item == key:                         # если ключ и элемент совпадают
            print(key, 'was found')
            break
    else:                                       # исключение для цикла если ключ не совпадает
            print(key, 'not found!')
            
for key in tests:                               # тоже самое только проще
    if key in tests:                            # вместо второго цикла в условии применяем in
        print(key, 'was found')
    else:
        print(key, 'not found')
        
seq1 = 'IaKrevedgo'
seq2 = 'BarabinsK'

res= []                                         # создаем пустой список
for x in seq1:                                  # для элементов seq1
    if x in seq2:                               # которые есть в seq2
        res.append(x)                           # добавялем  список res
print(sorted(res))                              # выводим список с сортировкой

res = [x for x in seq1 if x in seq2]            # теже тапки только в разы проще
print(sorted(res))


#ИСПОЛЬЗУЕМ RANGE
print(list(range(5)), list(range(2,5)), list(range(0, 10, 2)))  # генерация списков с помощью range

print(list(range(-5, 5)))                       # два аргумента - границы 
print(list(range(5, -10, -1)))                  # три аргументы - границы и интервал. В данном случае на -1 каждый цикл
 
for i in range(3, 10, 2):                       # применение range в циклах
    print(i, 'Krevedgos')

X = 'IaKrevedgo'
for x in X: print(x, end = ' ')


i = 0
while i < len(X):                               # интеграция в цикл while         
    print(X[i], end = '\n')
    i += 1

print(len(X))                                   # получаем длину строки Х
print(list(range(len(X))))                      # генерируем range с помощью длины строки
for i in range(len(X)): 
    print(X[i], end = ' ')                      # ручная итерация посредством range

for item in X:                                  # самый простой вариант цикла!
    print(item, end = ' ')

# бегущая строка епта
print('\n')
S = 'IaKrevedgo'                            
for item in range(len(S)):                      # для счетчиков повторений
    S = S[1:] + S[:1]                           # перемещает начальный элемент в конец
    print(S, end = ' ')
    
print('\n')

for i in range(len(S)):
    X = S[i:] + S[:i]
    print(X, end = ' ')

print('\n')

L = [1, 2, 3]
for i in range(len(L)):                         # работает с любыми последовательностями
    X = L[i:] + L[:i]
    print(X, end = ' ')
    
print('\n')
S = 'IaKrevedgo'
for i in range(0, len(S), 2):                   # каждый второй элемент из строки S
    print(S[i], end = ' ')
 
print('\n')    
for c in S[::2]:                                # тоже что и выше тока проще с использованием ::2
    print(c, end = ' ')

print('\n')     
L = [1, 2, 3, 4, 5]
for i in range(len(L)):                         # добавить 1 к каждому лементу в L
    L[i] += 1
print(L)

L1 = [1, 2, 3, 4]
L2 = [5, 6, 7, 8]
print(list(zip(L1, L2)))

for (x, y) in zip(L1, L2):
    print(x, y, '--', x + y)

T1, T2, T3 = (1, 2, 3), (4, 5, 6), (7, 8, 9)
print(list(zip(T1, T2, T3)))

S1, S2 = 'abc', 'xyz321'                        # удобная запись несоклькоих переменных в одну строку, правда менее информативная
print(list(zip(S1, S2)))

keys = ['spam', 'eggs', 'toast']                # собираем ключи и значения в один словаь с помощью цикла
vals = [1, 3, 5]
print(list(zip(keys, vals)))
D2 = {}
for (k, v) in zip(keys, vals):
    D2[k] = v
print(D2)

D3 = dict(zip(keys, vals))                      # те же тапки, только без цикла
print(D3)

print({k :v for (k, v) in zip(keys, vals)})     # тоже самое ваще в одну строчку ;) но менее читаемо


#Смещение

S = 'IaKrevedgo'
offset = 0

for item in S:
    print(item, 'смещено на', offset)           # нумерует каждый элемент из цикла
    offset += 1
    
for (offset, item) in enumerate(S):             # тоже самое только с помощью enumerate
    print(item, 'смещено на', offset)
    
E = enumerate(S)    
print(next(E), next(E), next(E))                # возращает номер и элемент


#Пример enumerate для файла
F = os.popen('dir')
F = F.readline()
print(F)
F = os.popen('dir')
F = F.read(50)
print(F)
print(os.popen('dir').readlines()[0])
for line in os.popen('dir'):
    print(line.rstrip())
    
print(os.system('systeminfo'))                  # получение информации о системы

for (i, line) in enumerate(os.popen('systeminfo')): # форматирование информации, оставляем только 4 строки первые
    if i == 4: break
    print('%02d) %s' % (i, line.rstrip()))      # добавляем нумерацию
    
for line in os.popen('systeminfo'):             # вытаскиваем название os
    parts = line.split(':')
    if parts and parts[0].lower() == 'Название ОС':
        print(parts[1].strip())
        
from urllib.request import urlopen
for line in urlopen('http://rambler.ru'):
    print(line)