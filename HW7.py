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

def find_sum(x):
    for value in range(1, x+1):
        if value % 3 == 0:
            print(value)
        else:
            continue
    # return a

find_sum(6)