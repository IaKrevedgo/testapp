import random, os
#import names #подключаем файл с именами
#import colorama #красивые разноцветные стили для текста. Нужно импортировать в питон через pip

from colorama import Fore, Back, Style 
from names import a, b, c, d, e, f, g, h, i, j, k, l, m, p, o, r #импортируем атрибуты из другого модуля без запуска модуля
w = [a, b, c, d, e, f, g, h, i, j, k, l, m, p, o, r]    
n=0
os.system ('cls')
print (Fore.YELLOW + 'ОТДЕЛ СИКН')
input(Fore.WHITE + 'Для запуска поиска самого квалифицированного специалиста, для поездки в командировку нажмите любую клавишу...')
os.system ('cls')
print(Fore.WHITE + 'КТО ПОЕДЕТ В КОМАНДИРОВКУ?' + '\n')
while True:             
        x = random.choice (w) #выбираем случайное имя из списка
        if n == 3 and (x != a or x !=b or x !=c or x !=d or x !=i): #если имя относится к плебейскому
            print('\n' + Fore.YELLOW + 'Автоматическая система не смогла сделать выбор, поэтому поедет '+ Fore.LIGHTRED_EX + 'ДЮСМЕТОВ!!!!!!!!!')
            input('Нажмите любую клавишу для завершения программы...')
            break
        if x == a or x == b or x == c or x == d or x == i:
            print('\n'+ Fore.YELLOW +'---> Выбор пал на ' + Fore.LIGHTGREEN_EX + x + '\n')
            n = 11
            z = input(Fore.WHITE + 'НАЖМИТЕ "y" чтобы оформить командировочный, или ENTER чтобы попытаться выбрать еще раз -->')
            try:
                if z == 'y':
                        break
                else:
                    os.system ('cls')
                    print(Fore.WHITE + 'КТО ПОЕДЕТ В КОМАНДИРОВКУ?' + '\n')
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
        elif x==r:
            print('\n' + 'Выбор пал на '+ Fore.LIGHTRED_EX + x + Fore.WHITE +', но он уже свалил к Минакову, а тот скорее всего пошлет нахуй, поэтому снова вращаем барабан' + '\n')              
            n=n+1
        else:
            print('\n' + 'Выбор пал на '+ Fore.LIGHTRED_EX + x + Fore.WHITE +', но ему нельзя ездить по жопам, поэтому снова вращаем барабан' + '\n')
            n+1

