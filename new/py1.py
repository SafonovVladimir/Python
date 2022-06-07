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

arr = [2, 2, 2, 2, 2, 2]

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
s = 1.09


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

