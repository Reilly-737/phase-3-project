 #lib/models/__init__.py
import sqlite3

def initialize_database():
    try:
        conn = sqlite3.connect('game_database.db')
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_profiles (
                id INTEGER PRIMARY KEY,
                username TEXT UNIQUE,
                progress TEXT
            )
        ''')

        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"Database error: {e}")