# Логические операторы. F-строки. Тернарный оператор. Функция bool
age = 20

if age > 18:
    print("You are older than 18")
    print("You can drive a car")
else:
    print("You are younger than 18")
    print("You should sit in a passenger seat")

# and - Позволяет соединить два логический выражения и требует, чтобы оба выполнялись. Название - логическое И
age = 18

if age > 6 and age < 99 and age % 2 == 0:
    print("You are allowed to play Lego game")

# or - Позволяет соединить два логический выражения и требует, чтобы хотя бы один из них выполнялся. Название - логическое ИЛИ
age = 10
ticket = True

if age < 7 or ticket:
    print("You are allowed to play Lego game")

# not - Переворачивает следующее за ним логическое значение. Название - логическое НЕ
age = 18

if not age != 18:
    print("You are allowed to play Lego game")

# ======================================================================================

age = int(input("Введите ваш возраст: "))

if age == 10 or age == 11 or age == 12:
    print("Вы приняты в команду!")
else:
    print("К сожалению, мы не можем вас принять")
