# 1. Создайте классы Rectangle и Square с методом calculate_perimeter, вычисляющим периметр фигур, которые эти классы представляют.
# Создайте объекты Rectangle и Square вызовите в них этот метод.
class Rectangle:
    def __init__(self, width, height):
        """
        Конструктор класса Rectangle.
        :param width: ширина прямоугольника
        :param height: высота прямоугольника
        """
        self.width = width
        self.height = height

    def calculate_perimeter(self):
        """
        Метод для вычисления периметра прямоугольника.
        Формула: 2 * (ширина + высота)
        :return: периметр прямоугольника
        """
        return 2 * (self.width + self.height)


class Square:
    def __init__(self, side_length):
        """
        Конструктор класса Square.
        :param side_length: длина стороны квадрата
        """
        self.side_length = side_length

    def calculate_perimeter(self):
        """
        Метод для вычисления периметра квадрата.
        Формула: 4 * длина стороны
        :return: периметр квадрата
        """
        return 4 * self.side_length


# Создаем объект Rectangle (ширина 5, высота 3)
rectangle = Rectangle(5, 3)
rect_perimeter = rectangle.calculate_perimeter()
print(f"Периметр прямоугольника {rectangle.width} x {rectangle.height} = {rect_perimeter}")

# Создаем объект Square (сторона 4)
square = Square(4)
square_perimeter = square.calculate_perimeter()
print(f"Периметр квадрата со стороной {square.side_length} = {square_perimeter}")

# 2. В классе Square определите метод change_size, позволяющий передавать ему число,
# которое увеличивает или уменьшает (если оно отрицательное) каждую сторону объекта Square на соответствующее значение.
class Square:
    def __init__(self, side_length):
        """
        Конструктор класса Square.
        :param side_length: длина стороны квадрата
        """
        self.side_length = side_length

    def calculate_perimeter(self):
        """
        Метод для вычисления периметра квадрата.
        :return: периметр квадрата
        """
        return 4 * self.side_length

    def change_size(self, delta):
        """
        Метод для изменения размера стороны квадрата.
        :param delta: число, на которое увеличивается (положительное)
                     или уменьшается (отрицательное) сторона квадрата
        """
        self.side_length += delta

        # Опционально: предотвращаем отрицательную длину стороны
        if self.side_length < 0:
            self.side_length = 0
            print("Предупреждение: сторона не может быть отрицательной. Установлено значение 0.")


# Создаем объект Square со стороной 5
square = Square(5)
print(f"Исходная сторона квадрата: {square.side_length}")
print(f"Периметр: {square.calculate_perimeter()}")

# Увеличиваем сторону на 3
square.change_size(3)
print(f"\nПосле увеличения на 3: сторона = {square.side_length}")
print(f"Периметр: {square.calculate_perimeter()}")

# Уменьшаем сторону на 4
square.change_size(-4)
print(f"\nПосле уменьшения на 4: сторона = {square.side_length}")
print(f"Периметр: {square.calculate_perimeter()}")

# Пробуем уменьшить до отрицательного значения
square.change_size(-10)
print(f"\nПосле попытки уменьшить на 10: сторона = {square.side_length}")

# 3. Создайте класс Shape. Определите в нем метод what_am_i, который при вызове выводит строку "Я - фигура".
# Измените ваши классы Rectangle и Square из предыдущих заданий для наследования от Square,
# создайте объекты Square и Rectangle и вызовите в них новый метод.
class Shape:
    def what_am_i(self):
        """Метод, выводящий информацию о том, что это фигура"""
        print("Я - фигура")


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)


class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_perimeter(self):
        return 4 * self.side_length

    def change_size(self, delta):
        self.side_length += delta
        if self.side_length < 0:
            self.side_length = 0
            print("Предупреждение: сторона не может быть отрицательной. Установлено значение 0.")


# Создаем объекты
rectangle = Rectangle(5, 3)
square = Square(4)

# Вызываем метод what_am_i для прямоугольника
print("Прямоугольник:", end = " ")
rectangle.what_am_i()

# Вызываем метод what_am_i для квадрата
print("Квадрат:", end = " ")
square.what_am_i()

# Дополнительно демонстрируем, что остальные методы работают
print(f"\nПериметр прямоугольника {rectangle.width} x {rectangle.height}: {rectangle.calculate_perimeter()}")
print(f"Периметр квадрата со стороной {square.side_length}: {square.calculate_perimeter()}")

# Проверяем метод change_size у квадрата
square.change_size(2)
print(f"\nПосле увеличения стороны квадрата на 2: сторона = {square.side_length}")
square.what_am_i()

# 4. Создайте классы Horse и Rider. Используйте композицию, чтобы смоделировать лошадь с всадником на ней.
class Horse:
    def __init__(self, name, breed, color):
        """
        Конструктор класса Horse.
        :param name: имя лошади
        :param breed: порода лошади
        :param color: масть лошади
        """
        self.name = name
        self.breed = breed
        self.color = color
        self.rider = None  # Изначально всадника нет

    def assign_rider(self, rider):
        """Назначает всадника лошади"""
        self.rider = rider
        print(f"{self.name} теперь имеет всадника {rider.name}")

    def remove_rider(self):
        """Убирает всадника с лошади"""
        if self.rider:
            print(f"{self.rider.name} слез(а) с {self.name}")
            self.rider = None
        else:
            print(f"На {self.name} нет всадника")

    def info(self):
        """Выводит информацию о лошади"""
        print(f"Лошадь: {self.name}, порода: {self.breed}, масть: {self.color}")
        if self.rider:
            print(f"  Сейчас на ней едет: {self.rider.name}")
        else:
            print(f"  Сейчас без всадника")


class Rider:
    def __init__(self, name, age, experience_level):
        """
        Конструктор класса Rider.
        :param name: имя всадника
        :param age: возраст всадника
        :param experience_level: уровень опыта (новичок, средний, профессионал)
        """
        self.name = name
        self.age = age
        self.experience_level = experience_level
        self.horse = None  # Лошадь, на которой сейчас едет всадник

    def mount(self, horse):
        """Всадник садится на лошадь"""
        if horse.rider is not None:
            print(f"На {horse.name} уже есть всадник - {horse.rider.name}")
            return False

        self.horse = horse
        horse.assign_rider(self)
        print(f"{self.name} сел(а) на {horse.name}")
        return True

    def dismount(self):
        """Всадник слезает с лошади"""
        if self.horse:
            horse_name = self.horse.name
            self.horse.remove_rider()
            self.horse = None
            print(f"{self.name} слез(а) с {horse_name}")
        else:
            print(f"{self.name} не сидит на лошади")

    def info(self):
        """Выводит информацию о всаднике"""
        print(f"Всадник: {self.name}, возраст: {self.age}, уровень: {self.experience_level}")
        if self.horse:
            print(f"  Сейчас едет на: {self.horse.name}")
        else:
            print(f"  Сейчас без лошади")


# Демонстрация работы
print("=== Создание объектов ===")
# Создаем лошадь
spirit = Horse("Буря", "Ахалтекинец", "золотисто-гнедая")
spirit.info()

# Создаем всадника
arthur = Rider("Артур", 28, "профессионал")
arthur.info()

print("\n=== Всадник садится на лошадь ===")
arthur.mount(spirit)

print("\n=== Состояние после посадки ===")
spirit.info()
arthur.info()

print("\n=== Попытка другого всадника сесть на ту же лошадь ===")
elena = Rider("Елена", 24, "средний")
elena.mount(spirit)

print("\n=== Всадник слезает с лошади ===")
arthur.dismount()

print("\n=== Состояние после того, как всадник слез ===")
spirit.info()
arthur.info()

print("\n=== Теперь другой всадник может сесть ===")
elena.mount(spirit)
spirit.info()