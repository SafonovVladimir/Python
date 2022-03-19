# arr = [1, 2, 3, 'even', 4, 5, 44, 7, 'odd']


# def odd_ball(arr):
#     global x
#     for i in arr:
#         if arr.__contains__(arr.index('odd')):
#             x = 'True'
#         else:
#             x = 'False'
#     return x
#
#
# print(odd_ball([1, 2, 3, 'even', 4, 5, 44, 7, 'odd']))
# print(odd_ball([1, 2, 3, 'even', 4, 5, 8, 7, 'odd']))
# print(odd_ball([1, 2, 3, 'even', 4, 5, 44, 7, 9,'odd']))

# def find_sum(x):
#     lst = []
#     for value in range(1, x + 1):
#         if (value % 3 == 0) or (value % 5 == 0):
#             lst.append(value)
#         else:
#             continue
#     total = sum(lst)
#     return total

# def find_sum(x):
#     return sum([i for i in range(1, x + 1) if (i % 3 == 0) or (i % 5 == 0)])
#
# print(find_sum(5))
# print(find_sum(10))
names = ['Ryan', 'John', 'David', 'Jessika', 'Vova', 'sdf', 'asdf', 'asfasdf']

def get_name_with_4_letters(names):
    # lst = []
    # for name in names:
    #     # print(name)
    #     if len(name) == 4:
    #         lst.append(name)
    # return lst
    return ([name for name in names if len(name) == 4])

print(get_name_with_4_letters(names))
# get_name_with_4_letters(names)