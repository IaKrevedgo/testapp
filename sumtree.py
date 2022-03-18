def sumtree(L):
    tot = 0
    for x in L:
        if not isinstance(x, list):
            tot += x
        else:
            tot += sumtree(x)
    return tot

L  = [1, [2, [3, 4], 5], 6, [7, 8]]                                 # произвольное вложение
print(sumtree(L))                                                   # выводит 36
print(sumtree([1, [2, [3, [4, 5]]]]))                               # выводит 15
print(sumtree([[[[[1], 2], 3], 4], 5]))                             # выводит 15


import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(10000)
print(sys.getrecursionlimit())
   