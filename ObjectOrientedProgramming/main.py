# class TheSimplestClass:
#     pass
#
# first_object = TheSimplestClass()
# print(first_object)

# ================================ Stack ============================================

# stack = []
#
# def push(value):
#     stack.append(value)
#
# def pop():
#     val = stack[-1]
#     del stack[-1]
#     return val
#
# push(3)
# push(2)
# push(1)
# print(pop())
# print(pop())
# print(pop())

# =====================================================================================

# class Stack:
#     def __init__(self):
#         self.__stack_list = []
#
#     def push(self, value):
#         self.__stack_list.append(value)
#
#     def pop(self):
#         val = self.__stack_list[-1]
#         del self.__stack_list[-1]
#         return val
#
#
# class AddingStack(Stack):
#     def __init__(self):
#         Stack.__init__(self)
#         self.__sum = 0
#
#     def push(self, value):
#         Stack.push(self, value)
#         self.__sum += value
#
#     def pop(self):
#         val = Stack.pop(self)
#         self.__sum += val
#         return val
#
#     def get_sum(self):
#         return self.__sum
#
# my_stack = AddingStack()
#
# for i in range(5):
#     my_stack.push(i)
# print(my_stack.get_sum())
#
# for i in range(5):
#     print(my_stack.pop())

# =====================================================================================

# from datetime import datetime
#
#
# class Person:
#     """Класс, представляющий человека с основными персональными данными."""
#
#     def __init__(self, full_name = "", birth_date = None, phone = "", city = "", country  = "", home_address = ""):
#         """
#         Конструктор класса.
#
#         Args:
#             full_name (str): ФИО
#             birth_date (datetime): Дата рождения
#             phone (str): Контактный телефон
#             city (str): Город
#             country (str): Страна
#             home_address (str): Домашний адрес
#         """
#         self._full_name = full_name
#         self._birth_date = birth_date if birth_date else datetime.now()
#         self._phone = phone
#         self._city = city
#         self._country = country
#         self._home_address = home_address
#
#     # ========== Методы ввода данных ==========
#     def input_data(self):
#         """Ввод данных о человеке с клавиатуры."""
#         print("\nВведите данные о человеке:")
#
#         self._full_name = input("ФИО: ").strip()
#
#         while True:
#             date_str = input("Дата рождения (гггг-мм-дд): ").strip()
#             try:
#                 self._birth_date = datetime.strptime(date_str, "%Y-%m-%d")
#                 break
#             except ValueError:
#                 print("Неверный формат даты. Попробуйте снова (гггг-мм-дд).")
#
#         self._phone = input("Контактный телефон: ").strip()
#         self._city = input("Город: ").strip()
#         self._country = input("Страна: ").strip()
#         self._home_address = input("Домашний адрес: ").strip()
#
#     # ========== Методы вывода данных ==========
#     def display_data(self):
#         """Вывод всей информации о человеке."""
#         print("\n--- Информация о человеке ---")
#         print(f"ФИО: {self._full_name}")
#         print(f"Дата рождения: {self._birth_date.strftime('%d.%m.%Y')}")
#         print(f"Телефон: {self._phone}")
#         print(f"Город: {self._city}")
#         print(f"Страна: {self._country}")
#         print(f"Домашний адрес: {self._home_address}")
#         print("-" * 33)
#
#     # ========== Методы доступа к полям (геттеры и сеттеры) ==========
#     # ФИО
#     def get_full_name(self):
#         """Возвращает ФИО."""
#         return self._full_name
#
#     def set_full_name(self, value):
#         """Устанавливает ФИО."""
#         self._full_name = value.strip() if value else ""
#
#     # Дата рождения
#     def get_birth_date(self):
#         """Возвращает дату рождения."""
#         return self._birth_date
#
#     def set_birth_date(self, value):
#         """Устанавливает дату рождения."""
#         if isinstance(value, datetime):
#             self._birth_date = value
#         else:
#             raise TypeError("Дата должна быть объектом datetime")
#
#     # Телефон
#     def get_phone(self):
#         """Возвращает контактный телефон."""
#         return self._phone
#
#     def set_phone(self, value):
#         """Устанавливает контактный телефон."""
#         self._phone = value.strip() if value else ""
#
#     # Город
#     def get_city(self):
#         """Возвращает город."""
#         return self._city
#
#     def set_city(self, value):
#         """Устанавливает город."""
#         self._city = value.strip() if value else ""
#
#     # Страна
#     def get_country(self):
#         """Возвращает страну."""
#         return self._country
#
#     def set_country(self, value):
#         """Устанавливает страну."""
#         self._country = value.strip() if value else ""
#
#     # Домашний адрес
#     def get_home_address(self):
#         """Возвращает домашний адрес."""
#         return self._home_address
#
#     def set_home_address(self, value):
#         """Устанавливает домашний адрес."""
#         self._home_address = value.strip() if value else ""
#
#     # ========== Дополнительные методы ==========
#     def get_age(self):
#         """
#         Вычисляет возраст человека в полных годах.
#
#         Returns:
#             int: Возраст в годах
#         """
#         today = datetime.now()
#         age = today.year - self._birth_date.year
#         # Проверяем, был ли уже день рождения в этом году
#         if (today.month, today.day) < (self._birth_date.month, self._birth_date.day):
#             age -= 1
#         return age
#
#     def __str__(self):
#         """Строковое представление объекта."""
#         return f"{self._full_name}, {self._birth_date.strftime('%d.%m.%Y')}, {self._phone}, {self._city}, {self._country}, {self._home_address}"
#
#
# # ========== Пример использования ==========
# def main():
#     """Демонстрация работы класса Person."""
#
#     # Создание объекта через конструктор по умолчанию
#     person1 = Person()
#     person1.input_data()  # Ввод данных с клавиатуры
#     person1.display_data()
#
#     # Создание объекта через конструктор с параметрами
#     person2 = Person(
#         full_name = "Иванов Иван Иванович",
#         birth_date = datetime(1990, 5, 15),
#         phone = "+7-900-123-45-67",
#         city = "Москва",
#         country = "Россия",
#         home_address = "ул. Ленина, д. 10, кв. 5"
#     )
#     person2.display_data()
#
#     # Использование методов доступа
#     print("\nИзменяем телефон через сеттер:")
#     person2.set_phone("+7-999-888-77-66")
#     print(f"Новый телефон: {person2.get_phone()}")
#
#     # Дополнительно — возраст
#     print(f"Возраст: {person2.get_age()} лет")
#
#     # Вывод через __str__
#     print(f"\nКраткая информация: {person2}")
#
#
# if __name__ == "__main__":
#     main()

# =====================================================================================

class Fraction:
    """Класс для работы с обыкновенными дробями"""

    def __init__(self, numerator = 0, denominator = 1):
        """
        Конструктор класса
        :param numerator: числитель (по умолчанию 0)
        :param denominator: знаменатель (по умолчанию 1)
        """
        if denominator == 0:
            raise ValueError("Знаменатель не может быть равен нулю!")

        self.__numerator = numerator
        self.__denominator = denominator
        self.__reduce()  # Сразу сокращаем дробь

    # Методы для ввода и вывода данных
    def input_data(self):
        """Метод для ввода данных с клавиатуры"""
        while True:
            try:
                num = int(input("Введите числитель: "))
                den = int(input("Введите знаменатель: "))

                if den == 0:
                    print("Ошибка: знаменатель не может быть равен нулю! Попробуйте снова.")
                    continue

                self.__numerator = num
                self.__denominator = den
                self.__reduce()
                break
            except ValueError:
                print("Ошибка: введите целые числа! Попробуйте снова.")

    def print_data(self):
        """Метод для вывода данных на экран"""
        print(self)

    # Методы доступа к полям (геттеры и сеттеры)
    def get_numerator(self):
        """Получить числитель"""
        return self.__numerator

    def set_numerator(self, value):
        """Установить числитель"""
        self.__numerator = value
        self.__reduce()

    def get_denominator(self):
        """Получить знаменатель"""
        return self.__denominator

    def set_denominator(self, value):
        """Установить знаменатель"""
        if value == 0:
            raise ValueError("Знаменатель не может быть равен нулю!")
        self.__denominator = value
        self.__reduce()

    def is_zero(self):
        """Проверка, является ли дробь нулевой"""
        return self.__numerator == 0

    # Вспомогательный метод для сокращения дроби
    def __reduce(self):
        """Приведение дроби к несократимому виду (приватный метод)"""
        # Если знаменатель отрицательный, переносим минус в числитель
        if self.__denominator < 0:
            self.__numerator = -self.__numerator
            self.__denominator = -self.__denominator

        # Если числитель равен 0, знаменатель делаем 1
        if self.__numerator == 0:
            self.__denominator = 1
            return

        # Находим НОД
        from math import gcd
        divisor = gcd(abs(self.__numerator), abs(self.__denominator))

        # Сокращаем дробь
        self.__numerator //= divisor
        self.__denominator //= divisor

    # Арифметические операции
    def add(self, other):
        """Сложение дробей"""
        if not isinstance(other, Fraction):
            raise TypeError("Операнд должен быть объектом класса Fraction")

        new_num = self.__numerator * other.__denominator + other.__numerator * self.__denominator
        new_den = self.__denominator * other.__denominator
        return Fraction(new_num, new_den)

    def subtract(self, other):
        """Вычитание дробей"""
        if not isinstance(other, Fraction):
            raise TypeError("Операнд должен быть объектом класса Fraction")

        new_num = self.__numerator * other.__denominator - other.__numerator * self.__denominator
        new_den = self.__denominator * other.__denominator
        return Fraction(new_num, new_den)

    def multiply(self, other):
        """Умножение дробей"""
        if not isinstance(other, Fraction):
            raise TypeError("Операнд должен быть объектом класса Fraction")

        new_num = self.__numerator * other.__numerator
        new_den = self.__denominator * other.__denominator
        return Fraction(new_num, new_den)

    def divide(self, other):
        """Деление дробей"""
        if not isinstance(other, Fraction):
            raise TypeError("Операнд должен быть объектом класса Fraction")

        if other.__numerator == 0:
            raise ZeroDivisionError("Деление на нулевую дробь невозможно!")

        new_num = self.__numerator * other.__denominator
        new_den = self.__denominator * other.__numerator
        return Fraction(new_num, new_den)

    # Дополнительные методы
    def to_decimal(self, precision = 2):
        """Преобразование в десятичную дробь"""
        return round(self.__numerator / self.__denominator, precision)

    # Перегрузка методов для удобства использования
    def __str__(self):
        """Строковое представление дроби"""
        if self.__denominator == 1:
            return str(self.__numerator)
        elif self.__numerator == 0:
            return "0"
        else:
            return f"{self.__numerator}/{self.__denominator}"

    def __repr__(self):
        """Представление для отладки"""
        return f"Fraction({self.__numerator}, {self.__denominator})"

    # Перегрузка арифметических операторов для удобства
    def __add__(self, other):
        return self.add(other)

    def __sub__(self, other):
        return self.subtract(other)

    def __mul__(self, other):
        return self.multiply(other)

    def __truediv__(self, other):
        return self.divide(other)

    def __eq__(self, other):
        """Сравнение на равенство"""
        if not isinstance(other, Fraction):
            return False
        return (self.__numerator == other.__numerator and self.__denominator == other.__denominator)


# Пример использования программы
def main():
    print("=" * 50)
    print("РАБОТА С ДРОБЯМИ")
    print("=" * 50)

    # Создание дроби через конструктор
    print("\n1. Создание дроби через конструктор:")
    f1 = Fraction(3, 4)
    print(f"Дробь 1: {f1}")

    # Создание дроби через ввод с клавиатуры
    print("\n2. Ввод дроби с клавиатуры:")
    f2 = Fraction()
    f2.input_data()
    print(f"Дробь 2: {f2}")

    # Демонстрация методов доступа к полям
    print("\n3. Доступ к полям через методы:")
    print(f"Числитель дроби 1: {f1.get_numerator()}")
    print(f"Знаменатель дроби 1: {f1.get_denominator()}")

    print("\nИзменение полей через методы:")
    f1.set_numerator(6)
    f1.set_denominator(8)
    print(f"После изменения: {f1}")  # Автоматически сократится до 3/4

    # Арифметические операции с обработкой ошибок
    print("\n4. Арифметические операции:")
    print(f"{f1} + {f2} = {f1.add(f2)}")
    print(f"{f1} - {f2} = {f1.subtract(f2)}")
    print(f"{f1} * {f2} = {f1.multiply(f2)}")

    # Проверка перед делением
    if f2.is_zero():
        print(f"{f1} / {f2} = Деление на ноль невозможно!")
    else:
        print(f"{f1} / {f2} = {f1.divide(f2)}")

    # Использование перегруженных операторов
    print("\n5. Использование перегруженных операторов:")
    f3 = Fraction(1, 2)
    f4 = Fraction(1, 3)
    print(f"{f3} + {f4} = {f3 + f4}")
    print(f"{f3} - {f4} = {f3 - f4}")
    print(f"{f3} * {f4} = {f3 * f4}")

    if f4.is_zero():
        print(f"{f3} / {f4} = Деление на ноль невозможно!")
    else:
        print(f"{f3} / {f4} = {f3 / f4}")

    # Десятичное представление
    print("\n6. Десятичное представление:")
    print(f"{f3} = {f3.to_decimal()}")
    print(f"{f3} = {f3.to_decimal(4)} (с точностью 4 знака)")

    # Сравнение дробей
    print("\n7. Сравнение дробей:")
    f5 = Fraction(2, 4)  # Сократится до 1/2
    print(f"{f3} == {f5} ? {f3 == f5}")

    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()