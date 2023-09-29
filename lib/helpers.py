# lib/helpers.py
from models.model_1 import *
# import ipdb
import time
import random


def print_slowly(output):
    for char in output:
        print(char, end='', flush=True)
        time.sleep(0.008)
        # time.sleep(0)
    print()


def display_scene_description(scene_id):
    scene = Scenes.get(Scenes.scene_id == scene_id)
    return (scene.scene_description)


def display_scene_name(scene_id):
    scene = Scenes.get(Scenes.scene_id == scene_id)
    return (scene.scene_name)


def display_option_description(option_id):
    option = Options.get(Options.option_id == option_id)
    return (option.option_description)


def print_somewhat_fast(output):
    for char in output:
        print(char, end='', flush=True)
        time.sleep(0.002)
        # time.sleep(0)
    print()


def list_players():
    players = Players.select()

    if players:
        for player in players:
            player_progress = display_scene_name(player.scene_id)
            print(
                f"Player Name: {player.player_name}, Save Location: {player_progress}")
    else:
        print("No players found.")


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


def change_player_name():
    try:
        player_name = input("Enter the name you wish to edit: ")
        new_name = input(f"What would you like to change {player_name} to? ")
        player = Players.get(Players.player_name == player_name)
        player.player_name = new_name
        player.save()

        print(f"Player name updated. Your name is now {new_name}")
    except Players.DoesNotExist:
        print(f"Player with '{player_name}' not found")
    except Exception as exc:
        print("Error updating player: ", exc)


def delete_player():
    player_name = str(
        input("Enter the name of the player you wish to delete: "))

    try:
        player = Players.get(Players.player_name == player_name)
        player.delete_instance()
        print(f"Player {player.player_name} deleted successfully.")
    except Players.DoesNotExist:
        print("Player not found.")


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

        if Options.select().count() == 0:
            options_data = [
                {'scene_id': 0, 'next_scene_id': 0, 'option_description':
                    'Join your friends for more shots and dive headfirst into the night\'s revelry.'},
                {'scene_id': 0, 'next_scene_id': 1, 'option_description':
                    'Opt for a more mellow approach, sipping on lemonade as you enjoy the company of your friends'},
                {'scene_id': 1, 'next_scene_id': 1, 'option_description':
                    'Continue vaping and head back inside, rejoining the festivities. Game over.'},
                {'scene_id': 1, 'next_scene_id': 2, 'option_description':
                    'Curiosity gets the better of you, and you decide to follow the cat behind the shed'},
                {'scene_id': 2, 'next_scene_id': 3,
                    'option_description': 'Enter ">_>" to continue'},
                {'scene_id': 3, 'next_scene_id': 3,
                    'option_description': 'Attempt to run from the ooze'},
                {'scene_id': 3, 'next_scene_id': 3,
                    'option_description': 'Share something unrelated'},
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
