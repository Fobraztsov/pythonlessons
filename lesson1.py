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
import time
sec = 63258
sec_value = sec % (24 * 3600)
hour_value = sec_value // 3600
sec_value %= 3600
min_value = sec_value // 60
sec_value %= 60
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

#4 задание
x = int(input("Введите число: "))
m = 0
while (x):
    if (x % 10 > m):
        m = x % 10
    x //= 10

print(m)

#5-6 задание
sum = int(input("Введите общую сумму: "))
outlay = int(input("Введите сумму издержек: "))
if sum > outlay:
    profit = sum-outlay
    rent = profit/sum
    print(f"Отлично. Ваш профит {profit} ")
    worker = int(input("Число работников фирмы: "))
    print(f"{profit/worker} прибыль на каждого работника")
elif sum == outlay:
    print("нулевой оборот")
else:
    print("Желаем эффективной работы")