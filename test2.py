import math,os


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
os.system ('cls')
print('БИТ |','ЗНАЧЕНИЕ |','HEX |','BIN |')
while n<32:
    print(n,' |   ', 2**n,'    |',hex(n),'       |',bin(n))
    n+=1

print(X<Y>Z)
print(int(1.1 + 2.2) == int(3.3))

print(5//2, 5//2.0, 5//-2.0, 5// -2)
print(math.floor(-2.5)) #ближайшее меньшее значение
print(math.trunc(2.5)) #усечение дробной части
