# lib/helpers.py
import sqlite3 
DATABASE_NAME = "game.db"

def create_database():
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        
def start_new_game(player_name):
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM scenes WHERE scene_id = 0")
        introduction = cursor.fetchone() 
        
        cursor.execute("UPDATE players SET scene_id = ? WHERE player_name = ?",(introduction[0], player_name))
        
        conn.commit()
        conn.close()
        print(f"New game started for {player_name}.")
    except sqlite3.Error as e: 
        print(f"Database error: {e}")
        
def continue_game(player_name):
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        
        conn.commit()
        conn.close()
        print(f"Continuing game for {player_name}.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
 
def delete_game_data(player_name):
    try: 
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        
        cursor.execute("DELETE FROM player_profiles WHERE playername= ?", (player_name))
        
        conn.commit()
        conn.close()
        
        print(f"Game data for {player_name} deleted.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        
def exit_game():
    print("Exiting the game")
    
def exit_program():
    print("Goodbye!")
    exit()




