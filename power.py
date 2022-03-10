# то же упражнение из 3 главы

L = [1, 2, 4, 8, 16, 32, 64]
X = 2

i = 0
while  i < len(L):
    if 2 ** X == L[i]:
        print('Найдено под индексом', i)
        break
    else:   
        print(X, 'not found')
        i += 1

for item in L:
    if 2 ** X == L[item]:
        print('Найдено под индексомс', L.index(item) + 1)
        break
else:   print(X, 'не найден')

L = [1, 2, 4, 8, 16, 32, 64]    
X = 16
item = 0

for item in iter(range(L)):
    print(item)
    if L[item] == 2 ** X:
        print('Найдено под индексомсу', item)
        break
else: print(X, 'Не найден') 

