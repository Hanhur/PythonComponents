# 1. Найдите у себя на компьютере файл и выведите его содержимое с помощью Python.
import os
from pathlib import Path

# Популярные места для поиска текстовых файлов
if os.name == 'nt':  # Windows
    possible_paths = [
        os.path.expanduser("~/Desktop/example.txt"),
        os.path.expanduser("~/Documents/example.txt"),
        "C:/example.txt"
    ]
else:  # Linux/Mac
    possible_paths = [
        os.path.expanduser("~/Desktop/example.txt"),
        os.path.expanduser("~/Documents/example.txt"),
        "/tmp/example.txt"
    ]

for path in possible_paths:
    if os.path.exists(path):
        print(f"Найден файл: {path}")
        with open(path, 'r', encoding = 'utf-8') as f:
            print(f.read())
        break
else:
    print("Не удалось найти файл example.txt в стандартных местах")

# 2. Напишите программу, которая задает пользователю вопрос и сохраняет ответ в файл.
import json
import csv
from datetime import datetime


def save_to_txt(question, answer, filename):
    """Сохранение в текстовый файл"""
    with open(filename, 'a', encoding = 'utf-8') as file:
        file.write(f"Вопрос: {question}\n")
        file.write(f"Ответ: {answer}\n")
        file.write(f"Время: {datetime.now().strftime('%H:%M:%S')}\n")
        file.write("-" * 40 + "\n")


def save_to_json(question, answer, filename):
    """Сохранение в JSON файл"""
    try:
        with open(filename, 'r', encoding = 'utf-8') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    data.append({
        "вопрос": question,
        "ответ": answer,
        "время": datetime.now().isoformat()
    })

    with open(filename, 'w', encoding = 'utf-8') as file:
        json.dump(data, file, ensure_ascii = False, indent = 2)


def save_to_csv(question, answer, filename):
    """Сохранение в CSV файл"""
    import os
    file_exists = os.path.exists(filename)

    with open(filename, 'a', newline = '', encoding = 'utf-8') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Вопрос", "Ответ", "Время"])
        writer.writerow([question, answer, datetime.now().strftime('%Y-%m-%d %H:%M:%S')])


# Основная программа
print("=== Сохранение ответов в файл ===\n")
print("Выберите формат сохранения:")
print("1. TXT (обычный текст)")
print("2. JSON")
print("3. CSV")

choice = input("Ваш выбор (1/2/3): ")

# Задаём вопрос
question = input("\nВаш вопрос: ")
answer = input("Ответ пользователя: ")

# Сохраняем в выбранном формате
if choice == '1':
    filename = 'ответы.txt'
    save_to_txt(question, answer, filename)
elif choice == '2':
    filename = 'ответы.json'
    save_to_json(question, answer, filename)
elif choice == '3':
    filename = 'ответы.csv'
    save_to_csv(question, answer, filename)
else:
    print("Неверный выбор. Сохраняю в TXT формате.")
    filename = 'ответы.txt'
    save_to_txt(question, answer, filename)

print(f"\nОтвет сохранён в файл: {filename}")

# 3. Примите элементы в списке списков [["Звездные войны", "Терминатор", "Искусственный интеллект"],
# ["Дурак", "Матильда", "Левиафан"], ["Люди в черном", "Я - робот", "Эволюция"]] и запишите их в CSV-файл.
# Да нные каждого списка должны быть строкой в файле, при этом каждый элемент списка должен быть отделен запятой.
# Исходный список списков
movies = [
    ["Звездные войны", "Терминатор", "Искусственный интеллект"],
    ["Дурак", "Матильда", "Левиафан"],
    ["Люди в черном", "Я - робот", "Эволюция"]
]

# Запись в CSV файл
filename = "фильмы.csv"

with open(filename, 'w', encoding = 'utf-8') as file:
    for row in movies:
        # Объединяем элементы списка через запятую и записываем в файл
        line = ",".join(row)
        file.write(line + "\n")

print(f"Данные успешно записаны в файл '{filename}'")