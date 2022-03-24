# i = 1
# while i <= 10:
#     print(i, end=', ')
#     i += 1
#
# s = 'Hello World!'
# for l in s:
#     if l == ' ':
#         continue
#     print(f'"{l}"', end=' ')

# s = 'HelloWorld!'
# for l in s:
#     if l == ' ':
#         break
#     print(f'"{l}"', end=' ')
# else:
#     print("\nNo spaces")
from datetime import date

first_year = 1900
todays_year = date.today().year
lst = []
while first_year <= todays_year:
    lst.append(first_year)
    first_year += 1
print(lst)
