# Функция getattr, setattr, hasattr, delattr
from fileinput import filename


# class My(int):
#     pass
#
# my_int = My()
# my_int.integer = 5
#
# print(getattr(my_int, "integer"))
# print(setattr(My, 'b', 2))
# print(hasattr(my_int, "integer"))
# print(delattr(my_int, "integer"))
#
# print(isinstance(my_int, My))
# print(issubclass(My, int))

# ===========================================================================================================

# class ShoppingCart:
#     def __init__(self):
#         self.items = {}
#
#     def add_item(self, item, price, quantity = 1):
#         if item in self.items:
#             self.items[item]["quantity"] += quantity
#         else:
#             self.items[item] = {"quantity": quantity, "price": price}
#
#     def remove_item(self, item, quantity = 1):
#         if item in self.items:
#             if quantity >= self.items[item]["quantity"]:
#                 del self.items[item]
#             else:
#                 self.items[item]["quantity"] -= quantity
#         else:
#             print(f"You don\'t have this amount of {item} in your cart!")
#
#     def get_total_price(self):
#         total = 0
#         for item in self.items:
#             total += self.items[item]["quantity"] * self.items[item]["price"]
#         return total
#
#     def list_all_items(self):
#         for key, value in self.items.items():
#             print(f"{key} в тележке {value["quantity"]} шт.")
#
# my_cart = ShoppingCart()
# my_cart.add_item(item = "Творог", price = 100, quantity = 1)
# my_cart.add_item(item = "Молоко", price = 50, quantity = 2)
# my_cart.add_item(item = "Яйца", price = 100, quantity = 1)
#
# print(my_cart.list_all_items())
# print(my_cart.get_total_price())
# my_cart.remove_item(item = "Молоко", quantity = 1)
#
# print(my_cart.get_total_price())
# my_cart.remove_item(item = "Яйца", quantity = 2)
#
# print(my_cart.get_total_price())
# my_cart.remove_item(item = "Творог", quantity = 1)

# ===========================================================================================================

class Textprocessor:
    def __init__(self, filename):
        self.filemane = filename
        self.read_file()

    def read_file(self):
        try:
            with open(self.filemane, 'r', encoding = "utf-8") as file:
                self.text = file.read()
        except FileNotFoundError:
            self.text = "File is not found, sorry"

    def write_file(self):
        with open(self.filemane, 'w', encoding = "utf-8") as file:
            file.write(self.text)

    def count_words(self):
        words = self.text.split()
        return len(words)

    def count_characters(self):
        return len(self.text)

    def count_sentences(self):
        sentences = self.text.split(".")
        return  len(sentences)

    def replace(self, old_word, new_word):
        self.text = self.text.replace(old_word, new_word)

    def reverse(self):
        self.text = self.text[::-1]

# read_file() читает файл
# write_file() запись файл
# count_words() количество слов в тексте
# count_characters() количество символов
# count_sentences() количество предложений
# replace(old_word, new_word) имплементация стандартной функции replace у строки
# reverce() переворот строки

tp = Textprocessor("example.txt")

tp.replace("example", "test")
tp.reverse()

tp.write_file()