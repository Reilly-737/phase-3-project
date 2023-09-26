# lib/helpers.py
import sqlite3 
#create function to create users login users and delete users
def create_user(username):
    try: 
        conn = sqlite3.connect('game_database.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO user_profiles (username, progress) VALUES (?,?) ', (username, ''))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        print("Username already exists")
        return False 
    
def login_user(username):
    try:
        conn = sqlite3.connect('game_database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM user_profiles WHERE username = ?', (username,))
        user = cursor.fetchone()
        conn.close()
        return user 
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        

def delete_user_progress(username):
    try:
        conn = sqlite3.connect('game_database.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE user_profiles SET progress = "" WHERE username = ?', (username))
        conn.commit()
        conn.close()
    except sqlite3.Error as e: 
        print(f"Database error: {e}")
        
def exit_program():
    print("Goodbye!")
    exit()




