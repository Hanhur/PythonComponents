# Словари в Python. Ключи и значения словарей. Методы словарей
# def digit_stats(numbers):
#     stats = {}
#     for num in numbers:
#         # Количество цифр в числе (убираем минус для отрицательных)
#         num_digits = len(str(abs(num)))
#         stats[num_digits] = stats.get(num_digits, 0) + 1
#
#     for digits, count in sorted(stats.items()):
#         print(f"{digits} цифр{'а' if digits % 10 == 1 and digits != 11 else 'ы'} — {count} элемент{'а' if count % 10 == 1 and count != 11 else 'ов' if count > 4 else ''}")
#
# # Пример использования
# t = (3, 45, 123, 7, 89, 6789, 0, -42, 1000)
# digit_stats(t)

# =============================================================================

def digit_stats_simple(numbers):
    stats = {}
    for num in numbers:
        d = len(str(abs(num)))
        stats[d] = stats.get(d, 0) + 1

    for d, c in sorted(stats.items()):
        print(f"{d} цифр{'а' if d == 1 else 'ы'} — {c} элементов")

t = (3, 45, 123, 7, 89, 6789, 0, -42, 1000)
digit_stats_simple(t)