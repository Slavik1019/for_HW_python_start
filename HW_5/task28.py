def sum(a, b):
    if b == 0:
        return a
    return sum(a + 1, b - 1)

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

result = sum(a, b)

print("Сумма двух чисел равна:", result)