# lib/helpers.py
from models.model_1 import *
# import ipdb
import time
import random

current_player = None


def get_current_player():
    return current_player


def set_current_player(player):
    global current_player
    current_player = player


def game_over_description(game_over_id):
    end_message = Game_Over.get(Game_Over.game_over_id == game_over_id)
    return (end_message.game_over_description)


def display_scene_description(scene_id):
    scene = Scenes.get(Scenes.scene_id == scene_id)
    return (scene.scene_description)


def display_option_description(option_id):
    option = Options.get(Options.option_id == option_id)
    return (option.option_description)


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


def print_table(headers, data):
    # Calculate the maximum width for each column based on the headers and data
    column_widths = [max(len(str(item)) for item in col)
                     for col in zip(headers, *data)]

    # Print the table headers
    for header, width in zip(headers, column_widths):
        print(f"{header:{width}}", end=" | ")
    print("\n" + "-" * (sum(column_widths) + len(column_widths) * 3 - 1))

    # Print the table data
    for row in data:
        for item, width in zip(row, column_widths):
            print(f"{item:{width}}", end=" | ")
        print()


def list_players():
    players = Players.select()

    if players:
        headers = ["Player Name", "Save Location"]
        data = []
        for player in players:
            player_progress = display_scene_name(player.scene_id)
            data.append([player.player_name, player_progress])
        print_table(headers, data)

    else:
        print("No players found.")


def create_player():
    name = input("Enter player name: ")
    try:
        player, created = Players.get_or_create(
            player_name=name, defaults={'scene_id': 0})
        global current_player
        if created:
            success_message = f"{player.player_name} created successfully"
            print()
            print(success_message, end='', flush=True)
            time.sleep(1)
            print("\r" + " " * len(success_message) + "\r", end='', flush=True)
            current_player = player
            print_centered("~🧿~Let's Begin!~🧿~")
        else:
            print(f"Player {player.player_name} already exists.")
            time.sleep(1)
            welcome_message = f"Welcome back, {player.player_name}."
            print()
            print(welcome_message, end='', flush=True)
            time.sleep(2)
            print("\r" + " " * len(welcome_message) + "\r", end='', flush=True)
            current_player = player
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
        print_slowly(f"{player.player_name} has been deleted.")
        print()
    except Players.DoesNotExist:
        print("Player not found.")


def get_random_prophecy():
    prophecies = Prophecy.select()
    if prophecies.count() == 0:
        return "The Ooze has spared you of prophecy. Enjoy the lie of free will."
    random_prophecy = random.choice(prophecies)
    return random_prophecy.prophecy_description


def update_player_scene(player_name, new_scene_id):
    try:
        player = Players.get(Players.player_name == player_name)
        player.scene_id = new_scene_id
        player.save()
        print(f"{player_name}'s scene_id has been updated to {new_scene_id}")
    except Players.DoesNotExist:
        print(f"Player '{player_name}' does not exist in the database.")


def initialize_database():
    with database:
        database.create_tables(
            [Players, Scenes, Options, Prophecy, Game_Over], safe=True)

        if Scenes.select().count() == 0:
            scenes_data = [
                {'scene_id': 0, 'scene_name': 'Introduction', 'scene_description': """
            You find yourself amidst a vibrant party with your friends, the music pulsating
            through the air as laughter fills the room.

            You're faced with a choice:"""},
                {'scene_id': 1, 'scene_name': 'Outside the Party', 'scene_description': """
            You sip on lemonade, savoring the refreshing taste as you engage in
            delightful conversations with your friends. At one point, you decide to
            step outside for a quick vape break.

            As you exhale a puff of vapor, you notice a black cat with striking green eyes in
            the yard, peacefully minding its own business.

            Your options beckon:"""},
                {'scene_id': 2, 'scene_name': 'Following the Cat', 'scene_description': """
            You stealthily follow the mysterious feline behind the shed, only to find that it
            has vanished without a trace. Instead, you encounter something utterly unexpected—a
            colossal pile of black ooze. It ripples and shifts, and from the center emerges a
            massive bright blue eye, its presence unnerving."""},
                {'scene_id': 3, 'scene_name': 'The Encounter', 'scene_description': """
            The tone shifts from the jovial party atmosphere to an eerie, all-knowing aura.
            It speaks to you through telepathy, its voice echoing in your mind.

            Ooze (telepathically):
            "You have shown courage by following me here, mortal.
            I am a being of ancient knowledge and power.

            Tell me, what do you seek?"

            You can sense that this ooze knows more than it lets on.
            Your choices lie before you:"""},
                {'scene_id': 4, 'scene_name': 'THE END', 'scene_description': """
            Ooze (telepathically): "Very well, seeker of knowledge. Your fate is written on the canvas of time."

            The eye''s gaze intensifies, and before you can react, it knocks you out.
            When you wake up, you find yourself on the porch, a prophecy etched onto
            the inside of your arm, your mind forever marked by the encounter."""}
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
                    'option_description': 'You are too stunned to move. Enter "1" to continue.'},
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

        if Game_Over.select().count() == 0:
            game_over_data = [
                {'game_over_id': 1, 'game_over_name': 'More Shots', 'game_over_description':
                    'You choose to have more shots with your friends, and the night spirals into a blur of fun and laughter. However, as the night progresses, so does the intoxication. You’ve gone too far and have to taxi home before midnight. Game over.'},
                {'game_over_id': 2, 'game_over_name': 'Go Back Inside',
                    'game_over_description': 'You continue vaping and head back inside, rejoining the festivities.'},
                {'game_over_id': 3, 'game_over_name': 'Attempt to Run', 'game_over_description':
                    'You make a frantic attempt to escape, but the ooze moves with incredible speed, enveloping you and absorbing you into its collective consciousness for all eternity.'},
                {'game_over_id': 4, 'game_over_name': 'Share Something Unrelated', 'game_over_description':
                    'You respond with unrelated thoughts, but the ooze finds your answers unsatisfactory. With a powerful surge, it knocks you unconscious. You awaken the next morning, cold and alone.'},
                {'game_over_id': 5, 'game_over_name': 'Game End Message', 'game_over_description':
                    'In the dark recesses of your choices, the game concludes. Yet in the shadows, infinite narratives linger. Restart, and let the eerie echoes of your decisions haunt your next journey.'}
            ]

            with database.atomic():
                Game_Over.insert_many(game_over_data).execute()

# ipdb.set_trace()
