from random import randint

random_num = randint(1, 10)


def guess_num():
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
            answ = input('Хотите сыграть еще раз? y/n \n')
            if answ == 'y':
                guess_num()
            else:
                print('Дякуємо за гру')
    return counter

guess_num()

