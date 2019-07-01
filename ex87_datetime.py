# napisz funkcje mierzaca czas wykonywania innej funkcji
#
# napisz funkcje szukajaca zadanej liczby w liscie majacej 10 000 000 elementow
# przy uzyciu petli for
#
# napisz funkcje szukajaca zadanej liczby w liscie majacej 10 000 000 elementow
# przy uzyciu randrange(10000000)
# porownaj czasy wykonywania obu funkcji



from datetime import *
from random import *

def calculate_exec_time(function, function_arg):
    start = datetime.now()
    function(function_arg)
    stop = datetime.now()
    print(f"Funkcja {function.__name__} wykonywala sie {stop-start} czasu.")

def find_num_using_for(number_to_find):
    for n in range(10000001):
        if n == number_to_find:
            return True

def find_num_using_randrange(number_to_find):
    while True:
        n = randrange(10000001)
        if n == number_to_find:
            return True

calculate_exec_time(find_num_using_for,9999999)
calculate_exec_time(find_num_using_randrange,9999999)














# import datetime
# from random import *
#
# def calculate_exec_time(function, number_to_find):
#     start = datetime.datetime.now()
#     function(number_to_find)
#     stop = datetime.datetime.now()
#     print(f"Funkcja {function.__name__} wykonywala sie {stop - start} sekund.")
#
# def find_a_for(a):
#     for n in range(10000000):
#         if n == a:
#             return True
#     return False
#
# def find_a_rand(a):
#     while True:
#         found = randrange(10000000)
#         if found == a:
#             return True
#
# calculate_exec_time(find_a_for, 9999999)
# calculate_exec_time(find_a_rand, 9999999)
