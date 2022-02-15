#Глава 6-7
<<<<<<< HEAD
import copy,sys

path = 'C:\\code\\testapp\\'
    
x= 1
y=3
# длинный коментария на несоклько строк, если надо закоментить часть кода к примеру
''' 
x= copy.copy(y)
'''
i= 'IaKrevedgo'
=======
import copy,sys,os,math
import string


os.system('cls')
x = 1
y = 3
x = copy.copy(y)

>>>>>>> ec277825efa7de10a9255766cd2301ad8ab3afc7
L1 = [2,3,4]
L2 = L1[:] #создать копию L1
L1[0] = 24
print(L1)
print(L2)
print(x == 5)

print(sys.getrefcount(1))
<<<<<<< HEAD
bigtxt = '''В среду состоялся телефонный разговор между президентом России 
        Владимиром Путиным и премьер-министром Великобритании Борисом Джонсоном. 
        Во время беседы они обменялись своими опасениями насчет ситуации, сложившейся вокруг Украины.'''
# print(r'Пример длинного\f текста.\n \t Яблони \r на снегу.\a Ильгиз лох!!!\'') #неформатированная строка, чтобы напритмерн набрать путь к имени файла
# print(bigtxt)
myfile = open(path + 'data.txt','w') #вместо r можно использовать \\
print(myfile)
print('Количество исмволов--->',len(bigtxt + bigtxt),bigtxt)
for c in i: print(c, end='  ') #После каждой буквы вставляет символ 
print(bigtxt[0:200])
=======
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
somelist= list('IaKrevedgo')
print('first={0},last={1}'.format(somelist[0],somelist[-1])) #Форматирование списка (вывод 1 и последнего элемента)
parts =somelist[0],somelist[-1],somelist[1:-2]
print('first={0}, last={1}, middle={2}'.format(*parts)) #разделение списка на части и вывод начала, конца и середины

#форматирование текста и переменных
print('{0:20} тут центр {1:20}'.format('spam',123.4567))
print('{0:>20} = {1:<20}'.format('spam',123.4567)) #добавляет поля
print('{0.platform:>20} = {1[kind]:<20}'.format(sys,dict(kind='Компьютер'))) #подключается словарь

print('e={0:e}, 2e={1:.2e}, g={2:g}'.format(math.pi,math.pi,math.pi)) #слева форматирование, справа подключаем значения из библиотеки math
print('e=%e, 2e=%1.2e, g=%2g' % (math.pi,math.pi,math.pi)) #!те же тапки, толко меньше писанины

print('{0:x}, {1:o}, {2:b}'.format(255,255,255)) #отображене 16-ти, 8-ми и 2 чного формата
print('%x, %o'% (255,255)) #!теже тапки, только меньше писанины

print(hex(255),int('FF',16), 0xFF, ' ', oct(255),int('377',8),0o377) #преобразования в/из 16ричного и 8ричного формата

print(format(math.pi,'06.3f')) #запись для одного элемента
data = dict(platform=sys.platform,kind='laptop')
print('My {kind:<2} runs {platform:>2}'.format(**data)) #вывод из созданой переменной
print('My %(kind) - 2s runs %(platform)2s' % data) #те же тапки

print('{0:d} {0:,d}'.format(3000000,3000000)) #вывод с разделителями и без

#Форматирование строк
t = string.Template('$num = $title')
print(t.substitute({'num':7,'title':'Strings around us'}))
print(t.substitute(num=7, title='Strings'))
print(t.substitute(dict(num=7, title='Strings2')))

