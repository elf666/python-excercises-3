# stworz pakiet matematyka
# w nim stworz moduly: algebra i geometria
# w module algebra stworz funkcje mnozaca liczbe a przez b
# w module geometria stworz funkcje obliczajaca pole trapezu (1/2 * (a + b) * h)
#
# zaimportuj modul algebra jako algebra i geometria jako geometria (uzyj as)
# przy uzyciu funkcji z tych modulow oblicz iloczyn 111 * 222
# oraz policz pole trapezu o podstawach a=6, b=7 i wysokosci h=4
#
# przetestuj kilka rodzajow importu:
# import pakiet.modul -> wywolanie funkcji przez pakiet.modul.funkcja
# from pakiet import modul -> wywolanie przez modul.funkcja
# from pakiet.modul import funkcja -> wywolanie przez funkcja

# import matematyka.algebra
# import matematyka.geometria
#
# print(matematyka.algebra.pomnoz_a_przez_b(111,222))
# print(matematyka.geometria.pole_trapezu(1,2,3))

# import matematyka.algebra as algebra
# import matematyka.geometria as geometria
#
# print(algebra.pomnoz_a_przez_b(111,222))
# print(geometria.pole_trapezu(1,2,3))

# from matematyka import algebra
# from matematyka import geometria
#
# print(algebra.pomnoz_a_przez_b(111,222))
# print(geometria.pole_trapezu(1,2,3))

from matematyka.algebra import pomnoz_a_przez_b
from matematyka.geometria import pole_trapezu

print(pomnoz_a_przez_b(111,222))
print(pole_trapezu(1,2,3))









# import matematyka.algebra as algebra
# import matematyka.geometria as geometria
# from matematyka import algebra
# from matematyka import geometria
# from matematyka.algebra import pomnoz_a_przez_b
# from matematyka.geometria import pole_trapezu

# print(algebra.pomnoz_a_przez_b(111, 222))
# print(geometria.pole_trapezu(6, 7, 4))
# print(pomnoz_a_przez_b(111, 222))
# print(pole_trapezu(6, 7, 4))
