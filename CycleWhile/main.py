# Исключения в Python. Цикл while. Оператор else

# try:
#     '''Попытайся выполнить этот код'''
# except ValueError:
#     '''Если возникла ошибка, выполни этот код'''

try:
    apples = int(input("Введите количество яблок: "))
    people = int(input("Введите количество людей: "))

    if apples < 0 or people < 0:
        raise Exception

    print(f"Каждый человек должен получить по {apples / people} яблок")
except ValueError:
    print("Введено неверное значение, попробуйте цифры")
except ZeroDivisionError:
    print("Людей не может быть 0!")
except Exception:
    print("Вы не можете использовать отрицательные числа!")
finally:
    print("Этот критический блок кода позади")