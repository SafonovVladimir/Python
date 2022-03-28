# import sys
#
def hello(name='World'):
    print("Hello, {}!".format(name))
hello('Wowa')

text = 'qwerty'

print(''.join(reversed(text)))
print(text[::-1])
print(''.join(text[::-1]))

s = ''
for i in reversed(text):
    s += i
print(s)

# import re
#
# s = "Tim's phone numbers are 12345-41512 and 78963 85214"
# match = re.findall(r'\d{5}', s)
#
# if match:
#     print(match)