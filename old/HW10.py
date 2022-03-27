'''All non-letter symbols should stay on the same places.
E.g. "a1bcd efg!h" => "d1cba hgf!e"
Use Latin alphabet for test only.'''

text = 'a1bcd efg!h lkjhdf7,j  zdf121aasf'
print(text)


def only_alphabet_revers(word):
    list_res = list(word)
    i = 0
    j = len(word) - 1
    while i < j:
        if not list_res[i].isalpha():
            i += 1
        elif not list_res[j].isalpha():
            j -= 1
        else:
            new_char = list_res[i]
            list_res[i] = list_res[j]
            list_res[j] = new_char
            # print(list_res)
            i += 1
            j -= 1
    return ''.join(list_res)


new_list = list(text.split(" "))


res = []

for i in new_list:
    res.append(only_alphabet_revers(i))

result = ' '.join(res)
print(result)
