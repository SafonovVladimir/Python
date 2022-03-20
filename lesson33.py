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
# f.write('String 4\n')  # write String 4 to file
lines = ['String New1', 'String New2']
# for i in lines:
#     f.write(i + '\n')
# text = f.read()
f.writelines(f'{i}\n' for i in lines)
f.close()
print(open('file.txt', 'r', encoding='utf-8').read())
# f.close()
# print(f.closed)
# print(open('file.txt', 'r', encoding='utf-8').read())