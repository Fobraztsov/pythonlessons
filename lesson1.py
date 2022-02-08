while True:
    number = int(input('Введите число: '))
    if number > 0 and number < 100:
        print(number*2)
        print(number / 2)
        print(number**2)
        break
    else:
        print('число должно быть > 0 и < 100')

#второе задание
import time

sec = 64852
type_result = time.gmtime(sec)
result = time.strftime("%H:%M:%S",type_result)
print(result)

#третье задание
number = int(input("Введите число: "))
res = str(number)
n1 = res + res
n2 = res + res + res
comp = number + int(n1) + int(n2)
print("Итог:", comp)