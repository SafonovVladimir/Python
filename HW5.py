def mult_table():
    a = int(input('Введіть перше число діапазона: '))
    b = int(input('Введіть друге число діапазона: '))
    for i in range(a, b + 1):
        for j in range(a + 1, b + 1):
            print(f'{j} * {i} = {j * i}', end='\t')
        print('')


print("Таблиця множення:")
mult_table()
print('Well Done!')
