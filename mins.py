# функция min
# три версиси написания функции min
# если аргументов нет то выдаст ошибку

def min1(*args):
    res = args[0]
    for arg in args[1:]:                                    # откидываем первй и остальные сравниваем
        if arg < res:                                       # если элемент оказался меньше первого то заменяем его и выводим
            res = arg
    return res

def min2(first, *rest):
    for arg in rest:                                        # сравниваем остальные с первым и если они меньше то назначаем первым и выводим
        if arg < first:
            first = arg
    return first

def min3(*args):                                            # сортируем по возрастанию список с помощью функции sort
    tmp = list(args)
    tmp.sort()
    return tmp[0]                                           # возвращаем первый элемент


def minmax(test, *args):                                    # вместо test подставляем функцию
    res = args[0]
    for arg in args[1:]:
        if test(arg, res):
            res = arg
    return res

def lessthan(x, y): return x < y                            # больше
def grtrthan(x, y): return x > y                            # меньше


print(min1(3, 4, 5, 6, 1, 2))
print(min2('bbbb', 'aaaa'))                                 # работает также со строками
print(min3([1, 2],[1, 3],[2, 2],[1,1]))

print(minmax(lessthan, 3, 4, 5, 1 ,66, 74))
print(minmax(grtrthan, 3, 234, 5, 1 , 66, 74))