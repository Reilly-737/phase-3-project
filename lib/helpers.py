# lib/helpers.py
from models.__init__ import CURSOR, CONN
from models.model_1 import Player
import time
import ipdb
import sqlite3

DATABASE_NAME = "lib/game.db"


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
