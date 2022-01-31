import os,re
import sys
import myfile #импортирует модуль из той же папки
import names #импортируем модуль с именами и проект и запускает его
import struct
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
s= 'IaTrevedoS'

l=list(s)
print(l)
l[2]='K'
''.join(l)
print(l)
l.remove('S')

print(l)
#print(dir(s)) #эта хрень выводит кучу атрибутов, которые можно применить к типу или классу

#print(help(s.swapcase)) #выводит подробный хелп по выбранному методы, но проще загуглит ьс примерами

msg= '\n'+ '''Битбарамиб рахатым лукум эйгагаг "ываывыЭ" барклай детоля 'sdsdsdsd'kk  dfdffdcwerjdfym сцуковань''' #большой разносортный текст вы больших кавычках 
print(msg)
match = re.match('Епанаврот что это за[\t]*(.*)херня','Епанаврот что это за лютая и говяная херня') #сравнивает две строки и выводит, что поменялось
eps = match.group(1)

print(eps)

M = [[1,2,3],
     [4,5,6],
     [7,8,9]]

col2 = [row[2] - 1 for row in M if row[1] % 2 == 0] #собрать элементы в столбце 2, и отфильтровать нечетные элементы
print(col2)
diag = [M[i][i] for i in [0,1,2]] #диагональ матрицы
print (diag)

doubles = [c * 2 for c in l] #повторить символы в строке
print(doubles)

print([[x,x/2,x**2] for x in range (-20,10,2) if x <0])

rec = {'name':{'first':'bob','last':'Smith'}, #сложный словарь со вложениями
       'jobs':['dev','mrg'],
       'age': 40.5}
recP = rec['name']['last']
rec['jobs'].append('janitor') #добавляем в словарь еще одну должность
print(rec)

D = {'food':'spam','quantity':4,'color':'pink'}
D ['quantity'] += 1
print(D)

D = {'a':1,'c':2,'b':3}
Ks = list(D.keys())
print(Ks)

Ks.sort()
print(Ks)

x=4
while x>0:
    print('iakrevedgo '*x)
    x-=1
for line in open('data.txt'): print(line) #открывать файл прямо в цикле

packed = struct.pack('>i4sh',7 , b'spam',8)
print(packed)
file = open('data.bin','wb')
file.write(packed)
file.close()

data = open('data.bin','rb')
print(data)

x= set('spam') #создать множетво

y= {'h','a','m','p'}
print(x,y)
print(x&y) 
print(x|y)
print(x-y)
print(x>y)
print(list(set([1,2,1,3,1])))
print('k' in set('IaKrevedgo'), 'p' in 'spam','ham' in ['ham','eggs','spam']) #используем in для множеств
    
print('\n'+'<--- Окончание программы--->') 
input('Для выхода нажмите ENTER') #чтобы окошко не исчезало сразу
