# SQL запросы в базе данных. Практика. Перенос данных
import sqlite3 as sq

with sq.connect("example.db") as conn:
    cur = conn.cursor()
    # cur.execute('''
    #     CREATE TABLE IF NOT EXISTS users(
    #         id INTEGER PRIMARY KEY AUTOINCREMENT,
    #         name TEXT NOT NULL,
    #         age INTEGER,
    #         phone BLOB
    #     )
    # ''')

    # cur.execute(''' ALTER TABLE users RENAME TO old_users ''')

    # cur.execute(''' ALTER TABLE old_users ADD COLUMN type TEXT NOT NULL DEFAULT 0 ''')

    cur.execute(''' INSERT INTO old_users(name) VALUES ('NEW') ''')