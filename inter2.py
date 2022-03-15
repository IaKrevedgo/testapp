# сведение последовательностей


def intersect(*args):
    res = []
    for x in args[0]:                                           # просмотре первой последовательности       
        if x in res: continue                                   # пропуск дубликатов
        for other in args[1:]:                                  # для всех остальных аргументов
            if x not in other: break                            # элемнт находится в овсех последовательностях? если нет: выйти из цикла
        
        else:                   
            res.append(x)                                         # да, добавить элементы в конец
    return res   
def union(*args):
    res = []
    for seq in args:                                            # для всех аргументов
        for x in seq:                                           # для всех узлов
            if not x in res:
                res.append(x)                                   # добавить новые элементы к резульату
    return res

                                               