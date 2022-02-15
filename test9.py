#Кортежи, файлы и вcе остальное
import pickle                           # библиотека для работы с файлами
import json                             # другая библиоткеа для рбаоты с двоичными файлами
import csv                              # бибилотека для работы с файлами csv
import struct                           # упауовщик для двоичных файлов

from collections import namedtuple      #класс для работы с кортежамив стандартной бибилиотеки


t= ('cc','aa','dd','bb')    # коретеж
tmp = list(t)               # список из кортежа
tmp.sort()
print(tmp)                  

T = tuple(tmp)              # кртеж из списка
print(T)
print(sorted(t))            # cортировка кортежа

rec = namedtuple('Rec',['name','age','jobs'])           # создание производного класса
bob = rec(name='Bob', age= 0.5, jobs=['dev','mgr'])
print(bob)
print(bob[0],bob[2])                                    # доступ по позиции
print(bob.name,bob.jobs)                                # доступ по атрибуту

O = bob._asdict()                                       # преобразование в словарь
O['name'],O['jobs']
print(O)


#РАБОТА С ФАЙЛАМИ
myfile = open('myfile.py','w')                          # открываем файл для записи w-перезапись, a-доавление
myfile.write('Hello text file\n')
myfile.write('Goodbye text file\n')
myfile.close()
myfile = open('myfile.py')
print(myfile.readline())                                # читаем открытый файл построчно

print(open('myfile.py').read())                         # читаем весь файл целиком

for line in open('myfile.py'):                          # читаем с помощью файловых итераторов, а не чтения
    print(line, end='')

print(open('D:\\_My\\desktop.ini').read())              # открываем файл в произвольном месте на диске

X, Y, Z = 43, 44, 45
S = 'Spam'
D = {'a':1,'b':2}
L = [1, 2, 3]

F = open('data.txt','w')
F.write(S +'\n')
F.write('%s, %s, %s\n' % (X, Y, Z))
F.write(str(L) + '$' + str(D) + '\n')
F.close()

#print(open('data.txt').read())
F = open('data.txt')
line = F.readline()
line = F.readline()
print(line)

line.rstrip()
parts = line.split(',')                                # делаем список из строк файла

print(parts)

int(parts[1])                                          # преобразуем строки в целые числа
numbers = [int(P)for P in parts]
print(numbers)

line = F.readline()
print(line)
parts = line.split('$')
print(parts)
eval(parts[0])                                          # делаем список из части строки
objects = [eval(P) for P in parts]                      # делаем список из строк полуученных из файла
print(objects)


#PICKLE
D = {'a': 1, 'b': 2}                                    # создание и запись файла с помощью библиотеки pickle
F = open('datafile.pk1','wb')
pickle.dump(D, F)
F.close

F = open ('datafile.pk1', 'rb')                         # откртие и чтение из файла с помощью библиотеки pickle
E = pickle.load(F)
print(E)
print(open ('datafile.pk1', 'rb').read())               # без пикла читается строка байтов

#JSON
name = dict(first = 'bob', last = ' Smith')
rec = dict(name = name, job =['dev', 'mgr'], age=40.5)
print(rec)                                              # словарь на Питоне

print(json.dumps(rec))                                  # тоже самое тока в json
S = json.dumps(rec)
O = json.loads(S)
print(O == rec)                                         # словари идеентичны

json.dump(rec, fp=open('testjson.txt','w'), indent=4)
print(open('testjson.txt').read())

P = json.load(open('testjson.txt'))
print(P)

rdr= csv.reader(open('csvdata.csv'))
for row in rdr: print(row)

F = open ('data.bin','wb')                              # Открываем двоичного упаковоанного файла
data = struct.pack('>i4sh', 7, b'IaKrevedgo', 8)
print(data)
F.write(data)                                           # запись строки байтов
F.close

F = open('data.bin','rb')                               # чиатем файл двоичный
data = F.read()
print(data)
values = struct.unpack('>i4sh',data)                    # перобразуем в объекты питон
print(values)

X = [1, 2, 3]
L = ['a', X, 'b']
D = {'x': X, 'y':2}

X[1] = 'suprise'
print(L, D)

A = L[:]                                                # копирование массивов и множеств
B = D.copy()                                            # то де самое
print(A, B)

X = [1, 2, 3]
L = ['a', X[:], 'b']                                    # используем копии множества вместо оригинала. При изменении не меняется в выражении
D = {'x': X[:], 'y':2}
X[1] = 'suprise'
print(L, D)

#СРАВНЕНИЯ

L1 = [1, ('a', 3)]
L2 = [1, ('a', 3)]
print(L1 == L2, L1 is L2)                               # значения равны? Тот же самый объект? (для поротких строк не работает)

