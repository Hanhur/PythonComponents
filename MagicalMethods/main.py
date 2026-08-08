# Перегрузка магических методов

class Fractal:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other: "Fractal") -> "Fractal":
        result = Fractal(self.numerator * other.denominator + other.numerator * self.denominator, self.denominator * other.denominator)
        return result

    def __str__(self) -> str:
        return f"{self.numerator} / {self.denominator}"


a = Fractal(3, 4)
b = Fractal(2, 3)
print(a + b)
print(a)
