# Задача 34

poem = input("Введите стихотворение: ")
poem = poem.lower()
vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
phrases = poem.split()
count_vowels = lambda phrase: sum([1 for char in phrase if char in vowels])
vowels_count = list(map(count_vowels, phrases))
if vowels_count.count(vowels_count[0]) == len(vowels_count):
    print("Парам пам-пам")
else:
    print("Пам парам")