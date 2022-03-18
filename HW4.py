import random

random_num = random.randrange(1, 100)
# print(random_num)
enter_num = 0
counter = 1
while enter_num != random_num:
    enter_num = int(input('Введите число: '))
    if enter_num < random_num:
        print('Вы ввели число меньше загаданного. Повторите попытку.')
        counter += 1
    elif enter_num > random_num:
        print('Вы ввели число больше загаданного. Повторите попытку.')
        counter += 1
    else:
        print('Вы угадали')
print(f'Количество попыток: {counter}')
