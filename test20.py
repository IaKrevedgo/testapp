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