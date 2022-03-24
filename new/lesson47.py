import sqlite3


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


db = sqlite3.connect('test_db.db')
cursor = db.cursor()

email = 'petroff@gmail.com'
name = 'Pushin Vasa'

# cursor.execute(f"SELECT name FROM users WHERE email = '{email}'")
# db.commit()
# cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
# cursor.execute("SELECT * FROM users WHERE email = ? OR name = ?", (email, name))
cursor.execute("SELECT * FROM users")

res = cursor.fetchall()

print(res)

db.close()
