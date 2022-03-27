# import sys

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
