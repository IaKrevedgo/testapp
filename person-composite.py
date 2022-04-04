# для 28 главы но другой пример

class Person:
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

    def __repr__(self):
        return '[Person: %s %s]' % (self.name, self.pay)

class Manager:
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)                                          # внедрить объект Peson
    def giveRaise(self, persent, bonus=.10):
        self.person.giveRaise(persent + bonus)                                          # перехватить и делегировать
    def __getatrr__(self, attr):
        return getattr(self.person, attr)                                               # делегировать все остальные аттрибуты
    def __repr__(self):
        return str(self.person)
    
class Department:                                                                       # класс где собраны все
    def __init__(self, *args):
        self.members = list(args)
    def addMembers(self, person):
        self.members.append(person)
    def giveRaises(self, percent):
        for person in self.members:
            person.giveRaise(percent)
    def showAll(self):
        for person in self.members:
            print(person)
    

# !!!код ниже для самотестирования класса и помещен в условие, чтобы не отображаться при импорте модуля      
if __name__ == '__main__':                                                                  # испонятся только внутри текущего модуля
    bob = Person('Bob Smith')                                                               # тестирование класса
    sue = Person('Sue Jones', job = 'dev', pay =10000)                                      # можно явно указывать аттрибуты для присваивания, так понятнее
    zoe = Person('Zoe Peterson', ['ceo','dev'], 15000)                                      # можно не указывать, так быстрее, но можно запутатся
    tom = Manager('Tom Jones', 50000)                                                       



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
        
        
                                                                                                 # выполняется специальная версия
    tom.giveRaise(.10)                                                                           # выполняется специальная верия
    #print(tom.lastName())                                                                       # выполняется унаследованный метод                                                                 
    print(tom)                                                                                  # выполняется унаследованный __repr__
    
    print('--All three--')   
    for obj in (bob, sue, tom):                                                                 # обработать объекты обощенным способом
        obj.giveRaise(.10)                                                                       # выполнить метод giverise для этого объкта
        print(obj)                                                                              # выполнить общий метод __repr__
            
    deployment = Department(zoe, bob, sue)
    deployment.addMembers(tom)
    deployment.giveRaises(.10)
    deployment.showAll()