# Базы данных в Python. Работа в SQLiteStudio. Создание БД. Запросы SQL
import sqlite3 as sq

with sq.connect("test.db") as conn:
    cur = conn.cursor()
    cur.execute(''' CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        address TEXT
    ) ''')