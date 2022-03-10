'''
Module Documentation
Words Go Here
'''
import docstrings

spam = 40
def square(x):
    '''
    function documentation
    can we have your liver then?
    '''
    return x ** 2                               # квадрат

class Employee:
    '''
    Class documentation
    '''
    pass

print(square(4))
print(square.__doc__)

print(docstrings.__doc__)                       # вывод документации модуля без функций и классов              
print(docstrings.Employee.__doc__)              # документация класса
print(docstrings.square.__doc__)                # документация на функцию

