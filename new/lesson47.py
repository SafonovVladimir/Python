import sqlite3


def dict_factory(cur, row):
    d = {}
    for idx, col in enumerate(cur.description):
        d[col[0]] = row[idx]
    return d


db = sqlite3.connect('test_db.db')
db.row_factory = dict_factory
cursor = db.cursor()

email = 'petroff@gmail.com'
name = 'Pushin Vasa'

# cursor.execute(f"SELECT name FROM users WHERE email = '{email}'")
# db.commit()
# cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
# cursor.execute("SELECT * FROM users WHERE email = ? OR name = ?", (email, name))
# cursor.execute("SELECT * FROM users")
# res = cursor.fetchall()
# for user in res:
#     print(user['name'], user['email'])
#
# print('********************')

cursor.execute("DELETE FROM users WHERE email = ?", ('petroff@gmail.com',))
db.commit()

cursor.execute("SELECT * FROM users")
res = cursor.fetchall()
for user in res:
    print(user['name'], user['email'])

db.close()
