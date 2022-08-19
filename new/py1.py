# def superset(set_1, set_2):
#     print(set_1)
#     print(set_2)
#     if set_1 > set_2:
#         print(f'Объект {set_1} является чистым супермножеством')
#     elif set_1 == set_2:
#         print(f'Множества равны')
#     elif set_1 < set_2:
#         print(f'Объект {set_2} является чистым супермножеством')
#     else:
#         print('Супермножество не обнаружено')
#
# superset("qwert", "qweru")

# from time import perf_counter_ns
#
# MAX_VALUE = 20_000
# SEARCH_ITEM = 19_999_000
#
#
# def measure_time(data):
#     start = perf_counter_ns()
#     SEARCH_ITEM in data
#     return perf_counter_ns() - start
#
# st = set(range(1, MAX_VALUE))
# lst = list(range(1, MAX_VALUE))
#
# print(f'Set search time: {measure_time(st)}ns')
# print(f'List search time: {measure_time(lst)}ns')


# import random
#
# n = int(input('Введіть число: '))
# array = list()
#
# for i in range(n):
#     array.append(random.randint(0, 30))
#
# print(array)

# from progressbar import ProgressBar
# import time
#
# pbar = ProgressBar(maxval=5)
# pbar.start()
#
# for i in range(4):
#     pbar.update(i)
#     time.sleep(i)
#
# pbar.finish()

# class Parent:
#     def __init__(self, param):
#         self.v1 = param
#
#
# class Child(Parent):
#    def __init__(self, param):
#        self.v2 = param
#
#
# obj = Child(11)
#
# print('%d %d' % (obj.v1, obj.v2))

# class A:
#     def __init__(self, i=2, j=3):
#         self.i = i
#         self.j = j
#
#     def __str__(self):
#         return A
#
#     def __eq__(self, other):
#         return self.i * self.j == other.i * other.j
#
#
# def main():
#     x = A(1, 2)
#     y = A(2, 1)
#     print(x == y)
#
# main()

# d = {"python": 40, "developer": 45}
# print(list(d.keys()))

# class A:
#     def __init__(self):
#         self.i = 1
#
#     def m(self):
#         self.i = 10
#
#
# class B(A):
#     def m(self):
#         self.i += 1
#         return self.i
#
#
# def main():
#     b = B()
#     print(b.m())
#
#
# main()


# number = 5
# even = True if number % 2 == 0 else False
# # even = number % 2 == 0
# # print("Code 3: even := {}".format(even))
# print("Code 2: even := {}".format(even))


# def factorial(n):
#     return n * factorial(n)
#
# print(factorial(3))
# string = 'qwe'
#
# if string:
#     print("Об'єкт стринг не пуст")

# class A:
#     def __init__(self):
#         self.x = 1
#         self.__y = 1
#
#     def getY(self):
#         return self.__y
#
# a = A()
# a.x = 45
# print(a.x)
# x = True
# y = False
# z = False
#
# if not x or y:
#     print(1)
# elif not x or not y and z:
#     print(2)
# elif not x or y or not y and x:
#     print(3)
# else:
#     print(4)

# counter = 1
#
# def lotsOfStaff():
#     global counter
#     for i in (1, 2, 3):
#         counter += 1
#
# lotsOfStaff()
# print(counter)

# class A():
#     def __str__(self):
#         return "A"
#
#
# class B(A):
#     def __init__(self):
#         super().__init__()
#
#
# class C(B):
#     def __init__(self):
#         super().__init__()
#
#
# def main():
#     a = A()
#     b = B()
#     c = C()
#     print(a, b, c)
#
#
# main()
#
# x = 2
# y = 1
# x *= y + 1
# print(x)
#
# list1 = [1, 3]
# list2 = list1
# list1[0] = 4
# print(list2)

# def f1(x=1, y=2):
#     x = x + y
#     y += 1
#     print(x, y)
#
# f1(y=2, x=1)
#
# my_list = [1, 5, 5, 5, 5, 1]
# max_ = my_list[0]
# index_of_max = 0
# for i in range(1, len(my_list)):
#     if my_list[i] > max_:
#         max_ = my_list[i]
#         index_of_max = i
#
# print(index_of_max)


# def chain_sum(number):
#     result = number
#     def wrapper(number2=None):
#         nonlocal result
#         if number2 is None:
#             return result
#         result += number2
#         return wrapper
#     return wrapper

# class chain_sum(int):
#     def __call__(self, addition=0):
#         return chain_sum(self + addition)
#
#
# print(1 + chain_sum(5)())
# print(1 + chain_sum(5)(2)())
# print(1 + chain_sum(5)(100)(-10)())


# def fibonacci(n):
#     a, b = 0, 1
#     for i in range(n):
#         yield a
#         a, b = b, a + b
#
# data = list(fibonacci(10))
# print(data)

# fib = lambda n: fib(n - 1) + fib(n - 2) if n > 2 else 1

# def fib(n):
#     a = 0
#     print(a)
#     b = 1
#     for i in range(n):
#         a, b = b, a + b
#         print(a)
#     return a
#
# fib(10)

# def fib(n):
#     if n <= 1:
#         return n
#     else:
#         return fib(n-1) + fib(n-2)
#
# print(fib(7))

# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print (f'{i} + FizzBuzz')
#     elif i % 3 == 0:
#         print (f'{i} + Fizz')
#     elif i % 5 == 0:
#         print (f'{i} + Buzz')
#     else:
#         print (str(i))
#
# A0 = dict(zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5)))
# print(f'A0 - {A0}')
# A1 = range(10)
# print(A1)
# A2 = sorted([i for i in A1 if i in A0])
# print(A2)
# A3 = sorted([A0[s] for s in A0])
# print(A3)
# A4 = [i for i in A1 if i in A3]
# print(A4)
# A5 = {i: i * i for i in A1}
# print(A5)
# A6 = [[i, i * i] for i in A1]
# print(A6)
# A7 = [i if i % 2 else 0 for i in A1 if 2 < i < 8]
# print(A7)
# print(','.join(str(j ** 2) for j in range(10)))

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []
#
# for x in fruits:
#   if "a" in x:
#     newlist.append(x)
#
# print(newlist)

# dictionary = [{'персона': 'человек',
#               'марафон': 'гонка бегунов длиной около 26 миль',
#               'противостоять': 'оставаться сильным, несмотря на давление',
#               'бежать': 'двигаться со скоростью'}]
#
#
# result = '; '.join([f' {value}' for key, value in dictionary[0].items()])
#
# print(result)

# dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# # Double each value in the dictionary
# double_dict1 = {v for (k, v) in dict1.items()}
# print(double_dict1)

# def calculator(expression):
#     allowed = '+-*/'
#     if not any(sign in expression for sign in allowed):
#         raise ValueError(f'Вираз повинен мати хочаб один знак ({allowed})')
#     for sign in allowed:
#         if sign in expression:
#             try:
#                 left, right = expression.split(sign)
#                 left, right = int(left), int(right)
#                 if sign == '+':
#                     return left + right
#                 elif sign == '-':
#                     return left - right
#                 elif sign == '*':
#                     return left * right
#                 else:
#                     return left / right
#             except (ValueError, TypeError):
#                 raise ValueError('Вираз повинен мати 2 целих числа та один знак')
#
#
# if __name__ == '__main__':
#     print(calculator('2+2.5'))

# array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(array[::-1][::2])

# my_dict = {'apples': 70, 'oranges': 80, 'bananas': 20, 'tomates': 30}
# print(sorted(my_dict, key=my_dict.get)[::-1])
# from pathlib import WindowsPath
#
# text = 'D:\data'
# start = WindowsPath(text + '\start.log')
#
# print(type(start))
# print(start)
# i = 1
# while i <= 10:
#     print(i)
#     i += 1
# from time import perf_counter_ns
#
# MAX_VALUE = 20_000_000
# SEARCH_ITEM = 19_999_999
#
#
# def meansure_item(data):
#     start = perf_counter_ns()
#     SEARCH_ITEM in data
#     return perf_counter_ns() - start
#
#
# st = set(range(1, MAX_VALUE))
# lst = list(range(1, MAX_VALUE))
#
# print(f'Set search time: {meansure_item(st)}ns')
# print(f'List search time: {meansure_item(lst)}ns')

# def most_frequent(list):
#     return max(set(list), key=list.count)
#
# numbers = [ 1, 2, 3, 3, 4, 2, 1, 6, 3]
#
# print(most_frequent(numbers))
# from time import sleep
# from tqdm import tqdm
#
# data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# for item in tqdm(data):
#     sleep(0.1)

# arr = [2, 2, 2, 2, 2, 2]

# def grow(arr):
#     i = 0
#     res = arr[i]
#     while i < (len(arr) - 1):
#         res *= arr[i+1]
#         i += 1
#     return res
# from math import prod as grow
#
# # def grow(arr):
# #     return prod(arr)
#
#
# print(grow(arr))

# def cockroach_speed(s):
#     return int(s / 3600 * 100000)
#
# print(cockroach_speed(s))
# e = True
# v = False
#
#
# def set_alarm(employed, vacation):
#     if employed == True and vacation == False:
#         return True
#     else:
#         return False
#
#
# print(set_alarm(e, v))
# name = 'patrick feeney'
# # name = 'Sam Harris'
#
# def abbrev_name(name):
#     res = []
#     for i in name.split():
#         res.append((i[0]).upper())
#     return '.'.join(res)
#     # return f'{name.split()[0][0].upper()}.{name.split()[1][0].upper()}'
#
# print(abbrev_name(name))

# def is_divide_by(number, a, b):
#     return (number / a == number // a) and (number / b == number // b)
#
# print(is_divide_by(-12, 2, -5))

# def digitize(n):
#     # res = []
#     # for i in str(n):
#     #     res.append(int(i))
#     # res.reverse()
#     # return res
#     return [int(i) for i in str(n)[::-1]]
#     # res.reverse()
#     # return res
#
# print(digitize(348597))

# def positive_sum(arr):
#     # new_arr = []
#     # for i in arr:
#     #     if i > 0:
#     #         new_arr.append(i)
#     # if len(new_arr) == 0:
#     #     return 0
#     # return sum(new_arr)
#     return sum([i for i in arr if i > 0])
#
#
#
# print(positive_sum([1, 2, 3, 4, 5]))
#
# def solution(string, ending):
#     return string.endswith(ending)
#
#
# # print('string'[-2::])
# print(solution('abcde', ''))

# def square_sum(numbers):
#     # res = []
#     # for i in numbers:
#     #     res.append(i * i)
#     return sum(pow(i, 2) for i in numbers)
#
#
# print(square_sum([0, 3, 4, 5]))


# def high_and_low(numbers):
#     num = numbers.split(' ')
#     list_num = list(num)
#     res = []
#     for i in list_num:
#         res.append(int(i))
#     return f"{max(res)} {min(res)}"
#
#
# print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))

# text = "This is an example!"
#
# def reverse_words(text):
#     # res = ''
#     # for i in text.split(' '):
#     #     res += i[::-1] + ' '
#     return ' '.join((i[::-1]) for i in text.split(' '))
#
# print(reverse_words(text))

# def count_bits(n):
#     return bin(n).count('1')
#
#     # return bin(n)
#
#
# print(count_bits(10))

# def create_phone_number(n):


# prefix = ''
# for i in n:
#     prefix += str(i)
# res = ''.join(str(i) for i in n)
# return f'({res[:3]}) {res[3:6]}-{res[6:]}'
#     return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
#
#     # return f'({prefix})'
#     # print(prefix)
#
# print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

# from aiohttp import web
#
# routes = web.RouteTableDef()
#
# @routes.get('/')
# async def hello(request):
#     return web.Response(text="Hello, wsdfasdfsadf")
#
# app = web.Application()
# app.add_routes(routes)
# web.run_app(app, port=5000)

# def filter_list(list):
#     return [l for l in list if type(l) is int]

# print(filter_list([1, 'a', 'b', 0, 15]))
# import math

#
# def square_digits(num):
#     return int(''.join([str(int(i) ** 2) for i in str(num)]))
#
#
# print(square_digits(9119))

# def find_smallest_int(arr):
#     return min(arr)
#
# print(find_smallest_int([34, -345, -1, 100]))

# age: int = 5
# print(age)

# set = {0, 5}
# print(type(set))
#
# a = 'sdf;asdfasdg;wqr'
# a.split(';')
# print(len(a))

# print(list(reversed(range(1,11))))
#
# list = [1,2,3,4]
# print(list[-2])
#
#
# my_list = [1, 'asf', 2]
# my_list[1] = 'qwe'
# print(my_list)

# import numpy as np
# a = {2, 1, 3, 4}
# a.add(4)
# a.add(4)
# a.add(5)
# print(a)

# def friend(x):
#     return [i for i in x if len(i) == 4]
#
#
# print(friend(["Ryan", "Kieran", "Mark",]))
# import warnings
# import warnings
# from datetime import datetime
# import pytz

# def make_readable(seconds):
#     m, s = divmod(seconds, 60)
#     h, m = divmod(m, 60)
#     return f'{h:02d}:{m:02d}:{s:02d}'

# def make_readable(seconds):
#     m, s = divmod(seconds, 60)
#     h, m = divmod(m, 60)
#     print(h)
#     return f'{h:02d}:{m:02d}:{s:02d}'
#
#
# print(make_readable(60))

# def tribonacci(signature, n):


# print([fibonacci_of(n) for n in range(15)])
#
# from functools import lru_cache
# import sys
#
# sys.setrecursionlimit(5000)
#
#
# @lru_cache()
# def recursiveFibCached(n):
#     if n in {0, 1}:
#         return 1
#     return recursiveFibCached(n - 1) + recursiveFibCached(n - 2)
#
#
# def iterativeFib(n):
#     a, b = 0, 1
#
#     for _ in range(n):
#         a, b = b, a + b
#
#     return a
#
# import time
#
# # print(recursiveFibCached(4990))
# # print(iterativeFib(1000000))
#
# import decimal
#
#
# def formulaFibWithDecimal(n):
#     decimal.getcontext().prec = 1000000
#     root_5 = decimal.Decimal(5).sqrt()
#     phi = ((1 + root_5) / 2)
#     a = ((phi ** n) - ((-phi) ** -n)) / root_5
#     return round(a)
#
#
# # print(formulaFibWithDecimal(1000000))
# start_time = time.time()
# # iterativeFib(1000000)
# formulaFibWithDecimal(1000000)
# print(time.time() - start_time, "seconds")

# lst = [1, 4, 4, 4, 2, 5, 6, 6, 7, 8, 9, 10]
#
#
# def maxim(text):
#     print(set(text))
#     return max(set(text), key=text.count)
#
# print(maxim(lst))

# occurrences = Counter(lst)
# values = sorted(list(occurrences.values()))
# # print(occurrences)
# print(values[-
# from collections import Counter
#
# def xo(s):
#     res = Counter(s.lower())
#     return res['o'] == res['x']
#
# print(xo("xxxoo"))
# def number(bus_stops):
#     # sum = 0
#     # for i in bus_stops:
#     #     sum += i[0] - i[1]
#     return sum(i - o for i, o in bus_stops)
#
#
# print(number([[3, 0], [9, 1], [4, 10], [12, 2], [6, 1], [7, 10]]))

# def fibo(n):
#     lst = []
#     a, b = 0, 1
#     lst.append(a)
#     for _ in range(n-1):
#         a, b = b, a + b
#         lst.append(a)
#     return lst

# def fibo(n):
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a+b
#     return a
#
# print(fibo(10))

# a = {2, 3, 4, 5}
# b = {4, 5, 6, 7}
# res = a ^ b
# print(res)
# import requests
# #
# # response = requests.get(url='https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json')
# # currencies = response.json()
# response = requests.get(url='https://api.exchangerate-api.com/v4/latest/USD').json()
# currencies = response.get('rates')
#
# print(currencies)
# from collections import Counter
#
# def anagrams(word, words):
#
#     return [w for w in words if Counter(word) == Counter(w)]
#
# print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))

# def narcissistic(value):
#     # sum = 0
#     # for i in value:
#     #     sum += i ** len(value)
#     # iter_value = str(value)
#     # for i in iter_value:
#     #     int(i) ** len(iter_value)
#     return value == sum(int(i) ** len(str(value)) for i in str(value))
# 
# print(narcissistic(153))

# import names
#
# # name = names.get_full_name(gender='male')
#
# for _ in range(5):
#     print(names.get_full_name(gender='female'))

# from art import *
#
# art_1 = art("coffee")
# print(art_1)
#
# art_2 = art("woman", number=2)
# print(art_2)
#
# print(art("random"))
# aprint("butterfly")
# print(randart())
#

# from pathlib import Path
#
# def mp3_to_pdf(file_path, language = 'en'):
#     if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
#         print('File is exist!')
#     else:
#         print('File does not exist! Check the file path.')
#     print(Path(file_path).stem)
#
# def main():
#     mp3_to_pdf('D:\PythonProjects\TextToMp3\Programming task.pdf')

# a = {'a':['b'], ['b']:'a'}


# def pr(s = '123', q='qwe'):
#     print("\"{}\" - {}".format(s,q))
#
# pr()

# if __name__ == '__main__':
#     main()

# array1 = [True,  True,  True,  False,
#           True,  True,  True,  True ,
#           True,  False, True,  False,
#           True,  False, False, True ,
#           True,  True,  True,  True ,
#           False, False, True,  True ]
#
#
# def count_sheeps(sheep):
#     # count = 0
#     # for i in array1:
#     #     if i is True:
#     #         count += 1
#     return sum(i for i in array1)
#
# def main():
#     print(count_sheeps(array1))
#
# if __name__ == '__main__':
#     main()

# import socket
#
# def get_ip_by_hostname():
#     hostname = input('Pelase enter the site name (URL): ')
#
#     try:
#         return f'Hostname: {hostname}\nIP address: {socket.gethostbyname(hostname)}'
#     except socket.gaierror as error:
#         return f'Invalid hostname - {error}'
#
# def main():
#     print(get_ip_by_hostname())
#
# if __name__ == '__main__':
#     main()

# def bool_to_word(boolean):
#     # if boolean == True:
#     return 'Yes' if boolean is True else 'No'
# elif:
#     return 'No'

# def decode_morse(morse_code):
#     # #
#     result_string = ''
#     MORSE_CODE = {
#         'A': '.-', 'B': '-...', 'C': '-.-.',
#         'D': '-..', 'E': '.', 'F': '..-.',
#         'G': '--.', 'H': '....', 'I': '..',
#         'J': '.---', 'K': '-.-', 'L': '.-..',
#         'M': '--', 'N': '-.', 'O': '---',
#         'P': '.--.', 'Q': '--.-', 'R': '.-.',
#         'S': '...', 'T': '-', 'U': '..-',
#         'V': '...-', 'W': '.--', 'X': '-..-',
#         'Y': '-.--', 'Z': '--..', '1': '.----',
#         '2': '..---', '3': '...--', '4': '....-',
#         '5': '.....', '6': '-....', '7': '--...',
#         '8': '---..', '9': '----.', '0': '-----',
#         'SOS': '...---...', '!': '--..--', ',': '--..--',
#         '.': '.-.-.-', '?': '..--..', '/': '-..-.',
#         '-': '-....-', '(': '-.--.', ')': '-.--.-'
#     }
#     # for i in morse_code.split('   '):
#     #     for j in i.split(' '):
#     #         for key, value in MORSE_CODE.items():
#     #             if j == value:
#     #                 result_string += key
#     #     result_string += ' '
#     return result_string.strip(' ')
#     # return morse_code.replace('.', MORSE_CODE['.']).replace('-', MORSE_CODE['-']).replace(' ', '')

# def main():
#     print(decode_morse('...---...'))
#
#
# if __name__ == '__main__':
#     main()

#
# import tornado.ioloop
# import tornado.web
#
# class MainHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.write("Hello, world")
#
# def make_app():
#     return tornado.web.Application([
#         (r"/", MainHandler),
#         (r'/(favicon.ico)', tornado.web.StaticFileHandler, {"path": ""}),
#     ])
#
# if __name__ == "__main__":
#     app = make_app()
#     app.listen(8000)
#     tornado.ioloop.IOLoop.current().start()

# from celery import Celery
#
# app = Celery('tasks', broker='redis://localhost')
#
# @app.task
# def add(x, y):
#     return x + y
#
# def rank(st, we, n):
#     alphabet = {
#         'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
#         'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23,
#         'x': 24, 'y': 25, 'z': 26
#     }
#     sum_dict = {}
#     x = 0
#     if st == '':
#         return 'No participants'
#     elif len(we) < n:
#         return 'Not enough participants'
#     else:
#         for i in st.split(","):
#             lst = list(i.lower())
#             value_list = []
#             value_list.append(len(i))
#             for j in lst:
#                 for k, v in alphabet.items():
#                     if j == k:
#                         value_list.append(v)
#             sum_dict.update({i: (sum(value_list) * we[x])})
#             x += 1
#         sorted_values_list = sorted(sum_dict.values())
#         sorted_values_list.reverse()
#         result_dict = {}
#         for k, v in sum_dict.items():
#             if v == sorted_values_list[n - 1]:
#                 result_dict.update({k: v})
#         if len(result_dict.values()) == n:
#             # print(list(result_dict))
#             return list(result_dict)[-1]
#         return sorted(result_dict.keys())[0]


# print(rank("Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin", [4, 2, 1, 4, 3, 1, 2], 1))
# print(rank("Lagon,Lily", [1, 5], 2))
# print(rank("Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin", [4, 2, 1, 4, 3, 1, 2], 8))
# print(rank("", [4, 2, 1, 4, 3, 1, 2], 6))
# print(rank('Aubrey,Olivai,Abigail,Chloe,Andrew,Elizabeth', [3, 1, 4, 4, 3, 2], 4))
# print(rank('Elijah,Chloe,Elizabeth,Matthew,Natalie,Jayden', [1, 3, 5, 5, 3, 6], 2))


# print(True + True)

# def bin_to_decimal(inp):
#     return int(inp, 2)
#
# print(bin_to_decimal("101010"))

# from collections import deque
#
# myDeque = deque([1, 2, 3, 4, 5])
#
# print('Deque is:', myDeque)

# import os
#
# PATH = 'D:\PythonProjects'
# dirCount = 0
# filesCount = 0
#
# for root, directories, files in os.walk(PATH):
#     for dir in directories:
#         dirCount += 1
#     for file in files:
#         filesCount += 1
#
# print('Count of Directories is: ', dirCount)
# print('Count of Files is: ', filesCount)

# def to_camel_case(text):
#     textList = text.replace('_', '-').split('-')
#     resText = textList[0]
#     for word in textList[1:]:
#         resText += word.capitalize()
#     return resText
#
# print(to_camel_case('the_stealth_warrior'))

# def validate_pin(pin):
#     # if len(pin) == 4 or len(pin) == 6) :
#     #     for i in pin:
#     #         return i.isdigit()
#     # else:
#     #     return
#     # # return i.isdigit() for i in pin
#
#     return pin.isdigit() and len(pin) in (4, 6)
#
#
# print(validate_pin('123'))

# def count_smileys(arr):
#     count = 0
#     for i in arr:
#         if (':' in i or ';' in i) and ((')' in i or 'D' in i) or ('~' in i or '-' in i)):
#             if ':' in i:
#                 if ':)' in i or ':D' in i:
#                         count += 1
#                 if ':~' in i or ':-' in i:
#                     if ':~)' in i or ':~D' in i or ':-)' in i or ':-D' in i:
#                         count += 1
#             if ';' in i:
#                 if ';)' in i or ';D' in i:
#                         count += 1
#                 if ';~' in i or ';-' in i:
#                     if ';~)' in i or ';~D' in i or ';-)' in i or ';-D' in i:
#                         count += 1
#     return count
#
#
# # print(count_smileys([':oD', '(-P', ';~D', '(D', ';D', 'o)', '8)', '5D', '(D', ';D', '4-dD', '5~)', ':)', '8~x', '5o)',
# #                      ';d', ';-x', '4ox', 'oxd', ';)d', '5~x)', '(x)', '~D', '5D', 'pP', 'o)', ';8)', 'pD']), 4)
# # print(count_smileys([':D', ':~)', ';~D', ':)', ';)']), 5)
# # print(count_smileys([':)', ':(', ':D', ':O', ':;']), 2)
# print(count_smileys([';]', ':[', ';*', ':$', ';-D']), 1)
# print(count_smileys(["xyz:-)", ":-)xyz", ":--);~-)", ":~))))", "))));D", "123;-D12"]), 5)


# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#
# def pre_order(node):
#     if node:
#         print(node.value)
#         pre_order(node.left)
#         pre_order(node.right)
#
# def post_order(node):
#     if node:
#         post_order(node.left)
#         post_order(node.right)
#         print(node.value)
#
# def in_order(node):
#     if node:
#         in_order(node.left)
#         print(node.value)
#         in_order(node.right)
#
# tree = Node(1)
# tree.left = Node(2)
# tree.right = Node(3)
# tree.left.left = Node(4)
# tree.left.right = Node(5)
# tree.right.left = Node(6)
# tree.right.right = Node(7)
#
#
# # pre_order(tree)
# # post_order(tree)
# in_order(tree)
# a = int(input('Enter a: '))
# b = int(input('Enter b: '))
# if a and b:
#     print(a * b)
# else:
#     'Enter the a and b'

# def countSumChars(text):
#     alphabet = {
#         1: 'aeioulnstr',
#         2: 'dg',
#         3: 'bcmp',
#         4: 'fhvwy',
#         5: 'k',
#         8: 'jx',
#         10: 'qz'
#     }
#     lowerText = text.lower()
#     return sum([k for i in lowerText for k, v in alphabet.items() if i in v])
#
# print(countSumChars('QQZZK'))

# emails = {'mgu.edu': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'kirill_stepanov'],
#           'gmail.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
#           'msu.edu': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
#           'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'],
#           'harvard.edu': ['john.doe', 'mark.zuckerberg', 'helen_hunt'],
#           'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']}
#
# print(*sorted({i + '@' + k for k, v in emails.items() for i in v}), sep='\n')
# # print(*sorted([i + '@' + k for k, v in emails.items() for i in v]), sep='\n')

# text = 'Дмитрий считает, что текст в скобках (например (asdfasdf) вот такой) читать не надо. Написать программу, которая ' \
#        'убирает скобки (и все что внутри них)().'
#
# def shortener(st):
#     while '(' in st or ')' in st:
#         left = st.rfind('(')
#         right = st.find(')', left)
#         st = st.replace(st[left:right + 1], '')
#     return st
#
# print(shortener(text))

# import time
#
# start_time = time.time()
# def do_something():
#     a = 5
#     b = 10
#     c = a ^ b
# do_something()
# time.sleep(5)
# end_time = time.time()
# do_time = end_time - start_time
#
# print('Program execution time is: ', do_time)

# def alphanumeric(password):
#     # if not password.isalnum():
#     #     return False
#     # elif password == "":
#     #     return False
#     # elif " " in password:
#     #     return False
#     # else:
#     #     return True
#     return password.isalnum()
#
# print(alphanumeric("Company123"))

# square = lambda n: n ** 2
# arg = 5
#
# print(f"Square of {arg} is {square(arg)}")

# def cleaned_str(st):
#     clean_lst = []
#     for symbol in st:
#         if symbol == '@' and clean_lst:
#             clean_lst.pop()
#         elif symbol != '@':
#             clean_lst.append(symbol)
#     return ''.join(clean_lst)
#
#
# print(cleaned_str('гр@оо@лк@оц@ва'))
# print(cleaned_str('сварка@@@@@лоб@ну@'))
#

# prime_numbers = [2, 3, 5, 7]
#
# removed_element = prime_numbers.pop()
#
# print('Removed Element:', removed_element)
# print('Updated List:', prime_numbers)
#
# # Output:
# # Removed Element: 5
# # Updated List: [2, 3, 7]

# def array_diff(a, b):
#     return [x for x in a if x not in b]
#
# print(array_diff([1,2,2,2,3],[2]))

# def alphabet_position(text):
#     alphabet = {
#         'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
#         'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23,
#         'x': 24, 'y': 25, 'z': 26
#     }
#     return " ".join([str(v) for i in text.lower() for k, v in alphabet.items() if i == k])
#
# print(alphabet_position("The sunset sets at twelve o' clock."))


# def rgb(r, g, b):
#     def rec(x):
#         if 0 <= x <= 255:
#             return ("{:02x}".format(x)).upper()
#         elif x > 255:
#             return 'FF'
#         else:
#             return '00'
#     return rec(r) + rec(g) + rec(b)
#
#
# print(rgb(-20, 275, 125))

# def move_zeros(lst):
#     zero_lst = []
#     nonzero_lst = []
#     for i in lst:
#         if i == 0:
#             zero_lst.append(i)
#         else:
#             nonzero_lst.append(i)
#     return nonzero_lst+zero_lst
#
# print(move_zeros([1, 0, 1, 2, 0, 1, 3]))

# def nb_year(p0, percent, aug, p):
#     count = 0
#     while p0 < p:
#         p0 += int(p0 * (percent / 100)) + aug
#         count += 1
#     return count
#
#
# print(nb_year(1500, 5, 100, 5000))
# print(nb_year(1500000, 2.5, 10000, 2000000))
# print(nb_year(1500000, 0.25, 1000, 2000000))

# def add_binary(a, b):
#     return bin(a + b)[2:]
#
#
# print(add_binary(1, 1))
# print(add_binary(0, 1))

# x = format('+', '*>4')
# print(x)
# print(dir(x))
# from itertools import combinations
#
# xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
#
# def choose_best_sum(t, k, list):
#     return max((sum(i) for i in combinations(list, k) if sum(i) <= t), default=None)
#
#     # return sorted(res)
#
# print(choose_best_sum(230, 4, xs))
# print(choose_best_sum(430, 5, xs))
# print(choose_best_sum(430, 8, xs))

# def invert(lst):
#     # res = []
#     # for i in lst:
#     #     if i != 0:
#     #         res.append(0-i)
#     #     else:
#     #         res.append(0)
#     return [(0 - i) if i != 0 else 0 for i in lst]
#
#
# print(invert([1, -2, 3, -4, 5]))
# print(invert([]))
# print(invert([0]))

# def first_non_consecutive(arr):
#     for i in range(0, len(arr)-1):
#         if (arr[i + 1] - arr[i]) > 1:
#             return arr[i + 1]
#
#
# print(first_non_consecutive([1, 2, 3, 4, 6, 7, 8]))
# print(first_non_consecutive([1, 2, 3, 4, 5, 6, 7, 8]))

# def get_count(sentence):
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     # count = 0
#     # for i in sentence:
#     #     if i in vowels:
#     #         count += 1
#     # return count
#     return sum(i in vowels for i in sentence)
#
# print(get_count("abracadabra"))

# def paint_letterboxes(start, finish):
#     return [([int(j) for i in range(start, finish + 1) for j in str(i)].count(digit)) for digit in range(0, 10)]
#
# print(paint_letterboxes(125, 132))
# # paint_letterboxes(123, 125)
#

# class RomanNumerals:
#
# def to_roman(val):
#     result = ""
#
#     if val >= 1000:
#         m = val // 1000
#         result += "M" * m
#         val -= m * 1000
#         to_roman(val)
#     elif 100 <= val < 1000:
#         if val >= 500:
#             result += "D"
#             val -= 500
#             to_roman(val)
#         if val < 500:
#             c = val // 100
#             result += "C" * c
#             val -= c * 100
#             to_roman(val)
#     elif 10 <= val < 100:
#         if val >= 50:
#             result += "L"
#             val -= 50
#             to_roman(val)
#         if val < 50:
#             x = val // 10
#             result += "X" * x
#             val -= x * 10
#             to_roman(val)
#     else:
#         if val >= 5:
#             result += "V"
#             val -= 5
#             to_roman(val)
#         if val < 5:
#             if val == 4:
#                 result += "VI"
#                 to_roman(val)
#             else:
#                 result += "I" * val
#     return result
#
# # print(to_roman(5))
# print(to_roman(25))

# def get_drinks(number_of_guests: int, step: int) -> int:
#     for i in range(1, number_of_guests+1, step):
#         print(i)
#     # return sum([i for i in range(0, number_of_guests+1, step)])
#
# print((get_drinks(10, 3)))

# from typing import Union
#
#
# def calculate_profit(amount: int, percent: Union[float, int], period: int) -> Union[float, int]:
#     dep = amount
#     start = 0
#     while start < period:
#         amount += (amount * percent / 100)
#         start += 1
#     profit = amount - dep
#     return round(profit, 2)
#
#
# # print(calculate_profit(1000, 5, 1))
# print(calculate_profit(12500, 3, 12))
# def make_abbr(words: str) -> str:
#     # res = []
#     # for word in words.split(' '):
#     #     res.append(word[0].upper())
#     return ''.join([word[0].upper() for word in words.split(' ') if words != ""])
#
# print(make_abbr(""))

# def is_werewolf(target: str) -> bool:
#     text = ''
#     for i in target:
#         if i.isalpha():
#             text += i
#     if text == text[::-1]:
#         return True
#     else:
#         return False
#
# # print(is_werewolf("racecar"))
# # print(is_werewolf("home"))
# print(is_werewolf("red rum sir is murder?"))

# def get_success_rate(statistics: str) -> int:
#     if statistics:
#         success_student_list = []
#         for i in statistics:
#             success_student_list.append(int(i))
#         sum_of_success_student = sum(success_student_list)
#         lenght = len(statistics)
#         return round(sum_of_success_student / lenght * 100)
#     else:
#         return 0

# def happy_birthday() -> None:
#     name = input("What's your name? ")
#     print(f"Hi, {name}!")
#
# happy_birthday()

# def parity_checker() -> None:
#     digit = input("What number do you want to check?")
#     if (int(digit) % 2) == 0:
#         print('Even')
#     else:
#         print('Odd')

# def get_location(coordinates: list, commands: list) -> list:
#     command = {
#         'forward': [0, 1],
#         'back': [0, -1],
#         'right': [1, 0],
#         'left': [-1, 0],
#     }
#     for c in commands:
#         for k, v in command.items():
#             if c in k:
#                 coordinates = [sum(x) for x in zip(coordinates, v)]
#     return coordinates
#
#
# print(get_location([0, 0], ["forward", "right"]))
# print(get_location([2, 3], ["back", "back", "back", "right"]))
# print(get_location([0, 5], ["back", "back", "back", "right", "left", "forward"]))
#
# import math
#
#
# def get_plan(current_production: int, month: int, percent: int):
#     res = []
#     for i in range(0, month):
#         current_production += math.floor(current_production * percent / 100)
#         res.append(current_production)
#     return res
#     # return [(current_production += math.floor(current_production * percent / 100)) for i in range(0, month)]
#
#
# print(get_plan(1000, 6, 30))  # [1300, 1690, 2197, 2856, 3712, 4825]
# print(get_plan(500, 3, 50))  # == [750, 1125, 1687]

# from math import floor
#
#
# def get_speed_statistic(test_results: list) -> list:
#     if test_results:
#         res = []
#         minimum = min(test_results)
#         maximum = max(test_results)
#         med = floor(sum(test_results)/len(test_results))
#         res.append(minimum)
#         res.append(maximum)
#         res.append(med)
#     return res
#     # return [min(test_results), max(test_results), floor(sum(test_results)/len(test_results))]

# print(get_speed_statistic([10, 10, 11, 9, 12, 8]))

# def split_string(string: str) -> list:
#     res = []
#     if len(string) % 2 == 0:
#         work_string = string
#     else:
#         work_string = string+'_'
#     for i in range(0, len(work_string)):
#         print(i)
#         if (i % 2) == 0:
#             res.append(work_string[i:i+2])
#     return res
#
# print(split_string('asd'))

# def scrolling_text(string: str) -> list:
#     res = []
#     for i in range(0, len(string)):
#         res.append(string.upper())
#         string = (string[1:] + string[0]).upper()
#     return res
#     # return [(string[1:] + string[0]).upper() for i in range(0, len(string))]
#
# print(scrolling_text("robot"))
#
# def check_number(number: int) -> list:
#     res = []
#     if number > 0:
#         res.append(True)
#     else:
#         res.append(False)
#     if number % 2 == 0:
#         res.append(True)
#     else:
#         res.append(False)
#     if str(number)[-1] == '0':
#         print(str(number)[-1])
#         res.append(True)
#     else:
#         res.append(False)
#     return res
#
# print(check_number(3))
# print(check_number(10))

# def get_lists_sum(ls1: list, ls2: list) -> int:
#     return sum(ls1+ls2)
#
# print(get_lists_sum([1, 2], [3, 4]))# == 10  # 1 + 2 + 3 + 4 = 10
# print(get_lists_sum([], [])) # == 0

# def combine_lists(ls1: list, ls2: list) -> list:
#     return [sum(x) for x in zip(list1, list2)]
# def is_special_number(number: int) -> str:
#     special = [1, 2, 3, 4, 5]
#     for i in str(number):
#         if int(i) not in special:
#             return 'NOT!!'
#     return 'Special!!'
#
#
# print(is_special_number(23))
# print(is_special_number(39))

# def is_tidy(number: int) -> bool:
#     return number == int(''.join(sorted(str(number))))
#
# print(is_tidy(123))

# def is_palindrome(string: str) -> bool:
#     # text = ''
#     # for i in string:
#     #     if i.isdigit():
#     #         return False
#     #     if i.isalpha():
#     #         text += i
#     # if text == text[::-1]:
#     #     return True
#     # else:
#     #     return False
#     return string == string[::-1]
# print(is_palindrome('palin0dnilap'))
# print(is_palindrome('anna'))

# def get_unique_items(ls: list) -> list:
#     return list(set(ls))
#
# print(get_unique_items([1, 2, 4, 4]))

# def get_three_largest(ls: list) -> list:
#     return sorted(ls)[-3:]
#
# print(get_three_largest([1, 4, 2, 3, -1]))# == [4, 2, 3]
# print(get_three_largest([]))# == []
# print(get_three_largest([2, 10]))# == [2, 10]
#
# import re
# data = b'A:B,C'
# x = re.split(b'[:,]', data)[1].decode()
# print(x)

# import antigravity
# word = 'mississippi'
# counter = {}
#
# for letter in word:
#     counter[letter] = counter.get(letter, 0) + 1
#
# print(counter)

# def descending_order(num):
#     # lst = []
#     # for i in str(num):
#     #     lst.append(i)
#     # result = sorted([i for i in str(num)])[::-1]
#     # result.reverse()
#     return int(''.join(sorted(str(num), reverse=True)))
#
# print(descending_order(15))

# def longest(a1, a2):
#     return ''.join(sorted(set(a1 + a2)))
#
# print(longest("aretheyhere", "yestheyarehere"))

# def count_positives_sum_negatives(arr):
#     if len(arr) == 0:
#         return []
#
#     pos = 0
#     neg = 0
#     for i in arr:
#         if i > 0:
#             pos += 1
#         elif i < 0:
#             neg += i
#
#     return [pos, neg]
#
# print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]), [10, -65])
# print(count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]), [8, -50])
# print(count_positives_sum_negatives([1]), [1, 0])
# print(count_positives_sum_negatives([-1]), [0, -1])
# print(count_positives_sum_negatives([0, 0, 0, 0, 0, 0, 0, 0, 0]), [0, 0])
# print(count_positives_sum_negatives([]), [])

# def find_short(text):
#     # res = []
#     # for word in text.split(' '):
#     #     res.append(len(word))
#     # # sorted(res)
#     # # print(sorted(res))
#     return sorted([len(word) for word in text.split(' ')])[0]
#
#
# print(find_short("bitcoin take over the world maybe who knows perhaps"), 3)
# print(find_short("turns out random test cases are easier than writing out basic ones"), 3)
# print(find_short("lets talk about javascript the best language"), 3)
# print(find_short("i want to travel the world writing code one day"), 1)
# print(find_short("Lets all go on holiday somewhere very cold"), 2)
# print(find_short("Let's travel abroad shall we"), 2)

# def fake_bin(x):
#     # result = ''
#     # for i in x:
#     #     if int(i) < 5:
#     #         result += '0'
#     #     else:
#     #         result += '1'
#     return ''.join(['0' if int(i) < 5 else '1' for i in x])
#
# print(fake_bin('45385593107843568'))

# def pig_it(text):
#     return ' '.join((word[1:]+word[0]+'ay') if word.isalpha() else word for word in text.split(' '))
#
# print(pig_it('Pig latin is cool'))

#
# def func(x):
#     intermediate_var = x ** 2 + x + 1
#
#     if intermediate_var % 2:
#         y = intermediate_var ** 3
#     else:
#         y = intermediate_var ** 3 + 1
#
#     # setting attributes here
#     func.optional_return = intermediate_var
#     func.is_awesome = 'Yes, my function is awesome.'
#
#     return y
#
#
# y = func(3)
#
# print('Final answer is', y)
# print('Show calculations -->', func.optional_return)
# print('Is my function awesome? -->', func.is_awesome)


# my_list = ['some', 'list', 'containing', 'five', 'elements']
#
# min_len = 3
#
# for element in my_list:
#     if len(element) < min_len:
#         print(f'Caught an element shorter than {min_len} letters')
#         break
# else:
#     print(f'All elements at least {min_len} letters long')

# print(bool(print(print(5))))
#
# lst = ['Python', 'C#', 'Java']
# i = iter(lst)
# next(i)
# print(next(i))

# import os
#
# current_directory = os.getcwd()
# os.chdir(r'C:\Users\restg\Downloads')
# list_dir = os.listdir()
# for dir in list_dir:
#     if dir.endswith('.zip'):
#         os.remove(dir)
#     print(dir)

# x = 23
# num = 0 if x > 10 else 11
# print(num)

# a = ['GSW', 'LAKERS', 'CLIPPERS']
# b = [1, 2, 3]
#
# print(dict(zip(a, b)))

# def reverse_words(text):
#     # result = []
#     # for word in text.split(' '):
#     #     print(word[::-1])
#     #     # reversed_word = reversed(word)
#     #     # result.append(reversed_word)
#     return ' '.join([word[::-1] for word in text.split(' ')])
#
# print(reverse_words('This is an example!'))

# def create_phone_number(n):
#     # str_n = ''
#     # for i in n:
#     #     str_n += str(i)
#     # return f'({str_n[:3]}) {str_n[3:7]}-{str_n[7:10]}'
#     return '({}{}{}) {}{}{}-{}{}{}{}'.format(*n)
#
# print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

# a = 5
# b = 10
# a, b = b, a
#
# print(a, b)

