#числовые типы глава 5
import math,os,decimal
from decimal import Decimal
from fractions import Fraction

os.system ('cls')
a = 3
b = 4
print(a + 1, a - 1)
print(b + 2, b // 41) #деление с результатом целым числом
print(a % 2, a ** 2)
num = 1/3.0
print ('%2.5f' % num) #формат вывода резуьтата где 5 - число знаков после запятой
print ('{0:0.2f}'.format(num)) #формат вывода резуьтата где 2 - число знаков после запятой
print(repr('spam'))
X = 2
Y = 4
Z = 6

n=0
#работа с разными типами 16,8, бинарные
print('БИТ |','ЗНАЧЕНИЕ |','HEX |','BIN |','OCT |')
while n<32:
    print(n,' |   ', 2**n,'    |',hex(n),'       |',bin(n),'       |',oct(n))
    n+=1

print(X<Y>Z)
print(int(1.1 + 2.2) == int(3.3))

#усечение
print(5//2, 5//2.0, 5//-2.0, 5// -2)
print(math.floor(-2.5)) #ближайшее меньшее значение
print(math.trunc(2.5)) #усечение дробной части

#матоперации
print(math.pi,math.e)
print(math.sqrt(144),math.sin(2*math.pi / 180))
print(pow(2,4),2**4,2.0**4.0) #разные записи возведения в степень
print(sum((1,2,3,4)),abs(-45),min(3,4,-5,6),max(2,4,5,6,-7,6))
print(round(-24.3435),round(2.567),round(22.566,1)) #округение
print((1/30),round(1/3.0,2),('%.2f'%(1/3.0)))
print(math.sqrt(144),144**.5,pow(144,.5)) #квадратный корень

#десятичные числа
decimal.getcontext().prec = 4 #фиксированная точность десятичных чисел (количество значащих цифр)
print(decimal.Decimal(10)/decimal.Decimal(7))
print (Decimal ('0.10')+Decimal ('0.1')+Decimal ('0.1')-Decimal ('0.3'))

with decimal.localcontext() as ctx: #фиксированная точность только внутри условия
    ctx.prec = 2
    print(decimal.Decimal(10)/decimal.Decimal(7))
    
#дроби    
x=Fraction(1,3)
y=Fraction(4,6) #дробь упращаетя автоматически до 2/3
print(x,y)
print(x+y,x-y,x*y)
z=Fraction('-.25') #создание дробей из чисел с плавающей точкой
print(z)
print((2.5).as_integer_ratio()) #преобразование в дробь
f=2.5
z=Fraction(*f.as_integer_ratio())
print(x+ Fraction(4,5))

#литералы и множества
print(set('spam'))
s1 = set()
s1.add(1.2), s1.add(2.3) #добавляем несколько элементов во множество
print(s1)

L=[1,2,3,4,5,4,5,6]
print(set(L))

L=list(set(L)) #удаление дубликатов из списка или сножества

print(L)
print(set([1,23,3,5,6]) - set([1,33,5,5,6,7,8,2])) #найти различия в списках

print(set('abcdefg')-set('abdefgt'))
engineers = {'bob','alan','ann','vic','sue'}
managers = {'tom','sue'}
print('bob' is managers)
print(engineers & managers,engineers ^ managers)

print(True + 4) # прибавляем к bool перемнной число и получаем результат
