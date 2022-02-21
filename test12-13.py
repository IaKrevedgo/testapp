# ГЛАВА 12

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
    
