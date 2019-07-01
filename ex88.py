# przy uzyciu petli for uruchomionej 100 razy oraz funkcji randrange
# stworz liste 100 losowych
# integerow z przedzialu 1 - 10
#
# przy uzyciu kolejnej petli przejrzyj te liste i odnotuj w slowniku
# czestotliwosc wystepowania na niej poszczegolnych wartosci

from random import *

L = list()
D = dict()

for _ in range(100):
    rand_num = randrange(1,11)
    L.append(rand_num)

for num in L:
    if num in D.keys():
        D[num] += 1
    else:
        D[num] = 1

suma = 0
for key in D:
    suma += D[key]

print(suma)











# from random import *
#
# input_list = list()
#
# for _ in range(100):
#     input_list.append(randrange(1,11))
#
# D = dict()
#
# for num in input_list:
#     if num in D.keys():
#         D[num] += 1
#     else:
#         D[num] =1
#
# print(D)
