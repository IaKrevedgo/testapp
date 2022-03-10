# глава 15 Документация
import sys
import docstrings                                               # импортим наш же модуль

print(len(dir(sys)))                                            # получаем количество атрибутов
print([a for a in dir(list) if not a.startswith('__')])         # выводим атрибуты без подсеркиваний
print([a for a in dir(dict) if not a.startswith('__')])

def dir1(x): 
    return [a for a in dir(x) if not a.startswith('__')]        # создаем функцию, которая будет выводить атрибуты для имен
print(dir1(dir))

print(sys.__doc__)
print(sys.getrefcount.__doc__)
print(int.__doc__)


#PyDoc
help(sys.getrefcount)
# help(sys)                                                      # информация о sys длинная, поэтому закоментил
# help(dict)                                                      
help(docstrings.square)                                         # вытаскиваем хелп по функции из стороннего модуля
print('\n')
help(docstrings)                                                # получаем полный хелп по модулю

