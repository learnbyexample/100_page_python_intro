from math import factorial

while True:
    try:
        num = int(input('Enter a positive integer: '))
        print(f'{num}! = {factorial(num)}')
        break
    except ValueError:
        print('Not a positive integer, try again')

