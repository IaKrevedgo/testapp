#Глава 6-7
import copy,sys
x= 1
y=3

x= copy.copy(y)


L1 = [2,3,4]
L2 = L1[:] #создать копию L1
L1[0] = 24
print(L1)
print(L2)
print(x == 5)

print(sys.getrefcount(1))