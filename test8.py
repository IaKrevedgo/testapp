# Глава8 СПИСКИ
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

