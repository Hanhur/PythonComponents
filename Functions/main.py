# 1. Напишите функцию, которая принимает число в качестве ввода, возводит его в квадрат и возвращает.

def square_number(num):
    """
    Принимает число, возводит его в квадрат и возвращает результат.

    Args:
        num (int или float): Число для возведения в квадрат

    Returns:
        int или float: Квадрат числа
    """
    return num ** 2

# Примеры использования:
print(square_number(5))  # 25
print(square_number(2.5))  # 6.25
print(square_number(-3))  # 9

# 2. Создайте функцию, которая принимает строку в качестве параметра и возвращает ее.

def return_string(text):
    """
    Принимает строку и возвращает её.

    Args:
        text (str): Входная строка

    Returns:
        str: Та же самая строка
    """
    return text

# Примеры использования:
print(return_string("Привет, мир!"))  # Привет, мир!
print(return_string("Python"))  # Python
print(return_string("12345"))  # 12345

# Сохранение результата в переменную
result = return_string("Hello World")
print(result)  # Hello World

# 3. Напишите функцию, которая принимает три обязательных и два необязательных параметра.
def process_data(name, age, city, country = "Не указана", phone = None):
    """
    Принимает три обязательных и два необязательных параметра.

    Args:
        name (str): Обязательный параметр - имя
        age (int): Обязательный параметр - возраст
        city (str): Обязательный параметр - город
        country (str): Необязательный параметр - страна (по умолчанию "Не указана")
        phone (str): Необязательный параметр - телефон (по умолчанию None)

    Returns:
        dict: Словарь со всеми параметрами
    """
    result = {
        "name": name,
        "age": age,
        "city": city,
        "country": country,
        "phone": phone
    }
    return result


# Примеры использования:

# 1. Только с обязательными параметрами
print(process_data("Анна", 25, "Москва"))
# Вывод: {'name': 'Анна', 'age': 25, 'city': 'Москва', 'country': 'Не указана', 'phone': None}

# 2. С одним необязательным параметром
print(process_data("Иван", 30, "СПб", country = "Россия"))
# Вывод: {'name': 'Иван', 'age': 30, 'city': 'СПб', 'country': 'Россия', 'phone': None}

# 3. С двумя необязательными параметрами
print(process_data("Мария", 28, "Казань", country = "Россия", phone = "+7-999-123-45-67"))
# Вывод: {'name': 'Мария', 'age': 28, 'city': 'Казань', 'country': 'Россия', 'phone': '+7-999-123-45-67'}

# 4. С использованием именованных аргументов
print(process_data(age = 35, name = "Петр", city = "Новосибирск", phone = "8-800-555-35-35"))


# Вывод: {'name': 'Петр', 'age': 35, 'city': 'Новосибирск', 'country': 'Не указана', 'phone': '8-800-555-35-35'}
# 4. Напишите программу с двумя функциями. Первая функция должна принимать в качестве параметра целое число и возвращать результат деления
# этого числа на 2. Вторая функция должна принимать в качестве параметра
# целое число и возвращать результат умножения этого числа на 4. Вызовите
# первую функцию, сохраните результат в переменной и передайте ее в качестве параметра во вторую функцию.

def divide_by_two(num):
    """Принимает целое число и возвращает результат деления на 2."""
    return num / 2

def multiply_by_four(num):
    """Принимает число и возвращает результат умножения на 4."""
    return num * 4

try:
    user_input = int(input("Введите целое число: "))

    # Пошаговое выполнение
    step1 = divide_by_two(user_input)
    step2 = multiply_by_four(step1)

    print(f"Результат: {step2}")
    print(f"(Проверка: {user_input} ÷ 2 × 4 = {user_input} × 2 = {user_input * 2})")

except ValueError:
    print("Ошибка: Пожалуйста, введите целое число!")

# 5. Напишите функцию, которая преобразовывает строку в тип данных float и возвращает результат.
# Используйте обработку исключений, чтобы перехватить возможные исключения.

def convert_to_float_advanced(string_value):
    """
    Преобразует строку в float с расширенной обработкой исключений.

    Args:
        string_value (str): Строка для преобразования

    Returns:
        float: Число с плавающей точкой

    Raises:
        TypeError: Если аргумент не является строкой
        ValueError: Если строка не может быть преобразована в число
    """
    if not isinstance(string_value, str):
        raise TypeError(f"Ожидается строка, получен {type(string_value).__name__}")

    try:
        # Удаляем лишние пробелы и заменяем запятую на точку
        cleaned_value = string_value.strip().replace(',', '.')
        return float(cleaned_value)
    except ValueError:
        raise ValueError(f"Строка '{string_value}' не может быть преобразована в число с плавающей точкой")


# Использование с обработкой исключений
def safe_convert_to_float(string_value):
    """
    Безопасная версия с полной обработкой всех исключений.
    """
    try:
        return convert_to_float_advanced(string_value)
    except (TypeError, ValueError) as e:
        print(f"Ошибка: {e}")
        return None


# Демонстрация работы
print("=== Демонстрация работы функции ===")
test_strings = ["123.456", "789", "-45.67", "  0.5  ", "abc", "12,34", "", "1.2.3", None]

for test in test_strings:
    result = safe_convert_to_float(test)
    if result is not None:
        print(f"✓ '{test}' -> {result} (тип: {type(result).__name__})")
    else:
        print(f"✗ '{test}' -> не удалось преобразовать")

print("\n=== Дополнительный пример с реальным использованием ===")


def calculate_average(num1, num2, num3):
    """
    Вычисляет среднее арифметическое трех чисел, переданных в виде строк.
    """
    numbers = []
    for i, val in enumerate([num1, num2, num3], 1):
        converted = safe_convert_to_float(val)
        if converted is None:
            print(f"Не удалось преобразовать значение {i} ('{val}')")
            return None
        numbers.append(converted)

    average = sum(numbers) / len(numbers)
    return average


# Тестирование
print(calculate_average("10", "20.5", "30"))  # 20.166...
print(calculate_average("10", "abc", "30"))  # None с сообщением об ошибке

# 6. Добавьте строку документации ко всем функциям, которые вы написали в заданиях 1–5.

def square_number(num):
    """Возводит число в квадрат."""
    return num ** 2

def return_string(text):
    """Принимает и возвращает строку."""
    return text

def process_data(name, age, city, country = "Не указана", phone = None):
    """Обрабатывает данные с обязательными и необязательными параметрами."""
    return {
        "name": name, "age": age, "city": city,
        "country": country, "phone": phone
    }

def divide_by_two(num):
    """Делит число на 2."""
    return num / 2

def multiply_by_four(num):
    """Умножает число на 4."""
    return num * 4

def convert_to_float(string_value):
    """Преобразует строку в float с обработкой исключений."""
    try:
        return float(string_value)
    except (ValueError, TypeError) as e:
        print(f"Ошибка: {e}")
        return None

# Просмотр документации
if __name__ == "__main__":
    print("=== Документация функций ===\n")

    print("1. square_number:")
    help(square_number)
    print("\n" + "=" * 50 + "\n")

    print("2. return_string:")
    help(return_string)
    print("\n" + "=" * 50 + "\n")

    print("3. process_data:")
    help(process_data)
    print("\n" + "=" * 50 + "\n")

    print("4. divide_by_two и multiply_by_four:")
    help(divide_by_two)
    help(multiply_by_four)
    print("\n" + "=" * 50 + "\n")

    print("5. convert_to_float:")
    help(convert_to_float)