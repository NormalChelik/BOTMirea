import sqlite3

connect = sqlite3.connect("users_db.db")
cursor = connect.cursor()
def create_db():
    cursor.execute("""CREATE TABLE IF NOT EXISTS users_delivery (
    id INT PRIMARY KEY NOT NULL,
    user_role VARCHAR(7) NOT NULL,
    user_order VARCHAR(1000) NOT NULL
    );""")

    connect.commit()


def check_order_client(message):
    print(cursor.execute("SELECT * FROM users_delivery WHERE 'id' = ?;", (message.from_user.id,)).fetchall())
    return cursor.execute("SELECT * FROM users_delivery WHERE 'id' = ?;", (message.from_user.id,)).fetchall()

def add_client_delivery(message):
    cursor.execute("INSERT INTO users_delivery VALUES(?,?,?)", (message.from_user.id, "client", message.text))
    connect.commit()

