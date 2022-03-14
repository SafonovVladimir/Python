# lst1 = list(str(123))
# l2 = [i for i in 'hello']
# l3 = [i for i in 'hello world!' if i !=' ' and i not in ['a', 'e', 'i', 'y', 'o']]
# l6 = list(range(1, 11))
# print(lst1, l2, l3, l6, sep='\n')

for i in range(1, 5):
    print(f'Внешньій цикл №{i}')
    for j in range(1, 5):
        print(f'\tВнутренний цикл №{j}')