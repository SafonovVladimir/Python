from itertools import compress

letters = ['A', 'B', 'C', 'B', 'D']
mask = [1, 0, 1, 0, 0]

result = compress(letters, mask)

print(list(result))
