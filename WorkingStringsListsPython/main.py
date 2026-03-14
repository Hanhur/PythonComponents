# Работа со строками и списками в Python
# string = "Hello World"
# string = 'Fry this' + string[5:]
# string = string.replace('F', 'G', 1)
# string = string.replace('i', 'I', 1)
# string = string.replace(' ', '-', 1)
# print(string[::-1])
# string = string.index('H')
# string = string.find('H')
# print(string)

# len() -> length - длина
# spisok = ["first", "second", "third", "fourth"]
# print(spisok[-1])

# spisok = [1, 2, 3]
# spisok.append(4)
# spisok.extend("456")
# spisok += list("456")
# spisok.sort(reverse = True)
# spisok.remove(3)
# print(spisok)


# spisok = []
# numbers = int(input("Сколько элементов должно быть в списке: "))
# for i in range(numbers):
#     num = int(input("Введите число, кратное 3:"))
#     if num % 3 == 0:
#         spisok.append(num)
#     else:
#         print(f"{num} не кратно 3")
# print(spisok)

spisok = [1, 2, 3]
spisok1 = [11, 22, 33]
new_spisok = []
for i in range(len(spisok)):
    new_spisok.append(spisok[i])
    new_spisok.append(spisok1[i])
print(new_spisok)