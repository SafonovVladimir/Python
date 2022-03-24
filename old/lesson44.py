import re

s = 'Это просто новая строка текста. А это еще одна строка текста. И еще одна строка текста'
pattern = 'строка'

# def search(str, s):
#     if str.__contains__(s):
#         return True
# else:
#     return False


# print(pattern in s)

# if re.search(pattern, s):
#     print('Yes')
# else:
#     print('No')

match = re.findall(pattern, s)
print(match)
