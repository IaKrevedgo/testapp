import os,re
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

print('\n'+'<--- Окончание программы--->') 
input('Для выхода нажмите ENTER') #чтобы окошко не исчезало сразу
