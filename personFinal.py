# пример программы для главы 28
'''
регистрирует и обрабатывает сведения о людях.
Для тестирования классов из этого файла запустите его напрямую
'''
from classtools import AttrDisplay                                                      # импортим класс из фалйа вывода аттрибутов из урока

class Person(AttrDisplay):
    '''
    Создает и обрабатывает сведения о людях
    '''
    def __init__(self, name, job=None, pay=0):                                          # конструктор принимает 3 аргумента, все аргументы справа от стандартного должны быть тоже присваиваемыми
        self.name = name                                                                # заполнить поля при создании
        self.job = job                                                                  # self - новый экземпляр класса
        self.pay = pay
        
    def lastName(self):
        if len(self.name.split()) == 2:                                                 # если указаны имя и фамилия
            return self.name.split()[-1]                                                # берем фамилию
        
    def firstName(self):   
        if len(self.name.split()) == 2:                                                 # если указаны имя и фамилия
            return self.name.split()[0]                                                 # берем имя
        
    def giveRaise(self, percent=0.0):                                                    # увеличиваем зарплату
        self.pay = int(self.pay * (1 + percent))


class Manager(Person):                                                                  # создаем подкласс
    '''
    Настроенная версия Person со специальными требованиями
    '''
    def __init__(self, name, pay):                                                      # инит для подкласса
        Person.__init__(self, name, 'mgr', pay)                                         # для манагеров указываем срауз должность 'mgr'

    def giveRise(self, persent=0.0, bonus=.10):                                         # манагер, сцука такая, всегда получает на 10% больше
#        self.pay = int(self.pay *(1 + persent + bonus))                                # плохой способ!!!
        Person.giveRaise(self, persent + bonus)                                         # хороший способ. Используем метод родительского класса



# !!!код ниже для самотестирования класса и помещен в условие, чтобы не отображаться при импорте модуля      
if __name__ == '__main__':                                                                  # испонятся только внутри текущего модуля
    bob = Person('Bob Smith')                                                               # тестирование класса
    sue = Person('Sue Jones', job = 'dev', pay =10000)                                      # можно явно указывать аттрибуты для присваивания, так понятнее
    zoe = Person('Zoe Peterson', ['ceo','dev'], 15000)                                      # можно не указывать, так быстрее, но можно запутатся

    print(bob.name, bob.job, bob.pay)                                                       # извлечение аттрибутов, кроме имени посдтавляются стандартные значения
    print(sue.name, sue.job, sue.pay)                                                       # все экземпляры разные
    print(zoe.name, zoe.job, zoe.pay)
    print(bob.name.split()[-1])                                                             # выводим фамилию
    sue.pay *= 1.10                                                                         # увеличиваем зарплату явно
    print('%.2f' % sue.pay)                                                                 # извлекаем аттрибут экземпляра применяя форматирование строки
    print(bob.lastName(),zoe.lastName())
    print(bob.firstName(),sue.firstName(),zoe.firstName())                                  # выводим имена
    zoe.giveRaise(.10)
    print(zoe.pay)
    name = 'Den Ned'                                                                            # небольшой пример разделения имени и фамилии
    name.split()                                                                                # разделяем по пробелу
    if len(name.split()) == 2:                                                                  # если введены только Имя и фамиля то выводим фамилию                                                                                
        print(name.split()[-1])
        
        
    tom = Manager('Tom Jones', 50000)                                                           # создааем экземпляр  выполняется специальная версия
    tom.giveRise(.10)                                                                           # выполняется специальная верия
    print(tom.lastName())                                                                       # выполняется унаследованный метод                                                                 
    print(tom)                                                                                  # выполняется унаследованный __repr__
    
    print('--All three--')   
    for obj in (zoe, bob, sue, tom):                                                                 # обработать объекты обощенным способом
        obj.giveRaise(.10)                                                                      # выполнить метод giverise для этого объкта
        print(obj)                                                                              # выполнить общий метод __repr__
        
    
                                                  
