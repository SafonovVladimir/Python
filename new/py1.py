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



number = 5
even = True if number % 2 == 0 else False
# even = number % 2 == 0
# print("Code 3: even := {}".format(even))
print("Code 2: even := {}".format(even))


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
