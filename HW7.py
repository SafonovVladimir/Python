# arr = [1, 2, 3, 'even', 4, 5, 44, 7, 'odd']


def odd_ball(arr):
    global x
    for i in arr:
        if arr.__contains__(arr.index('odd')):
            x = 'True'
        else:
            x = 'False'
    return x


print(odd_ball([1, 2, 3, 'even', 4, 5, 44, 7, 'odd']))
print(odd_ball([1, 2, 3, 'even', 4, 5, 8, 7, 'odd']))
print(odd_ball([1, 2, 3, 'even', 4, 5, 44, 7, 9,'odd']))
