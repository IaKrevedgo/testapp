S = 'IaKrevedgo'
sum = 0
for a in S:
    sum = sum + ord(a)                                                  # считаем сумму всех элементов по одному
    print(ord(a), end= ' ')
print('Сумма всех аскикодов = ',sum)
print('А это список из всех букв в аски кодах= ', [ord(a) for a in S])  # список вложения вместо цикла

for i in range(5):
    print('hello %d\n\a' % i)
    
L = {124:'q', 12:'w', 23:'e', 14:'r', 75:'t', 86: 'y'}

print(sorted(L.keys()), ' ')


