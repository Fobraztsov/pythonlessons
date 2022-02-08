while True:
    number = int(input('Введите число: '))
    if number > 0 and number < 100:
        print(number*2)
        print(number / 2)
        print(number**2)
        break
    else:
        print('число должно быть > 0 и < 100')