# 1. Измените порядок символов строки "позавчера" при помощи стека.
def reverse_string_using_stack(s):
    # Создаём пустой стек (список)
    stack = []

    # 1. Кладём все символы в стек
    for char in s:
        stack.append(char)

    # 2. Извлекаем символы из стека в обратном порядке
    reversed_string = ''
    while stack:
        reversed_string += stack.pop()

    return reversed_string


# Исходная строка
original = "позавчера"
result = reverse_string_using_stack(original)

print(f"Исходная строка: {original}")
print(f"Перевёрнутая строка: {result}")

# 2. Используйте стек, чтобы создать новый список с элементами списка [1, 2, 3, 4, 5] в обратном порядке.
original = [1, 2, 3, 4, 5]
stack = original[:]  # копируем в стек
reversed_list = []

while stack:
    reversed_list.append(stack.pop())

print(reversed_list)  # [5, 4, 3, 2, 1]