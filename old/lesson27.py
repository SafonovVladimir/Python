# def get_sum(*args):
#     print(args)
#
#
# get_sum(1, 2)

# def get_sum(**kwargs):
#     print(kwargs)
#
#
# get_sum(a=1, b=2)

def f(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)


f(1, 2, 3, 4, 5, 5, 7, c=2, d='sdg')
