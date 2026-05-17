# 1. Добавьте переменную square_list в класс Square так, чтобы всякий раз, когда вы создаете новый объект Square, он добавлялся в список.
class Square:
    # Переменная класса (список всех созданных квадратов)
    square_list = []

    def __init__(self, side_length):
        """
        Конструктор класса Square.
        :param side_length: длина стороны квадрата
        """
        self.side_length = side_length
        # Добавляем созданный объект в список
        Square.square_list.append(self)

    def calculate_perimeter(self):
        """Метод для вычисления периметра квадрата"""
        return 4 * self.side_length

    def change_size(self, delta):
        """Метод для изменения размера стороны квадрата"""
        self.side_length += delta
        if self.side_length < 0:
            self.side_length = 0
            print("Предупреждение: сторона не может быть отрицательной. Установлено значение 0.")


# Демонстрация работы
print("=== Создаем квадраты ===\n")

# Создаем несколько квадратов
square1 = Square(5)
print(f"Создан квадрат со стороной {square1.side_length}")

square2 = Square(10)
print(f"Создан квадрат со стороной {square2.side_length}")

square3 = Square(3)
print(f"Создан квадрат со стороной {square3.side_length}")

square4 = Square(7)
print(f"Создан квадрат со стороной {square4.side_length}")

print(f"\n=== Всего создано квадратов: {len(Square.square_list)} ===\n")

# Выводим информацию о всех созданных квадратах
print("=== Список всех квадратов ===")
for i, square in enumerate(Square.square_list, 1):
    print(f"{i}. Квадрат со стороной {square.side_length}, периметр: {square.calculate_perimeter()}")

# Дополнительная демонстрация: изменение одного квадрата не влияет на список
print("\n=== Изменяем квадрат square1 ===")
square1.change_size(2)
print(f"Новая сторона square1: {square1.side_length}")

print("\n=== Обновленный список квадратов ===")
for i, square in enumerate(Square.square_list, 1):
    print(f"{i}. Квадрат со стороной {square.side_length}")

# 2. Измените класс Square так, чтобы когда вы выводите объект Square, выводилось сообщение с длинами всех четырех сторон фигуры.
# Например, если вы создадите квадрат при помощи Square(29) и осуществите вывод, Python должен вывести строку 29 на 29 на 29 на 29.
class Square:
    # Переменная класса (список всех созданных квадратов)
    square_list = []

    def __init__(self, side_length):
        """
        Конструктор класса Square.
        :param side_length: длина стороны квадрата
        """
        self.side_length = side_length
        # Добавляем созданный объект в список
        Square.square_list.append(self)

    def __str__(self):
        """
        Метод для строкового представления объекта Square.
        Возвращает строку с длинами всех четырех сторон.
        """
        return f"{self.side_length} на {self.side_length} на {self.side_length} на {self.side_length}"

    def calculate_perimeter(self):
        """Метод для вычисления периметра квадрата"""
        return 4 * self.side_length

    def change_size(self, delta):
        """Метод для изменения размера стороны квадрата"""
        self.side_length += delta
        if self.side_length < 0:
            self.side_length = 0
            print("Предупреждение: сторона не может быть отрицательной. Установлено значение 0.")


# Демонстрация работы
print("=== Демонстрация метода __str__ ===\n")

# Создаем квадрат со стороной 29
square1 = Square(29)
print(square1)  # Вывод: 29 на 29 на 29 на 29

# Создаем другие квадраты
square2 = Square(5)
square3 = Square(10)
square4 = Square(3)

# Выводим их
print(f"Квадрат 2: {square2}")  # Квадрат 2: 5 на 5 на 5 на 5
print(f"Квадрат 3: {square3}")  # Квадрат 3: 10 на 10 на 10 на 10
print(f"Квадрат 4: {square4}")  # Квадрат 4: 3 на 3 на 3 на 3

# Демонстрация с изменением стороны
print(f"\n=== После изменения стороны ===")
square1.change_size(3)
print(square1)  # 32 на 32 на 32 на 32

square1.change_size(-10)
print(square1)  # 22 на 22 на 22 на 22

# Показываем, что список квадратов тоже работает
print(f"\n=== Список всех квадратов ===")
for i, square in enumerate(Square.square_list, 1):
    print(f"{i}. {square}")

# 3. Напишите функцию, которая принимает два объекта в качестве параметров и возвращает True,
# если они являются одним и тем же объектом, и False в противном случае.

# Определяем класс Square
class Square:
    square_list = []

    def __init__(self, side_length):
        self.side_length = side_length
        Square.square_list.append(self)

    def __str__(self):
        return f"{self.side_length} на {self.side_length} на {self.side_length} на {self.side_length}"

    def calculate_perimeter(self):
        return 4 * self.side_length

    def change_size(self, delta):
        self.side_length += delta
        if self.side_length < 0:
            self.side_length = 0


# Функция для проверки, являются ли два объекта одним и тем же
def is_same_object(obj1, obj2):
    """
    Функция проверяет, являются ли два объекта одним и тем же объектом.
    :param obj1: первый объект
    :param obj2: второй объект
    :return: True, если объекты идентичны, иначе False
    """
    return obj1 is obj2


# Демонстрация работы
print("=== Проверка объектов ===\n")

# Пример 1: Один и тот же объект
a = [1, 2, 3]
b = a  # b ссылается на тот же объект, что и a
print(f"a = {a}, b = {b}")
print(f"is_same_object(a, b) = {is_same_object(a, b)}")  # True

# Пример 2: Разные объекты с одинаковым содержимым
c = [1, 2, 3]
d = [1, 2, 3]
print(f"\nc = {c}, d = {d}")
print(f"is_same_object(c, d) = {is_same_object(c, d)}")  # False

# Пример 3: Числа (небольшие целые числа могут кэшироваться)
x = 5
y = 5
print(f"\nx = {x}, y = {y}")
print(f"is_same_object(x, y) = {is_same_object(x, y)}")  # True (из-за интернирования)

# Пример 4: Строки (тоже могут интернироваться)
s1 = "hello"
s2 = "hello"
print(f"\ns1 = '{s1}', s2 = '{s2}'")
print(f"is_same_object(s1, s2) = {is_same_object(s1, s2)}")  # True

# Пример 5: Разные объекты Square
square1 = Square(5)
square2 = Square(5)
print(f"\nДва разных квадрата со стороной 5")
print(f"is_same_object(square1, square2) = {is_same_object(square1, square2)}")  # False

# Пример 6: Один и тот же объект после присваивания
square3 = square1
print(f"\nsquare3 = square1")
print(f"is_same_object(square1, square3) = {is_same_object(square1, square3)}")  # True

# Пример 7: None (особый случай)
nothing1 = None
nothing2 = None
print(f"\nnothing1 = None, nothing2 = None")
print(f"is_same_object(nothing1, nothing2) = {is_same_object(nothing1, nothing2)}")  # True

# Пример 8: Разные типы объектов
number = 42
string = "42"
print(f"\nnumber = {number}, string = '{string}'")
print(f"is_same_object(number, string) = {is_same_object(number, string)}")  # False