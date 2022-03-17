# words = ['мадам', 'топот', 'test', 'madam', 'word']
# w2 = []
# for i in words:
#     lst = ''.join(reversed(i))
#     if lst == i:
#         w2.append(i)
# print(w2)
# for i in words:
#     if i != i[::-1]:
#         words.remove(i)
# print([i for i in words if i == i[::-1]])
my_lst = ['Око за око', 'Около Миши молоко', 'А роза упала на лапу Азора']
polydromes = []
for word in my_lst:
    word_r = word.replace(' ', '').lower()
    if word_r == word_r[::-1]:
        polydromes.append(word)
print(polydromes)

