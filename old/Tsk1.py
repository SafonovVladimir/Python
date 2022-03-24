num = int(input('Введите любое число '))

if num < 0:
    print("Число {} меньше 0" .format(num))
elif num == 0:
    print("Число {} равно 0".format(num))
else:
    print("Число {} больше 0".format(num))
