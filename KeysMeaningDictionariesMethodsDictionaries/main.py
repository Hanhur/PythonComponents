# Словари в Python. Ключи и значения словарей. Методы словарей
# def digit_stats(numbers):
#     stats = {}
#     for num in numbers:
#         # Количество цифр в числе (убираем минус для отрицательных)
#         num_digits = len(str(abs(num)))
#         stats[num_digits] = stats.get(num_digits, 0) + 1
#
#     for digits, count in sorted(stats.items()):
#         print(f"{digits} цифр{'а' if digits % 10 == 1 and digits != 11 else 'ы'} — {count} элемент{'а' if count % 10 == 1 and count != 11 else 'ов' if count > 4 else ''}")
#
# # Пример использования
# t = (3, 45, 123, 7, 89, 6789, 0, -42, 1000)
# digit_stats(t)

# =============================================================================

# def digit_stats_simple(numbers):
#     stats = {}
#     for num in numbers:
#         d = len(str(abs(num)))
#         stats[d] = stats.get(d, 0) + 1
#
#     for d, c in sorted(stats.items()):
#         print(f"{d} цифр{'а' if d == 1 else 'ы'} — {c} элементов")
#
# t = (3, 45, 123, 7, 89, 6789, 0, -42, 1000)
# digit_stats_simple(t)

# =============================================================================

# my_dict = {1: 2, 3: 4, 5: 6}
#
# # .keys() возвращает список всех ключей словаря
# print(type(my_dict.keys()))
# for key in my_dict.keys():
#     print(key)
#
# # .values() возвращает список всех значений словаря
# print(type(my_dict.values()))
# for value in my_dict.values():
#     print(value)
#
# # .items() возвращает список всех пар словаря
# print(type(my_dict.items()))
# for key, value in my_dict.items():
#     print(key, value)

# =============================================================================

# data = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
#
# result = 1
# for value in data.values():
#     result *= value
#
# print(result)

# =============================================================================
#
# # Создаем пустой словарь
# vegetables = {}
#
# # Запрашиваем 4 овоща и сохраняем с индексами 1-4
# for i in range(1, 5):
#     veg = input(f"-> ")
#     vegetables[i] = veg
#
# # Выводим словарь
# print(vegetables)
#
# # Запрашиваем индекс элемента для удаления
# index_to_remove = int(input("Какой элемент исключить: "))
#
# # Удаляем элемент
# if index_to_remove in vegetables:
#     del vegetables[index_to_remove]
#
# # Выводим обновленный словарь
# print(vegetables)

# =============================================================================

# # Исходный словарь
# employee = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
#
# # Создаем новый словарь с именем и зарплатой
# name_salary = {key: employee[key] for key in ['name', 'salary']}
#
# # Удаляем эти ключи из исходного словаря
# for key in ['name', 'salary']:
#     del employee[key]
#
# # Выводим результаты
# print(employee)
# print(name_salary)

# =============================================================================

# # Исходный словарь
# employee = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
#
# # Создаем новый словарь и одновременно удаляем значения из исходного
# name_salary = {
#     'name': employee.pop('name'),
#     'salary': employee.pop('salary')
# }
#
# # Выводим результаты
# print(employee)
# print(name_salary)

# =============================================================================

# Вот решение для переименования ключа в словаре:
# # Исходный словарь
# data = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
#
# # Переименовываем ключ 'city' в 'location'
# data['location'] = data.pop('city')
#
# # Выводим результат
# print(data)

# =============================================================================

# # Альтернативный вариант (более безопасный, с проверкой наличия ключа):
# data = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
#
# if 'city' in data:
#     data['location'] = data.pop('city')
#
# print(data)

# =============================================================================

# # Исходный список
# mixed_list = ["one", 1, 2, 3, "two", 10, 20, "three", 15, 36, 60, "four", -20]
#
# # Результирующий словарь
# result = {}
# current_key = None
#
# for item in mixed_list:
#     if isinstance(item, str):  # если элемент - строка
#         current_key = item
#         result[current_key] = []  # создаем пустой список для будущих чисел
#     else:  # если элемент - число
#         if current_key is not None:
#             result[current_key].append(item)  # добавляем число к текущему ключу
#
# print(result)

# =============================================================================

# Альтернативное решение (более компактное):
# mixed_list = ["one", 1, 2, 3, "two", 10, 20, "three", 15, 36, 60, "four", -20]
#
# result = {}
# key = None
#
# for item in mixed_list:
#     if isinstance(item, str):
#         key = item
#         result[key] = []
#     else:
#         result[key].append(item)
#
# print(result)

# =============================================================================

# Хранилище данных: ключ - ФИО, значение - рост
# basketball_players = {}
#
#
# def show_menu():
#     print("\n" + "=" * 50)
#     print("Управление данными о баскетболистах")
#     print("=" * 50)
#     print("1. Добавить баскетболиста")
#     print("2. Удалить баскетболиста")
#     print("3. Найти баскетболиста")
#     print("4. Заменить данные")
#     print("5. Показать всех баскетболистов")
#     print("6. Выйти")
#     print("-" * 50)
#
#
# def add_player():
#     name = input("Введите ФИО баскетболиста: ").strip()
#     if name in basketball_players:
#         print(f"Баскетболист {name} уже существует!")
#         return
#
#     try:
#         height = float(input("Введите рост (в см): "))
#         basketball_players[name] = height
#         print(f"Баскетболист {name} с ростом {height} см добавлен!")
#     except ValueError:
#         print("Ошибка: рост должен быть числом!")
#
#
# def remove_player():
#     name = input("Введите ФИО баскетболиста для удаления: ").strip()
#     if name in basketball_players:
#         del basketball_players[name]
#         print(f"Баскетболист {name} удален!")
#     else:
#         print(f"Баскетболист {name} не найден!")
#
#
# def search_player():
#     name = input("Введите ФИО баскетболиста для поиска: ").strip()
#     if name in basketball_players:
#         print(f"Найден: {name} - рост {basketball_players[name]} см")
#     else:
#         print(f"Баскетболист {name} не найден!")
#
#
# def update_player():
#     name = input("Введите ФИО баскетболиста для замены данных: ").strip()
#     if name in basketball_players:
#         try:
#             new_height = float(input(f"Введите новый рост для {name} (было {basketball_players[name]} см): "))
#             basketball_players[name] = new_height
#             print(f"Данные обновлены: {name} - рост {new_height} см")
#         except ValueError:
#             print("Ошибка: рост должен быть числом!")
#     else:
#         print(f"Баскетболист {name} не найден!")
#
#
# def show_all_players():
#     if not basketball_players:
#         print("Список баскетболистов пуст!")
#     else:
#         print("\nСписок всех баскетболистов:")
#         print("-" * 40)
#         for name, height in basketball_players.items():
#             print(f"{name}: {height} см")
#         print("-" * 40)
#         print(f"Всего: {len(basketball_players)} баскетболистов")
#
#
# def main():
#     while True:
#         show_menu()
#         choice = input("Выберите действие (1-6): ").strip()
#
#         if choice == '1':
#             add_player()
#         elif choice == '2':
#             remove_player()
#         elif choice == '3':
#             search_player()
#         elif choice == '4':
#             update_player()
#         elif choice == '5':
#             show_all_players()
#         elif choice == '6':
#             print("До свидания!")
#             break
#         else:
#             print("Неверный выбор! Пожалуйста, выберите от 1 до 6.")
#
#
# if __name__ == "__main__":
#     # Добавим несколько примеров для демонстрации
#     basketball_players = {
#         "Майкл Джордан": 198,
#         "Леброн Джеймс": 203,
#         "Коби Брайант": 198
#     }
#
#     main()

# =============================================================================

# Хранилище данных: ключ - английское слово, значение - французский перевод
# eng_fre_dict = {}
#
# def show_menu():
#     print("\n" + "=" * 50)
#     print("АНГЛО-ФРАНЦУЗСКИЙ СЛОВАРЬ")
#     print("=" * 50)
#     print("1. Добавить слово и перевод")
#     print("2. Удалить слово")
#     print("3. Найти перевод")
#     print("4. Заменить перевод")
#     print("5. Показать все слова")
#     print("6. Выйти")
#     print("-" * 50)
#
#
# def add_word():
#     english = input("Введите слово на английском: ").strip().lower()
#     if english in eng_fre_dict:
#         print(f"Слово '{english}' уже существует! Текущий перевод: {eng_fre_dict[english]}")
#         choice = input("Хотите заменить перевод? (да/нет): ").strip().lower()
#         if choice == 'да':
#             french = input("Введите новый перевод на французский: ").strip()
#             eng_fre_dict[english] = french
#             print(f"Перевод для '{english}' обновлен: {french}")
#         return
#
#     french = input("Введите перевод на французский: ").strip()
#     eng_fre_dict[english] = french
#     print(f"Слово '{english}' -> '{french}' добавлено!")
#
#
# def remove_word():
#     english = input("Введите слово на английском для удаления: ").strip().lower()
#     if english in eng_fre_dict:
#         del eng_fre_dict[english]
#         print(f"Слово '{english}' удалено из словаря!")
#     else:
#         print(f"Слово '{english}' не найдено в словаре!")
#
#
# def search_word():
#     english = input("Введите слово на английском для поиска: ").strip().lower()
#     if english in eng_fre_dict:
#         print(f"{english} -> {eng_fre_dict[english]}")
#     else:
#         print(f"Слово '{english}' не найдено в словаре!")
#         choice = input("Хотите добавить это слово? (да/нет): ").strip().lower()
#         if choice == 'да':
#             french = input("Введите перевод на французский: ").strip()
#             eng_fre_dict[english] = french
#             print(f"Слово '{english}' -> '{french}' добавлено!")
#
#
# def update_word():
#     english = input("Введите слово на английском для замены перевода: ").strip().lower()
#     if english in eng_fre_dict:
#         print(f"Текущий перевод: {eng_fre_dict[english]}")
#         new_french = input("Введите новый перевод на французский: ").strip()
#         eng_fre_dict[english] = new_french
#         print(f"Перевод для '{english}' обновлен: {new_french}")
#     else:
#         print(f"Слово '{english}' не найдено в словаре!")
#
#
# def show_all_words():
#     if not eng_fre_dict:
#         print("Словарь пуст!")
#     else:
#         print("\nСОДЕРЖИМОЕ СЛОВАРЯ:")
#         print("=" * 40)
#         # Сортировка по алфавиту
#         for english, french in sorted(eng_fre_dict.items()):
#             print(f"{english:15} -> {french}")
#         print("=" * 40)
#         print(f"Всего слов: {len(eng_fre_dict)}")
#
#
# def main():
#     # Добавим несколько примеров для демонстрации
#     global eng_fre_dict
#     eng_fre_dict = {
#         "hello": "bonjour",
#         "goodbye": "au revoir",
#         "thank you": "merci",
#         "please": "s'il vous plaît",
#         "yes": "oui",
#         "no": "non"
#     }
#
#     while True:
#         show_menu()
#         choice = input("Выберите действие (1-6): ").strip()
#
#         if choice == '1':
#             add_word()
#         elif choice == '2':
#             remove_word()
#         elif choice == '3':
#             search_word()
#         elif choice == '4':
#             update_word()
#         elif choice == '5':
#             show_all_words()
#         elif choice == '6':
#             print("Merci! До свидания!")
#             break
#         else:
#             print("Неверный выбор! Пожалуйста, выберите от 1 до 6.")
#
#
# if __name__ == "__main__":
#     main()

# =============================================================================

# Хранилище данных: ключ - ФИО, значение - словарь с информацией о сотруднике
# company = {}
#
# def show_menu():
#     print("\n" + "=" * 60)
#     print("ПРОГРАММА «ФИРМА» - Управление сотрудниками")
#     print("=" * 60)
#     print("1. Добавить сотрудника")
#     print("2. Удалить сотрудника")
#     print("3. Найти сотрудника")
#     print("4. Заменить данные сотрудника")
#     print("5. Показать всех сотрудников")
#     print("6. Выйти")
#     print("-" * 60)
#
#
# def get_employee_info():
#     """Сбор информации о сотруднике"""
#     print("\nВведите данные сотрудника:")
#     phone = input("Телефон: ").strip()
#     email = input("Рабочий email: ").strip()
#     position = input("Название должности: ").strip()
#     office = input("Номер кабинета: ").strip()
#     skype = input("Skype: ").strip()
#
#     return {
#         "phone": phone,
#         "email": email,
#         "position": position,
#         "office": office,
#         "skype": skype
#     }
#
#
# def display_employee_info(name, info):
#     """Вывод информации о сотруднике"""
#     print(f"\n--- {name} ---")
#     print(f"  Телефон: {info['phone']}")
#     print(f"  Email: {info['email']}")
#     print(f"  Должность: {info['position']}")
#     print(f"  Кабинет: {info['office']}")
#     print(f"  Skype: {info['skype']}")
#
#
# def add_employee():
#     name = input("Введите ФИО сотрудника: ").strip().title()
#
#     if name in company:
#         print(f"Сотрудник {name} уже существует!")
#         choice = input("Хотите обновить информацию? (да/нет): ").strip().lower()
#         if choice == 'да':
#             company[name] = get_employee_info()
#             print(f"Информация о сотруднике {name} обновлена!")
#         return
#
#     company[name] = get_employee_info()
#     print(f"Сотрудник {name} успешно добавлен!")
#
#
# def remove_employee():
#     name = input("Введите ФИО сотрудника для удаления: ").strip().title()
#
#     if name in company:
#         print(f"\nНайден сотрудник:")
#         display_employee_info(name, company[name])
#         confirm = input(f"\nУдалить сотрудника {name}? (да/нет): ").strip().lower()
#         if confirm == 'да':
#             del company[name]
#             print(f"Сотрудник {name} удален!")
#         else:
#             print("Удаление отменено.")
#     else:
#         print(f"Сотрудник {name} не найден!")
#
#
# def search_employee():
#     print("\nПоиск сотрудника:")
#     print("1. Поиск по ФИО")
#     print("2. Поиск по номеру кабинета")
#     print("3. Поиск по должности")
#     choice = input("Выберите способ поиска (1-3): ").strip()
#
#     if choice == '1':
#         name = input("Введите ФИО: ").strip().title()
#         if name in company:
#             display_employee_info(name, company[name])
#         else:
#             print(f"Сотрудник {name} не найден!")
#
#     elif choice == '2':
#         office = input("Введите номер кабинета: ").strip()
#         found = False
#         for name, info in company.items():
#             if info['office'] == office:
#                 display_employee_info(name, info)
#                 found = True
#         if not found:
#             print(f"Сотрудники в кабинете {office} не найдены!")
#
#     elif choice == '3':
#         position = input("Введите название должности: ").strip().lower()
#         found = False
#         for name, info in company.items():
#             if info['position'].lower() == position:
#                 display_employee_info(name, info)
#                 found = True
#         if not found:
#             print(f"Сотрудники с должностью '{position}' не найдены!")
#
#     else:
#         print("Неверный выбор!")
#
#
# def update_employee():
#     name = input("Введите ФИО сотрудника для замены данных: ").strip().title()
#
#     if name not in company:
#         print(f"Сотрудник {name} не найден!")
#         return
#
#     print(f"\nТекущие данные сотрудника {name}:")
#     display_employee_info(name, company[name])
#
#     print("\nЧто вы хотите изменить?")
#     print("1. Телефон")
#     print("2. Email")
#     print("3. Должность")
#     print("4. Номер кабинета")
#     print("5. Skype")
#     print("6. Все данные")
#
#     choice = input("Выберите пункт (1-6): ").strip()
#
#     if choice == '1':
#         company[name]['phone'] = input("Новый телефон: ").strip()
#         print("Телефон обновлен!")
#     elif choice == '2':
#         company[name]['email'] = input("Новый email: ").strip()
#         print("Email обновлен!")
#     elif choice == '3':
#         company[name]['position'] = input("Новая должность: ").strip()
#         print("Должность обновлена!")
#     elif choice == '4':
#         company[name]['office'] = input("Новый номер кабинета: ").strip()
#         print("Номер кабинета обновлен!")
#     elif choice == '5':
#         company[name]['skype'] = input("Новый Skype: ").strip()
#         print("Skype обновлен!")
#     elif choice == '6':
#         company[name] = get_employee_info()
#         print("Все данные обновлены!")
#     else:
#         print("Неверный выбор!")
#
#
# def show_all_employees():
#     if not company:
#         print("\nСписок сотрудников пуст!")
#     else:
#         print("\n" + "=" * 60)
#         print("СПИСОК ВСЕХ СОТРУДНИКОВ")
#         print("=" * 60)
#
#         # Сортировка по ФИО
#         for name in sorted(company.keys()):
#             info = company[name]
#             print(f"\n{name}")
#             print(f"  📞 {info['phone']}  |  ✉️ {info['email']}")
#             print(f"  💼 {info['position']}  |  🚪 Каб. {info['office']}  |  💬 {info['skype']}")
#             print("-" * 50)
#
#         print(f"\nВсего сотрудников: {len(company)}")
#
#
# def main():
#     # Добавим несколько примеров для демонстрации
#     global company
#     company = {
#         "Иван Петров": {
#             "phone": "+7 (495) 123-45-67",
#             "email": "ivan.petrov@company.ru",
#             "position": "Менеджер",
#             "office": "101",
#             "skype": "ivan.petrov"
#         },
#         "Елена Смирнова": {
#             "phone": "+7 (495) 234-56-78",
#             "email": "elena.smirnova@company.ru",
#             "position": "Разработчик",
#             "office": "205",
#             "skype": "e.smirnova"
#         },
#         "Алексей Иванов": {
#             "phone": "+7 (495) 345-67-89",
#             "email": "alex.ivanov@company.ru",
#             "position": "Директор",
#             "office": "301",
#             "skype": "alex.ivanov"
#         }
#     }
#
#     while True:
#         show_menu()
#         choice = input("Выберите действие (1-6): ").strip()
#
#         if choice == '1':
#             add_employee()
#         elif choice == '2':
#             remove_employee()
#         elif choice == '3':
#             search_employee()
#         elif choice == '4':
#             update_employee()
#         elif choice == '5':
#             show_all_employees()
#         elif choice == '6':
#             print("До свидания!")
#             break
#         else:
#             print("Неверный выбор! Пожалуйста, выберите от 1 до 6.")
#
#
# if __name__ == "__main__":
#     main()

# =============================================================================

# Хранилище данных: ключ - ID книги (или название+автор), значение - словарь с информацией
# Для удобства будем использовать название книги + автор как уникальный ключ
book_collection = {}

def show_menu():
    print("\n" + "=" * 60)
    print("ПРОГРАММА «КНИЖНАЯ КОЛЛЕКЦИЯ»")
    print("=" * 60)
    print("1. Добавить книгу")
    print("2. Удалить книгу")
    print("3. Найти книгу")
    print("4. Заменить данные книги")
    print("5. Показать все книги")
    print("6. Статистика коллекции")
    print("7. Выйти")
    print("-" * 60)


def get_book_key(author, title):
    """Создание уникального ключа для книги"""
    return f"{author}||{title}".lower()


def get_book_info():
    """Сбор информации о книге"""
    print("\nВведите данные книги:")
    author = input("Автор: ").strip().title()
    title = input("Название книги: ").strip().title()
    genre = input("Жанр: ").strip().title()

    while True:
        try:
            year = int(input("Год выпуска: "))
            if 1450 <= year <= 2026:  # Примерные границы
                break
            else:
                print("Пожалуйста, введите корректный год (1450-2026)")
        except ValueError:
            print("Ошибка: год должен быть числом!")

    while True:
        try:
            pages = int(input("Количество страниц: "))
            if pages > 0:
                break
            else:
                print("Количество страниц должно быть положительным!")
        except ValueError:
            print("Ошибка: количество страниц должно быть числом!")

    publisher = input("Издательство: ").strip().title()

    return {
        "author": author,
        "title": title,
        "genre": genre,
        "year": year,
        "pages": pages,
        "publisher": publisher
    }


def display_book_info(key, book):
    """Вывод информации о книге"""
    print(f"\n📚 {book['title']}")
    print(f"   Автор: {book['author']}")
    print(f"   Жанр: {book['genre']}")
    print(f"   Год выпуска: {book['year']}")
    print(f"   Страниц: {book['pages']}")
    print(f"   Издательство: {book['publisher']}")
    print("-" * 40)


def add_book():
    author = input("Введите автора: ").strip().title()
    title = input("Введите название книги: ").strip().title()
    key = get_book_key(author, title)

    if key in book_collection:
        print(f"\nКнига уже существует в коллекции!")
        book_collection[key]['author'] = author
        book_collection[key]['title'] = title
        display_book_info(key, book_collection[key])
        choice = input("\nХотите обновить информацию? (да/нет): ").strip().lower()
        if choice == 'да':
            book_collection[key] = get_book_info()
            print("Информация о книге обновлена!")
        return

    # Если книга новая, собираем полную информацию
    book_info = {
        "author": author,
        "title": title,
        "genre": input("Жанр: ").strip().title(),
        "year": int(input("Год выпуска: ")),
        "pages": int(input("Количество страниц: ")),
        "publisher": input("Издательство: ").strip().title()
    }

    book_collection[key] = book_info
    print(f"\nКнига '{title}' успешно добавлена в коллекцию!")


def remove_book():
    author = input("Введите автора: ").strip().title()
    title = input("Введите название книги: ").strip().title()
    key = get_book_key(author, title)

    if key in book_collection:
        print("\nНайдена книга:")
        display_book_info(key, book_collection[key])
        confirm = input(f"\nУдалить книгу '{title}'? (да/нет): ").strip().lower()
        if confirm == 'да':
            del book_collection[key]
            print(f"Книга '{title}' удалена из коллекции!")
        else:
            print("Удаление отменено.")
    else:
        print(f"Книга '{title}' автора {author} не найдена в коллекции!")


def search_book():
    print("\nПоиск книги:")
    print("1. Поиск по названию")
    print("2. Поиск по автору")
    print("3. Поиск по жанру")
    print("4. Поиск по году выпуска")
    print("5. Поиск по издательству")

    choice = input("Выберите способ поиска (1-5): ").strip()

    if choice == '1':
        title = input("Введите название книги: ").strip().lower()
        found = False
        for key, book in book_collection.items():
            if book['title'].lower() == title:
                display_book_info(key, book)
                found = True
        if not found:
            print(f"Книги с названием '{title}' не найдены!")

    elif choice == '2':
        author = input("Введите автора: ").strip().lower()
        found = False
        for key, book in book_collection.items():
            if book['author'].lower() == author:
                display_book_info(key, book)
                found = True
        if not found:
            print(f"Книги автора '{author}' не найдены!")

    elif choice == '3':
        genre = input("Введите жанр: ").strip().lower()
        found = False
        for key, book in book_collection.items():
            if book['genre'].lower() == genre:
                display_book_info(key, book)
                found = True
        if not found:
            print(f"Книги жанра '{genre}' не найдены!")

    elif choice == '4':
        try:
            year = int(input("Введите год выпуска: "))
            found = False
            for key, book in book_collection.items():
                if book['year'] == year:
                    display_book_info(key, book)
                    found = True
            if not found:
                print(f"Книги {year} года не найдены!")
        except ValueError:
            print("Ошибка: год должен быть числом!")

    elif choice == '5':
        publisher = input("Введите издательство: ").strip().lower()
        found = False
        for key, book in book_collection.items():
            if book['publisher'].lower() == publisher:
                display_book_info(key, book)
                found = True
        if not found:
            print(f"Книги издательства '{publisher}' не найдены!")

    else:
        print("Неверный выбор!")


def update_book():
    author = input("Введите автора: ").strip().title()
    title = input("Введите название книги: ").strip().title()
    key = get_book_key(author, title)

    if key not in book_collection:
        print(f"Книга '{title}' автора {author} не найдена!")
        return

    print(f"\nТекущие данные книги:")
    display_book_info(key, book_collection[key])

    print("\nЧто вы хотите изменить?")
    print("1. Автора")
    print("2. Название")
    print("3. Жанр")
    print("4. Год выпуска")
    print("5. Количество страниц")
    print("6. Издательство")
    print("7. Все данные")

    choice = input("Выберите пункт (1-7): ").strip()

    if choice == '1':
        new_author = input("Новый автор: ").strip().title()
        old_author = book_collection[key]['author']
        old_title = book_collection[key]['title']
        new_key = get_book_key(new_author, old_title)
        book_collection[key]['author'] = new_author
        if new_key != key:
            book_collection[new_key] = book_collection.pop(key)
        print("Автор обновлен!")

    elif choice == '2':
        new_title = input("Новое название: ").strip().title()
        old_author = book_collection[key]['author']
        new_key = get_book_key(old_author, new_title)
        book_collection[key]['title'] = new_title
        if new_key != key:
            book_collection[new_key] = book_collection.pop(key)
        print("Название обновлено!")

    elif choice == '3':
        book_collection[key]['genre'] = input("Новый жанр: ").strip().title()
        print("Жанр обновлен!")

    elif choice == '4':
        try:
            book_collection[key]['year'] = int(input("Новый год выпуска: "))
            print("Год выпуска обновлен!")
        except ValueError:
            print("Ошибка: год должен быть числом!")

    elif choice == '5':
        try:
            book_collection[key]['pages'] = int(input("Новое количество страниц: "))
            print("Количество страниц обновлено!")
        except ValueError:
            print("Ошибка: количество страниц должно быть числом!")

    elif choice == '6':
        book_collection[key]['publisher'] = input("Новое издательство: ").strip().title()
        print("Издательство обновлено!")

    elif choice == '7':
        new_info = get_book_info()
        new_key = get_book_key(new_info['author'], new_info['title'])
        book_collection[new_key] = new_info
        if new_key != key:
            del book_collection[key]
        print("Все данные обновлены!")

    else:
        print("Неверный выбор!")


def show_all_books():
    if not book_collection:
        print("\nКоллекция книг пуста!")
    else:
        print("\n" + "=" * 60)
        print("КНИЖНАЯ КОЛЛЕКЦИЯ")
        print("=" * 60)

        # Сортировка по автору и названию
        for key in sorted(book_collection.keys()):
            book = book_collection[key]
            print(f"\n📖 {book['title']}")
            print(f"   👤 {book['author']} | 📚 {book['genre']}")
            print(f"   📅 {book['year']} | 📄 {book['pages']} стр. | 🏢 {book['publisher']}")
            print("-" * 50)

        print(f"\nВсего книг в коллекции: {len(book_collection)}")


def show_statistics():
    if not book_collection:
        print("\nКоллекция пуста! Добавьте книги для просмотра статистики.")
        return

    total_books = len(book_collection)
    total_pages = sum(book['pages'] for book in book_collection.values())
    avg_pages = total_pages / total_books

    # Статистика по жанрам
    genres = {}
    for book in book_collection.values():
        genre = book['genre']
        genres[genre] = genres.get(genre, 0) + 1

    # Статистика по годам
    years = {}
    for book in book_collection.values():
        year = book['year']
        years[year] = years.get(year, 0) + 1

    # Самая старая и новая книга
    oldest_book = min(book_collection.values(), key=lambda x: x['year'])
    newest_book = max(book_collection.values(), key=lambda x: x['year'])

    print("\n" + "=" * 60)
    print("СТАТИСТИКА КОЛЛЕКЦИИ")
    print("=" * 60)
    print(f"📚 Всего книг: {total_books}")
    print(f"📄 Всего страниц: {total_pages}")
    print(f"📊 Среднее количество страниц: {avg_pages:.1f}")
    print(f"\n📖 Самая старая книга: {oldest_book['title']} ({oldest_book['year']})")
    print(f"🆕 Самая новая книга: {newest_book['title']} ({newest_book['year']})")

    print(f"\n📚 Книги по жанрам:")
    for genre, count in sorted(genres.items()):
        print(f"   {genre}: {count} книг")

    print(f"\n📅 Книги по годам:")
    for year in sorted(years.keys()):
        print(f"   {year}: {years[year]} книг")


def main():
    # Добавим несколько примеров для демонстрации
    global book_collection
    book_collection = {
        "михаил булгаков||мастер и маргарита".lower(): {
            "author": "Михаил Булгаков",
            "title": "Мастер и Маргарита",
            "genre": "Роман",
            "year": 1967,
            "pages": 480,
            "publisher": "Эксмо"
        },
        "лев толстой||война и мир".lower(): {
            "author": "Лев Толстой",
            "title": "Война и мир",
            "genre": "Роман-эпопея",
            "year": 1869,
            "pages": 1225,
            "publisher": "АСТ"
        },
        "федор достоевский||преступление и наказание".lower(): {
            "author": "Федор Достоевский",
            "title": "Преступление и наказание",
            "genre": "Роман",
            "year": 1866,
            "pages": 672,
            "publisher": "Азбука"
        }
    }

    while True:
        show_menu()
        choice = input("Выберите действие (1-7): ").strip()

        if choice == '1':
            add_book()
        elif choice == '2':
            remove_book()
        elif choice == '3':
            search_book()
        elif choice == '4':
            update_book()
        elif choice == '5':
            show_all_books()
        elif choice == '6':
            show_statistics()
        elif choice == '7':
            print("До свидания! Хорошего дня!")
            break
        else:
            print("Неверный выбор! Пожалуйста, выберите от 1 до 7.")


if __name__ == "__main__":
    main()