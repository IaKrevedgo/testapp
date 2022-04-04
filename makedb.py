from personFinal import Person, Manager                                                                                 # закгружаем наши классы из последней итерации

bob = Person('Bob Smith')
sue = Person('Sue Jones', job='dev', pay = 10000)
tom = Manager('Tom Jones', 50000)
zoe = Person('Zoe Givershment', job = ['dev','ceo'], pay = 15000)

import shelve

db = shelve.open('persondb')                                                                                            # имя файла в котором хранятся объекты
for obj in (bob, sue, tom, zoe):                                                                                        # использовать атрибут name в качестве ключа
    db[obj.name] = obj                                                                                                  # сохранить объект shelve по ключу
db.close()                                                                                                              # закрыть после изменений


import glob
print(glob.glob('persondb*'))                                                                                           # ищет в каталоге нужные файлы
print(open('persondb.dir').read())                                                                                      # открываем dir файл созданный вместе с bd
print(open('persondb.dat','rb').read())                                                                                 # пытаемся открыть двоичный файл но выдает чушь

db = shelve.open('persondb')                                                                                            # повторно открыть хранилище shelve, расширение можно не указывать
print(len(db))                                                                                                          # база содерижт 4 записи
print(list(db.keys()))                                                                                                  # ключи (имена) являются индексами
bob = db['Bob Smith']                                                                                                   # извлеч объект bob по ключу
print(bob)                                                                                                              # выполняет __repr__ из AttrDisplay
print(bob.lastName())                                                                                                   # выполняет lastName из Person

for key in db:
    print(key, '=>', db[key])                                                                                           # выводим все ключи и значения циклом

for key in sorted(db):                                                                                                  # выводим отсортированные ключи
    print(key, '=>', db[key])
