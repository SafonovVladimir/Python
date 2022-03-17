# l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print([i * 2 for i in l1])

# l1 = [1, 2, 3]
# res = 0
# for num in l1:
#     res += num ** 2
# print(res)

# time = float(input('Введите время: '))
# print('litres = ' + str(int(time / 2)))

s = str(input('Введите строку: '))
if ' ' in s:
    s = s.upper()
else:
    s = s.lower()
print(s)
