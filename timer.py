# Любительские инструменты для измерения времени выолнения вызовов функций.
# Определяет суммарное время, лучшее время и лучшее суммарное время.

import time, sys

timer = time.time if sys.platform[:3] == 'win' else time.time               # условие не работает так как куда-то делся time.clock из питона 3.10     

def total (reps, func,*pargs, **kargs):
    ''' 
    Сумарное время выполнения функции func() reps раз
    Возращает (усммарное времяб последний результат)
    '''
    repslist = list(range(reps))                                            # Вынесены ха пределы
    start = timer()
    for i in repslist:
        ret = func(*pargs, **kargs)
        elasped = timer() - start
    return (elasped, ret)

def bestof (reps, func, *pargs, **kargs):
    ''' 
    Самая быстрая функция func() среди reps запусков.
    Возвращает (лучшее время, последний результат)
    '''
    best = 2 ** 32                                                          # 136 лет будет достаточно
    for i in range(reps):
        start = timer()
        ret = func(*pargs, **kargs)
        elapsed = timer() - start
        if elapsed < best: best = elapsed
    return (best, ret)

def bestoftotal(reps1, reps2, func, *pargs, **kargs):
    ''' 
    Лучшее суммарное время из resp1 запусков
    '''
    return bestof(reps1, total, reps2, func, *pargs, **kargs)
