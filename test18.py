# АРГУМЕНТЫ

def f(a):
    a = 99                                                  # тут изменяется только локальная переменная

b = 88
f(b)                                                        # значение b не изменилось
print(b)

def changer (a, b):
    a = 2
    b[0] = 'Iakrevedgo'                                     # список - изменяемый объект
    
X = 3
L = [1, 2]  
changer(X, L)
print(X, L)                                                 # число остается прежним, а список изменяет функция

def multiple (x , y):
    x = 2
    y = [3, 4]
    return x, y                                             # при использовании return возращается то, что натворила функция

X = 1
L = [1, 3]
X, L = multiple(X, L)
print(X, L)


# сопоставление имен и аргументов

def D(a, b ,c): print(a, b, c)                              # сопоставление слева направо
D(1, 2, 3)

D(c=3, b=2, a=1)                                            # сопоставление по присваиванию
D(1, b=2, c=3)                                              # сначала соапостовляются аргументы по позиции, потом по имени

# стандартные значения
def a(a, b=2, c=3): print(a, b, c)                          # аргумент а обязательный, b и с стандартные
a(1)                                                        # a присваивается в(), b и c берутся стандартными из функции
a(1, 5, 6)                                                  # при использовании 3 аргументов, стандартные значения заменяются на аргументы функции
a(1, c=6)                                                   # переприсваивает стандартное значение, a присваивается по позиции, b берется стандартное, 
                                                            # с присваевается по ключевому слову
                                                            
def func(spam, eggs, toast=0, ham=0):                       # обязательны 2 аргумента! 
    print((spam, eggs, toast, ham))

func(1, 2)
func(1, ham=1, eggs=0)
func(spam=1, eggs=0)
func(toast =1, eggs=2, spam=3)
func(1, 2, 3, 4)


# Произвольное количество аргументов
def args(*args): print(args)                                # * собирает все аргументы в кортеж
args()
args(1)
args(1, 2, 3, 4)

def dec(**args): print(args)                                # ** собирает элементы в новый словарь
dec()
dec(a=1,b=2)                                                # необходимо явно указывать ключи и значения иначе нихт
dec(a=3,b=4,c=5)

def xar(a, *pargs,**kargs): print(a, pargs, kargs)          # можно комбинировать разные типы аргументов. Тут требуется как минимум 1 оргумент у функции
xar(2)
xar(1, 2, 3, x=1, t=4)                                      # выдает 1 (2, 3) {'x': 1, 't': 4}, 1, кортеж (2, 3) и словарь {'x': 1, 't': 4}


# выхов функций и распаковка аргументов
def trum(a, b, c, d): print(a, b, c, d)
args = (1, 2)
args += (3, 4)
trum(*args)                                                 # то же, что и trum(1, 2, 3, 4)

args = {'a':1, 'b':2, 'c':3}
args['d'] = 4
trum(**args)                                                # то же, что и func(a=1, b=2, c=3, d=4)

trum(*(1, 2), **{'d':4, 'c':3})                             # тоже что и trum(1, 2, d=4, c=3)
trum(1, *(2,3), **{'d':4})                                  # тоже что и trum(1, 2, 3, d=4)
trum(1, c=3, *(2,), **{'d':4})                              # тоже что и trum(1, 2, c=3, d=4)
trum(1, *(2,3), d=4)                                        # тоже что и trum(1, 2, 3, d=4)
trum(1, * (2,), c=3, **{'d': 4})                            # тоже что и trum (1,2, c=3, d=4)


# обобщенное применение функций
args = (2, 3)
args += (4, 2)
print(args)
trum(*args)

def knowly(a, *, b = 'spam', c = 'IaKrevedgo'):             # можно указывать, что после * идут стандартные аргументы
    print(a, b, c)
knowly(1)
#knowly(1, 2)                                               # работать не будет так как ждет 1 аргумент для а
knowly(a=1)
knowly(c=3, b=2, a=1)

def xx(a, *b, c=6,**d): print(a, b, c, d)
xx(1, 2, 3, x=4, y=5)                                       # стандартные значения
xx(1, 2, 3, x=4, y=5, c=7)                                  # переопределяется стандартное значенние с помощью имени c
xx(1, 2, 3, c=7, x=4, y=5)                                  # можно указывать где угодно в ключевых аргументом
xx(1,*(2,3), **dict(x=4,y=5))                               # с или не указывается или должно быть между аргументами * и **
xx(1, *(2,3), c=88, **dict(x=4,y=5))                        # как здесь
xx(1, c=833, *(2,3),  **dict(x=4,y=5))

xx(1,  *(2,3),  **dict(x=4,y=5, c=823))
def fa(a, c=6, *b, **d): print(a, b, c, d)                  # здесь с - не аргумент потомучто не находит между * и **???
fa(1, 2, 3, x=4)
#fa(1, *(2,3), **dict(x=4,y=5), c=99)                       # так работать не будет потомучто с должно быть определено между * и ** или перед *


# Обобщенные функции для рбаоты со множетсвами
from inter2 import intersect, union
s1, s2, s3 = 'IaKrevedgo', 'babeluhaK', 'zerguloid'

print('Совпадают =', intersect(s1,s2),'\n','Отличные =', union(s1,s2))                          # два операнда
print('Совпадают =', intersect([1,2,4],(1,4)),'\n','Отличные =', union('grilcK',s2))            # разнородные типы
print('Совпадают =', intersect(s1,s2,s3),'\n','Отличные =', union(s1,s2,s3))                    # три операнда
            

def tester(func, items, trace=True):
    for i in range(len(items)):
        items = items[1:] + items[:1]
        if trace: print(items)
        print(sorted(func(*items)))
tester(intersect, ('a', 'asbdftre','asdfert','qwertydf'))

tester(union, ('a','asdfg','avzxcadft','asdafqw',), False)
tester(intersect,('ba','abcdefg','adbst','almbcnd'),False)
print(intersect([1, 2, 1, 3],(1, 1, 4)))
print(union([1, 2, 1, 3],(1, 1, 4)))

def func(a, b=4,c=5):
    print(a, b, c)
func(1,2)

def func(a, *pargs):                                                                            # созадет список
    print(a, pargs)
func(1,2,3)

def func(a, **kargs):                                                                           # созадет словарь
    print(a, kargs)
func(a=1,b= 2,c=3)

def func(a,b,c=3,d=4): print(a, b ,c, d)
func(1,*(5,6))

def func(a, b, c):
    a = 2
    b[0] = 'x'
    c['a']= 'y'
l=1
m=[1]
n={'a':0}
func(l, m, n)
print(l, n, m)