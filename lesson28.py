# def get_sum(a, b):
#     """
#     Возвращает сумму аргументов а и b.
#
#     """
#     return a + b
#
#
# print(get_sum(1, 2))
a = 5
# def f():
#     a = 10
#     a += 1
#     print(id(a))
# print(id(a))
# f()
# print(id(a))

# def f():
#     global a
#     a += 1
#
# f()
# print(a)

l = [1, 2, 4, 5]


# print([i * 2 for i in l])

# def f(l):
#     return [i * 2 for i in l]
#
# print(f(l))

def get_mult(x):
    return x * 2


def f2(l):
    return [get_mult(i) for i in l]

print(f2(l))