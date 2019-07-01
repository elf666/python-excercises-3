# stworz plik tekstowy abc.txt zawierajacy trzy linijki:
# a
# b
# c
# otworz plik w trybie do odczytu
# przeczytaj wszystkie jego linijki i wypisz je na ekran,  stosujac na kazdej metode
# upper()
# nie wypisuj znakow nowej linijki
# nie zapomnij zamknac pliku


f = open('abc.txt','r')
for line in f:
    print(line[:-1].upper())
f.close()

# f = open('abc.txt','r')
# content = f.read().splitlines()
# for s in content:
#     print(s.upper())

# f = open('abc.txt','r')
# for line in f:
#     if line[-1] == '\n':
#         line = line[:-1]
#     print(line.upper())





# abc = open("abc.txt", "r")
#
# for line in abc:
#     print(line[:-1].upper())
#
# abc.close()
