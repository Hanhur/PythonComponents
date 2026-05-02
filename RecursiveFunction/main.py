# Рекурсивная функция в Python. Числа Фибоначчи. Факториалы

# def fibbo(n):
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return fibbo(n - 1) + fibbo(n - 2)
# print(fibbo(4))

# ===============================================================

# num = int(input("Введите номер числа: "))
# fibbos = [0, 1]
# for i in range(2, num):
#     fibbos.append(fibbos[i - 1] + fibbos[i - 2])
# print(fibbos[-1])

# ===============================================================

# def fact(n):
#     if n <= 1:
#         return 1
#     return n * fact(n - 1)
# print(fact(10))

# ===============================================================

# def ranged_summa(a, b):
#     if a == b:
#         return a
#     else:
#         return b + ranged_summa(a, b - 1)
# print(ranged_summa(1, 10))

# ===============================================================

# def recur_star(n):
#     if n == 0:
#         return
#     print('*', end = '')
#     recur_star(n - 1)
#
# recur_star(5)

# ===============================================================

# def gcd(a, b):
#     # Приводим числа к абсолютному значению (для отрицательных чисел)
#     a, b = abs(a), abs(b)
#
#     # Базовый случай: если b = 0, то НОД = a
#     if b == 0:
#         return a
#
#     # Рекурсивный случай: НОД(a, b) = НОД(b, a % b)
#     return gcd(b, a % b)
#
#
# # Примеры использования:
# print(gcd(48, 18))  # 6
# print(gcd(100, 35))  # 5
# print(gcd(17, 19))  # 1
# print(gcd(-48, 18))  # 6
# print(gcd(0, 5))  # 5
# print(gcd(0, 0))  # 0

# ===============================================================

import random

def generate_secret_number():
    """Генерирует случайное четырёхзначное число с уникальными цифрами"""
    digits = list('0123456789')
    random.shuffle(digits)
    # Первая цифра не может быть 0
    if digits[0] == '0':
        digits[0], digits[1] = digits[1], digits[0]
    return ''.join(digits[:4])


def calculate_bulls_and_cows(secret, guess):
    """Возвращает количество быков и коров"""
    bulls = 0
    cows = 0

    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1

    return bulls, cows


def game_loop(secret, attempts):
    """Рекурсивный игровой цикл"""
    # Ввод числа от пользователя
    guess = input(f"\nПопытка #{attempts}. Введите четырёхзначное число: ").strip()

    # Проверка корректности ввода
    if len(guess) != 4 or not guess.isdigit() or guess[0] == '0' or len(set(guess)) != 4:
        print("Ошибка! Введите четырёхзначное число с неповторяющимися цифрами (первая цифра не 0).")
        return game_loop(secret, attempts)  # Рекурсивный вызов при ошибке

    # Подсчёт быков и коров
    bulls, cows = calculate_bulls_and_cows(secret, guess)

    print(f"Быков: {bulls}, Коров: {cows}")

    # Базовый случай: число угадано
    if bulls == 4:
        print(f"\nПоздравляю! Вы угадали число {secret} за {attempts} попыток!")
        return attempts

    # Рекурсивный случай: продолжаем игру
    return game_loop(secret, attempts + 1)


def main():
    """Основная функция игры"""
    print("=" * 50)
    print("Добро пожаловать в игру «Быки и коровы»!")
    print("Правила:")
    print("- Компьютер загадал четырёхзначное число с неповторяющимися цифрами.")
    print("- «Быки» — цифры, которые угаданы и стоят на своих местах.")
    print("- «Коровы» — цифры, которые угаданы, но стоят не на своих местах.")
    print("=" * 50)

    secret_number = generate_secret_number()
    # Для отладки (можно закомментировать):
    # print(f"(Для отладки загадано число: {secret_number})")

    # Рекурсивный игровой процесс
    total_attempts = game_loop(secret_number, 1)
    print(f"\nИгра окончена! Количество попыток: {total_attempts}")


if __name__ == "__main__":
    main()