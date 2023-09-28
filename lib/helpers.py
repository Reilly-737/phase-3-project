# lib/helpers.py
from models.__init__ import CURSOR, CONN
from models.model_1 import Player
import time
import ipdb
import sqlite3

DATABASE_NAME = "lib/game.db"

import sqlite3

DATABASE_NAME = "lib/game.db"


def start_new_game(player_name):
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM scenes WHERE scene_id = 0")
        introduction = cursor.fetchone()

        cursor.execute("UPDATE players SET scene_id = ? WHERE player_name = ?",
                       (introduction[0], player_name))

        conn.commit()
        conn.close()
        print(f"New game started for {player_name}.")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        
def continue_game(player_name):
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        
      
        cursor.execute("SELECT scene_id FROM players WHERE player_id = ?", (player_name,))
        current_scene_id = cursor.fetchone()
        
        if current_scene_id:
            current_scene_id = current_scene_id[0]
            
          
            cursor.execute("SELECT * FROM scenes WHERE scene_id = ?", (current_scene_id,))
            scene = cursor.fetchone()
            
            if scene:
                print(f"Continuing game for {player_name}.")
                print(scene[0])  
            else:
                print(f"Error: Scene data not found for scene_id {current_scene_id}. Starting a new game.")
                start_new_game(player_name)
        else:
            print(f"No saved game found for {player_name}. Starting a new game.")
            start_new_game(player_name)
        
        conn.close()
    except sqlite3.Error as e: 
        print(f"Oh no. Database error: {e}")
        
def delete_game_data(player_name):
    try: 
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        
        cursor.execute("DELETE FROM players WHERE player_id = ?", (player_name,))
        conn.commit()
        conn.close()
        
        print(f"Game data for {player_name} deleted.")
    except sqlite3.Error as e:
        print(f"oops! Database error: {e}")

def list_players():
    players = Player.get_all()
    for player in players:
        print(player.player_name)


def create_player():
    player_name = input("Enter your player_name: ")
    scene_id = input("Enter the current scene id: ")
    try:
        player = Player.create(player_name, scene_id)
        print(f"Success: {player.player_name}")
    except Exception as exc:
        print("Error creating player_name: ", exc)


def update_player():
    id_ = input("Enter the player's id: ")
    if player := Player.find_by_id(id_):
        try:
            name = input("Enter the players new name: ")
            player.player_name = name
            scene = input("Enter the player's current scene: ")
            player.scene_id = scene

            player.update()
            print(f'Success: {player}')
        except Exception as exc:
            print("Error updating player: ", exc)
    else:
        print(f'Player {id_} not found')


def delete_player():
    id_ = input("Enter the player's id: ")
    if player := Player.find_by_id(id_):
        player.delete()
        print(f'Player {id_} deleted')
    else:
        print(f'Player {id_} not found')


ipdb.set_trace()


def game_over():
    print("Game over. Goodbye!")
    exit()


def head_outside():
    print("You're outside!")


def exit_program():
    print("Goodbye!")
    exit()


def print_slowly(output):
    for char in output:
        print(char, end='', flush=True)
        time.sleep(0.008)
        # time.sleep(0)
    print()
ipdb.set_trace()
