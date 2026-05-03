# Все о сортировке в Python. Сложность алгоритмов. Параметры функций

# def foo(a: int = 0, b: int = 10) -> list:
#     spisok = []
#     for i in range(min(a, b), max(a, b)):
#         if i % 2 == 1:
#             spisok.append(i)
#     return spisok
#
# print(foo(0, 10))

# ===================================================================

# from random import randint
#  Сортировка пузырьком
# spisok = [randint(1, 20) for i in range(10)]
# print(spisok)
#
# for i in range(len(spisok)):
#     for j in range(i + 1):
#         if spisok[i] < spisok[j]:
#             spisok[i], spisok[j] = spisok[j], spisok[i]

#  Сортировка вставками
# for i in range(1, len(spisok)):
#     key = spisok[i]
#     j = i
#     while j >= 1 and spisok[j - 1] > key:
#         spisok[j] = spisok[j - 1]
#         j -= i
#     spisok[j] = key

# print(spisok)

# ===================================================================

def improved_bubble_sort(arr):
    """
    Сортировка списка улучшенным методом пузырька.
    На каждом проходе подсчитывается количество перестановок.
    Если перестановок нет – сортировка завершается.
    """
    n = len(arr)

    for i in range(n - 1):
        swaps = 0  # счётчик перестановок на текущем проходе

        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1

        print(f"Проход {i + 1}: перестановок = {swaps}, массив: {arr}")

        # Если перестановок не было, массив уже отсортирован
        if swaps == 0:
            print("Массив отсортирован. Досрочное завершение.")
            break

    return arr


# Пример использования
if __name__ == "__main__":
    # Тестовые примеры
    test_list = [64, 34, 25, 12, 22, 11, 90]
    print("Исходный список:", test_list)
    sorted_list = improved_bubble_sort(test_list.copy())
    print("Отсортированный список:", sorted_list)

    print("\n" + "=" * 50 + "\n")

    # Уже отсортированный список
    sorted_test = [1, 2, 3, 4, 5]
    print("Исходный список:", sorted_test)
    sorted_list2 = improved_bubble_sort(sorted_test.copy())
    print("Отсортированный список:", sorted_list2)