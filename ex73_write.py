# stworz liste trzydziestu kolejnych liczb naturalnych podzielnych przez 17
# przy uzyciu konstrukcji with - as oraz .writelines() wpisz te liste do pliku,
# kazda liczbe w osobnej linijce

counter = 0
number = 1
L = list()
while(counter < 30):
    if number % 17 == 0:
        L.append(str(number)+'\n')
        counter += 1
    number += 1

with open("numbers.txt", 'w') as f:
    f.writelines(L)










# counter = 0
# number = 0
# L = list()
# while (counter < 31):
#     if number % 17 == 0:
#         L.append(str(number) + "\n")
#         counter += 1
#     number += 1
#
# with open("podzielne_przez_17.txt","w") as f:
#     f.writelines(L)
