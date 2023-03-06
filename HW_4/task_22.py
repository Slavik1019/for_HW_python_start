n = int(input("Введите количество элементов первого множества: "))
m = int(input("Введите количество элементов второго множества: "))
a = set(map(int, input("Введите элементы первого множества через пробел: ").split()))
b = set(map(int, input("Введите элементы второго множества через пробел: ").split()))

intersection = set()

for x in a:
    if x in b:
        intersection.add(x)

intersection = sorted(list(intersection))
print("Общие элементы в порядке возрастания:", intersection)