# stworz nowy pakiet i nazwij go 'muzyka'
# w nim stworz dwa moduly: britney i iron_maiden
# w britney stworz funkcje sing() ktora drukuje "Ups I did it again"
# w iron_maiden stworz funkcje sing() ktora drukuje "666 the number of the beast"
# nie zapomnij o specjlanym pliku potrzebnym do stworzenia pakietu
# 1
# zaimportuj i uruchom funkcje sing dla britney i iron_maiden uzywajac:
# package_name.module_name.function_name
# 2
# uruchom te funkcje uzywajac tylko module_name.function_name
# 3
# uruchom te funkcje dla britney i iron_maiden uzywajac tylko nazwy funkcji
# sprobuj rozwiazac problem, ktory sie pojawi



# 1
# import music.britney
# import music.iron_maiden
#
# music.britney.sing()
# music.iron_maiden.sing()


# 2
# from music import britney
# from music import iron_maiden
#
# britney.sing()
# iron_maiden.sing()


# 3
# from music.britney import sing as sing_britney
# from music.iron_maiden import sing as sing_iron_maiden
#
# sing_britney()
# sing_iron_maiden()
