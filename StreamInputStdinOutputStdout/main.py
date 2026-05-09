# Режимы открытия файлов в Python. Потоковый ввод stdin и вывод stdout
# IO - In Out

# print(f.read()) -> считывает весь файл целиком и возвращает строку
# print(f.readline()) -> считывает строку и возвращает строку
# print(f.readlines()) -> считывает все строки и возвращает список

# import  sys

# sys.stdout -> поток для вывода данных в консоль
# sys.stdin -> поток для считывания данных из крнсоли
# sys.stderr -> поток для вывода ошибок

# with open(file = "file.txt", mode = 'r', encoding = 'UTF-8') as f:
#     for string in f:
#         print(string, end = '')

# =============================================================================

# Способ 1: Подсчёт всех символов (включая пробелы и переносы строк)
# Способ 1: Чтение всего файла и подсчёт символов
# Способ 1: Чтение всего файла и подсчёт символов
# filename = "file.txt"  # Укажите путь к вашему файлу
#
# try:
#     with open(filename, 'r', encoding='utf-8') as file:
#         content = file.read()
#         char_count = len(content)
#
#     print(f"Количество символов в файле '{filename}': {char_count}")
# except FileNotFoundError:
#     print(f"Файл '{filename}' не найден!")
# except Exception as e:
#     print(f"Ошибка при чтении файла: {e}")

# =============================================================================

# Способ 2: Подсчёт символов без учёта пробелов и переносов строк
# import re
#
# filename = "file.txt"
#
# try:
#     with open(filename, 'r', encoding = 'utf-8') as file:
#         content = file.read()
#         # Удаляем пробелы, табуляции и переносы строк
#         content_no_spaces = re.sub(r'\s', '', content)
#         char_count = len(content_no_spaces)
#
#     print(f"Количество символов (без пробелов и переносов строк): {char_count}")
# except FileNotFoundError:
#     print(f"Файл '{filename}' не найден!")

# =============================================================================

# Способ 3: Подробная статистика
# filename = "file.txt"
#
# try:
#     with open(filename, 'r', encoding = 'utf-8') as file:
#         content = file.read()
#
#         total_chars = len(content)
#         chars_no_spaces = len(content.replace(' ', '').replace('\n', '').replace('\t', ''))
#         spaces = content.count(' ')
#         newlines = content.count('\n')
#         tabs = content.count('\t')
#
#     print(f"Статистика файла '{filename}':")
#     print(f"Всего символов: {total_chars}")
#     print(f"Символов без пробелов и переносов: {chars_no_spaces}")
#     print(f"Пробелов: {spaces}")
#     print(f"Переносов строк: {newlines}")
#     print(f"Табуляций: {tabs}")
#
# except FileNotFoundError:
#     print(f"Файл '{filename}' не найден!")

# =============================================================================

# Способ 4: Построчный подсчёт (для больших файлов)
# filename = "file.txt"
#
# try:
#     total_chars = 0
#     with open(filename, 'r', encoding = 'utf-8') as file:
#         for line in file:
#             total_chars += len(line)
#
#     print(f"Количество символов в файле '{filename}': {total_chars}")
# except FileNotFoundError:
#     print(f"Файл '{filename}' не найден!")

# =============================================================================

# Создаём тестовый файл для проверки
# test_content = """Привет, мир!
# Это тестовый файл.
# Он содержит несколько строк.
# Всего символов нужно подсчитать."""
#
# with open("test_file.txt", 'w', encoding = 'utf-8') as f:
#     f.write(test_content)
#
# # Теперь подсчитываем символы
# filename = "test_file.txt"
#
# try:
#     with open(filename, 'r', encoding = 'utf-8') as file:
#         content = file.read()
#         char_count = len(content)
#
#     print(f"Содержимое файла '{filename}':")
#     print(content)
#     print(f"\nКоличество символов: {char_count}")
# except FileNotFoundError:
#     print(f"Файл '{filename}' не найден!")

# =============================================================================

# Универсальная функция для подсчёта символов
# def count_characters_in_file(filename, ignore_whitespace = False):
#     """
#     Подсчитывает количество символов в файле.
#
#     Параметры:
#     filename - имя файла
#     ignore_whitespace - если True, не учитывает пробелы, табуляции и переносы строк
#
#     Возвращает:
#     количество символов
#     """
#     try:
#         with open(filename, 'r', encoding = 'utf-8') as file:
#             content = file.read()
#
#             if ignore_whitespace:
#                 # Убираем все пробельные символы
#                 import re
#                 content = re.sub(r'\s', '', content)
#
#             return len(content)
#     except FileNotFoundError:
#         print(f"Ошибка: Файл '{filename}' не найден!")
#         return None
#     except Exception as e:
#         print(f"Ошибка при чтении файла: {e}")
#         return None
#
#
# # Использование
# filename = input("Введите имя файла: ")
# count = count_characters_in_file(filename)
#
# if count is not None:
#     print(f"Количество символов: {count}")
#
#     # Спрашиваем, нужно ли исключить пробелы
#     choice = input("Исключить пробелы и переносы строк? (да/нет): ").strip().lower()
#     if choice == 'да':
#         count_no_spaces = count_characters_in_file(filename, ignore_whitespace = True)
#         print(f"Количество символов (без пробелов и переносов): {count_no_spaces}")

# =============================================================================

# Чтение исходного файла и запись слов из 7+ букв в новый файл

# input_filename = "file.txt"  # Исходный файл
# output_filename = "long_words.txt"  # Файл для результата
#
# try:
#     with open(input_filename, 'r', encoding = 'utf-8') as infile:
#         content = infile.read()
#
#     # Разбиваем текст на слова (учитываем знаки препинания)
#     # Заменяем знаки препинания на пробелы
#     import string
#
#     for punct in string.punctuation:
#         content = content.replace(punct, ' ')
#
#     # Разбиваем на слова и фильтруем
#     words = content.split()
#     long_words = [word for word in words if len(word) >= 7]
#
#     # Записываем результат в новый файл
#     with open(output_filename, 'w', encoding = 'utf-8') as outfile:
#         outfile.write('\n'.join(long_words))
#
#     print(f"Найдено слов из 7+ букв: {len(long_words)}")
#     print(f"Результат сохранён в файл '{output_filename}'")
#     if long_words:
#         print("\nНайденные слова:")
#         for word in long_words:
#             print(f"  - {word}")
#
# except FileNotFoundError:
#     print(f"Ошибка: Файл '{input_filename}' не найден!")
# except Exception as e:
#     print(f"Ошибка: {e}")

# =============================================================================

# import re
#
# input_filename = "file.txt"
# output_filename = "long_words.txt"
#
# try:
#     with open(input_filename, 'r', encoding = 'utf-8') as infile:
#         content = infile.read()
#
#     # Регулярное выражение для поиска слов (только буквы)
#     words = re.findall(r'\b[а-яА-Яa-zA-Z]+\b', content)
#
#     # Фильтруем слова длиной 7 и более символов
#     long_words = [word for word in words if len(word) >= 7]
#
#     # Записываем результат
#     with open(output_filename, 'w', encoding = 'utf-8') as outfile:
#         for word in long_words:
#             outfile.write(word + '\n')
#
#     print(f"Обработано слов всего: {len(words)}")
#     print(f"Слов из 7+ букв: {len(long_words)}")
#     print(f"Результат сохранён в '{output_filename}'")
#
#     # Показываем первые 10 найденных слов (если есть)
#     if long_words:
#         print("\nПримеры найденных слов:")
#         for word in long_words[:10]:
#             print(f"  • {word}")
#         if len(long_words) > 10:
#             print(f"  ... и ещё {len(long_words) - 10} слов")
#
# except FileNotFoundError:
#     print(f"Ошибка: Файл '{input_filename}' не найден!")

# =============================================================================

# import re
#
# input_filename = "file.txt"
# output_filename = "long_words.txt"
#
# try:
#     long_words = []
#     total_words = 0
#
#     with open(input_filename, 'r', encoding = 'utf-8') as infile:
#         for line_num, line in enumerate(infile, 1):
#             # Находим слова в строке
#             words_in_line = re.findall(r'\b[а-яА-Яa-zA-Z]+\b', line)
#             total_words += len(words_in_line)
#
#             # Добавляем длинные слова
#             for word in words_in_line:
#                 if len(word) >= 7:
#                     long_words.append(word)
#
#     # Записываем результат
#     with open(output_filename, 'w', encoding = 'utf-8') as outfile:
#         outfile.write('\n'.join(long_words))
#
#     print(f"Всего слов в файле: {total_words}")
#     print(f"Слов из 7+ букв: {len(long_words)}")
#     print(f"Результат сохранён в '{output_filename}'")
#
# except FileNotFoundError:
#     print(f"Ошибка: Файл '{input_filename}' не найден!")

# =============================================================================

# import re
# from collections import Counter
#
#
# def process_words_by_length(input_file, output_file, min_length= 7):
#     """Обрабатывает файл и сохраняет слова указанной длины"""
#
#     try:
#         with open(input_file, 'r', encoding = 'utf-8') as f:
#             content = f.read()
#
#         # Находим все слова
#         words = re.findall(r'\b[а-яА-Яa-zA-Z]+\b', content)
#
#         # Группируем слова по длине
#         words_by_length = {}
#         for word in words:
#             length = len(word)
#             if length not in words_by_length:
#                 words_by_length[length] = []
#             words_by_length[length].append(word)
#
#         # Выбираем слова нужной длины
#         long_words = []
#         for length in range(min_length, max(words_by_length.keys()) + 1):
#             if length in words_by_length:
#                 long_words.extend(words_by_length[length])
#
#         # Сохраняем результат
#         with open(output_file, 'w', encoding = 'utf-8') as f:
#             f.write('\n'.join(long_words))
#
#         # Выводим статистику
#         print(f"Файл обработан: {input_file}")
#         print(f"Всего слов: {len(words)}")
#         print(f"Уникальных слов: {len(set(words))}")
#         print(f"\nРаспределение по длине слов:")
#         for length in sorted(words_by_length.keys()):
#             count = len(words_by_length[length])
#             if length >= min_length:
#                 print(f"  {length} букв: {count} слов ✨")
#             else:
#                 print(f"  {length} букв: {count} слов")
#
#         print(f"\nСлов из {min_length}+ букв: {len(long_words)}")
#         print(f"Результат сохранён в '{output_file}'")
#
#         return long_words
#
#     except FileNotFoundError:
#         print(f"Ошибка: Файл '{input_file}' не найден!")
#         return []
#     except Exception as e:
#         print(f"Ошибка: {e}")
#         return []
#
#
# # Использование функции
# input_filename = "file.txt"
# output_filename = "long_words.txt"
#
# long_words = process_words_by_length(input_filename, output_filename, min_length = 7)
#
# if long_words:
#     print(f"\nПервые 5 найденных слов:")
#     for word in long_words[:5]:
#         print(f"  • {word}")

# =============================================================================

# import re
# # Создаём тестовый файл для проверки
# test_content = """Программирование это увлекательный процесс создания компьютерных программ.
# Python является мощным языком программирования с простым синтаксисом.
# Длинные слова: компьютеризация, искусственный интеллект, разработка.
# Короткие слова: кот, дом, лес, мир."""
#
# input_filename = "test_file.txt"
# output_filename = "result.txt"
#
# # Записываем тестовые данные
# with open(input_filename, 'w', encoding = 'utf-8') as f:
#     f.write(test_content)
#
# print(f"Создан тестовый файл '{input_filename}'")
# print("=" * 50)
#
# # Обрабатываем файл
# try:
#     with open(input_filename, 'r', encoding = 'utf-8') as infile:
#         content = infile.read()
#
#     # Находим все слова
#     words = re.findall(r'\b[а-яА-Яa-zA-Z]+\b', content)
#     long_words = [word for word in words if len(word) >= 7]
#
#     # Записываем результат
#     with open(output_filename, 'w', encoding = 'utf-8') as outfile:
#         outfile.write('\n'.join(long_words))
#
#     print(f"Исходный текст:")
#     print(content)
#     print(f"\nВсего слов: {len(words)}")
#     print(f"Слов из 7+ букв: {len(long_words)}")
#     print(f"\nСлова из 7+ букв:")
#     for i, word in enumerate(long_words, 1):
#         print(f"  {i}. {word} (длина: {len(word)})")
#     print(f"\nРезультат сохранён в '{output_filename}'")
#
# except Exception as e:
#     print(f"Ошибка: {e}")

# =============================================================================

# Способ 1: Базовая замена (с сохранением в новый файл)
# def replace_in_file():
#     """Замена слова в файле"""
#
#     # Запрашиваем данные у пользователя
#     filename = input("Введите имя файла: ").strip()
#
#     try:
#         # Проверяем существование файла
#         with open(filename, 'r', encoding = 'utf-8') as file:
#             content = file.read()
#
#         print(f"\nСодержимое файла '{filename}':")
#         print("-" * 50)
#         print(content)
#         print("-" * 50)
#
#         # Запрашиваем слово для поиска и замены
#         search_word = input("\nКакое слово найти? ").strip()
#         replace_word = input("На что заменить? ").strip()
#
#         # Подсчитываем количество замен
#         count = content.count(search_word)
#
#         # Выполняем замену
#         new_content = content.replace(search_word, replace_word)
#
#         # Запрашиваем имя выходного файла
#         output_filename = input("Введите имя файла для сохранения результата: ").strip()
#
#         # Сохраняем результат
#         with open(output_filename, 'w', encoding = 'utf-8') as file:
#             file.write(new_content)
#
#         print(f"\n✅ Замена выполнена успешно!")
#         print(f"   Найдено вхождений: {count}")
#         print(f"   Заменено: {count}")
#         print(f"   Результат сохранён в '{output_filename}'")
#
#         # Показываем изменённый текст
#         if count > 0:
#             print("\nИзменённый текст:")
#             print("-" * 50)
#             print(new_content)
#             print("-" * 50)
#         else:
#             print(f"\n⚠️ Слово '{search_word}' не найдено в файле!")
#
#     except FileNotFoundError:
#         print(f"❌ Ошибка: Файл '{filename}' не найден!")
#     except Exception as e:
#         print(f"❌ Ошибка: {e}")
#
#
# # Запуск программы
# replace_in_file()

# =============================================================================

# Способ 2: Замена с учётом регистра и целых слов
# import re
#
# def replace_word_with_options():
#     """Замена слова с дополнительными опциями"""
#
#     filename = input("Введите имя файла: ").strip()
#
#     try:
#         # Читаем файл
#         with open(filename, 'r', encoding = 'utf-8') as file:
#             content = file.read()
#
#         print(f"\nТекущее содержимое файла:")
#         print("=" * 50)
#         print(content)
#         print("=" * 50)
#
#         # Запрашиваем параметры замены
#         search_word = input("\n🔍 Какое слово найти? ").strip()
#         replace_word = input("✏️ На что заменить? ").strip()
#
#         # Дополнительные опции
#         print("\nОпции замены:")
#         print("1. Учитывать регистр (Word ≠ word)")
#         print("2. Игнорировать регистр (Word = word)")
#         case_choice = input("Выберите (1/2): ").strip()
#
#         print("1. Только целые слова")
#         print("2. Любое вхождение (включая части слов)")
#         whole_choice = input("Выберите (1/2): ").strip()
#
#         # Выполняем замену с учётом опций
#         if case_choice == '1':  # Учитываем регистр
#             flags = 0
#         else:  # Игнорируем регистр
#             flags = re.IGNORECASE
#
#         if whole_choice == '1':  # Только целые слова
#             pattern = r'\b' + re.escape(search_word) + r'\b'
#             new_content = re.sub(pattern, replace_word, content, flags = flags)
#             # Подсчитываем количество замен
#             matches = re.findall(pattern, content, flags = flags)
#             count = len(matches)
#         else:  # Любое вхождение
#             if case_choice == '1':
#                 count = content.count(search_word)
#                 new_content = content.replace(search_word, replace_word)
#             else:
#                 # Для регистронезависимой замены используем re.sub с флагом IGNORECASE
#                 pattern = re.escape(search_word)
#                 new_content = re.sub(pattern, replace_word, content, flags = re.IGNORECASE)
#                 matches = re.findall(pattern, content, flags = re.IGNORECASE)
#                 count = len(matches)
#
#         # Сохраняем результат (в тот же файл или в новый)
#         save_choice = input("\nСохранить в тот же файл? (да/нет): ").strip().lower()
#
#         if save_choice == 'да':
#             output_filename = filename
#         else:
#             output_filename = input("Введите имя файла для сохранения: ").strip()
#
#         with open(output_filename, 'w', encoding = 'utf-8') as file:
#             file.write(new_content)
#
#         print(f"\n✅ Готово!")
#         print(f"   Найдено и заменено: {count} раз(а)")
#         print(f"   Результат сохранён в '{output_filename}'")
#
#         if count > 0:
#             print("\nОбновлённый текст:")
#             print("=" * 50)
#             print(new_content)
#             print("=" * 50)
#
#     except FileNotFoundError:
#         print(f"❌ Файл '{filename}' не найден!")
#     except Exception as e:
#         print(f"❌ Ошибка: {e}")
#
#
# # Запуск
# replace_word_with_options()

# =============================================================================

# Способ 3: Замена с предварительным просмотром и подтверждением
# import re
#
# def preview_and_replace():
#     """Поиск и замена с предварительным просмотром каждого вхождения"""
#
#     filename = input("Введите имя файла: ").strip()
#
#     try:
#         # Читаем файл
#         with open(filename, 'r', encoding = 'utf-8') as file:
#             lines = file.readlines()
#
#         search_word = input("🔍 Какое слово найти? ").strip()
#         replace_word = input("✏️ На что заменить? ").strip()
#
#         # Опция учёта регистра
#         case_sensitive = input("Учитывать регистр? (да/нет): ").strip().lower() == 'да'
#
#         # Находим все вхождения
#         occurrences = []
#         for line_num, line in enumerate(lines, 1):
#             if case_sensitive:
#                 if search_word in line:
#                     occurrences.append((line_num, line))
#             else:
#                 if search_word.lower() in line.lower():
#                     occurrences.append((line_num, line))
#
#         if not occurrences:
#             print(f"\n⚠️ Слово '{search_word}' не найдено в файле!")
#             return
#
#         print(f"\n📊 Найдено {len(occurrences)} строк(и) с искомым словом:")
#         for line_num, line in occurrences[:5]:  # Показываем первые 5
#             print(f"   Строка {line_num}: {line.strip()}")
#         if len(occurrences) > 5:
#             print(f"   ... и ещё {len(occurrences) - 5} строк")
#
#         # Спрашиваем подтверждение
#         confirm = input(f"\n✏️ Заменить все вхождения '{search_word}' на '{replace_word}'? (да/нет): ").strip().lower()
#
#         if confirm != 'да':
#             print("Замена отменена.")
#             return
#
#         # Выполняем замену
#         new_lines = []
#         total_replacements = 0
#
#         for line in lines:
#             if case_sensitive:
#                 new_line = line.replace(search_word, replace_word)
#                 replacements = line.count(search_word)
#             else:
#                 # Регистронезависимая замена
#                 pattern = re.compile(re.escape(search_word), re.IGNORECASE)
#                 new_line, count = pattern.subn(replace_word, line)
#                 replacements = count
#
#             new_lines.append(new_line)
#             total_replacements += replacements
#
#         # Сохраняем результат
#         output_filename = filename + ".new" if filename.endswith('.txt') else filename + "_new.txt"
#         with open(output_filename, 'w', encoding = 'utf-8') as file:
#             file.writelines(new_lines)
#
#         print(f"\n✅ Замена выполнена!")
#         print(f"   Всего замен: {total_replacements}")
#         print(f"   Результат сохранён в '{output_filename}'")
#
#         # Показываем изменения
#         print("\nПример изменений (первые 3 строки):")
#         for i in range(min(3, len(occurrences))):
#             line_num = occurrences[i][0]
#             print(f"Было: {lines[line_num - 1].strip()}")
#             print(f"Стало: {new_lines[line_num - 1].strip()}")
#             print("-" * 40)
#
#     except FileNotFoundError:
#         print(f"❌ Файл '{filename}' не найден!")
#     except Exception as e:
#         print(f"❌ Ошибка: {e}")
#
#
# # Запуск
# preview_and_replace()

# =============================================================================

# Способ 4: Интерактивная замена (построчно с подтверждением)
# def interactive_replace():
#     """Интерактивная замена - пользователь подтверждает каждую замену"""
#
#     filename = input("Введите имя файла: ").strip()
#
#     try:
#         # Читаем файл
#         with open(filename, 'r', encoding = 'utf-8') as file:
#             lines = file.readlines()
#
#         search_word = input("🔍 Какое слово найти? ").strip()
#         replace_word = input("✏️ На что заменить? ").strip()
#
#         case_sensitive = input("Учитывать регистр? (да/нет): ").strip().lower() == 'да'
#
#         new_lines = []
#         total_replacements = 0
#
#         for line_num, line in enumerate(lines, 1):
#             # Проверяем, есть ли слово в строке
#             line_lower = line if case_sensitive else line.lower()
#             search_lower = search_word if case_sensitive else search_word.lower()
#
#             if search_lower in line_lower:
#                 print(f"\n--- Строка {line_num} ---")
#                 print(f"Было: {line.strip()}")
#
#                 # Показываем предполагаемые изменения
#                 if case_sensitive:
#                     preview = line.replace(search_word, f"[{replace_word}]")
#                 else:
#                     pattern = re.compile(re.escape(search_word), re.IGNORECASE)
#                     preview = pattern.sub(f"[{replace_word}]", line)
#
#                 print(f"Будет: {preview}")
#
#                 # Спрашиваем у пользователя
#                 choice = input("Заменить в этой строке? (да/нет/все): ").strip().lower()
#
#                 if choice == 'все':
#                     # Заменяем все оставшиеся вхождения
#                     for remaining_line in lines[line_num - 1:]:
#                         if case_sensitive:
#                             new_remaining = remaining_line.replace(search_word, replace_word)
#                             replacements = remaining_line.count(search_word)
#                         else:
#                             pattern = re.compile(re.escape(search_word), re.IGNORECASE)
#                             new_remaining, count = pattern.subn(replace_word, remaining_line)
#                             replacements = count
#                         new_lines.append(new_remaining)
#                         total_replacements += replacements
#
#                     print(f"\n✅ Заменено {total_replacements} вхождений во всех оставшихся строках")
#                     break
#
#                 elif choice == 'да':
#                     # Заменяем в текущей строке
#                     if case_sensitive:
#                         new_line = line.replace(search_word, replace_word)
#                         replacements = line.count(search_word)
#                     else:
#                         pattern = re.compile(re.escape(search_word), re.IGNORECASE)
#                         new_line, count = pattern.subn(replace_word, line)
#                         replacements = count
#                     new_lines.append(new_line)
#                     total_replacements += replacements
#                     print(f"   ✓ Заменено {replacements} раз(а)")
#
#                 else:  # нет
#                     new_lines.append(line)
#                     print("   ✗ Пропущено")
#             else:
#                 new_lines.append(line)
#
#         # Если не было прерывания через "все", обрабатываем оставшиеся строки
#         if len(new_lines) < len(lines):
#             # Уже обработали все строки в цикле с break
#             pass
#         elif len(new_lines) == 0:
#             new_lines = lines
#
#         # Сохраняем результат
#         if total_replacements > 0:
#             output_filename = input("\nВведите имя файла для сохранения: ").strip()
#             with open(output_filename, 'w', encoding = 'utf-8') as file:
#                 file.writelines(new_lines)
#             print(f"\n✅ Замена выполнена! Сохранено в '{output_filename}'")
#         else:
#             print("\n⚠️ Замен не было выполнено")
#
#     except FileNotFoundError:
#         print(f"❌ Файл '{filename}' не найден!")
#     except Exception as e:
#         print(f"❌ Ошибка: {e}")
#
#
# # Запуск
# interactive_replace()

# =============================================================================

import re
import os

def show_menu():
    print("\n" + "=" * 50)
    print("ПОИСК И ЗАМЕНА В ФАЙЛЕ")
    print("=" * 50)
    print("1. Простая замена (весь файл)")
    print("2. Замена с опциями (регистр/целые слова)")
    print("3. Замена с предпросмотром")
    print("4. Интерактивная замена (построчно)")
    print("5. Выход")
    print("-" * 50)

def simple_replace():
    """Простая замена"""
    filename = input("Имя файла: ").strip()
    try:
        with open(filename, 'r', encoding = 'utf-8') as f:
            content = f.read()

        search = input("Что искать? ").strip()
        replace = input("На что заменить? ").strip()

        count = content.count(search)
        new_content = content.replace(search, replace)

        output = input("Имя файла для сохранения: ").strip()
        with open(output, 'w', encoding = 'utf-8') as f:
            f.write(new_content)

        print(f"✅ Заменено {count} раз(а). Сохранено в '{output}'")
    except FileNotFoundError:
        print("❌ Файл не найден!")

def advanced_replace():
    """Замена с опциями"""
    filename = input("Имя файла: ").strip()
    try:
        with open(filename, 'r', encoding = 'utf-8') as f:
            content = f.read()

        search = input("Что искать? ").strip()
        replace = input("На что заменить? ").strip()

        case = input("Учитывать регистр? (да/нет): ").strip().lower() == 'да'
        whole = input("Только целые слова? (да/нет): ").strip().lower() == 'да'

        if whole:
            pattern = r'\b' + re.escape(search) + r'\b'
            flags = 0 if case else re.IGNORECASE
            new_content = re.sub(pattern, replace, content, flags = flags)
            count = len(re.findall(pattern, content, flags = flags))
        else:
            if case:
                count = content.count(search)
                new_content = content.replace(search, replace)
            else:
                pattern = re.escape(search)
                new_content = re.sub(pattern, replace, content, flags = re.IGNORECASE)
                count = len(re.findall(pattern, content, flags = re.IGNORECASE))

        output = input("Имя файла для сохранения: ").strip()
        with open(output, 'w', encoding = 'utf-8') as f:
            f.write(new_content)

        print(f"✅ Заменено {count} раз(а)")
    except FileNotFoundError:
        print("❌ Файл не найден!")

def main():
    while True:
        show_menu()
        choice = input("Выберите действие (1-5): ").strip()

        if choice == '1':
            simple_replace()
        elif choice == '2':
            advanced_replace()
        elif choice == '3':
            preview_and_replace()
        elif choice == '4':
            interactive_replace()
        elif choice == '5':
            print("До свидания!")
            break
        else:
            print("Неверный выбор!")

# Запуск основной программы
if __name__ == "__main__":
    main()