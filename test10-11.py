# Глава 10-11
# операторы питона

import sys
'''
while True:                                     # бесконечный цикл
    reply = input('Enter text: ')
    if reply == 'stop': break                   # условие в одну строку
    elif reply.isdigit():                       # проверка, является ли переменная числом
        print('Вы ввели число! ' * 4)
    else: print(reply.upper())                  # выводит тескт в верхнем регистре
print('Bye')                                    # сообзение после заверщения работы цикла
'''
'''
while True:                                     # тоже самое, только с помощью TRY
    reply = input('Enter text: ')
    if reply == 'stop': break
    try:
        print(float(reply) ** 2)                # пытается перевести строку в число
    except:
        print('-->Вы ввели строку')             # если не получилось
print('Bye')

'''

# Глава 11

nudge = 1
wink  = 2

a, b = nudge, wink
[c, d] = [nudge, wink]

print(a,b,c,d)

nudge, wink = wink, nudge                       # переприсваивание
print(nudge, wink)

(i,a,k,r,e,v,e,d,k,o) = 'IaKrevedGo'            # присваивание строки символов

print(i,a,k,r,e,v,e,d,k,o)

string = "SPAM"
a, b, c = string[0],string[1], string[:-1]
print(a,b,c)

red, green, blue = range(3)                     # сходу присваиваем номера цветам
print(red,blue)

L = [1, 2, 3, 4, 5, 6, 7]
while L:
    front, L = L[-1], L[:-1]                    # уменьшает список по циклу
    print(front, L)
    
    
seq = [1, 2, 3, 4]
a, b, c, d = seq                                # каждому элементу по переменной
print(a, b, c, d)
a, *b = seq                                     # запаковкам 1 элемент = аб остальные пишутся в Б
print(a, b)
*a, b = seq                                     # запаковка в а пишется все, кроме посленего элемента
print(a, b)
a, *b, c = seq                                  # в Б пишется все, кроме начала и конца
print(a, b, c)
a, *b, c = 'IaKrevedgo'
print(a, b, c)
a, *b, c, d = range(1,11)                       # упаковка чичсел в диапазоне c 1
print(a, b, c, d)

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
while L:
    front, *L = L                               # получение 1 и остальных элементов без нарезания
    print(front, *L)
a = b = c = 'IaKrevedgo'
print(a, b, c)
a = b = 0                                       # групповое обнуление, например счетчиков 
b += 1
print(a, b)

S = 'iakrevedgo'                                
S += 'IAKREVEDGO'                               # инкремент строки
print(S)

L = [1, 2, 3, 4]                                
L += [5, 6, 7]                                  # инкримент списка
print(L)

print(open('personal.csv').read())

temp = sys.stdout                           # вывод во внешни файл начало
sys.stdout = open('log.txt', 'a')
print('spam')
print(1, 2, 3)
sys.stdout.close()                          # вывод во внешний файл окончание
sys.stdout = temp
print('back here')
print(open('log.txt').read())

log = open('log.txt','a')
print('Еще одна запись в лог', file=log)
log.close()
print(open('log.txt').read())