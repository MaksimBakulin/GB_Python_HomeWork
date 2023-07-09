num = int(input("Введите число: "))

if num < 0 or num > 100000:
    print("Введенное число вне диапазона! (от 0 до 100000)")
else:
    k = 0
    for i in range(2, num // 2 + 1):
        if (num % i == 0):
            k = k + 1
    if (k <= 0):
        print("Число простое")
    else:
        print("Число не является простым")