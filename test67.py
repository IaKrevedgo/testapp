#Глава 6-7
import copy,sys,os

os.system('cls')
x = 1
y = 3
x = copy.copy(y)

L1 = [2,3,4]
L2 = L1[:] #создать копию L1
L1[0] = 24
print(L1)
print(L2)
print(x == 5)

print(sys.getrefcount(1))
z = 'Здавствуй, мой старый друг. Как поживаешь? Долго ли ты был в пути?'
e = z[::-1] #Смена порядка следования элементов на противоположный
print(z)
print(len(z[::-1]))
x = int('333')
print('--->', ord('!'))

B = '1101'
I = 0
while B != '':
    I = I*2 + (ord(B[0])-ord('0'))
    B = B[1:]
print(I)
I = int('11101',2)
print(I)
print(bin(I)) #тоже, что и цикл выше

S = 'splot'
S = S.replace('pl','killa') #заменяет искомый смвол на нужный
print(S)
print('Эточ что за %s %s %g %s поебень?!!!'%('змееподобная' ,'ебучая', 667.8, 'и важная')) #заменяет символы %s и %d в строке на строки и символы в скобках количество % и аргументов должно совпадать
F = 'Здравствуй$, мой старый друг$. Как поживаешь?$ Долго ли$ ты был в $пути?'
print(F.replace('$','',2)) #заменяет найденныйе символы на нужные. Третий аргумент число замен
L = list(F)
L[4] = 'WWW'
print(L)

L = ''.join(L)
print(L)
Line = 'aaa bbb ccc'
Line2 = 'Setup;id;ip;value'
col1 = Line [0:3]
col2 = Line [8:]
cols = Line.split() #разделить строку
txt = Line2.split(';')#разделяет строку по символу, удобно для csv
print(col1,col2,cols,txt)

Line3 = 'The knights who say Ni!'
print(Line3.startswith('The')) #проверка на символ в начале строки
print(Line3.endswith('Ni!')) #проверка на символ в конце строки

x = 133.23456789
print('%-10.4e | %06.1f | %-004.2g | %d' %(x,x,x,x)) #Форматирование чисел

print('%(qty)d more %(food)s'%{'qty':1,'food':'spam'})
bigtxt = '''Доброе утро. Приветствуем господина %(name)s! Ваш возраст составляет %(age)s!'''
values = {'name':'Denis','age':'37'}
print(bigtxt % values)

food = 'spam'
qty = 10

print('%(qty)d more %(food)s' % vars())
