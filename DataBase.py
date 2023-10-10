import sqlite3

conn = sqlite3.connect('db.db')

cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS userInfo (id int primary key, roles varchar(7), coins int)''')

conn.commit()
conn.close()

