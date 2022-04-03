from math import sqrt

# a = 15
# b = 11
# c = 9
#
# p = (a + b + c) / 2
# x = p * (p - a) * (p - b) * (p - c)
# s = round(sqrt(x), 2)
#
#
# pi = 3.14
# r = 12
#
# s = pi * r ** 2
#
# print(s)

# for i in range(1, 11):
#     if i % 2 == 0:
#         print(f'{i} число четное')
#     else:
#         print(f'{i} число нечетное')

# name = 'Vladimir Safonov'
# list1 = list(name.split(' '))
# print(list1)
# list = []
#
# for i in name:
#     list.append(i)

# print(list)

some_list = [('qwe', 22), ('asd', 44), ('zxc', 66)]

for (name, age) in some_list:
    print(f'{name} is {age} years old')
