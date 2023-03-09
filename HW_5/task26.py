def f(x, y):
    if y >= 1:
        return x * f(x, y - 1)
    elif y == 0:
        return 1
    else:
        return f(x, y + 1) / x

A = int(input('Введите число: '))
B = int(input('Введите степень: '))
print('Результат равен = ', f(A, B))
