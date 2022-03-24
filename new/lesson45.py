import sqlite3

# import sys

db = sqlite3.connect('test_db.db')

cursor = db.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE)''')

# cursor.execute("INSERT INTO users (name, email) VALUES ('Ivanov Ivan', 'ivanov@gmail.com')")
# cursor.execute("INSERT INTO users (name, email) VALUES ('Petroff Petr', 'petroff@gmail.com')")
# cursor.execute("INSERT INTO users (name, email) VALUES ('Sidorov Sidr', 'sidorov@gmail.com')")
# cursor.execute("INSERT INTO users (name, email) VALUES ('Pushin Vasa', 'pusha@gmail.com')")

# cursor.executescript('''
#     INSERT INTO users (name, email) VALUES ('Resel Kurt', 'resel@gmail.com');
#     INSERT INTO users (name, email) VALUES ('Vilosin Firan', 'vilosin@gmail.com');
# ''')

# users = [
#     ('user1', 'user1@gmail.com'),
#     ('user2', 'user2@gmail.com'),
#     ('user3', 'user3@gmail.com')
# ]
#
# cursor.executemany("INSERT INTO users (name, email) VALUES (?, ?)", users)

# db.commit()

db.close()

# con = sqlite3.connect('new_db.db')
# cur = con.cursor()
# cur.execute("create table lang (name, first_appeared)")
#
# # This is the qmark style:
# cur.execute("insert into lang values (?, ?)", ("C", 1972))
#
# # The qmark style used with executemany():
# lang_list = [
#     ("Fortran", 1957),
#     ("Python", 1991),
#     ("Go", 2009),
# ]
# cur.executemany("insert into lang values (?, ?)", lang_list)
#
# # And this is the named style:
# cur.execute("select * from lang where first_appeared=:year", {"year": 1972})
# print(cur.fetchall())
#
# con.close()
