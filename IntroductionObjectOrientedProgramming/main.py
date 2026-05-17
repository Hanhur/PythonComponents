# 1. Определите класс Apple с четырьмя переменными экземпляра, представляющими четыре свойства яблока.
class Apple:
    def __init__(self, sort, color, weight, sweetness):
        """
        Конструктор класса Apple.
        :param sort: сорт яблока (str)
        :param color: цвет яблока (str)
        :param weight: вес яблока в граммах (float или int)
        :param sweetness: сладость по шкале 1-10 (int)
        """
        self.sort = sort          # сорт
        self.color = color        # цвет
        self.weight = weight      # вес
        self.sweetness = sweetness # сладость

apple1 = Apple("Гренни Смит", "зеленый", 180, 7)
apple2 = Apple("Фуджи", "красный", 200, 9)

print(apple1.sort, apple1.color, apple1.weight, apple1.sweetness)
print(apple2.sort, apple2.color, apple2.weight, apple2.sweetness)

# 2. Создайте класс Circle с методом area, подсчитывающим и возвращающим
# площадь круга. Затем создайте объект Circle, вызовите в нем метод area и
# выведите результат. Воспользуйтесь функцией pi из встроенного в Python
# модуля math.
import math

class Circle:
    def __init__(self, radius):
        """
        Конструктор класса Circle.
        :param radius: радиус круга
        """
        self.radius = radius

    def area(self):
        """
        Метод для вычисления площади круга.
        Формула: π * r²
        :return: площадь круга
        """
        return math.pi * (self.radius ** 2)


# Создаем объект Circle с радиусом 5
circle = Circle(5)

# Вызываем метод area и выводим результат
result = circle.area()
print(f"Площадь круга с радиусом {circle.radius} равна: {result}")

# 3. Создайте класс Triangle с методом area, подсчитывающим и возвращающим площадь треугольника.
# Затем создайте объект Triangle, вызовите в нем area и выведите результат.

import math

class Triangle:
    def __init__(self, side_a, side_b, side_c):
        """
        Конструктор класса Triangle.
        :param side_a: сторона a
        :param side_b: сторона b
        :param side_c: сторона c
        """
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def area(self):
        """
        Вычисление площади по формуле Герона.
        :return: площадь треугольника
        """
        # Полупериметр
        s = (self.side_a + self.side_b + self.side_c) / 2
        # Формула Герона
        return math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))


# Создаем объект Triangle со сторонами 3, 4, 5
triangle = Triangle(3, 4, 5)

# Вызываем метод area и выводим результат
result = triangle.area()
print(f"Площадь треугольника со сторонами 3, 4, 5 равна: {result}")

# 4. Создайте класс Hexagon с методом calculate_perimeter, подсчитывающим и возвращающим периметр шестиугольника.
# Затем создайте объект Hexagon, вызовите в нем calculate_perimeter и выведите результат.
class Hexagon:
    def __init__(self, side1, side2, side3, side4, side5, side6):
        """
        Конструктор для шестиугольника с разными сторонами.
        :param side1-side6: длины шести сторон
        """
        self.sides = [side1, side2, side3, side4, side5, side6]

    def calculate_perimeter(self):
        """
        Метод для вычисления периметра шестиугольника.
        :return: сумма всех сторон
        """
        return sum(self.sides)


# Создаем объект Hexagon с разными сторонами
hexagon = Hexagon(3, 4, 5, 3, 4, 5)

# Вызываем метод calculate_perimeter и выводим результат
perimeter = hexagon.calculate_perimeter()
print(f"Периметр шестиугольника равен: {perimeter}")