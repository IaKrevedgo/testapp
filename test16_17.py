# Глава 16 ФУНКЦИИ

def times(x, y):                                            # простая функция с двумя аргументами
    return x*y                                              # действие функции
print(times(2, 8))                                          # вывод на экран результатов при введенных двух аргументах

x = times(2, 8)                                             # можно записать результат в переменную и вызвать потом
print(x)
print(times('Ia', 4))                                       # вводим разные типы



def intersect (seq1, seq2):                                 # функция вывода общего из 2 последовательностей
    res = []                                                # изначально обнуляем последовательность
    for x in seq1:                                          # дял элементов из последовательности 1
        if x in seq2:                                       # если он же есть в последовательности 2
            res.append(x)                                   # добавляем в новый список
    return res                                              # результат - новй список

s1 = 'IaKrevedgo'                                           # задаем списки для сравнений
s2 = '@venger'
print(intersect(s1, s2))                                    # выводим результат работы функции      
print(intersect([1,2,3,4],(1,4,6)))                         # выбираем из разных типов




# Глава 17 ОСНОВЫ ОБЛАСТЕЙ ВИДИМОСТИ

# глобальная область вдимости
X = 99                                                      # имена X и func присваиваются в модуле: глобальные
def func (Y):                                               # имена Y и Z присваиваются в функции: локальные
    # локальная область видимости
    Z = X + Y                                               # имя X является глобальным
    return Z
print(func(1))                                              # имя func в модуле: result = 1000


X = 88                                                      # глобальная переменная
def fun():
    X = 99                                                  # локальная переменная
fun()
print(X)                                                    # выведет глобальную переменную

# то же самое только с global
X = 88                                                      # глобальная переменная
def fun2():
    global X
    X = 99                                                  # теперь тут обращение к глобальной переменной
fun2()
print(X)                                                    # выводит значение после функции

def maker(N):                                               # функция с первым аршументом
    def action(X):                                          # вложеная функция со вторным аргументом
        return(X ** N)                                      # вложенная функция возвовдит в степень
    return action                                           # исходная функция возвращает результат

f = maker(2)                                                # тут присваем аргумент N
print(f)                                                    # Без второго аргумента вывозит только описание функции
print(f(3))                                                 # со вторым аргументом Х уже вовзводит в степень и выводит результат
print(f(4))

g = maker(3)                                                # заново вызываем функцию и присваиваем N = 3
print(g(3))                                                 # тут уже функция вызывается с N = 3
print(f(4))                                                 # но предыдущее присваивание переменной также работает с N = 2

def maker1(N):                                              # тот же прием, только с использованием функции lambda, без второго def
    return lambda X: X ** N

h = maker1(3)
print(h(4))


def f1():
    x = 88                                          
    f2(x)                                                   # вместо ретурна вызываем тут следующую функцию с присвоенным в первой функции параметром х

def f2(x):
    print(x)

f1()                                                        # выводит 88

def makeActions():
    acts = []
    for i in range(5):
        acts.append(lambda x, i=i: i ** x)                  # присваиваем переменную i из цикла, иначе не будет работать!
    return acts

acts = makeActions()
print(acts[0])                                              # с одним аргументом не работает
print(acts[0](2))                                           # с двумя аргументами будет работать (первы элемент списка 1..5, второй степень x из функции)
print(acts[1](2))

def f1():                                                   # в куче вложенных функций всеравно передается х из f1()
    x = 898                                                 # НУЖНО ИЗБЕГАТЬ таких вложений, лучше написать несколько функций подряд
    def f2():
        def f3():
            print(x)
        f3()
    f2()
    
f1()    

def tester(start):
    state = start
    def nested(label):
        print(label, state)                                 # берет state из объемлющей области, должен по идеи выводить start и state
    return nested
F = tester(2)
F('IaKrevedgo')                                             # если в функции есть принт то моно print не писат

def tester1(start):
    state = start
    def nested(label):
        nonlocal state                                      # дулаем стейт общим для всей функции включая вложения
        print(label, state)
        state += 1                                          # после каждого вызова функции будет добавлятся +1 к сетйту
    return nested

F = tester1(0)
F('Iakrevedgo')
F('Venger')
F('Stephan')
G = tester1(44)                                             # если присвоить функцию другой переменной, то счетик пойжет со значения start в ней и не удет влиять на пердыдущий
G('qwerty')
G('trewq')
F('Valhala')                                                # тут продожается первый счетчик

def tester3(start):
    global state                                            # обявление global необходимо во всех вложенных функций
    state = start
    def nested(label):
        global state
        print(label, state)
        state += 1
    return nested

F = tester3(0)   
F('hui')
F('iuh') 

G = tester3(44)                                             # если использовался global, то state в предыдущей переменной такжеперезаписывается
G('grow')
G('Viwa')
F('zilda')                                                  # вызывется предыдущая переменная, но state уже берется из нового с инкриментом +2 (46)

class testerC:                                              # альтернатива на основе класса
    def __init__ (self, start):                             # при создани обектов состояние
        self.state = start                                  # явно сохраняем в новом объекте
    def nested(self, label):                    
        print(label, self.state)                            # явная ссылка на состояние
        self.state += 1                                      # изменения также вохзможны

Z = testerC(0)                                              # создание экземпляра, вызов __init__
Z.nested('IaKrevedgo')                                      # F передается аргументу self
Z.nested('fire')

G = testerC(22)                                             # каждый экземпляр поулчает новую куопию состояния
G.nested('Brain')                                           # изменеие одного не влияет на остальные
Z.nested('Grill')                                           # состояние F осталось прежним
print(Z.state)                                              # можно получить доступ к состоянию

class testerC2:                                             # класс написанный более правильно
    def __init__(self, start):
        self.state = start
    def __call__(self, label):                              # перехватывает прямые обращения к экземпляру
        print(label, self.state)                            # таким образом .nested не требуется
        self.state += 1
H = testerC2(0)
H('firefox')                                                # вызывает __call__
H('police')        

def tester4(start):
    def nested(label):
        print(label, nested.state)
        nested.state += 1                                   # тут изменяется атрибут, а не сама функция nested
    nested.state = start
    return nested

F = tester4(0)
F('IaKrevedgo')
F('Zigan')
print(F.state)                                              # также можно получить доступ к состоянию извне

G = tester4(11)
G('Zhiza')
G('Bratuha')
F('Gloria')
print(G.state, F.state)                                     # не влияет на статусы в предыдущей функции
print(F is G)                                               # можно сравнивать проверкой. В данном случае выдает false

A = open('script2.py')
print('\n', A.read())

from makeopen import makeopen                               # вызываем функцию из стороннего модуля
makeopen('IaKrevedgo')                                      # специальный open
A = open('script2.py')
print('\n', A.read())

makeopen('Zira')
A = open('script2.py')
print('\n', A.read())
 



#УПРАЖНЕНИЯ
    
X = 'SPAM'
def func():
    print(X)
func()

X = 'spam'
def func():
    X = 'Ni'

func()
print(X)  

X = 'spam'
def func():
    X = 'Ni'
    print(X)
func()
print(X)  
  
X = 'sss'
def func():
    global X
    X = 'ni'
func()
print(X)

X = 'Iak'
def func():
    X = 'MIU'
    def nested():
        print(X)
    nested()
func()
print(X)

def func():
    X = 'NNNI'
    def nested():
        nonlocal X
        X = 'spam'
    nested()
    print(X)
func()


      