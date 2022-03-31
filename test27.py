# ОСНОВЫ НАПИСАНИЯ КЛАССОВ

class Firstclass:                                                                           # определяем объект класса
    def setdata(self, value):                                                               # определить метод класса
        self.data = value                                                                   # self это экземпляр
    def display(self):
        print(self.data)                                                                    # self.data: для каждого экземпляра
        
x = Firstclass()                                                                            # создаем два экземпляра
y = Firstclass()                                                                            # оба представляют собой новое пространство имен

x.setdata('IaKrevedgo')                                                                     # вызывать метод: self - это х
y.setdata(3.14159)                                                                          # выполняется firstclass.setdata(y, 3.14159)

x.display()                                                                                 # self.data отличается в каждом экземпляере
y.display()                                                                                 # Выполняется Firstclass.display(y)

x.data = 'New value'                                                                        # можно получать и устанавливать аттрибуты
x.display()                                                                                 # отображает новый атрибут
x.newattribute = 'IaBLOKO'                                                                  # можно устанавливать новые атрибуты и затем обращаться к ним
print(x.newattribute)

class Secondclass(Firstclass):                                                              # наследует setdata
    def display(self):                                                                      # изменяет display
        print('Current value = "%s"'% self.data)

z = Secondclass()
z.setdata(42)                                                                               # находит setdata в классе Firstclass
z.display()                                                                                 # Находит переопределенны метод в Secondcalss
x.display()

class Thirdcalss(Secondclass):                                                              # унаследован от SecondClass
    def __init__(self, value):                                                              # вызывается для ThirdClass
        self.data = value
    def __add__(self, other):                                                               # Вызывается self + other
        return Thirdcalss(self.data + other)
    def __str__(self):                                                                      # вызыватся для print(self, str())
        return '[Thirdclass: %s]' % self.data
    def mul(self, other):                                                                   # изменение на месте: именованный метод
        self.data *= other

a = Thirdcalss('abc')                                                                       # вызывается __init__
a.display()                                                                                 # вызывается унаследованный метод,
print(a)                                                                                    # вызывается __mul__
b = a + 'xyz'                                                                               # __add__ создает новый экземпляр
b.display()                                                                                 # b имеет все методы класа Thirdclass
print(b)                                                                                    # __str__ возвращает отображаемую строку

a.mul(3)                                                                                    # mul изменяет класс на месте
print(a)                                                                                    # возвращает измененную строку

class rec: pass                                                                             # класс - заглушка
rec.name = 'bob'                                                                            # Добавляем новый аттрибут
rec.age = 40                                                                                # и еще один
print(rec.name)                                                                             # извлекаем аттрибут по имени класса

x = rec()                                                                                   # наследуем имена класса
y = rec()

print(x.name, y.name)                                                                       # name хранится только в классе. Оба экземплаяра ссылюатся на него
x.name = 'Sue'                                                                              # присваиваем аттрибуту экземпляра собственное значение

print(rec.name, x.name, y.name)                                                             # тут x.name уж ссылатеся на свое значение уникальнеое для х

print(list(rec.__dict__.keys()))                                                            # выводим все аттрибуты класса rec
print(list(name for name in rec.__dict__ if not name.startswith('__')))                     # выводим только наши аттрибуты без стандартных
print(list(x.__dict__.keys()))                                                              # У х свой аттрибут name, потомушо его присваивали выше
print(list(y.__dict__.keys()))                                                              # У у нет своих аттрибутов

print(x.name, x.__dict__['name'])                                                           # представленные тут атрибуты являются ключами словаря
print(x.age)                                                                                # но извлечение аттрибута проверяется также классы, выхов тут словаря выдаст исключение

print(x.__class__)                                                                          # показывает связь с классом
print(b.__class__)

print(rec.__bases__)                                                                        # показывает ссылку наобъект суперкласса
print(Thirdcalss.__bases__)

def uppername(obj):
    return obj.name.upper()                                                                 # требует аргумент self(obj)

print(uppername(x))                                                                         # вызываем функцию на экземпляр класса
rec.method = uppername                                                                      # теперь uppername метод класса rec!!!!
print(x.method())                                                                           # запустить метод для обработки х
print(y.method())                                                                           # и для y

rec.method(x)                                                                               # можно вызывать через экземпляр или класс



sec = ('Bob', 40.5, ['dev','mgr'])                                                          # запись на основе кортежа                                                
print(sec[0])

sec = {}    
sec['name'] = 'Bob'                                                                         # запись на основе словаря
sec['age'] = 40.5
sec['jobs'] = ['dev', 'mgr']

print(sec['name'])

class zec: pass                                                                             # запись на основе класса
zec.name = 'Bob'
zec.age = 40.5
zec.jobc = ['dev','mgr']

print(zec.name)

Pers1 = rec()                                                                               # запись на основе экземпляров
Pers2 = rec()
Pers2.name = 'Yohan'
Pers2.age = 20
Pers2.jobs = ['dev','ceo']

print(Pers1.name, Pers2.name)

class Person:
    def __init__(self, name=None, jobs=None, age=None):                                               # класс = данные + логика
        self.name = name
        self.jobs = jobs
        self.age = age
    def info(self):
        return (self.name, self.jobs, self.age)                                             
    
rec1 = Person('Bob',['dev', 'mrg', 40.5])                                                   # вызов конструктора
rec2 = Person('Sue',['dev','ceo'])                                                          # тут пишет None, если не присвоен аттрибут age
rec3 = Person()                                                                             # если пустой запрос то и пустой ответ!!
print(rec1.jobs, rec2.info(), rec3.info())                                                  # вызов атрибута, вызов методы





