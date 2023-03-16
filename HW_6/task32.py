lst = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
minimum = 6
maximum = 10

result = [i for i, x in enumerate(lst) if minimum <= x <= maximum]

print(result)