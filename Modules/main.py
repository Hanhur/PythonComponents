# 1. Вызовите какую-нибудь другую функцию из модуля statistics.
import statistics

# Пример данных
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
data2 = [5, 7, 8, 9, 10, 10, 11, 12, 13, 15]

print("=== Функции модуля statistics ===\n")

# 1. mean() - среднее арифметическое
print(f"Среднее арифметическое: {statistics.mean(data)}")

# 2. median() - медиана (среднее значение)
print(f"Медиана: {statistics.median(data)}")

# 3. median_low() - нижняя медиана
print(f"Нижняя медиана: {statistics.median_low(data2)}")

# 4. median_high() - верхняя медиана
print(f"Верхняя медиана: {statistics.median_high(data2)}")

# 5. mode() - мода (самое частое значение)
print(f"Мода: {statistics.mode(data2)}")

# 6. multimode() - все моды
print(f"Все моды: {statistics.multimode([1, 2, 2, 3, 3, 4])}")

# 7. stdev() - стандартное отклонение (выборка)
print(f"Стандартное отклонение: {statistics.stdev(data)}")

# 8. pstdev() - стандартное отклонение (генеральная совокупность)
print(f"Стандартное отклонение (генер.): {statistics.pstdev(data)}")

# 9. variance() - дисперсия (выборка)
print(f"Дисперсия: {statistics.variance(data)}")

# 10. pvariance() - дисперсия (генеральная совокупность)
print(f"Дисперсия (генер.): {statistics.pvariance(data)}")

# 11. quantiles() - квантили
print(f"Квантили: {statistics.quantiles(data, n = 4)}")  # квартили

# 12. harmonic_mean() - среднее гармоническое
print(f"Среднее гармоническое: {statistics.harmonic_mean([10, 20, 30])}")

# 2. Создайте модуль cubed, содержащий функцию, которая принимает в качестве параметра число, возводит это число в куб и возвращает его.
# Импортируйте и вызовите функцию из другого модуля.
# Импортируем модуль cubed (предполагается, что файл cubed.py находится в той же папке)

# Способ 1: импорт всего модуля
import cubed

# Используем функцию из модуля
result1 = cubed.cube(5)
print(f"5 в кубе = {result1}")

result2 = cubed.cube(3.5)
print(f"3.5 в кубе = {result2}")

result3 = cubed.cube(-4)
print(f"(-4) в кубе = {result3}")

print("-" * 30)

# Способ 2: импорт конкретной функции
from cubed import cube

number = 7
print(f"{number} в кубе = {cube(number)}")

# Способ 3: импорт с псевдонимом
import cubed as cb

print(f"10 в кубе = {cb.cube(10)}")