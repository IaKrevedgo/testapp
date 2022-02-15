# Глава8 СПИСКИ и СЛОВАРИ
from winreg import DeleteKey


print(3 in [1,2,3,4])

listX = [1,2,3,4,5,6,7,8,9,0]
listX.sort()

for x in listX: print(x, end='\n')  # вывод списка с разделителем в кавычках
res = [c*4 for c in 'IaKrevedgo']
print(res)

listX[1:2] = [32,33]                # добавлаем в заданное место
listX.extend([11,22])               # добавляем в конец списка
print(listX)
listXS = ['Денис','Катя','Полина']
listXS.append('Антон')              # добавляем в конец списка строковое значение
listXS.sort()                       # сортировка списка
print(listXS)

print(listXS.sort(key=str.lower, reverse=True))             # сортировка списка c реверсом

print(sorted([x.upper() for x in listXS], reverse=True))    # преобразованеие строки в цикле перед сортировкой 
#print(listXS.pop())                        # удаление и взврат последнего элемента

print(listXS.index('Антон'))                # получаем индекс нужного элемента в списке (3)
listXS.insert(listXS.index('Антон'), 'Рашид'), print(listXS)    # вставляет  пред указаным элементом значение. Можно добавить смещение +1

print(listXS.count('Рашид'))                # показывает количество искомых элементов с списке

del listXS[3]                               # удаляем заданый элемент из списка
print(listXS)

#СЛОВАРИ

D ={'spam':2,'ham':1,'eggs':3}
print(D['spam'])

print(len(D))                               # количество элементов в словаре

print('ham' in D)                           # проверка на наличие в словаре

print(list(D.keys()))                       # вывод ключей словаря
D['ham'] = ['grill','bake','fry']           # изменение элементов в словаре
print(D)

del D['eggs']                               # удаление ключа
print(D)

D['branch'] = 'bacon'                       # добавление элемента в словарь
print(D)

print(list(D.values()))                     # вывод значений словаря

print(list(D.items()))                      # вывод значений и ключей словаря

print(D.get('spam'))                        # проверка наличия ключа. ключ присутствует

print(D.get('toast'))                       # проверка наличия ключа. ключ отсутсвует

D.get('toast', 88)                          # Добавляем новый ключ вместо отсутствующего

D2 = {'toast':2,'maffin':5}                 # объеденение словарей с перезаписываением ключей при совпадении
D.update(D2)
print(D)

#БД о фильмах

table = {'1975': 'Holy Grail',              # ключ: значение
         '1979': 'Life of Brain',
         '1983': 'The Meaning of Life'}
year = '1983'
movie = table[year]                         # словарь[ключ] => значение
print(movie)

for year in table:                          # тоже, что и for year in table.keys()
    print(year + '\t' + table[year])        

tableD = {1975: 'Holy Grail',              # ключ: значение
         1979: 'Life of Brain',
         1983: 'The Meaning of Life'}
print(list(tableD.items()))

Matrix = {}
Matrix[(2,3,4)] = 88
Matrix[(7,8,9)] = 99
x = 2; y = 3; z = 4         #присваеваем операторы мыссивам
print(Matrix[(x, y, z)]) 
print(Matrix)

#варианты исключения ошибок из кода
if (2,3,6) in Matrix:
    print(Matrix[(2,3,5)])
else:
    print('None')

try:
    print(Matrix[(2,3,6)])
except KeyError:
    print('None')

print(Matrix.get((2,3,4),0))
print(Matrix.get((2,3,6),'None'))           # если не существет подставляем стандартный аргумент после запятой

rec = {}                                    # запись профиля объекта по шагам
rec['name'] = 'Bob'
rec['age'] = 40.5
rec['job'] = 'developer/manager'
print(rec['name'])


rec = {'name':'Bob',                        # запись профиля разом
        'jobs':['development','manager'],
        'web':'www.bobs.org/bobs',
        'home':{'state':'Overworked','zip':'12345'}}
print(rec['name'])
print(rec['jobs'])
print(rec['jobs'][1])
print(rec['home']['zip'])

zet = dict(name='Bob',age=40)               # !!! кроткая форма записи словаря !!!!
print(zet)
D = {}
D['state1'] = True
print('state1' in D)

list(zip(['a','b','c'],[1,2,3]))
D = dict(zip(['a','b','c'],[1,2,3]))        # создание словаря из упакованного списка
print(D)                

D = {k : v for (k,v) in zip(['a','b','c'],[1,2,3])}  # тоже самое тока проще
print(D)

D = dict.fromkeys(['a','b','c'],'NULL')     # инициализация словаря с фиксированным ключом
print(D)

D = dict.fromkeys('IaKrevedgo')      # создание словаря для каждого элемента слова
print(D)

D = dict(a=1,b=2,c=3)               # создает быстрый словарь из строк
print(D)

L = list(D.keys())                  # создает быстрый список из ключей словаря (можно использовать list(D))
print(L)

V = list(D.values())                # тоже самое, только для значений словаря
print(V)

for k in D.keys(): print(k)            
for key in D: print(key)            # не обязательно указывать .keys

for k in reversed(D): print(k, D[k])        # сортирует список перед отображением в обратном порядке

