import sqlite3

connect = sqlite3.connect("users_db.db")
cursor = connect.cursor()
def create_db():
    cursor.execute("""CREATE TABLE IF NOT EXISTS users_delivery (
    id INT PRIMARY KEY NOT NULL,
    user_role VARCHAR(7) NOT NULL,
    user_order VARCHAR(1000) NOT NULL
    );
    CREATE TABLE IF NOT EXISTS users_predloshka (
    id INT PRIMARY KEY NOT NULL,
    user_offer VARCHAR(10000)
    )
    """)

    connect.commit()

#Предложка
def add_offer(messageID, messageTEXT):
    cursor.execute("INSERT INTO users_predloshka VALUES(?,?)", (messageID, messageTEXT))
    connect.commit()

def check_order_client(messageID):
    return cursor.execute("SELECT * FROM users_predloshka WHERE id = ?;", (messageID,)).fetchall()




#Доставка
def check_order_client(messageID):
    return cursor.execute("SELECT * FROM users_delivery WHERE id = ?;", (messageID,)).fetchall()

def add_client_delivery(messageID, messageTEXT):
    cursor.execute("INSERT INTO users_delivery VALUES(?,?,?)", (messageID, "client", messageTEXT))
    connect.commit()

def update_client_delivery(messageID, messageTEXT):
    cursor.execute("UPDATE users_delivery SET user_order = ? WHERE id = ?;", (messageTEXT, messageID))
    connect.commit()

def delete_client_delivery(messageID):
    cursor.execute("DELETE FROM users_delivery WHERE id = ?;", (messageID,))
    connect.commit()
def all_order_courier():
    return cursor.execute("SELECT id, user_order FROM users_delivery;").fetchall()
