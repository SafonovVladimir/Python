lst = [1, 2, 3, 'hello', ['test', 10], 'world', True]
lst2 = [4, 6, 'rest']
lenth = len(lst)
print(lst[4][0])
print(lst[0:3])
lst[2] = 5
lst.extend(lst2)
lst.insert(1, 'world')
lst.remove('world')
print(lst.pop(1))
print(lst)
