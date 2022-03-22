# try:
#     print(100 / 0)
# except ZeroDivisionError:
#     print(0)

while True:
    try:
        num = int(input('Enter your number: '))
        print(f'100 / {num} = {100 // num}')
        break
    except ZeroDivisionError:
        print('The number must be higher than ')
    except ValueError:
        print('Must be a number')
