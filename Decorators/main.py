# import time
#
# def timer(func):
#     def wrapper(*args):
#         start_time = time.time()
#         result = func(*args)
#         end_time = time.time()
#         print(f"{func.__name__} took {round(end_time - start_time, 3)} seconds to execute")
#         return result
#     return wrapper
#
# @timer
# def make_list(length):
#     return [i for i in range(length)]
#
# make_list(10000)
# make_list(100000)
# make_list(1000000)

# ================================================================================================================

# def cache(func):
#     cached_results = {}
#
#     def wrapper(*args):
#         if args in cached_results:
#             return cached_results[args]
#         result = func(*args)
#         cached_results[args] = result
#         return result
#     return  wrapper
#
# @cache
# def fibo(n):
#     if n == 0 or n == 1:
#         return 1
#     return fibo(n - 1) + fibo(n - 2)
#
# print(fibo(25))

# ================================================================================================================

# def validate_args(*types):
#     def decorator(func):
#         def wrapper(*args):
#             for arg, arg_type in zip(args, types):
#                 if not isinstance(arg, arg_type):
#                     raise TypeError(f"Expected {arg_type}, got {type(arg)}")
#             return func(*args)
#         return wrapper
#     return decorator
#
# @validate_args(int, int)
# def sum_string(first, second):
#     return first + second
#
# print(sum_string(3, 8))

# ================================================================================================================

# class Class:
#     @staticmethod
#     def summa(a, b):
#         return a + b
#
#     @classmethod
#     def multiply(cls, a, b):
#         return cls.summa(a, b) * b
#
# print(Class.summa(3, 4))
# print(Class.multiply(3, 4))

# ================================================================================================================

# from abc import ABC, abstractclassmethod
#
# class Mammal(ABC):
#     def __init__(self):
#         self.spine = True
#
#     @abstractclassmethod
#     def transport(self):
#         pass
#
# class Cat(Mammal):
#     def __init__(self):
#         Mammal.__init__(self)
#         self.paws = 4
#
#     @classmethod
#     def transport(self):
#         pass
#
# cat = Cat()

# ================================================================================================================

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square:
    def __init__(self, side_size):
        self.side_size = side_size

    def area(self):
        return self.side_size ** 2

class CircleInSquare(Circle, Square):
    def __init__(self, circle, square):
        # Initialize the parent classes
        Circle.__init__(self, circle.radius)
        Square.__init__(self, square.side_size)

        # Validate that the circle fits exactly in the square
        if self.radius != self.side_size / 2:
            raise ValueError(f"You can't create a circle in square with these two figures")

        self.circle = circle
        self.square = square

    def area(self):
        # Calculate the area of the square minus the circle
        return self.square.area() - self.circle.area()

# Create objects
circle = Circle(5)
square = Square(10)

print(square.area())  # 100
print(circle.area())  # 78.5

# Create CircleInSquare (note: fixed spelling from cirlce to circle)
circle_in_square = CircleInSquare(circle, square)
print(circle_in_square.area())  # 21.5 (100 - 78.5)