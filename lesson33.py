# f = open('file.txt', encoding='utf-8')
# text = f.read()
#
# # print(f.encoding)
# # print(type(text))
# lst = []
# for i in text:
#     print(f'{i}', end='', sep='\n')
#     lst.append(i)
# print('')
# print(lst)

# with open('file.txt', 'a',encoding='utf-8') as f:
f = open('file.txt', 'a', encoding='utf-8')
f.write('String 4\n')  # write String 4 to file
lines = ['String 11', 'String 12']
for i in lines:
    f.write(i + '\n')
# text = f.read()
print(open('file.txt', 'r', encoding='utf-8').read())
f.close()
# print(f.closed)
# print(open('file.txt', 'r', encoding='utf-8').read())