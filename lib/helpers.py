# lib/helpers.py
from models.model_1 import *
# import ipdb
import time
import random


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
    
#def print_slowly_centered(output):
   # lines = output.split('\n')
   # for line in lines:
      #  print_centered_slowly(line)

#def print_centered_slowly(message):
  #  terminal_width = 75  
 #   padding = " " * ((terminal_width - len(message)) // 2)
   # print_slowly(padding + message)


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
            success_message = f"{player.player_name} created successfully"
            print(success_message, end='', flush=True)
            time.sleep(2)
            print("\r" + " " * len(success_message) + "\r", end='', flush=True)
            print_centered("~🧿~Let's Begin!~🧿~")
        else:
            print(f"Player {player.player_name} already exists.")
            time.sleep(2)
            print_centered("~🧿~Let's Begin!~🧿~")
    except Exception as exc:
        print("Error creating player_name: ", exc)
        print()
        
def print_centered(message):
    terminal_width = 75  
    padding = " " * ((terminal_width - len(message)) // 2)
    print(padding + message)
        
def remove_message(delay):
    time.sleep(delay)
    print("\033[A\033[K", end="")
    

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
        
def get_random_prophecy():
    prophecies = Prophecy.select()
    if prophecies.count() == 0:
            return "The Ooze has spared you of prophecy. Enjoy the lie of free will."
    random_prophecy = random.choice(prophecies)
    return random_prophecy.prophecy_description
    


def initialize_database():
    with database:
        database.create_tables([Players, Scenes, Options, Prophecy], safe=True)

        if Scenes.select().count() == 0:
            scenes_data = [
                {'scene_id': 0, 'scene_name': 'Introduction', 'scene_description':
                    'You find yourself amidst a vibrant party with your friends, the music pulsating through the air as laughter fills the room. You''re faced with a choice:'},
                {'scene_id': 1, 'scene_name': 'Outside the Party', 'scene_description':
                    'As you exhale a puff of vapor, you notice a black cat with striking green eyes in the yard, peacefully minding its own business. Your options beckon:'},
                {'scene_id': 2, 'scene_name': 'Following the Cat', 'scene_description': 'You stealthily follow the mysterious feline behind the shed, only to find that it has vanished without a trace. Instead, you encounter something utterly unexpected—a colossal pile of black ooze. It ripples and shifts, and from the center emerges a massive bright blue eye, its presence unnerving.'},
                {'scene_id': 3, 'scene_name': 'The Encounter', 'scene_description':
                    'The tone shifts from the jovial party atmosphere to an eerie, all-knowing aura. It speaks to you through telepathy, its voice echoing in your mind. Ooze (telepathically): "You have shown courage by following me here, mortal. I am a being of ancient knowledge and power. Tell me, what do you seek?" You can sense that this ooze knows more than it lets on. Your choices lie before you:'},
                {'scene_id': 4, 'scene_name': 'THE END', 'scene_description':
                    'Ooze (telepathically): "Very well, seeker of knowledge. Your fate is written on the canvas of time." The eye''s gaze intensifies, and before you can react, it knocks you out. When you wake up, you find yourself on the porch, a prophecy etched onto the inside of your arm, your mind forever marked by the encounter.'}
            ]

            with database.atomic():
                Scenes.insert_many(scenes_data).execute()

        if Options.select().count() == 0:
            options_data = [
                {'scene_id': 0, 'next_scene_id': 0, 'option_description':
                    'Join your friends for more shots and dive headfirst into the night\'s revelry.'},
                {'scene_id': 0, 'next_scene_id': 1, 'option_description':
                    'Opt for a more mellow approach, sipping on lemonade as you enjoy the company of your friends'},
                {'scene_id': 1, 'next_scene_id': 1, 'option_description':
                    'Continue vaping and head back inside, rejoining the festivities.'},
                {'scene_id': 1, 'next_scene_id': 2, 'option_description':
                    'Curiosity gets the better of you, and you decide to follow the cat behind the shed'},
                {'scene_id': 2, 'next_scene_id': 3,
                    'option_description': 'You are too stunned to move. Press 1 to continue.'},
                {'scene_id': 3, 'next_scene_id': 4,
                    'option_description': 'Attempt to run from the ooze'},
                {'scene_id': 3, 'next_scene_id': 4,
                    'option_description': 'Express your desire for a prophecy'}
            ]

            with database.atomic():
                Options.insert_many(options_data).execute()

        if Prophecy.select().count() == 0:
            prophecy_data = [
                {'prophecy_id': 1, 'prophecy_name': 'Seekers Fate', 'prophecy_description':
                    'In the depths of darkness, a glimmer of light shall guide you to your destiny. Seek the path less traveled, for therein lies the truth.'},
                {'prophecy_id': 2, 'prophecy_name': 'Wealth of Self', 'prophecy_description':
                    'Fortunes may rise and fall like tides, but the true wealth lies within. Seek not the gold of others, but cultivate the treasure of self-awareness, for therein lies the key to prosperity.'},
                {'prophecy_id': 3, 'prophecy_name': 'Phoenix or Rebirth', 'prophecy_description':
                    'As the moon wanes, so too must all things find their end. But from the ashes of mortality, the phoenix of rebirth shall rise, ushering in a new chapter of your eternal journey.'},
                {'prophecy_id': 4, 'prophecy_name': 'Constellations of Connection', 'prophecy_description':
                    'In the labyrinth of hearts, you will find both love and loss. Trust in the constellations of connection, for even in endings, new beginnings await.'},
                {'prophecy_id': 5, 'prophecy_name': 'Threads of Life', 'prophecy_description':
                    'In the tapestry of existence, the threads of your life shall weave a pattern unique to your soul. Embrace the moments, for they are the stitches that bind your story.'}
            ]

            with database.atomic():
                Prophecy.insert_many(prophecy_data).execute()
   
# ipdb.set_trace()
