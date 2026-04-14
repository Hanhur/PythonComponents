# def summa(a, b):
#     print(a + b)
#     return
#
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# summa(a, b)

# =====================================================

# def change(a):
#     a = a * 2
#     return a
#
# num = int(input("Введите число: "))
# num = change(num)
# print(num)

# ======================================================

# def draw_line(length: int, direction, symbol):
#     if direction == "horizontal":
#         print(symbol * length)
#     elif direction == "vertical":
#         for i in range(length):
#             print(symbol)
#     else:
#         print("There is no such a dimension!")
#
# draw_line(12, "horizontal", '%')

# ======================================================

def odd_numbers_between(start: int, end: int):
    spisok = [start, end]
    spisok.sort()

    for i in range(spisok[0], spisok[-1]):
        if i % 2 == 1:
            print(i)

odd_numbers_between(11, 6)
