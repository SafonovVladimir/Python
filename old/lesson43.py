# def get_square(num):
#     return num ** 2
#
#
# print(get_square(10))

# get_square = lambda num: num ** 2
# print(get_square(5))

# print((lambda num: num ** 2)(7))
# print((lambda num: num ** 2)(5))
# print((lambda num: num ** 2)(10))

l = [1, 2, 3]  # получить список 2, 4, 6 с помощью лямбда-функции


def get_double():
    return list(map(lambda num: num * 2, l))


print(get_double())
