# Исключения в Python. Цикл while. Оператор else

# try:
#     '''Попытайся выполнить этот код'''
# except ValueError:
#     '''Если возникла ошибка, выполни этот код'''

# try:
#     apples = int(input("Введите количество яблок: "))
#     people = int(input("Введите количество людей: "))
#
#     if apples < 0 or people < 0:
#         raise Exception
#
#     print(f"Каждый человек должен получить по {apples / people} яблок")
# except ValueError:
#     print("Введено неверное значение, попробуйте цифры")
# except ZeroDivisionError:
#     print("Людей не может быть 0!")
# except Exception:
#     print("Вы не можете использовать отрицательные числа!")
# finally:
#     print("Этот критический блок кода позади")

# start, end = int(input("Введите старт: ")), int(input("Введите конец: "))
#
# while start <= end:
#     if start % 2 == 1:
#         print(start)
#     start += 1

# start, end = int(input("Введите старт: ")), int(input("Введите конец: "))
#
# while start != end:
#     print(end)
#     end -= 1

# start, end = int(input("Введите старт: ")), int(input("Введите конец: "))
#
# if start > end:
#     start, end = end, start
# while start < end:
#     print(start)
#     start += 1

# while True:
#     password = input("Введите пароль: ")
#     if password == 'qwerty':
#         print("Добро пожаловать!")
#         break
#     else:
#         print("Пароль неверный, попробуйте снова!")

# while True:
#     number = int(input("Введите ваше число: "))
#     if number > 0 and number != 17:
#         continue
#     print("Ваше число мне не нравится")

# a = 1
# while a < 10:
#     print(f"Я {a}!")
#     if a > 15:
#         break
#     a += 1
# else:
#     print("Перекличка окончена!")

try:
    a = int(input("Введите число: "))
    b = int(input("Введите число: "))
    print(a + b)
except ValueError:
    print(a + b)