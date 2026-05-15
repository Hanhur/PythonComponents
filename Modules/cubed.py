# Модуль cubed - содержит функцию для возведения числа в куб

def cube(number):
    """
    Функция принимает число и возвращает его куб.

    Параметры:
    number (int или float): число для возведения в куб

    Возвращает:
    int или float: число в третьей степени
    """
    return number ** 3


# Альтернативный вариант с проверкой типа
def cube_with_check(number):
    """Функция с проверкой, что переданное число - числовой тип"""
    if isinstance(number, (int, float)):
        return number ** 3
    else:
        raise TypeError("Параметр должен быть числом (int или float)")