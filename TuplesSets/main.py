# Алгоритмы поиска в Python. Кортежи и множества
from itertools import count

import random
import time
#
# a = [random.randint(0, 10000) for i in range(10000)]
# logging = a[random.randint(0, len(a))]
#
# start = time.time()
# for i in range(len(a)):
#     if a[i] == logging:
#         print("Found looking:", logging)
#         break
# end = time.time()
# print(end - start)

# ===================================================================

# fruits = ("apple", "banana", "pear", "mango")
# fruit_in = input("Введите название фрукта: ")
# count = 0
#
# for fruit in fruits:
#     if fruit_in in fruit:
#         count += 1
# print(count)

# ===================================================================

# a = list(set([random.randint(0, 100) for i in range(100)]))
# print(a)

# ===================================================================

# # Пример данных
# set1 = {"Москва", "Санкт-Петербург", "Казань", "Новосибирск"}
# set2 = {"Екатеринбург", "Казань", "Сочи", "Москва"}
#
# # Пересечение множеств
# set3 = set1 & set2  # или set1.intersection(set2)
#
# print(set3)  # {'Москва', 'Казань'}

# ===================================================================

# # Пример данных
# tuple1 = (1, 2, 3, 4, 5)
# tuple2 = (3, 4, 5, 6, 7)
# tuple3 = (5, 6, 7, 8, 9)
#
# # Преобразуем кортежи во множества и находим пересечение
# result = set(tuple1) & set(tuple2) & set(tuple3)
#
# # Результат можно оставить множеством или снова преобразовать в кортеж
# result_tuple = tuple(result)
#
# print(result)        # {5}
# print(result_tuple)  # (5,)

# ===================================================================

# tuple1 = (1, 2, 3, 4, 5)
# tuple2 = (3, 4, 5, 6, 7)
# tuple3 = (5, 6, 7, 8, 9)
#
# common = []
# for num in tuple1:
#     if num in tuple2 and num in tuple3:
#         common.append(num)
#
# result_tuple = tuple(common)
# print(result_tuple)  # (5,)

# ===================================================================

# # Пример данных
# tuple1 = (1, 2, 3, 4)
# tuple2 = (3, 4, 5, 6)
# tuple3 = (4, 6, 7, 8)
#
# # Находим уникальные элементы для каждого кортежа
# set1 = set(tuple1)
# set2 = set(tuple2)
# set3 = set(tuple3)
#
# # Элементы, уникальные для tuple1 (есть в 1, нет во 2 и 3)
# unique_to_1 = set1 - set2 - set3
#
# # Элементы, уникальные для tuple2
# unique_to_2 = set2 - set1 - set3
#
# # Элементы, уникальные для tuple3
# unique_to_3 = set3 - set1 - set2
#
# # Объединяем все уникальные элементы (если нужно одним списком)
# all_unique = unique_to_1 | unique_to_2 | unique_to_3
#
# print(f"Уникальные для 1-го кортежа: {unique_to_1}")  # {1, 2}
# print(f"Уникальные для 2-го кортежа: {unique_to_2}")  # {5}
# print(f"Уникальные для 3-го кортежа: {unique_to_3}")  # {8, 7}
# print(f"Все уникальные элементы: {all_unique}")       # {1, 2, 5, 7, 8}

# ===================================================================

# tuple1 = (1, 2, 3, 4)
# tuple2 = (3, 4, 5, 6)
# tuple3 = (4, 6, 7, 8)
#
# from collections import Counter
#
# # Считаем вхождения всех элементов
# all_nums = tuple1 + tuple2 + tuple3
# count = Counter(all_nums)
#
# # Оставляем те, которые встретились ровно 1 раз
# unique = [num for num in count if count[num] == 1]
# print(unique)  # [1, 2, 5, 7, 8]

# ===================================================================

# # Пример данных
# tuple1 = (1, 2, 3, 4, 5)
# tuple2 = (1, 7, 3, 9, 5)
# tuple3 = (1, 8, 3, 0, 5)
#
# # Находим минимальную длину (чтобы не выйти за границы)
# min_len = min(len(tuple1), len(tuple2), len(tuple3))
#
# # Собираем элементы, совпадающие на одинаковых позициях
# result = []
# for i in range(min_len):
#     if tuple1[i] == tuple2[i] == tuple3[i]:
#         result.append(tuple1[i])
#
# # Результат в виде кортежа
# result_tuple = tuple(result)
# print(result_tuple)  # (1, 3, 5)

# ===================================================================

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (1, 7, 3, 9, 5)
tuple3 = (1, 8, 3, 0, 5)

min_len = min(len(tuple1), len(tuple2), len(tuple3))

result = tuple(
    tuple1[i]
    for i in range(min_len)
    if tuple1[i] == tuple2[i] == tuple3[i]
)

print(result)  # (1, 3, 5)