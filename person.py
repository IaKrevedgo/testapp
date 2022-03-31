# пример программы для главы 28
class Person:
    def __init__(self, name, job=None, pay=0):                                          # конструктор принимает 3 аргумента, все аргументы справа от стандартного должны быть тоже присваиваемыми
        self.name = name                                                                # заполнить поля при создании
        self.job = job                                                                  # self - новый экземпляр класса
        self.pay = pay
        x
    def lastName(self):
        if len(self.name.split()) == 2:                                                 # если указаны имя и фамилия
            return self.name.split()[-1]                                                # берем фамилию
        
    def firstName(self):   
        if len(self.name.split()) == 2:                                                 # если указаны имя и фамилия
            return self.name.split()[0]                                                 # берем имя
        
    def giverise(self, percent=0.0):                                                    # увеличиваем зарплату
        self.pay = int(self.pay * (1 + percent))


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
    zoe.giverise(.10)
    print(zoe.pay)


name = 'Den Ned'                                                                            # небольшой пример разделения имени и фамилии
name.split()                                                                                # разделяем по пробелу
if len(name.split()) == 2:                                                                  # если введены только Имя и фамиля то выводим фамилию                                                                                
    print(name.split()[-1])
