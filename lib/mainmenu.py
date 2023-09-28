# import ipdb
from helpers import *
from cli import *


def main_menu():
    print_somewhat_fast(game_title)
    print_slowly(game_instructions)
    print("1. Enter Player")
    print("2. Quit")

    while True:
        choice = input("Select an option: ")

        if choice == '1':
            create_player()
            introduction()
        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print("Please select a valid option.")


# def enter_player():
#     player_name = input("Enter player name: ")
#     print(f"Welcome, {player_name}!")

#     while True:
#         choice = input(
#             "Start a new game (new). Continue current game(con). Delete current game(del). Exit(exit).")

#         if choice == "new":
#             helpers.start_new_game(player_name)
#             introduction()
#             break
#         elif choice == "con":
#             helpers.continue_game(player_name)
#             break
#         elif choice == "del":
#             helpers.delete_game_data(player_name)
#             break
#         elif choice == "exit":
#             helpers.exit_program(player_name)
#             break
#         else:
#             print("Whoops! Invalid choice. Please Select a valid option.")


game_title = """
▄▄▄█████▓ ██░ ██ ▓█████     ▒█████   ███▄ ▄███▓ ██▓ ███▄    █  ▒█████   █    ██   ██████    ▓█████  ███▄    █  ▄████▄   ▒█████   █    ██  ███▄    █ ▄▄▄█████▓▓█████  ██▀███
▓  ██▒ ▓▒▓██░ ██▒▓█   ▀    ▒██▒  ██▒▓██▒▀█▀ ██▒▓██▒ ██ ▀█   █ ▒██▒  ██▒ ██  ▓██▒▒██    ▒    ▓█   ▀  ██ ▀█   █ ▒██▀ ▀█  ▒██▒  ██▒ ██  ▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒
▒ ▓██░ ▒░▒██▀▀██░▒███      ▒██░  ██▒▓██    ▓██░▒██▒▓██  ▀█ ██▒▒██░  ██▒▓██  ▒██░░ ▓██▄      ▒███   ▓██  ▀█ ██▒▒▓█    ▄ ▒██░  ██▒▓██  ▒██░▓██  ▀█ ██▒▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒
░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄    ▒██   ██░▒██    ▒██ ░██░▓██▒  ▐▌██▒▒██   ██░▓▓█  ░██░  ▒   ██▒   ▒▓█  ▄ ▓██▒  ▐▌██▒▒▓▓▄ ▄██▒▒██   ██░▓▓█  ░██░▓██▒  ▐▌██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄
  ▒██▒ ░ ░▓█▒░██▓░▒████▒   ░ ████▓▒░▒██▒   ░██▒░██░▒██░   ▓██░░ ████▓▒░▒▒█████▓ ▒██████▒▒   ░▒████▒▒██░   ▓██░▒ ▓███▀ ░░ ████▓▒░▒▒█████▓ ▒██░   ▓██░  ▒██▒ ░ ░▒████▒░██▓ ▒██▒
  ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░   ░ ▒░▒░▒░ ░ ▒░   ░  ░░▓  ░ ▒░   ▒ ▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░   ░░ ▒░ ░░ ▒░   ▒ ▒ ░ ░▒ ▒  ░░ ▒░▒░▒░ ░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒   ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░
    ░     ▒ ░▒░ ░ ░ ░  ░     ░ ▒ ▒░ ░  ░      ░ ▒ ░░ ░░   ░ ▒░  ░ ▒ ▒░ ░░▒░ ░ ░ ░ ░▒  ░ ░    ░ ░  ░░ ░░   ░ ▒░  ░  ▒     ░ ▒ ▒░ ░░▒░ ░ ░ ░ ░░   ░ ▒░    ░     ░ ░  ░  ░▒ ░ ▒░
  ░       ░  ░░ ░   ░      ░ ░ ░ ▒  ░      ░    ▒ ░   ░   ░ ░ ░ ░ ░ ▒   ░░░ ░ ░ ░  ░  ░        ░      ░   ░ ░ ░        ░ ░ ░ ▒   ░░░ ░ ░    ░   ░ ░   ░         ░     ░░   ░
          ░  ░  ░   ░  ░       ░ ░         ░    ░           ░     ░ ░     ░           ░        ░  ░         ░ ░ ░          ░ ░     ░              ░             ░  ░   ░
                                                                                                              ░
"""

game_instructions = """
Welcome!
Instructions
Select "Enter Player" to start or continue your adventure.
If you have a recorded name, you can choose to start a new game
or continue your current game.
Follow the story's choices carefully and make decisions to uncover your fate.
Enjoy the experience and see where your choices lead you. Good luck!
"""
