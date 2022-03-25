import time
def timer(func, *args):                                                             # упрощенная функция измерения времени
    start = time.time()                                                             # в книжке исполовался time.clock() но в питоне 3.10 эта функция была заменена на time.time()
    for i in range(1000):
        func(*args)
    return time.time() - start                                                      # сумарное измерение времени в секундаъ