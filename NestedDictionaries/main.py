# # Работа с файлами в Python - практика. Вложенные словари. Добавление ключа в словарь
# firma = {"разработка" :
#              {"программисты" :
#                   {"Иванов А.А." :
#                        {"телефон" : "+7922142155", "адрес почты" : "ivanovaa@gmail.com"},
#                    "Александров В.А." :
#                        {"телефон" : "+7922142155", "адрес почты" : "aleksander@gmail.com"}
#                    }
#               },
#          "маркетинг" : {}
#          }
# print(firma["разработка"]["программисты"])

# =====================================================================================================================

# Возможности программы:
# 1. Ввод данных — добавление нового сотрудника с проверкой ввода
#
# 2. Редактирование — изменение любых полей сотрудника
#
# 3. Удаление — удаление сотрудника с подтверждением
#
# 4. Поиск по фамилии — точное совпадение фамилии
#
# 5. Поиск по возрасту — определение возраста по году рождения
#
# 6. Поиск по первой букве фамилии — все сотрудники, чья фамилия начинается на указанную букву
#
# 7. Вывод всех сотрудников — таблица с нумерацией
#
# 8. Сохранение результатов поиска — в отдельный JSON-файл
#
# 9. Автосохранение — при выходе из программы
#
# 10. Ручное сохранение — по команде пользователя
#
# 11. Загрузка при старте — из указанного пользователем файла

import json
import os
from datetime import datetime


class Employee:
    """Класс, представляющий сотрудника"""

    def __init__(self, last_name, first_name, patronymic, birth_year, position, salary):
        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic
        self.birth_year = birth_year
        self.position = position
        self.salary = salary

    def get_full_name(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"

    def get_age(self, current_year = None):
        if current_year is None:
            current_year = datetime.now().year
        return current_year - self.birth_year

    def to_dict(self):
        """Преобразование в словарь для JSON"""
        return {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "patronymic": self.patronymic,
            "birth_year": self.birth_year,
            "position": self.position,
            "salary": self.salary
        }

    @staticmethod
    def from_dict(data):
        """Создание сотрудника из словаря"""
        return Employee(
            data["last_name"],
            data["first_name"],
            data["patronymic"],
            data["birth_year"],
            data["position"],
            data["salary"]
        )

    def __str__(self):
        return f"{self.get_full_name():<25} | {self.birth_year:>4} | {self.position:<20} | {self.salary:>8} руб."


class EmployeeDatabase:
    """Класс для управления базой данных сотрудников"""

    def __init__(self):
        self.employees = []
        self.current_file = None

    def load_from_file(self, filename):
        """Загрузка списка сотрудников из файла"""
        try:
            if not os.path.exists(filename):
                print(f"Файл {filename} не найден. Будет создан новый файл при сохранении.")
                self.employees = []
                self.current_file = filename
                return True

            with open(filename, 'r', encoding = 'utf-8') as f:
                data = json.load(f)
                self.employees = [Employee.from_dict(emp) for emp in data]

            self.current_file = filename
            print(f"Загружено {len(self.employees)} сотрудников из файла {filename}")
            return True
        except Exception as e:
            print(f"Ошибка при загрузке файла: {e}")
            return False

    def save_to_file(self, filename = None):
        """Сохранение списка сотрудников в файл"""
        if filename is None:
            filename = self.current_file

        if filename is None:
            filename = input("Укажите имя файла для сохранения: ")

        try:
            data = [emp.to_dict() for emp in self.employees]
            with open(filename, 'w', encoding = 'utf-8') as f:
                json.dump(data, f, ensure_ascii = False, indent = 2)

            self.current_file = filename
            print(f"Сохранено {len(self.employees)} сотрудников в файл {filename}")
            return True
        except Exception as e:
            print(f"Ошибка при сохранении файла: {e}")
            return False

    def add_employee(self):
        """Добавление нового сотрудника"""
        print("\n--- Добавление нового сотрудника ---")
        last_name = input("Фамилия: ").strip()
        first_name = input("Имя: ").strip()
        patronymic = input("Отчество: ").strip()

        while True:
            try:
                birth_year = int(input("Год рождения: "))
                if 1900 <= birth_year <= datetime.now().year:
                    break
                else:
                    print(f"Год должен быть между 1900 и {datetime.now().year}")
            except ValueError:
                print("Введите корректный год")

        position = input("Должность: ").strip()

        while True:
            try:
                salary = float(input("Зарплата: "))
                if salary >= 0:
                    break
                else:
                    print("Зарплата не может быть отрицательной")
            except ValueError:
                print("Введите корректную зарплату")

        employee = Employee(last_name, first_name, patronymic, birth_year, position, salary)
        self.employees.append(employee)
        print(f"Сотрудник {employee.get_full_name()} успешно добавлен!")

    def edit_employee(self):
        """Редактирование данных сотрудника"""
        if not self.employees:
            print("Список сотрудников пуст")
            return

        self.list_all_employees()

        try:
            index = int(input("\nВведите номер сотрудника для редактирования: ")) - 1
            if 0 <= index < len(self.employees):
                emp = self.employees[index]
                print(f"\nРедактирование сотрудника: {emp.get_full_name()}")
                print("(оставьте поле пустым, чтобы не менять)")

                last_name = input(f"Фамилия ({emp.last_name}): ").strip()
                if last_name:
                    emp.last_name = last_name

                first_name = input(f"Имя ({emp.first_name}): ").strip()
                if first_name:
                    emp.first_name = first_name

                patronymic = input(f"Отчество ({emp.patronymic}): ").strip()
                if patronymic:
                    emp.patronymic = patronymic

                birth_year_str = input(f"Год рождения ({emp.birth_year}): ").strip()
                if birth_year_str:
                    try:
                        birth_year = int(birth_year_str)
                        if 1900 <= birth_year <= datetime.now().year:
                            emp.birth_year = birth_year
                        else:
                            print("Некорректный год, оставлено прежнее значение")
                    except ValueError:
                        print("Некорректный ввод, оставлено прежнее значение")

                position = input(f"Должность ({emp.position}): ").strip()
                if position:
                    emp.position = position

                salary_str = input(f"Зарплата ({emp.salary}): ").strip()
                if salary_str:
                    try:
                        salary = float(salary_str)
                        if salary >= 0:
                            emp.salary = salary
                        else:
                            print("Некорректная зарплата, оставлено прежнее значение")
                    except ValueError:
                        print("Некорректный ввод, оставлено прежнее значение")

                print("Данные сотрудника обновлены!")
            else:
                print("Неверный номер")
        except ValueError:
            print("Неверный ввод")

    def delete_employee(self):
        """Удаление сотрудника"""
        if not self.employees:
            print("Список сотрудников пуст")
            return

        self.list_all_employees()

        try:
            index = int(input("\nВведите номер сотрудника для удаления: ")) - 1
            if 0 <= index < len(self.employees):
                emp = self.employees[index]
                confirm = input(f"Удалить сотрудника {emp.get_full_name()}? (да/нет): ").lower()
                if confirm == 'да':
                    del self.employees[index]
                    print("Сотрудник удалён!")
                else:
                    print("Удаление отменено")
            else:
                print("Неверный номер")
        except ValueError:
            print("Неверный ввод")

    def search_by_last_name(self):
        """Поиск сотрудника по фамилии"""
        if not self.employees:
            print("Список сотрудников пуст")
            return

        last_name = input("Введите фамилию для поиска: ").strip().lower()
        results = [emp for emp in self.employees if emp.last_name.lower() == last_name]

        if results:
            print(f"\nНайдено {len(results)} сотрудников:")
            self.print_employee_table(results)
            self.save_results_to_file(results)
        else:
            print(f"Сотрудники с фамилией '{last_name}' не найдены")

    def search_by_age(self):
        """Поиск сотрудников указанного возраста"""
        if not self.employees:
            print("Список сотрудников пуст")
            return

        try:
            age = int(input("Введите возраст: "))
            current_year = datetime.now().year

            results = []
            for emp in self.employees:
                if emp.get_age(current_year) == age:
                    results.append(emp)

            if results:
                print(f"\nНайдено {len(results)} сотрудников возраста {age} лет:")
                self.print_employee_table(results)
                self.save_results_to_file(results)
            else:
                print(f"Сотрудники возраста {age} лет не найдены")
        except ValueError:
            print("Введите корректный возраст")

    def search_by_last_name_start(self):
        """Поиск сотрудников, фамилия которых начинается на указанную букву"""
        if not self.employees:
            print("Список сотрудников пуст")
            return

        letter = input("Введите букву: ").strip().lower()
        if not letter:
            print("Буква не введена")
            return

        results = [emp for emp in self.employees if emp.last_name.lower().startswith(letter)]

        if results:
            print(f"\nНайдено {len(results)} сотрудников с фамилией на букву '{letter}':")
            self.print_employee_table(results)
            self.save_results_to_file(results)
        else:
            print(f"Сотрудники с фамилией на букву '{letter}' не найдены")

    def list_all_employees(self):
        """Вывод информации обо всех сотрудниках"""
        if not self.employees:
            print("Список сотрудников пуст")
            return

        self.print_employee_table(self.employees)

    def print_employee_table(self, employees):
        """Печать таблицы сотрудников"""
        print("\n" + "=" * 90)
        print(f"{'№':<3} | {'ФИО':<25} | {'Год':<4} | {'Должность':<20} | {'Зарплата':>8}")
        print("-" * 90)

        for i, emp in enumerate(employees, 1):
            print(f"{i:<3} | {emp.get_full_name():<25} | {emp.birth_year:>4} | {emp.position:<20} | {emp.salary:>8.2f}")

        print("=" * 90)
        print(f"Всего сотрудников: {len(employees)}")

    def save_results_to_file(self, employees):
        """Сохранение найденной информации в файл"""
        if not employees:
            return

        save = input("\nСохранить найденные данные в файл? (да/нет): ").lower()
        if save == 'да':
            filename = input("Имя файла для сохранения: ").strip()
            if not filename:
                filename = "search_results.json"

            try:
                data = [emp.to_dict() for emp in employees]
                with open(filename, 'w', encoding = 'utf-8') as f:
                    json.dump(data, f, ensure_ascii = False, indent = 2)
                print(f"Результаты сохранены в файл {filename}")
            except Exception as e:
                print(f"Ошибка при сохранении: {e}")

    def auto_save(self):
        """Автоматическое сохранение при выходе"""
        if self.employees and self.current_file:
            self.save_to_file()
        elif self.employees:
            save = input("Сохранить данные перед выходом? (да/нет): ").lower()
            if save == 'да':
                self.save_to_file()


def main():
    """Главная функция программы"""
    db = EmployeeDatabase()

    # Загрузка данных из файла
    print("Добро пожаловать в информационную систему 'Сотрудники'")
    filename = input("Укажите имя файла для загрузки (или нажмите Enter для нового файла): ").strip()

    if filename:
        db.load_from_file(filename)
    else:
        print("Будет создана новая база данных")

    # Главное меню
    while True:
        print("\n" + "=" * 50)
        print("ИНФОРМАЦИОННАЯ СИСТЕМА 'СОТРУДНИКИ'")
        print("=" * 50)
        print("1. Добавить сотрудника")
        print("2. Редактировать сотрудника")
        print("3. Удалить сотрудника")
        print("4. Поиск по фамилии")
        print("5. Поиск по возрасту")
        print("6. Поиск по первой букве фамилии")
        print("7. Вывести всех сотрудников")
        print("8. Сохранить в файл")
        print("9. Выйти")
        print("-" * 50)

        choice = input("Выберите действие (1-9): ").strip()

        if choice == '1':
            db.add_employee()
        elif choice == '2':
            db.edit_employee()
        elif choice == '3':
            db.delete_employee()
        elif choice == '4':
            db.search_by_last_name()
        elif choice == '5':
            db.search_by_age()
        elif choice == '6':
            db.search_by_last_name_start()
        elif choice == '7':
            db.list_all_employees()
        elif choice == '8':
            db.save_to_file()
        elif choice == '9':
            db.auto_save()
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()