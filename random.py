import random
import names
import os


def Main (exit):
    n=0
    os.system ('cls')
    o=input('Для запуска поиска самого квалифицированнрого специалиста, для поездки в командировку нажмите любую клавишу...')
    os.system ('cls')
    print('КТО ПОДЕДЕТ В КОМАНДИРОВКУ?' + '\n')
    from names import a, b, c, d, e, f, g, h, i, j #импортируем атрибуты из другого модуля без запуска модуля
    while(n<10):
    
        x = random.choice ([a, b, c, d, e, f, g, h, i, j])
        if n == 10 and x != [a,b,c,d,i]:
            print('Выбор не сделан. Не поедет никто')
        
        if x == a or x == b or x == c or x == d or x == i:
            print('\n' +'---> Выбор пал на ' + x + '\n')
            n = 11
            z = input('НАЖМИТЕ ENTER чтобы оформить командировочный? (y/n) ')
            try:
                if z == 'y':
                        break
                elif z == 'n':
                    os.system ('cls')
                    print('КТО ПОДЕДЕТ В КОМАНДИРОВКУ?' + '\n')
                    n=0
            except KeyError(): #любая другая клавиша
                pass        
            
        elif x==j:
            print('\n' + 'Выбор пал на '+ x +', но он договорился, поэтому снова вращаем барабан' + '\n')
            x = random.choice ([a, b, c, d, e, f, g, h, i, j])
            n=n+1
        else:
            print('\n' + 'Выбор пал на '+ x +', но ему нильзя ездить по жопам, поэтому снова вращаем барабан' + '\n')
            x = random.choice ([a, b, c, d, e, f, g, h, i, j])
            n=n+1

Main (0)
