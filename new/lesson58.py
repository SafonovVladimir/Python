def stringToList(string):
    listRes = list(string.split(" "))
    return listRes


def reverse(word):
    return word[::-1]


def reversed_word_in_List(list):
    newList = []
    for i in list:
        newList.append(reverse(i))
    return newList


strA = "Millie Bobby Brown"
print(strA)
list = stringToList(strA)
newString = ' '.join(reversed_word_in_List(list))
print(newString)
