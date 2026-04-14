import random

# randint -> random integer
# x = random.randint(1, 10)
# count1 = 0
# count2 = 0
# for i in range(10000):
#     x = random.random()
#     if x >= 0.5:
#         count1 += 1
#     else:
#         count2 += 1
# print(count1, count2)

# =========================================================

# spisok = ['a', 'b', 'c', 'd', 'e', 'f']
# spisok = ' '.join(spisok)
# print(spisok[spisok.index('b') : spisok.index('b') + 1])

# =========================================================

# name = input("Введите своё имя: ")
# if name == "Mango":
#     print("Вам положена скидка в часть акции в размере 15 %")
#
# name.isdigit() # -> Проверка, что все символы строки - цифры
# name.isalpha() # -> Проверка, что все символы строки - буквы
# name.isalnum() # -> Проверка, что все символы строки или цифры или буквы
# name.islower() # -> Проверка, что все символы строки в нижнем регистре
# name.capitalize() # -> Переводит первый символ строки в верхний регистер, если возможно
# name.startswith('G') # -> Проверяет начало строки на совпадение с подстрокой
# name.endswith("bay") # -> Проверяет конец строки на совпадение с подстрокой

# ===========================================================

# Ввод строки с клавиатуры
# text = input("Введите строку: ")
#
# spisok = [i.isdigit() for i in text]
# print("Количество букв:", spisok.count(True), "Количество цифр:", spisok.count(False))

# Инициализация счетчиков
# letters_count = 0
# digits_count = 0
#
# # Подсчет букв и цифр
# for char in text:
#     if char.isalpha():  # проверка, является ли символ буквой
#         letters_count += 1
#     elif char.isdigit():  # проверка, является ли символ цифрой
#         digits_count += 1
#
# # Вывод результатов
# print(f"Количество букв: {letters_count}")
# print(f"Количество цифр: {digits_count}")

# ======================================================================

# spisok = [random.randint(1, 10) for i in range(10) if i % 2 == 0]
# print(spisok)

# Генерация двух списков случайных чисел
list1 = [random.randint(1, 20) for _ in range(10)]
list2 = [random.randint(1, 20) for _ in range(10)]

print("Первый список:", list1)
print("Второй список:", list2)
print("-" * 50)

# 1. Содержащий элементы обоих списков
merged = list1 + list2
print("1. Объединение списков:", merged)

# 2. Элементы обоих списков без повторений
unique_merged = list(set(merged))
print("2. Без повторений:", unique_merged)

# 3. Общие для двух списков элементы
common = list(set(list1) & set(list2))
print("3. Общие элементы:", common)

# 4. Только уникальные элементы каждого из списков
unique_to_list1 = [x for x in list1 if x not in list2]
unique_to_list2 = [x for x in list2 if x not in list1]
print("4. Уникальные элементы первого списка:", unique_to_list1)
print("   Уникальные элементы второго списка:", unique_to_list2)

# 5. Минимальное и максимальное значение каждого из списков
min_max_list1 = [min(list1), max(list1)]
min_max_list2 = [min(list2), max(list2)]
print("5. Мин и макс первого списка:", min_max_list1)
print("   Мин и макс второго списка:", min_max_list2)
