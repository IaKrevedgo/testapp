# программка для вытаскивания данных из файла ксв в консоль
import os, csv                                                              # импортируем нужные модули

# INIT
# чтобы код был более читаемый выносим инит запакованный в строку вызов класса    
y = '''Personal_data(x['Pers_id'], x['Pers_name'], x['Pers_family'],
                x['Pers_midname'], x['Pers_bdate'], x['Pers_job'],
                       x['Pers_dep'], x['Pers_email'], x['Pers_tel'])''' 
run = 1                                                                     # запуск программы
class Personal_data:                                                        # класс с параметрами сотрудника
    def __init__(self, Person_id, Person_name, Person_family,
                 Person_midname, Person_bdate, Person_job, Person_dep,
                 Person_email, Person_tel):
        self.id = Person_id
        self.name = Person_name
        self.family = Person_family
        self.midname = Person_midname
        self.bdate = Person_bdate
        self.job = Person_job
        self.dep = Person_dep
        self.email = Person_email
        self.tel = Person_tel
 
    def _kart(self):                                                     # делаем сразу метод для вывода карточки сотрудника, чтобы главная прога была читабельнее
        return f'''Карточка сотрудника: \n
Персональный номер: {self.id}
Сотрудник:          {self.family} {self.name[0]}. {self.midname[0]}.
Отдел:              {self.dep}
Должность:          {self.job}
Дата рождения:      {self.bdate}
Электронная почта:  {self.email}
Телефон сотрудника: {self.tel[0]} ({self.tel[1:4]}) {self.tel[4:7]} {self.tel[7:9]} {self.tel[9:11]}            
\n'''
                                 
os.system ('cls')                                                           # очищаем окно
while run == 1:                                                             
    with open ('personal.csv', encoding='UTF-8') as csv_file:               # открываем файл ксв
        data = csv.DictReader(csv_file, delimiter = ';')                    # читаем содержимое ксв с указанием разделителя ";"
        line_count = 0
        Enter_ID = input('---Введите номер ID сотрудника(1-10): ')          # просим ввести ID сотрудника                                        
        if Enter_ID == '':                                                  # пустой ввод завершает программу
            print('---Пользователь завершил программу\n')
            run = 0                                                         # флаг завершения программы
        elif not Enter_ID.isdigit():                                        # введеные данные не являются числом
                print('Введены неверные данные\n')
        else:
            for row in data:                                                # перебираем строки из файла
                line_count += 1                                             # сразу пропускаем 1 строку из ксв так как там описание, столбцов,а не данные
                x = dict(row)                                               # создаем словарь из разделенного сожержимого строки
                Person = eval(y)                                            # присваеваем переменной свойства класса объекта из собраной строки
                if int(Enter_ID) == int(Person.id):                         # обращение к параметру объекта
                    os.system ('cls')                                       # очищаем окно
                    print(Person._kart())                                # вызываем метод с карточкой из класса
             