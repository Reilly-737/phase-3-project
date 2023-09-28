# lib/helpers.py
from models.model_1 import *
# import ipdb
import time
import random

DATABASE_NAME = "lib/game.db"


DATABASE_NAME = "lib/game.db"


def print_slowly(output):
    for char in output:
        print(char, end='', flush=True)
        time.sleep(0.008)
        # time.sleep(0)
    print()


def print_somewhat_fast(output):
    for char in output:
        print(char, end='', flush=True)
        time.sleep(0.002)
        # time.sleep(0)
    print()


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

        cursor.execute(
            "SELECT scene_id FROM players WHERE player_id = ?", (player_name,))
        current_scene_id = cursor.fetchone()

        if current_scene_id:
            current_scene_id = current_scene_id[0]

            cursor.execute(
                "SELECT * FROM scenes WHERE scene_id = ?", (current_scene_id,))
            scene = cursor.fetchone()

            if scene:
                print(f"Continuing game for {player_name}.")
                print(scene[0])
            else:
                print(
                    f"Error: Scene data not found for scene_id {current_scene_id}. Starting a new game.")
                start_new_game(player_name)
        else:
            print(
                f"No saved game found for {player_name}. Starting a new game.")
            start_new_game(player_name)

        conn.close()
    except sqlite3.Error as e:
        print(f"Oh no. Database error: {e}")


def delete_game_data(player_name):
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM players WHERE player_id = ?", (player_name,))
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
    name = input("Enter player name: ")
    try:
        player, created = Players.get_or_create(
            player_name=name, defaults={'scene_id': 0})
        if created:
            print(f"Success: {player.player_name} created successfully")
        else:
            print(f"Player {player.player_name} already exists.")
    except Exception as exc:
        print("Error creating player_name: ", exc)


def update_player():
    id_ = input("Enter the player's id: ")
    if player := Players.find_by_id(id_):
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
    if player := Players.find_by_id(id_):
        player.delete()
        print(f'Player {id_} deleted')
    else:
        print(f'Player {id_} not found')


def initialize_database():
    with database:
        database.create_tables([Players, Scenes, Options, Prophecy], safe=True)

        if Scenes.select().count() == 0:
            scenes_data = [
                {'scene_id': 0, 'scene_name': 'Introduction', 'scene_description':
                    'You find yourself amidst a vibrant party with your friends, the music pulsating through the air as laughter fills the room. You''re faced with a choice:'},
                {'scene_id': 1, 'scene_name': 'Outside the Party', 'scene_description':
                    'As you exhale a puff of vapor, you notice a black cat with striking green eyes in the yard, peacefully minding its own business. Your options beckon:'},
                {'scene_id': 2, 'scene_name': 'Following the Cat', 'scene_description': 'You stealthily follow the mysterious feline behind the shed, only to find that it has vanished without a trace. Instead, you encounter something utterly unexpected—a colossal pile of black ooze. It ripples and shifts, and from the center emerges a massive bright blue eye, akin to the evil eye shade of blue with a black center. The eye locks onto you; its presence unnerving.'},
                {'scene_id': 3, 'scene_name': 'The Encounter', 'scene_description':
                    'The tone shifts from the jovial party atmosphere to an eerie, all-knowing aura. It speaks to you through telepathy, its voice echoing in your mind. Ooze (telepathically): "You have shown courage by following me here, mortal. I am a being of ancient knowledge and power. Tell me, what do you seek?" You can sense that this ooze knows more than it lets on. Your choices lie before you:'},
                {'scene_id': 4, 'scene_name': 'THE END', 'scene_description':
                    'Ooze (telepathically): "Very well, seeker of knowledge. Your fate is written on the canvas of time." The eye''s gaze intensifies, and before you can react, it knocks you out. When you wake up, you find yourself on the porch, a prophecy etched onto the inside of your arm, your mind forever marked by the encounter. (Prophecy) Game Over.'}
            ]

            with database.atomic():
                Scenes.insert_many(scenes_data).execute()

        # if Options.select().count() == 0:
        #     options_data =
# ipdb.set_trace()
