# def hello():
#     return 'Hello. I\'m function "Hello"'
#
#
# def super_func(func):
#     print('Hello. I\'m function "SUPER_FUNC"')
#     print(func())
#
#
# super_func(hello)

# def hello():
#     return 'Hello. I\'m function "Hello"'
#
#
# print(hello())
#
# test = hello
# print(test())

# def my_decorator(func):
#     def func_wrapper():
#         print('Code before')
#         func()
#         print('Code after')
#     return func_wrapper
#
# @my_decorator
# def func_test():
#     print('Hello. I\'m func "Func_Test"')

# test = my_decorator(func_test)
# test()

# func_test()


def make_title(fn):
    def wrapped():
        title = fn()
        title = title.capitalize()
        title = title.replace(',', '')
        return title
    return wrapped

@make_title
def hi():
    return 'hello,,,, World!'

print(hi())
