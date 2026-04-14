import sqlite3
import datetime

def save_chat(user, bot):
    conn = sqlite3.connect("chat.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS chats(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user TEXT,
        bot TEXT,
        time TEXT
    )
    """)

    cursor.execute("INSERT INTO chats (user, bot, time) VALUES (?, ?, ?)",
                   (user, bot, str(datetime.datetime.now())))

    conn.commit()
    conn.close()