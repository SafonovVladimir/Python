# class Axe:
#
#     def __init__(self, x: int, y: int):
#         self.x = x
#         self.y = y
#
#
# if __name__ == '__main__':
#     axe = Axe(x=5, y=18)
# #
# print(axe.x)
# print(axe.y)
#
# del axe
# # print(axe.x)
# # print(axe.y)

dic = {}
print(type(dic))
tup = {'1', '2', '3', '4', '5'}
print(type(tup))
print(tup)

text = 'World Hello New'
print(text)


def rev(word):
    # new_word = ''.join(reversed(word))
    new_word = word[::-1]
    return new_word.upper()


# my_list = list()

lst = list(text.split(" "))
print(lst)

result = []
for i in lst:
    result.append(rev(i))

new_string = ' '.join(result)

print(new_string)

#
#
#
# lst.reverse()
# print(''.join(lst))
# print(''.join(reversed(text)))
# # print(text[::-1])
