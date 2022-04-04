# from math import sqrt
# import time
#
# # a = 15
# # b = 11
# # c = 9
# #
# # p = (a + b + c) / 2
# # x = p * (p - a) * (p - b) * (p - c)
# # s = round(sqrt(x), 2)
# #
# #
# # pi = 3.14
# # r = 12
# #
# # s = pi * r ** 2
# #
# # print(s)
#
# # for i in range(1, 11):
# #     if i % 2 == 0:
# #         print(f'{i} число четное')
# #     else:
# #         print(f'{i} число нечетное')
#
# # name = 'Vladimir Safonov'
# # list1 = list(name.split(' '))
# # print(list1)
# # list = []
# #
# # for i in name:
# #     list.append(i)
#
# # print(list)
# #
# # some_list = [('qwe', 22), ('asd', 44), ('zxc', 66)]
# #
# # for (name, age) in some_list:
# #     print(f'{name} is {age} years old')
#
# # some_dict = {
# #     'Alex': 234,
# #     'Max': 453,
# #     'Anna': 435
# # }
# #
# # print(some_dict)
# #
# # for k, v in some_dict.items():
# #     print(f'{k} has {v} number')
#
# # list = [1 ,2, 3, 4, 5, 6, 7, 8]
# # # i = 1
# # sum = 0
# #
# # for i in list:
# #     if i % 2 != 0:
# #         # print(i)
# #         continue
# #     else:
# #         sum += i
# #         # print(sum)
# #     if sum > 10:
# #         break
# # print(sum)
# # time.sleep(1)
# # break
# # break
#
# # while True:
# #     if i <= 5:
# #         print(i)
# #         i += 1
# #         time.sleep(1)
# #     else:
# #         i = 1
# #         # print(i)
# #         continue
#
# # def get_square(r):
# #     return 3.1415 * (r ** 2)
# #
# # print(get_square(2))
# # print(get_square(3))
# # print(get_square(4))
#
# # a = ['asd', 'qwe', 'zxc']
# #
# # b = list(map(str.upper, a))
# # print(b)
#
# # age = [12, 22, 45, 2, 4, 67, 54]
# #
# # # def isAdalt(age):
# # #     return age >= 18
# #
# # isAdalt = lambda age: age >= 18
# #
# # f = filter(isAdalt, age)
# # print(list(f))
#
# # def tagMaker(func):
# #     def wrapper(*args, **kwargs):
# #         print('<div>')
# #         func(*args, **kwargs)
# #         print('</div>')
# #     return wrapper
# #
# # @tagMaker
# # def printText(text):
# #     print(text)
# #
# # printText('Hello')
# # tag1 = tagMaker(printText)
# #
# # tag1('Hello')
# #
# # import time
# # import datetime
# # from functools import wraps
# #
# # def recTime(func):
# #     @wraps(func)
# #     def wrapper(*args, **kwargs):
# #         '''
# #         Ф1
# #         '''
# #         start = datetime.datetime.now()
# #         func(*args, **kwargs)
# #         done = datetime.datetime.now() - start
# #         print(f'Функция завершена через {done} секунд')
# #
# #     return wrapper
# #
# #
# # def sfunc():
# #     time.sleep(3)
# #     print('Завершено')
# #
# # @recTime
# # def finFunc():
# #     '''
# #     Функция, которая ждет 3 сек.
# #     '''
# #     time.sleep(5)
# #     print('Завершено')
# #
# #
# # # sfunc()
# # # finFunc()
# # help(recTime)
#
# import requests
# import time
# from datetime import datetime
#
# while True:
#     try:
#         a = requests.get('https://mail1.ukr.net/')
#         print(a)
#         time.sleep(60)
#         if a == '<Response [200]>':
#             pass
#         elif a == '<Response [503]>':
#             print('Ошибка сайта')
#         else:
#             print('Иная сайта')
#     except requests.exceptions.ConnectionError:
#         error_time = datetime.now()
#         print('Сервер упал\n ' + str(error_time))
#         quit()
#
help(list)