# Глава 28 БОЛЕЕ РЕАЛИСТИЧНЫЙ ПРИМЕР КЛАССОВ

from person import Person                                                                       # импортируем класс из файла person.py
bob = Person('Bob Smith')
print(bob)                                                                                      # вызывается __repr__ объекта bob
print(bob.__class__)
print(bob.__class__.__name__)                                                                   # показывает класс и его имя для bob
print(bob.__dict__.keys())                                                                      # показывает все аттрибуты для класса bob
for key in bob.__dict__:
    print(key, '=>', getattr(bob, key))                                                         # сопоставляет аттрибуты и имена в экземпляре bob
