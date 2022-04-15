#база данных сотрудников
import os, csv

#INIT
# чтобы код был более читаемый выносим инит запакованный в строку вызов класса    
y = '''Personal_data(x['id'], x['name'], x['lastName'], x['midName'], x['birthDate'], x['companyName'], x['work'],
                x['workAt'], x['certificate'], x['email1'], x['email2'], x['tel1'], x['tel2'], x['citizenship'],
                x['adrCountry'], x['adrCity'], x['adrStreet'], x['adrHNum'], x['adrRNum'], x['add1'], x['add2'],
                x['add3'], x['pas1'], x['pas2'], x['pas3'], x['pasLastDate'])''' 
BDName = 'persDB.csv'                                                                                       # имя базы для файловой базы
run = 1                                                                                                     # автостарт

class Personal_data:                                                                                        # данные персонала
    def __init__(self, Person_id=None, name=None, lastName=None, midName=None, birthDate=None, companyName=None,        
                 work=None, workAt=None, certificate=None, email1=None, email2=None, tel1=None, tel2=None, citizenship=None,
                 adrCountry=None, adrCity=None, adrStreet=None, adrHNum=None, adrRNum=None, add1=None, add2=None,
                 add3=None, pas1=None, pas2=None, pas3=None, pasLastDate=None, BDName=None):
        self.id = Person_id
        self.name = name
        self.lastName = lastName
        self.midName = midName
        self.birthDate = birthDate
        self.companyName = companyName
        self.work=work
        self.workAt=workAt
        self.certificate=certificate
        self.email1=email1
        self.email2=email2
        self.tel1=tel1
        self.tel2=tel2
        self.citizenship=citizenship
        self.adrCountry=adrCountry
        self.adrCity=adrCity
        self.adrStreet=adrStreet
        self.adrHNum=adrHNum
        self.adrRNum=adrRNum
        self.add1=add1
        self.add2=add2
        self.add3=add3
        self.pas1=pas1
        self.pas2=pas2
        self.pas3=pas3
        self.pasLastDate=pasLastDate

        self.BDName = 'persDB.csv'                                                                          # имя базы данных CSV
        
    def readCsv(type=0):                                                                              # функция чтения из файла
        with open('persDB.csv','r') as csv_file:
            csvData = csv.DictReader(csv_file, delimiter=';')
            print('\n')
            for row in csvData:
                if type == 0:                                                                               # для вывода на экран
                    return row
                    #return row['id'], row['name'],row['lastName'], row['thirdName'], row['thirdName'], row['birthDate'], row['companyName'], row['work'], row['workAt'], row['certificate'], row['certificate'] 
                if type == 3:                                                                               # для вывода в консоль
                    print(row['id'], row['name'], row['lastName'], row['midName'], row['birthDate'], row['companyName'], row['work'],
                          row['workAt'], row['certificate'], row['email1'], row['email2'], row['tel1'], row['tel2'],
                          row['adrCountry'], row['adrCity'], row['adrStreet'], row['adrHNum'], row['adrRNum'], row['add1'], row['add2'], row['add3'],
                          row['pas1'], row['pas2'], row['pas3'], row['pasLastDate'])
            print('--Конец базы данных---')           
                    
    def _kart(self):                                                     # делаем сразу метод для вывода карточки сотрудника, чтобы главная прога была читабельнее
        return f'''Карточка сотрудника: \n
Персональный номер:         {self.id}
Сотрудник:                  {self.lastName} {self.name[0].upper()}. {self.midName[0].upper()}.
Дата рождения:              {self.birthDate}
Компания:                   {self.companyName}
Должность:                  {self.work}
Дата устройства на работу:  {self.workAt}
Наличие сертификатов:       {self.certificate}
Электронная почта:          {self.email1}
Электронная почта (доп.):   {self.email2}
Телефон сотрудника:         {self.tel1}
Телефон сотрудника (доп.):  {self.tel2}
Гражданство:                {self.citizenship}
Адрес проживания:           {self.adrCountry}, г. {self.adrCity}, ул. {self.adrStreet}, {self.adrHNum},  {self.adrRNum}
Дополнительная информация:  {self.add1}, {self.add2}, {self.add3}
Данные взяты из архива:     {self.BDName}           
\n''' 
                           
    def showall():
        Personal_data.readCsv(3)
    
    def __resp__():
        return (row['id'], row['name'], row['lastName'], row['midName'], row['birthDate'], row['companyName'], row['work'],
                          row['workAt'], row['certificate'], row['email1'], row['email2'], row['tel1'], row['tel2'],
                          row['adrCountry'], row['adrCity'], row['adrStreet'], row['adrHNum'], row['adrRNum'], row['add1'], row['add2'], row['add3'],
                          row['pas1'], row['pas2'], row['pas3'], row['pasLastDate'])
    
    def Upload():
        pass
    
os.system ('cls')                                                           # очищаем окно
while run == 1:                                                             
    with open (BDName) as csv_file:                                         # открываем файл ксв
        data = csv.DictReader(csv_file, delimiter = ';')                    # читаем содержимое ксв с указанием разделителя ";"
        line_count = 0
        Enter_ID = input('---Введите номер ID сотрудника(1-10): ')          # просим ввести ID сотрудника                                        
        if Enter_ID == '':                                                  # пустой ввод завершает программу
            print('---Пользователь завершил программу\n')
            run = 0                                                         # флаг завершения программы
        elif Enter_ID == 'ф':                                               # флаг для тестирования функций
            Personal_data.showall()
        elif not Enter_ID.isdigit():                                        # введеные данные не являются числом
                print('Введены неверные данные\n')
        else:
            for row in data:                                                # перебираем строки из файла
                line_count += 1                                             # сразу пропускаем 1 строку из ксв так как там описание, столбцов,а не данные
                x = dict(row)                                               # создаем словарь из разделенного сожержимого строки
                Person = eval(y)                                            # присваеваем переменной свойства класса объекта из собраной строки
                if int(Enter_ID) == int(Person.id):                         # обращение к параметру объекта
                    os.system ('cls')                                       # очищаем окно
                    print(Person._kart())                                   # вызываем метод с карточкой из класса
                    

