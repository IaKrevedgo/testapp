import random
import names
import os
import colorama
from colorama import Fore, Back, Style


def Main (exit):
    n=0
    os.system ('cls')
    print ('ОТДЕЛ СИКН')
    o=input('Для запуска поиска самого квалифицированнрого специалиста, для поездки в командировку нажмите любую клавишу...')
    os.system ('cls')
    print('КТО ПОДЕДЕТ В КОМАНДИРОВКУ?' + '\n')
    from names import a, b, c, d, e, f, g, h, i, j, k, l, m, p, o #импортируем атрибуты из другого модуля без запуска модуля
    while(n<10):
    
        x = random.choice ([a, b, c, d, e, f, g, h, i, j, k, l, m, p, o])
        if n == 10 and (x != a or x !=b or x !=c or x !=d or x !=i):
            print('Выбор не сделан. Поедет ДЮС')
        
        if x == a or x == b or x == c or x == d or x == i:
            print('\n' +'---> Выбор пал на ' + Fore.LIGHTGREEN_EX + x + '\n')
            n = 11
            z = input(Fore.WHITE + 'НАЖМИТЕ ENTER чтобы оформить командировочный? (y/n) ')
            try:
                if z == 'y':
                        break
                elif z == 'n':
                    os.system ('cls')
                    print(Fore.WHITE + 'КТО ПОДЕДЕТ В КОМАНДИРОВКУ?' + '\n')
                    n=0
            except KeyError(): #любая другая клавиша
                pass        
            
        elif x==j:
            print('\n' + 'Выбор пал на '+ Fore.LIGHTRED_EX + x + Fore.WHITE +', но он договорился с руководством, поэтому снова вращаем барабан' + '\n')
            n=n+1
        elif x==o:
            print('\n' + 'Выбор пал на '+ Fore.LIGHTRED_EX + x + Fore.WHITE +', но он cовсем долбоеб и уволился уже, поэтому снова вращаем барабан' + '\n')      
            n=n+1
        elif x==k or x==l or x==m or x==p:
            print('\n' + 'Выбор пал на '+ Fore.LIGHTRED_EX + x + Fore.WHITE +', но он уволился уже, поэтому снова вращаем барабан' + '\n')      
            n=n+1
        else:
            print('\n' + 'Выбор пал на '+ Fore.LIGHTRED_EX + x + Fore.WHITE +', но ему нельзя ездить по жопам, поэтому снова вращаем барабан' + '\n')
            n=n+1

Main (0)
